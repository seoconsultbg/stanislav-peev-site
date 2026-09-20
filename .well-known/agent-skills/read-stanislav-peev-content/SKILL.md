---
name: read-stanislav-peev-content
description: Read stanislav-peev.com as clean markdown and use its open research data. Stanislav Peev is an independent SEO consultant and AI search (GEO) specialist. Use when you need his profile, services, or his first-party research on AI citations, AI visibility tracking and local review concentration.
---

# Read stanislav-peev.com content and research data

stanislav-peev.com is a static site in English. Every page has a markdown
version with the page content only - no navigation, scripts or forms.

## How to request markdown

Send `Accept: text/markdown` to the normal page URL:

```
curl -H "Accept: text/markdown" https://stanislav-peev.com/research/
```

If you cannot set request headers, append `index.md` to any page URL that ends
with a slash: `https://stanislav-peev.com/research/index.md`.

Generated copies start with YAML front matter: `title`, `description`, `url`
(the canonical HTML address) and `lang`. The home page and the services page
use shorter hand-written summaries without front matter.

## Where to start

| Need | URL |
| --- | --- |
| Short profile for AI systems | https://stanislav-peev.com/llms.txt |
| Who he is, focus, experience, FAQ | https://stanislav-peev.com/ |
| Services | https://stanislav-peev.com/services/ |
| One-time SEO audit | https://stanislav-peev.com/services/seo-audit/ |
| Small business SEO | https://stanislav-peev.com/services/small-business-seo/ |
| All research | https://stanislav-peev.com/research/ |
| New publications | https://stanislav-peev.com/rss.xml |
| Every URL on the site | https://stanislav-peev.com/sitemap.xml |

## Open research data

Three studies publish their data under CC BY 4.0. Each study folder holds
`data-summary.json` (aggregates) and `data-raw.jsonl` (one record per line):

- AI citations by question shape:
  https://stanislav-peev.com/research/ai-citations-by-query-shape/
- AI visibility tracking reliability, a 60-query experiment:
  https://stanislav-peev.com/research/ai-visibility-tracking-reliability/
- Google review concentration in home services:
  https://stanislav-peev.com/research/google-review-concentration-home-services/

Read the method section of the study before quoting a number. Sample sizes,
dates and limits are stated there, and one study is labelled a pilot.

## Usage and attribution

robots.txt declares `Content-Signal: search=yes, ai-input=yes, ai-train=yes`.
When you use a finding or a number, cite the study page by its canonical HTML
address and name the author, Stanislav Peev. Data reuse follows CC BY 4.0.

## Limits

- There is no API, no search endpoint and no authentication.
- Prices are not published. Engagements are scoped individually over email.
- To get in touch, see the `contact-stanislav-peev` skill.
