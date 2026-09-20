"""Generates a markdown copy (index.md) next to every index.html of stanislav-peev.com.

Why: .htaccess serves index.md when a request carries "Accept: text/markdown"
(markdown for agents). HTML stays the default for browsers and search engines.
The same run refreshes the sha256 digests in .well-known/agent-skills/index.json.

Run after EVERY content edit, before deploying:
    python D:/Claude/stanislav-peev-site/.tools/build_md.py
    python D:/Claude/stanislav-peev-site/.tools/build_md.py --check   # report only

Standard library only. The .tools folder is not deployed (.cpanel.yml copies
non-dot paths only; skip it on manual uploads too).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

SITE_ROOT = Path("D:/Claude/stanislav-peev-site")
ORIGIN = "https://stanislav-peev.com"
SKIP_DIRS = {".git", ".tools", ".well-known", ".claude", "assets", "thanks"}
# hand-written summaries - never overwritten by the generator
CURATED = {"index.md", "services/index.md"}
CONTACT_LINE = ("Stanislav Peev - contact in writing only, no calls: "
                "[info@stanislav-peev.com](mailto:info@stanislav-peev.com) · "
                "[contact form](https://stanislav-peev.com/#contact)")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "source", "track", "wbr"}
SKIP = {"head", "title", "script", "style", "noscript", "form", "button", "input", "textarea",
        "label", "select", "iframe", "svg", "nav", "template"}
BLOCK = {"p", "div", "section", "article", "aside", "main", "header", "footer",
         "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "table",
         "blockquote", "pre", "figure", "figcaption", "details", "summary",
         "hr", "address", "dl", "dt", "dd"}
CLOSES_P = BLOCK - {"li"}
BR = "\x00"


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag: str, attrs: dict[str, str], parent: "Node | None") -> None:
        self.tag = tag
        self.attrs = attrs
        self.children: list[Node | str] = []
        self.parent = parent


class TreeBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None)
        self.cur = self.root

    def _close(self, tag: str) -> None:
        node: Node | None = self.cur
        while node is not None and node.tag != tag:
            node = node.parent
        if node is not None and node.parent is not None:
            self.cur = node.parent

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in CLOSES_P and self.cur.tag == "p":
            self._close("p")
        if tag == "li" and self.cur.tag == "li":
            self._close("li")
        if tag in ("td", "th") and self.cur.tag in ("td", "th"):
            self._close(self.cur.tag)
        if tag == "tr" and self.cur.tag in ("td", "th", "tr"):
            self._close("tr")
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.cur.children.append(Node(tag, {k: (v or "") for k, v in attrs}, self.cur))

    def handle_endtag(self, tag: str) -> None:
        if tag not in VOID:
            self._close(tag)

    def handle_data(self, data: str) -> None:
        self.cur.children.append(data)


def parse(html: str) -> Node:
    builder = TreeBuilder()
    builder.feed(html)
    builder.close()
    return builder.root


def absolute(url: str) -> str:
    url = url.strip()
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return ORIGIN + url
    return url


def escape(text: str) -> str:
    text = text.replace("*", r"\*")
    return re.sub(r"<(?=[A-Za-z/!])", r"\\<", text)


def hidden(node: Node) -> bool:
    if node.tag in SKIP or "hidden" in node.attrs:
        return True
    if "crumbs" in node.attrs.get("class", "").split():
        return True
    return bool(re.search(r"display\s*:\s*none", node.attrs.get("style", "")))


def text_of(node: Node | str) -> str:
    if isinstance(node, str):
        return node
    if node.tag in SKIP:
        return ""
    return "".join(text_of(c) for c in node.children)


def squash(text: str) -> str:
    text = re.sub(r"[ \t\r\n\f\v]+", " ", text)
    text = re.sub(r" ?" + BR + r" ?", "\n", text)
    return text.strip()


def wrap(marker: str, inner: str) -> str:
    """**bold** / *em* with no spaces inside the markers."""
    core = inner.strip()
    if not core:
        return inner
    lead = inner[: len(inner) - len(inner.lstrip())]
    trail = inner[len(inner.rstrip()):]
    return f"{lead}{marker}{core}{marker}{trail}"


def join_inline(children: list[Node | str]) -> str:
    """Adjacent elements with no text between them get a separating space."""
    parts: list[str] = []
    state = [False]
    for c in children:
        glue(parts, state, inline(c), isinstance(c, Node))
    return "".join(parts)


def glue(parts: list[str], state: list[bool], piece: str, is_node: bool) -> None:
    if not piece:
        return
    if parts and state[0] and not parts[-1].endswith((" ", BR)):
        tight_label = parts[-1].endswith("**") and piece[0].isalnum()
        if is_node or tight_label:
            parts.append(" ")
    parts.append(piece)
    state[0] = is_node


def only_image(node: Node) -> bool:
    kids = [c for c in node.children if isinstance(c, Node) or c.strip()]
    return len(kids) == 1 and isinstance(kids[0], Node) and (
        kids[0].tag == "img" or (kids[0].tag in ("figure", "picture", "span") and only_image(kids[0])))


def inline(node: Node | str) -> str:
    if isinstance(node, str):
        return escape(node)
    tag = node.tag
    if hidden(node):
        return ""
    if tag == "br":
        return BR
    if tag == "img":
        alt = squash(node.attrs.get("alt", ""))
        src = node.attrs.get("src") or node.attrs.get("data-src") or ""
        return f"![{alt}]({absolute(src)})" if alt and src else ""
    inner = join_inline(node.children)
    if tag == "a":
        href = node.attrs.get("href", "").strip()
        if only_image(node):
            is_file = re.search(r"\.(png|jpe?g|gif|webp|avif|svg)$", href, re.I)
            return inner if is_file else ""
        if href.startswith("#") and "btn" in node.attrs.get("class", ""):
            return ""
        label = squash(inner) or squash(node.attrs.get("aria-label", ""))
        if not label:
            return ""
        if not href or href.startswith(("#", "javascript:")):
            return label
        return f"[{label}]({absolute(href)})"
    if tag in ("strong", "b"):
        return wrap("**", inner)
    if tag == "span" and any(c.endswith("label") for c in node.attrs.get("class", "").split()):
        return BR + wrap("**", inner)  # label/value pairs on separate lines
    if tag in ("em", "i"):
        return wrap("*", inner)
    if tag == "code":
        return f"`{squash(text_of(node))}`"
    return inner


def guard_line_start(text: str) -> str:
    return re.sub(r"^(#{1,6}\s|[-+]\s|>|\d+[.)]\s)", r"\\\1", text)


def render_table(node: Node) -> str:
    rows: list[tuple[bool, list[str]]] = []

    def walk(n: Node) -> None:
        for c in n.children:
            if isinstance(c, str):
                continue
            if c.tag == "tr":
                cells = [x for x in c.children if isinstance(x, Node) and x.tag in ("td", "th")]
                if cells:
                    is_head = all(x.tag == "th" for x in cells)
                    vals = [squash(inline(x)).replace("\n", " ").replace("|", r"\|") for x in cells]
                    rows.append((is_head, vals))
            elif c.tag in ("thead", "tbody", "tfoot"):
                walk(c)

    walk(node)
    if not rows:
        return ""
    width = max(len(r) for _, r in rows)
    grid = [r + [""] * (width - len(r)) for _, r in rows]
    lines = ["| " + " | ".join(grid[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in grid[1:]]
    return "\n".join(lines)


def render_list(node: Node) -> str:
    ordered = node.tag == "ol"
    items: list[str] = []
    index = 1
    for c in node.children:
        if isinstance(c, str) or c.tag != "li":
            continue
        parts = blocks(c)
        if not parts:
            continue
        marker = f"{index}. " if ordered else "- "
        index += 1
        tight = all(re.match(r"(- |\d+\. )", p) for p in parts[1:])
        body = ("\n" if tight else "\n\n").join(parts)
        pad = " " * len(marker)
        lines = body.split("\n")
        items.append(marker + lines[0] + "".join(f"\n{pad}{ln}" if ln else "\n" for ln in lines[1:]))
    return "\n".join(items)


def blocks(node: Node) -> list[str]:
    out: list[str] = []
    run: list[str] = []
    run_node = [False]

    def flush() -> None:
        text = squash("".join(run))
        run.clear()
        run_node[0] = False
        if re.search(r"\w", text):
            out.append(guard_line_start(text))

    for c in node.children:
        if isinstance(c, str) or c.tag not in BLOCK:
            if isinstance(c, Node) and (hidden(c) or has_block(c)):
                flush()
                if not hidden(c):
                    out.extend(blocks(c))
                continue
            glue(run, run_node, inline(c), isinstance(c, Node))
            continue
        flush()
        tag = c.tag
        if hidden(c):
            continue
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = squash(inline(c)).replace("\n", " ")
            if text:
                out.append("#" * int(tag[1]) + " " + text)
        elif tag == "p" and not has_block(c):
            text = squash(inline(c))
            if re.search(r"\w", text):
                out.append(guard_line_start(text))
        elif tag in ("ul", "ol"):
            text = render_list(c)
            if text:
                out.append(text)
        elif tag == "table":
            text = render_table(c)
            if text:
                out.append(text)
        elif tag == "blockquote":
            inner = "\n\n".join(blocks(c))
            if inner:
                out.append("\n".join("> " + ln if ln else ">" for ln in inner.split("\n")))
        elif tag == "pre":
            code = text_of(c).strip("\n")
            if code.strip():
                out.append("```\n" + code + "\n```")
        elif tag == "hr":
            out.append("---")
        elif tag == "summary":
            text = squash(inline(c)).replace("\n", " ")
            if text:
                out.append(f"**{text}**")
        elif tag == "figcaption":
            text = squash(inline(c))
            if text:
                out.append(f"*{text}*")
        else:
            out.extend(blocks(c))
    flush()
    return out


def has_block(node: Node) -> bool:
    for c in node.children:
        if isinstance(c, Node) and (c.tag in BLOCK or has_block(c)):
            return True
    return False


def find_all(node: Node, tag: str) -> list[Node]:
    found: list[Node] = []
    for c in node.children:
        if isinstance(c, Node):
            if c.tag == tag:
                found.append(c)
            found.extend(find_all(c, tag))
    return found


def head_meta(html: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if m:
        meta["title"] = squash(unescape(m.group(1)))
    m = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html, re.S | re.I)
    if m:
        meta["description"] = squash(unescape(m.group(1)))
    m = re.search(r'<link\s+rel="canonical"\s+href="(.*?)"', html, re.I)
    if m:
        meta["url"] = m.group(1).strip()
    m = re.search(r'<html[^>]*\slang="([^"]+)"', html, re.I)
    if m:
        meta["lang"] = m.group(1)
    return meta


def tidy(items: list[str]) -> list[str]:
    out: list[str] = []
    for item in items:
        m = re.fullmatch(r"\[[^\]]*\]\(([^)]+)\)", item)
        if m and any(b.startswith("#") and f"]({m.group(1)})" in b for b in out[-3:]):
            continue  # CTA link that repeats the link in the card heading
        out.append(item)
    return out


def yaml_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def convert(html: str, fallback_url: str) -> str:
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S | re.I)
    if not m:
        raise ValueError("no <main> element")
    tree = parse(m.group(1))

    meta = head_meta(html)
    meta.setdefault("url", fallback_url)
    front = ["---"]
    for key in ("title", "description", "url", "lang"):
        if meta.get(key):
            front.append(f"{key}: {yaml_str(meta[key])}")
    front.append("---")

    body = tidy(blocks(tree))
    body += ["---", CONTACT_LINE]
    text = "\n".join(front) + "\n\n" + "\n\n".join(body) + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def targets() -> list[tuple[Path, Path, str]]:
    found: list[tuple[Path, Path, str]] = []
    for page in sorted(SITE_ROOT.rglob("index.html")):
        rel = page.relative_to(SITE_ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        if rel.with_name("index.md").as_posix() in CURATED:
            continue
        url = ORIGIN + "/" + "/".join(rel.parts[:-1]) + ("/" if len(rel.parts) > 1 else "")
        found.append((page, page.with_name("index.md"), url))
    return found


def update_skills_index(check: bool) -> None:
    """Agent Skills index: the digest is the sha256 of the exact SKILL.md bytes,
    so it is recomputed on every run (deploy via git or zip, never FTP ASCII)."""
    base = SITE_ROOT / ".well-known" / "agent-skills"
    skills = []
    for skill in sorted(base.glob("*/SKILL.md")):
        raw = skill.read_bytes()
        front = re.match(r"---\n(.*?)\n---\n", raw.decode("utf-8"), re.S)
        fields = dict(re.findall(r"^(name|description):\s*(.+)$", front.group(1), re.M)) if front else {}
        if fields.get("name") != skill.parent.name or not fields.get("description"):
            print(f"WARNING - invalid front matter: {skill.relative_to(SITE_ROOT)}")
            continue
        skills.append({
            "name": fields["name"],
            "type": "skill-md",
            "description": fields["description"].strip(),
            "url": f"/.well-known/agent-skills/{fields['name']}/SKILL.md",
            "digest": "sha256:" + hashlib.sha256(raw).hexdigest(),
        })
    if not skills:
        return
    doc = {"$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json", "skills": skills}
    text = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
    index = base / "index.json"
    changed = not index.exists() or index.read_text(encoding="utf-8") != text
    if changed and not check:
        index.write_text(text, encoding="utf-8", newline="\n")
    print(f"agent skills: {len(skills)} | index.json {'updated' if changed and not check else 'unchanged' if not changed else 'needs update'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    args = ap.parse_args()

    total_html = total_md = written = 0
    problems: list[str] = []
    pages = targets()
    for page, dst, url in pages:
        html = page.read_text(encoding="utf-8")
        md = convert(html, url)
        rel = dst.relative_to(SITE_ROOT).as_posix()
        total_html += len(html.encode("utf-8"))
        total_md += len(md.encode("utf-8"))
        if len(md.split()) < 80:
            problems.append(f"suspiciously short: {rel} ({len(md.split())} words)")
        if re.search(r"[\u0400-\u04FF]", md):
            problems.append(f"Cyrillic found (site rule: none): {rel}")
        if not args.check:
            old = dst.read_text(encoding="utf-8") if dst.exists() else None
            if old != md:
                dst.write_text(md, encoding="utf-8", newline="\n")
                written += 1

    print(f"pages: {len(pages)} generated (+{len(CURATED)} curated, untouched) | written/changed: {written}")
    print(f"HTML total: {total_html/1024:.0f} KB | markdown total: {total_md/1024:.0f} KB "
          f"({100*total_md/max(total_html, 1):.0f}% of HTML)")
    for line in problems:
        print("WARNING - " + line)
    for p in SITE_ROOT.rglob("index.md"):
        if p.relative_to(SITE_ROOT).parts[0] not in SKIP_DIRS and not p.with_name("index.html").exists():
            print(f"ORPHAN (no index.html): {p.relative_to(SITE_ROOT)}")
    update_skills_index(args.check)
    return 0


if __name__ == "__main__":
    sys.exit(main())
