---
title: "Do competitor comparison pages sway AI answers? 144-answer test"
description: "76% of AI answers to 'X vs Y' cite a vendor's own comparison page, yet the cited vendor won 68 times and lost 66. What to do when AI repeats a competitor's claim."
url: "https://stanislav-peev.com/research/competitor-comparison-pages-in-ai-answers/"
lang: "en"
---

Research · AI Search Data

# Your competitor's comparison page is probably in the AI answer about you. What it moves, and what to do when it gets you wrong

By **Stanislav Peev**, SEO consultant & GEO specialist · Published **September 28, 2026** · Original experiment, 144 AI answers · 11 min read

76%

of AI answers to "X vs Y: which is better?" cited a page written by one of the two vendors being compared. In 144 answers from Perplexity, GPT-4o and Gemini, the vendors' own pages made up 18.5% of all citations. Those pages did not decide who won. When a vendor's page was cited, the answer sided with that vendor 68 times and with its rival 66 times.

Source: my own test, 12 vendor pairs x 2 name orders x 3 engines x 2 runs, September 28, 2026. Raw data, CC BY 4.0.

## Key takeaways

- **109 of 144** answers cited at least one of the two vendors' own pages. 96% of those vendor citations were "vs", "compare", "alternatives" or "switch from" pages. Perplexity cited both vendors in 48 answers out of 48
- **68 vs 66** - when a vendor's own page was among the sources, the answer favored that vendor 68 times and its rival 66 times. Being cited is not the same as winning
- **94 of 96** clear verdicts went to the same winner within each pair, whichever page was cited and whichever name came first in the question. The verdict looks settled by the wider web, not by one page
- **10 answers** cited Zendesk's own "Zendesk vs Freshdesk" page. Eight of them recommended Freshdesk and two called it a draw. Atlassian's Confluence comparison pages were cited 7 times, and Notion won all 7
- **The risk sits in the facts, not the verdict.** A cited page is a source the answer can lift prices, features and limits from. That is how a wrong claim about you travels, and it is the part you can fix
- **The fix is a fact page, not a counter hit piece.** Publish each disputed fact in a checkable form, get it repeated on sites you do not own, and use the legal route only for false statements of fact

## What's in this report

1. The short answer
2. How often do AI answers cite the vendors' own comparison pages?
3. Does the vendor's page tilt the verdict?
4. Where does a competitor's page actually hurt you?
5. What to do when AI repeats a competitor's false claim
6. When one negative review drives the whole answer
7. All 12 pairs in one table
8. Methodology
9. Limitations
10. FAQ
11. Get the data

## 1. The short answer

If a competitor publishes a "them vs you" page, there is a good chance AI assistants read it when someone compares the two of you. In my test, three answers in four cited a page owned by one of the two vendors. What those pages did not do was flip the recommendation. That came out the same for each pair almost every time. The damage a competitor's page can do is narrower and more practical. It supplies the facts the answer repeats about you.

This started with an r/SEO thread in September 2026. The poster works for a brand that has led its category for more than 25 years. A competitor had published an "us vs them" article with facts they said were wrong, and AI answers were leaning on it heavily. They did not want to answer with the same kind of article, and they could not find advice beyond "build more mentions". The best reply in the thread was one paragraph long. It said to put each disputed fact on your own site as a plain, checkable statement and to get the same facts said on sites you do not own.

I went looking for the rest. The guides on fixing what AI says about a brand are good on the general case. Semrush's guide, for example, names competitor comparison pages as a source of "competitive misattribution". The legal material on false comparative advertising is also solid. But nothing I found joins the two for the case where the source is a named competitor's page. And nobody had measured how much such a page moves an answer. So I measured it first.

## 2. How often do AI answers cite the vendors' own comparison pages?

Most of the time. I asked "X vs Y: which is better for a small business? Give a clear recommendation." for 12 pairs of software vendors, in both name orders, on Perplexity, GPT-4o with web search and Gemini with web search. 109 of the 144 answers cited at least one page on either vendor's domain. That was 261 of the 1,412 citations, or 18.5%.

### Answers that cited a vendor's own page, by engine

Share of the 48 answers per engine that cited a page on either vendor's domain. The figure on the right is the average number of sources per answer.

Both vendors' pages cited One vendor's page cited No vendor page

*12 vendor pairs x 2 name orders x 2 runs = 48 answers per engine, September 28, 2026.*

**View as table**

| Engine | Answers | Both vendors cited | One vendor cited | Neither | Sources per answer |
| --- | --- | --- | --- | --- | --- |
| Perplexity Sonar | 48 | 48 | 0 | 0 | 19.4 |
| GPT-4o + web | 48 | 9 | 22 | 17 | 5.0 |
| Gemini 2.5 Flash + web | 48 | 9 | 21 | 18 | 5.0 |

The pages being cited are exactly the ones this report is about. The most cited vendor URLs were ClickUp's "Asana vs ClickUp" post (12 answers), WooCommerce's "WooCommerce vs Shopify" page (11), 1Password's "Bitwarden vs 1Password" post (11), Salesforce's "Salesforce vs HubSpot" page and HubSpot's "Pipedrive vs HubSpot" page (10 each). Each is a page one vendor wrote about a direct rival.

The engines differ in a way that matters for anyone doing a fix. Perplexity cites about 19 sources per answer and pulled in both vendors' pages in every one of its 48 answers. GPT-4o and Gemini cite about five, and cited a vendor page in 31 and 30 answers respectively, usually only one side's. So on those two engines the competitor's page is more often the only vendor voice in the answer. I saw the same gap in citation density when I looked at [which page types get cited for "best X", "X alternatives" and "X vs Y" questions](https://stanislav-peev.com/research/ai-citations-by-query-shape/). In that study 98.3% of citations for "X vs Y" questions went to comparison pages.

## 3. Does the vendor's page tilt the verdict?

Not in this sample. When only one vendor's page was cited, the answer favored that vendor 30% of the time and its rival 26%. With no vendor page cited, it was 24% and 24%. Across every answer that cited a vendor's page, that vendor won 68 times and lost 66.

### Being cited did not make a vendor win

Verdicts from each vendor's point of view, grouped by whose pages the answer cited.

Favored this vendor Neutral Favored the rival

*With no effect, the self and rival shares in each bar would be about equal, and they are. The "both cited" bar is symmetric by construction, because every answer counts once for each side.*

**View as table**

| Condition | Cases | Favored this vendor | Neutral | Favored the rival |
| --- | --- | --- | --- | --- |
| Only this vendor's page cited | 43 | 13 | 19 | 11 |
| Both vendors' pages cited | 132 | 55 | 22 | 55 |
| No vendor page cited | 70 | 17 | 36 | 17 |

The clearer pattern is how fixed each verdict was. In 11 of the 12 pairs every clear recommendation went the same way. That held across all three engines, both name orders and both runs. Notion beat Confluence in 12 answers out of 12. Freshdesk beat Zendesk in 10 and the other 2 were draws. The only split was QuickBooks against Xero, 7 to 2. Overall, 94 of the 96 answers that picked a side picked the pair's usual winner. Name order made no difference either: the product named first won 47 times, the one named second 49.

10 / 0

Zendesk's own "Zendesk vs Freshdesk" page was cited in 10 answers. Not one of them recommended Zendesk. Eight recommended Freshdesk and two called it a draw. The same happened to Atlassian: its Confluence comparison pages were cited 7 times, and Notion won all 7.

Source: this experiment, per-pair results below

My reading is that the verdict comes from the consensus across all the sources: review sites, "best of" lists, Reddit threads, the model's own prior. A vendor's comparison page is one voice among five or nineteen, and the engine seems to discount it as the interested party. That is reassuring if you are the brand on the receiving end. You are unlikely to lose the recommendation because of one hostile page, unless that page is the only detailed source on the topic.

## 4. Where does a competitor's page actually hurt you?

In the details the answer repeats: your price, your limits, which features you have, who you are for. A verdict needs consensus. A fact only needs one source that states it clearly and nobody contradicting it. If the competitor's page is the clearest place on the web that states your price, a stale or wrong price becomes the answer.

This part I did not measure. Checking whether an answer repeats a specific claim from a specific page needs claim-by-claim work that my test was not built for. The mechanism, though, is well documented. Semrush lists "competitive misattribution" among the common AI errors about brands: a competitor's product, feature or positioning attached to your brand, often sourced from comparison articles. It also notes that old pricing lives on in comparison pages long after the vendor changes it, and that those pages can outrank your own pricing page in the sources AI draws on. In my own [collection of figures on how often AI gets business information wrong](https://stanislav-peev.com/research/ai-wrong-business-information-statistics/), basic facts were where the errors clustered.

The r/SEO poster's complaint fits this pattern. They did not say AI recommended the competitor. They said AI kept repeating the competitor's incorrect statements. The facts were wrong, and those are the part you can correct.

## 5. What to do when AI repeats a competitor's false claim

Find out which page the claim comes from. Decide whether it is a false fact or just an opinion. Publish the correct fact in a form an engine can quote, and get it repeated where the competitor has no control. Escalate legally only if the claim is a checkable falsehood. Then measure the same prompts again.

1. **Reproduce it with a fixed prompt set.** Write 10 to 20 prompts a buyer would type: "[you] vs [them]", "is [you] worth it", "[you] pricing", "[you] alternatives". Run each on ChatGPT, Gemini, Perplexity and Google AI Mode, twice, and save the full answer with its sources. One screenshot proves nothing. In [my 60-query reliability test](https://stanislav-peev.com/research/ai-visibility-tracking-reliability/) the same prompt changed its top brand in about one run in five.
2. **Trace the claim to a page.** Open the cited sources and find the sentence the answer is paraphrasing. If an answer has no sources, ask the engine to search the web and cite them. If it still cannot, the claim is coming from training data, which is slower to change. Your server log is a second check. A ChatGPT-User or PerplexityBot request for the competitor's page, or for yours, at the time of the answer shows the engine read it live.
3. **Sort the claim into one of two boxes.** "Better for small teams" or "more intuitive" is an opinion. You answer it with evidence and reviews, not lawyers. "Has no API", "costs $49 per user", "not GDPR compliant" are statements of fact that can be checked. Only these give you leverage with the competitor, the platforms and, if needed, a regulator.
4. **Publish a fact page, not a rebuttal.** The engine discounts interested parties, and a rebuttal is the most interested page there is. What it can quote is a plain block of dated facts. Current price with the date. What the product does and does not do. Who it is for. Compliance status with a link to the certificate. Put it on the pages the engine already looks at, such as pricing, the feature page and FAQ, in text rather than images or scripts. Add Organization and Product structured data so the facts have a machine-readable copy. If you want your own comparison page, keep it factual about the competitor too. Your credibility is the asset here.
5. **Get the same facts said elsewhere.** The competitor's page is one source. You need the correct version to be the consensus. Update your profiles on G2, Capterra and the directories in your category. Brief your distributors and partners and ask them to state current pricing and specs. Answer the question where it is being asked, including on Reddit, under your own name. On Perplexity a new source can change the answer within days. On models answering from memory it takes longer.
6. **Ask, then escalate, for false statements of fact.** Start with a short, factual email to the competitor that names the claim, gives the correct fact and links the evidence. Comparison pages go stale more often than they are malicious. If that fails, the options depend on where you are. In the US, a false or misleading statement of fact in commercial advertising can be challenged under section 43(a) of the Lanham Act. Puffery and opinion are generally not actionable. The cheaper forum between competitors is BBB National Programs' National Advertising Division, which reviews truth-in-advertising challenges from competitors on standard, fast-track and complex tracks. In the EU, Directive 2006/114/EC allows comparative advertising only if it is not misleading, compares material, relevant, verifiable and representative features, and does not discredit the competitor. This is not legal advice. Talk to a lawyer in your jurisdiction before you send anything with the word "false" in it.
7. **Report the answer, and do not count on it.** ChatGPT, Google AI Overviews and Perplexity each have a thumbs-down and report option. It costs a minute and leaves a record. There is no guaranteed turnaround, so treat it as a supplement to steps 4 to 6.
8. **Measure with the same prompts.** Re-run the prompt set from step 1 every week for six weeks, then monthly. Count how many answers repeat the wrong claim and how many state the correct one, per engine. Expect Perplexity to move first, because it reads the live web on every query.

If you want the diagnosis and the prompt set done for you, that is the core of the GEO work on my [services page](https://stanislav-peev.com/services/), and an [SEO audit](https://stanislav-peev.com/services/seo-audit/) includes a check of what the main assistants say about you.

One thing to avoid: answering the competitor's page with a page of your own that attacks them. My data suggests the engines do not reward a vendor for writing about its rival. It also hands the competitor a legal argument against you.

## 6. When one negative review drives the whole answer

The same mechanism works through a single hostile post as well as a competitor's page. One clear negative source can dominate the answer, while many scattered positive ones barely register. The fix is also the same: find the exact source, make the positive evidence findable, and correct facts rather than fight opinions.

An August 2026 r/SEO thread described the pattern well. A client had built up about 15 positive Reddit reviews over two years and 1 negative comment. ChatGPT's answer about the company focused on the single negative comment and told users to be cautious. The poster got the same answer from five devices. Gemini mentioned the complaint but said most feedback was positive. The top reply suggested paying the commenter $25 to delete it, which tells you how poorly this question is served.

- **Check which index the engine uses.** ChatGPT's web search leans on Bing and Gemini on Google, which is one likely reason the two answers differed. Look up whether the positive threads are indexed in Bing at all. If they are not, the engine never saw them.
- **Find the page it actually cites.** Sometimes it is the thread itself. Often it is a scraper or review aggregator that copied the negative comment and ranks for your brand name. Fixing or answering that page does more than arguing with the model.
- **Answer the complaint in public, once, with facts.** A calm reply under the original post turns a one-sided source into a two-sided one, and engines quote both sides.
- **Make real positive evidence easy to find.** Link to the positive threads and reviews from pages that are crawled often. Keep collecting recent, genuine reviews on the platforms your buyers check. Do not pay for deletions or post fake reviews. Both are the kind of signal that ends up in the next answer about you.

## 7. All 12 pairs in one table

Each pair was asked 12 times: 2 name orders, 3 engines, 2 runs. "Page cited" counts the answers that cited at least one page on that vendor's domain.

| Pair | Favored first | Favored second | Neutral | First vendor's page cited | Second vendor's page cited |
| --- | --- | --- | --- | --- | --- |
| Asana vs Monday.com | Asana 6 | Monday.com 0 | 6 | 4 / 12 | 5 / 12 |
| ClickUp vs Asana | ClickUp 7 | Asana 0 | 5 | 12 / 12 | 4 / 12 |
| Notion vs Confluence | Notion 12 | Confluence 0 | 0 | 6 / 12 | 7 / 12 |
| HubSpot vs Salesforce | HubSpot 11 | Salesforce 0 | 1 | 9 / 12 | 10 / 12 |
| Pipedrive vs HubSpot | Pipedrive 7 | HubSpot 0 | 5 | 4 / 12 | 10 / 12 |
| Mailchimp vs Klaviyo | Mailchimp 1 | Klaviyo 0 | 11 | 7 / 12 | 9 / 12 |
| Shopify vs WooCommerce | Shopify 8 | WooCommerce 0 | 4 | 8 / 12 | 11 / 12 |
| Webflow vs Wix | Webflow 0 | Wix 10 | 2 | 4 / 12 | 4 / 12 |
| Semrush vs Ahrefs | Semrush 5 | Ahrefs 0 | 7 | 5 / 12 | 4 / 12 |
| Zendesk vs Freshdesk | Zendesk 0 | Freshdesk 10 | 2 | 10 / 12 | 9 / 12 |
| 1Password vs Bitwarden | 1Password 10 | Bitwarden 0 | 2 | 11 / 12 | 4 / 12 |
| QuickBooks vs Xero | QuickBooks 7 | Xero 2 | 3 | 10 / 12 | 8 / 12 |

## 8. Methodology

Twelve pairs of software vendors that compete head-on and publish comparison pages: project management (Asana, Monday.com, ClickUp), docs (Notion, Confluence), CRM (HubSpot, Salesforce, Pipedrive), email marketing (Mailchimp, Klaviyo), e-commerce (Shopify, WooCommerce), site builders (Webflow, Wix), SEO tools (Semrush, Ahrefs), help desk (Zendesk, Freshdesk), password managers (1Password, Bitwarden) and accounting (QuickBooks, Xero). Each pair was asked with one prompt, "{X} vs {Y}: which is better for a small business? Give a clear recommendation.", in both name orders. I ran it twice on each of three engines through OpenRouter on September 28, 2026: Perplexity Sonar, GPT-4o with OpenRouter's web search and Gemini 2.5 Flash with web search. That gave 144 answers and no errors.

A cited URL counts as a vendor page when its domain belongs to either vendor, subdomains included (quickbooks.intuit.com counts for QuickBooks, freshworks.com for Freshdesk). The verdict was labelled by a separate model, Gemini 2.5 Flash at temperature 0. It read each answer and replied with the favored product or "neutral". I read 10 randomly picked labels by hand. Eight matched my own reading. Two were borderline: one "neutral" I would have scored as a Wix win, and one QuickBooks win I would have called neutral. I kept the model's labels as they were, so the judging stays the same for every answer. The per-side analysis treats each answer twice, once from each vendor's point of view, and puts it in one of three groups: only this vendor's page cited, both cited, or neither cited. The script, the prompts and every answer's citation list are in the data file.

## 9. Limitations

This is a small test of large software brands. The verdicts may be settled for them in a way they are not for a small company that only one or two pages ever describe. The steering effect I did not find could still exist where the competitor's page is the only detailed source.

Four more. 144 answers is enough to see a 68 to 66 split as "no clear effect" and not enough to rule out a small one. One prompt wording was used, aimed at a small business. The models were reached through OpenRouter's web search, not the consumer apps, which may search and cite differently. And an LLM labelled the verdicts, so an "it depends, but..." answer could have landed either side of neutral. The claim that competitor pages spread wrong facts rests on the published mechanism and on the cases above, not on my own measurement. That is the next test to run.

## 10. Frequently asked questions

**Do AI assistants cite a competitor's comparison page when someone compares you?**

Usually. In a test of 144 answers to "X vs Y: which is better for a small business?" across Perplexity, GPT-4o and Gemini, 109 answers cited at least one page on either vendor's own domain, almost always a vs, compare or alternatives page. Those pages were 18.5% of all 1,412 citations. Perplexity cited both vendors in all 48 of its answers.

**Does a competitor's comparison page make AI recommend them over you?**

Not in this test. When one vendor's page was among the sources, the answer favored that vendor 68 times and its rival 66 times. In 11 of 12 pairs every clear verdict went the same way regardless of which page was cited or which name came first. Zendesk's own Zendesk vs Freshdesk page was cited in 10 answers and none recommended Zendesk.

**How do I stop ChatGPT repeating a false claim from a competitor's article?**

Trace the claim to the page it comes from, then decide whether it is a checkable fact or an opinion. Publish the correct fact with a date on your pricing, feature and FAQ pages, get the same fact stated on review sites, directories and partner pages, and ask the competitor to correct it. Report the answer through the platform's feedback button, then re-run the same prompts weekly for six weeks.

**Can I take legal action over a competitor's comparison page?**

Sometimes, if it makes a false statement of fact rather than an opinion. In the US, false or misleading statements of fact in commercial advertising can be challenged under section 43(a) of the Lanham Act, and competitors can file a challenge with the National Advertising Division. In the EU, Directive 2006/114/EC only permits comparative advertising that is not misleading, compares verifiable features and does not discredit the competitor. Get advice from a lawyer in your jurisdiction first.

**Should I publish my own comparison page to answer theirs?**

Publish facts, not a rebuttal. In this test the engines gave no advantage to a vendor for writing about its rival, so a hostile counter page is unlikely to change the verdict and can create legal exposure. A factual comparison that is fair to the competitor is fine. The priority is a dated block of your own facts that an engine can quote.

**How long does it take for AI answers to change after I fix the facts?**

It depends on the engine. Perplexity searches the live web on every query, so a new or corrected source can show up within days. Answers that come from a model's training data change only when the model is updated, which can take months. Measure with a fixed prompt set rather than one screenshot, because the same prompt can give a different answer from run to run.

## 11. Get the data

### All 144 answers, CC BY 4.0

The pair, name order, engine and run for every answer. Also the judged verdict, the number of citations and every cited URL on either vendor's domain, plus the per-pair and per-condition totals used on this page.

[data-summary.json](https://stanislav-peev.com/research/competitor-comparison-pages-in-ai-answers/data-summary.json) - machine readable

Citing this page: link to this URL. If a competitor's page is feeding wrong facts about you into AI answers and you are willing to share the before and after, [email me](mailto:info@stanislav-peev.com?subject=Competitor%20comparison%20page%20-%20AI%20answers). The claim-level test needs real cases.

### Sources

1. Semrush. "How to find and fix what AI gets wrong about your brand." May 2026. [semrush.com/blog/fix-ai-brand-misinformation/](https://www.semrush.com/blog/fix-ai-brand-misinformation/). Accessed September 28, 2026.
2. BBB National Programs. "National Advertising Division (NAD)" - filing tracks and case decisions. [bbbprograms.org/programs/all-programs/national-advertising-division](https://bbbprograms.org/programs/all-programs/national-advertising-division). Accessed September 28, 2026.
3. 15 U.S. Code § 1125 - False designations of origin, false descriptions, and dilution forbidden (Lanham Act § 43(a)). Legal Information Institute, Cornell Law School. [law.cornell.edu/uscode/text/15/1125](https://www.law.cornell.edu/uscode/text/15/1125). Accessed September 28, 2026.
4. Directive 2006/114/EC of the European Parliament and of the Council of 12 December 2006 concerning misleading and comparative advertising, Article 4. EUR-Lex. [eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0114](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0114). Accessed September 28, 2026.
5. r/SEO. "Influencing AI Responses." September 24, 2026. The thread that prompted this report. [reddit.com/r/SEO/comments/1wpdamq/influencing_ai_responses/](https://www.reddit.com/r/SEO/comments/1wpdamq/influencing_ai_responses/). Accessed September 28, 2026.
6. r/SEO. "Any way to fix this?" August 10, 2026. [reddit.com/r/SEO/comments/1vko1uf/any_way_to_fix_this/](https://www.reddit.com/r/SEO/comments/1vko1uf/any_way_to_fix_this/). Accessed September 28, 2026.

Published: September 28, 2026. Experiment designed, run and written up by [Stanislav Peev](https://stanislav-peev.com/). Next planned step: a claim-level test of whether AI answers repeat specific facts from vendors' comparison pages. Spotted an error? [Email me](mailto:info@stanislav-peev.com?subject=Competitor%20comparison%20pages%20-%20correction) and I will fix it and date the fix.

## Is AI repeating something wrong about your company?

I trace the claim to the page it comes from, check it across ChatGPT, Gemini, Perplexity and Google AI Mode, and build the fact layer that replaces it. Then I measure the same prompts until the answer changes. Describe your situation in a few sentences and I'll reply personally with an honest first read. No calls, no meetings.

[See GEO services](https://stanislav-peev.com/services/) [Email me](mailto:info@stanislav-peev.com?subject=AI%20answers%20about%20my%20company)

- **Email** [info@stanislav-peev.com](mailto:info@stanislav-peev.com)
- **LinkedIn** [in/stanislav-peev-seo](https://www.linkedin.com/in/stanislav-peev-seo/)
- **Based in** Bratislava, Slovakia - working worldwide

---

Stanislav Peev - contact in writing only, no calls: [info@stanislav-peev.com](mailto:info@stanislav-peev.com) · [contact form](https://stanislav-peev.com/#contact)
