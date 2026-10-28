---
title: "Why is site-wide CTR so low? Data from 15 sites (2026)"
description: "Low site-wide CTR is mostly brand mix and positions 4-10, not page 2. Search Console data from 15 sites, 2.85M impressions, plus a calculator."
url: "https://stanislav-peev.com/research/why-site-wide-ctr-is-low/"
lang: "en"
---

Research · Original data

# Why is your site-wide CTR so low? It is rarely page 2

By **Stanislav Peev**, SEO consultant & GEO specialist · Published **October 26, 2026** · 15 sites, 2.85 million impressions, 28 days of Search Console data · [Download the data (CSV)](data-sites.csv) · 13 min read

58%

**Why is my site-wide CTR so low?** Mostly because of where your impressions sit, and how few of your searches are for your name. On the median of 15 sites, positions 4 to 10 held 58% of non-branded impressions at a 1.4% CTR, while positions 1 to 3 held 19% of impressions and earned 37% of clicks. Page 2 was a much smaller drag: keeping only top-10 queries lifted the median site's non-branded CTR from just 1.2% to 1.5%.

My data: Search Console, web search, September 26 to October 23, 2026. Published benchmarks for comparison: Ahrefs (1% to 2% is typical) and Databox (0.91% median).

## Key takeaways

- **4.1% vs 1.2%** - median site-wide CTR with and without branded searches. The total you see in Search Console says more about how often people search your name than about your snippets
- **3.5% of impressions, 24% of clicks** - what branded queries contributed on the median site, at a 25% CTR. Sites with the highest site-wide CTR were the ones whose clicks came mostly from branded searches
- **58% of impressions at 1.4% CTR** - positions 4 to 10 on the median site, non-branded queries only. It was the biggest position band on 10 of the 15 sites
- **+17%** - median lift in non-branded CTR when you drop everything below position 10. Page 2 was the main drag on two sites, one with 73% of its impressions beyond position 10
- **43% of impressions are invisible** - the median share of impressions that never shows up in the query table, because Google anonymizes rare queries. Any query-level CTR analysis sees only part of the site
- **No clear drop in a year** - median site-wide CTR was 3.5% in autumn 2025 and 3.8% in autumn 2026 for the 14 sites with data in both years, though 9 of them went down

## What's in this study

1. Why I ran this
2. What is a normal site-wide CTR?
3. How much do branded searches inflate CTR?
4. Where do the non-branded impressions sit?
5. Does page 2 drag your CTR down?
6. Why your query rows do not add up
7. Did site-wide CTR fall in the last year?
8. How to diagnose a low CTR on your own site
9. Calculator: split your CTR into four groups
10. Methodology and limitations
11. Frequently asked questions

## 1. Why I ran this

In one week of October 2026, four Reddit threads asked the same thing: why does my site get so many impressions and so few clicks? Three of them reported site-wide CTRs between 0.2% and 0.6%. The answers offered advice but no numbers.

A niche content site had 275,000 impressions and about 600 clicks in 28 days, a 0.2% CTR, and asked whether to fix titles or rankings (r/SEO). Another site had 136,000 weekly impressions at 0.3% and an average position of 8.2 (r/SEO). An agency founder had 600 keywords and almost no clicks (r/SEO). A ten-year-old hobby site had 1.17 million impressions at 0.6% (r/bigseo).

The best replies said the same sensible thing: stop looking at the site-wide number, split it by position, and check the top 10 separately. Nobody showed what that split usually looks like, or how much each part moves the total. So I ran it on the Search Console data of 15 sites I work on: small business, ecommerce and information sites, mostly in Bulgarian, with some Slovak, English and Romanian search. I keep the sites anonymous. The [per-site file](data-sites.csv) labels them Site A to Site O, sorted from the lowest site-wide CTR to the highest.

## 2. What is a normal site-wide CTR?

Published benchmarks put the typical site at roughly 1% to 2%, and below 1% is common for newer sites. My 15 sites had a median of 4.1%, but only 1.2% once branded searches are removed.

| Benchmark | Sample | Site-wide CTR |
| --- | --- | --- |
| Ahrefs, June 2026 data | 422,421 websites | 1% to 2% typical |
| Databox, Search Console median | Over 4,800 companies | 0.91% |
| This study, all queries (median site) | 15 sites | 4.1% |
| This study, non-branded queries only (median site) | 15 sites | 1.2% |

The range in my sample is wide: from 0.36% to 24.5% for all queries. Two of the 15 sites were under 1% site-wide, and four were under 1% on non-branded queries. Ahrefs also found that the median rises steadily with Domain Rating, roughly six times from the weakest to the strongest sites, and reads that as recognition: people click names they know (Ahrefs, vendor). My data points the same way from a different angle, which is the next section.

So a 0.2% site-wide CTR is low, but the number alone does not show a fault. Look at what is inside it. One more caution: the published benchmarks include branded searches, so compare them with your total, and compare your non-branded CTR only with other non-branded figures, such as the ones in this study.

## 3. How much do branded searches inflate CTR?

A lot. On the median site, branded queries were 3.5% of impressions but 24% of clicks, at a 25% CTR. Sites with a bigger share of branded clicks tended to have a higher site-wide CTR, though not always.

24%

Median share of clicks from branded searches, from just 3.5% of impressions. Across all 15 sites, branded queries made up 7% of visible impressions and 45% of visible clicks.

15 sites, visible query rows, my data

The rank correlation between a site's branded click share and its site-wide CTR was 0.64: strong, with exceptions. Site M had a 10.5% site-wide CTR with only 10% of clicks branded and a 14.9% non-branded CTR. Two other sites show why the total misleads. Site O had a 24.5% site-wide CTR, the best in the sample, but 99% of its clicks were branded, and its non-branded CTR was 1.1%. Site H looked healthy at 4.1% site-wide, with 89% of its clicks branded and a non-branded CTR of 0.56%.

That is why comparing your total CTR with someone else's tells you little. A local restaurant that people search by name and a new content site that nobody knows yet can have the same snippets and very different totals. If you report CTR to a client or a boss, report non-branded CTR next to it. The same mix problem distorts other channel comparisons, for example [AI referral traffic against organic](https://stanislav-peev.com/research/ai-referral-traffic-conversion-vs-organic/).

## 4. Where do the non-branded impressions sit?

Mostly on the lower half of page 1. On the median site, positions 4 to 10 held 58% of non-branded impressions at a 1.4% CTR, while positions 1 to 3 held 19% of impressions and earned 37% of the clicks.

| Average position (non-branded, median site) | Share of impressions | Share of clicks | CTR |
| --- | --- | --- | --- |
| 1-3 | 19% | 37% | 6.6% |
| 4-5 | 12% | 21% | 2.3% |
| 6-10 | 37% | 27% | 1.1% |
| 4-10 together | 58% | 52% | 1.4% |
| 11 and deeper | 20% | 6% | 0.38% |

Position 1

12.0%

Position 2

9.0%

Position 3

4.1%

Position 4

3.4%

Position 5

2.6%

Positions 6-10

0.95%

Each cell is the median across the 15 sites, so the columns do not add up to 100%. Positions 4 to 10 were the biggest band on 10 of the 15 sites and held more than half of non-branded impressions on 8 of them. The chart pools all sites (1.64 million non-branded impressions and 32,380 clicks in positions 1 to 20), where one large site makes up about half of the impressions, so read it for the shape of the curve, not the shares. The per-site medians follow the same shape, from 11.9% at position 1 to 0.76% at position 10. Without the largest site, the pooled split is close to the median: positions 4 to 10 held 58% of impressions and 39% of clicks, positions 1 to 3 held 19% of impressions and 57% of clicks.

Most "impressions but no clicks" threads miss this. On most of these sites the bulk of impressions sits on the lower half of page 1, not on page 2: shown often but rarely clicked, under ads, AI Overviews, a map pack or a block of forum results. Average position also hides it. A query reported at position 8 can be a result that moves between 5 and 11 during the month. For the queries that also show an AI Overview, I measured the extra loss separately: [CTR fell 28% on the same query a year later](https://stanislav-peev.com/research/ai-overviews-ctr-same-query/).

## 5. Does page 2 drag your CTR down?

Not much, on most sites. Keeping only non-branded queries in the top 10 raised each site's CTR by a median of 17%; the median site's non-branded CTR went from 1.2% to 1.5% (the two medians come from different sites, which is why they differ by more than 17%). Page 2 matters on the sites where it holds a big share of impressions.

| Measure (15 sites) | Median | Range |
| --- | --- | --- |
| Share of impressions beyond position 10 | 19% | 0.4% to 73% |
| Share of impressions beyond position 20 | 4% | 0.2% to 33% |
| Share of clicks from the top 10 | 95% | 62% to 99.9% |
| Lift in non-branded CTR from dropping positions 11+ | +17% | +1% to +113% |

The share of impressions beyond position 10 still matters as a warning sign. Its rank correlation with site-wide CTR was -0.72, and the two lowest sites in the sample show it. Site A had 73% of its visible impressions beyond position 10 and a 0.36% site-wide CTR. Site B had 49% beyond position 10 and 0.96%. For sites like these, the reply in the r/bigseo thread is right: most impressions live in a tail where nobody clicks, and no title rewrite fixes that.

For the other 13 sites, page 2 was a minor part of the picture: positions 11 and deeper held a median 20% of non-branded impressions and earned 6% of the clicks. Older advice about deep impressions also predates a change: since September 9, 2025, Google no longer honors the &num=100 parameter that rank-tracking bots used to load 100 results at once, which had inflated impressions at deep positions; by November 2025 impressions were climbing again as tools adapted (Measure Minds Group, vendor). Both of my windows fall after that change, and the share of impressions beyond position 10 was 19% on the median site in both years.

## 6. Why your query rows do not add up

Because Google hides rare queries from the query table but keeps them in the totals. On the median site, visible query rows covered 57% of impressions and 48% of clicks.

Google calls these anonymized queries: searches not issued by more than a few dozen users over two to three months. They are always left out of the tables and included in the chart totals unless you filter by query (Google Search Central). That has two practical effects on a CTR analysis.

- **Your position buckets describe about half of the site.** Everything in sections 4 and 5 is based on the visible rows. The hidden half is long-tail searches you cannot see one by one.
- **The hidden half often clicks better.** On 10 of the 15 sites, the anonymized remainder had a higher CTR than the visible queries. That is why a site's top-10 CTR can come out lower than its site-wide CTR. My data does not show why; one likely reason is that rare, very specific searches often have one obvious result.

If you filter by query to split branded from non-branded traffic, the anonymized queries drop out of both sides, so the two parts will not add up to the total. That is expected, not a bug.

## 7. Did site-wide CTR fall in the last year?

Not clearly. For the 14 sites with enough data in both years, the median site-wide CTR went from 3.5% to 3.8%, but 9 of the 14 sites went down. The median top-10 CTR stayed at 3.7%.

I compared September 27 to October 24, 2025 with September 26 to October 23, 2026, the same weekdays a year apart. Site-wide CTR is a weak measure for this question, because it moves with the query mix: a site that starts ranking for a big new informational term can lose CTR while gaining traffic. When I compared the same query at the same position a year apart, the loss was clear on queries with an AI Overview and unclear on the rest ([same-query study](https://stanislav-peev.com/research/ai-overviews-ctr-same-query/)). For trend questions, use same-query comparisons, not the site-wide line.

## 8. How to diagnose a low CTR on your own site

Split the site-wide number into branded queries, non-branded positions 1 to 3, non-branded 4 to 10, and non-branded 11 and beyond (11+), then see which group holds the impressions and which one earns the clicks.

1. **Export 28 days of queries** from the Performance report or the API, with clicks, impressions and position. Note the chart totals before you filter anything.
2. **Tag branded queries**: your name, its misspellings, and brands you sell if people search for them. Track non-branded CTR as your main number, and compare it with non-branded figures such as the 1.2% median in this study, not with total-CTR benchmarks.
3. **Bucket the non-branded rows by average position**: 1-3, 4-10 and 11+. Sum clicks and impressions per bucket. The calculator below does the rest.
4. **Read the result.** If 11+ holds most of the impressions, as on Site A, the problem is ranking and relevance: prune or merge pages that rank for queries you should not target, and pause publishing new pages for a while. If 4-10 holds most of them, as on 10 of the 15 sites here, the lever is moving a smaller number of pages into the top 3, then checking the live results page of each query for AI Overviews, ads and map packs above you.
5. **Only then work on titles and descriptions**, for queries in positions 1 to 5 whose CTR is clearly below the curve in section 4. A snippet rewrite rarely helps a result that nobody scrolls to.

An [SEO audit](https://stanislav-peev.com/services/seo-audit/) that starts from this split usually finds the problem faster than one that starts from the site-wide CTR.

## 9. Calculator: split your CTR into four groups

Enter clicks and impressions from your Search Console export for each group.

Branded queries Non-branded, positions 1-3 Non-branded, positions 4-10 Non-branded, positions 11+

Pre-filled with this study's pooled visible totals (the 11+ group here covers positions 11 to 20). Nothing you type leaves your browser.

## 10. Methodology and limitations

Search Console data from 15 sites, web search, all countries and devices, September 26 to October 23, 2026, with the same window in 2025 for the year-over-year check.

- **Sites:** 15 small business, ecommerce and information sites I work on, in several verticals, mostly in Bulgarian search. Two more properties had too little data and were left out. Names, verticals and query text are withheld.
- **Totals:** daily clicks and impressions from the date dimension, which include anonymized queries: 2,853,158 impressions and 101,412 clicks in 2026.
- **Query rows:** the query dimension for the same 28 days, up to 25,000 rows per site; no site reached the limit. Position is the average position Search Console reports for the query over the period, rounded for the per-position curve.
- **Branded queries** were tagged with a keyword list per site: the site's name and its spellings, and brands the site sells when people search for them. A keyword list misses some variants.
- **Pooled vs median:** tables that say "pooled" sum all sites, so large sites weigh more. Medians are per site. Both are shown where they differ.
- **Year-over-year:** 14 sites with more than 5,000 impressions in the 2025 window.
- **Limits:** 15 sites is a small, non-random sample, heavy on Bulgarian and on small businesses; large publishers will look different. Average position is a blend, so a query at 8 may spend days at 5 and at 11. This is descriptive data, not a test of what causes CTR.
- **Data:** [data-sites.csv](data-sites.csv) (one anonymized row per site) and [data-summary.json](data-summary.json) (every number on this page), CC BY 4.0.

## 11. Frequently asked questions

**What is a normal site-wide CTR in Google Search Console?**

Most benchmarks put the typical site between about 1% and 2%. Ahrefs reports 1% to 2% as the usual range across 422,421 websites, and Databox lists a 0.91% median for Search Console CTR. In my 15 sites the median was 4.1% for all queries but 1.2% for non-branded queries, because a few branded searches with very high CTR lift the total.

**Why do I have lots of impressions but a very low CTR?**

Usually because most of your impressions sit in positions 4 to 10, not on page 2. On the median site in my data, positions 4-10 held 58% of non-branded impressions at a 1.4% CTR, while positions 1-3 held 19% of impressions and earned 37% of clicks. A site with almost no branded searches will also look low, since branded queries carry a large share of clicks.

**Does page 2 drag down my CTR?**

Less than most people think. Keeping only non-branded queries in the top 10 raised CTR by a median of 17% across my 15 sites, from 1.2% to 1.5%. Page 2 matters only on sites where it holds a big share of impressions; on one site, 73% of impressions were beyond position 10 and its site-wide CTR was 0.36%.

**How much do branded searches affect site-wide CTR?**

A lot. Branded queries were a median 3.5% of impressions but 24% of clicks, with a median CTR of 25%. Sites with a bigger branded share of clicks tended to have a higher site-wide CTR, so compare non-branded CTR with non-branded CTR, not totals.

**Why don't my Search Console query rows add up to the total?**

Because Google hides anonymized queries (those not issued by more than a few dozen users over two to three months) from the query table but keeps them in the chart totals. In my sites the visible query rows covered a median 57% of impressions and 48% of clicks, so any analysis by query sees only part of the site.

**Has site-wide CTR dropped in the last year?**

Not clearly in my data. For 14 sites with data in both years, the median site-wide CTR was 3.5% in autumn 2025 and 3.8% in autumn 2026, though 9 of the 14 sites went down. Same-query comparisons show a clearer loss where an AI Overview appears, which I measured separately.

## Sources

1. r/SEO. "Getting 200k+ Google impressions but only 0.2% CTR. What should I improve?" October 25, 2026. [reddit.com/r/SEO/comments/1xf4lgy/getting_200k_google_impressions_but_only_02_ctr/](https://www.reddit.com/r/SEO/comments/1xf4lgy/getting_200k_google_impressions_but_only_02_ctr/). Accessed October 26, 2026.
2. r/SEO. "How do I get more clicks on AI overviews?" October 21, 2026. [reddit.com/r/SEO/comments/1xbkpaq/how_do_i_get_more_clicks_on_ai_overviews/](https://www.reddit.com/r/SEO/comments/1xbkpaq/how_do_i_get_more_clicks_on_ai_overviews/). Accessed October 26, 2026.
3. r/SEO. "6 months of SEO on a competitive agency niche: 600+ keywords, tons of impressions, almost no clicks." October 22, 2026. [reddit.com/r/SEO/comments/1xca0da/6_months_of_seo_on_a_competitive_agency_niche_600/](https://www.reddit.com/r/SEO/comments/1xca0da/6_months_of_seo_on_a_competitive_agency_niche_600/). Accessed October 26, 2026.
4. r/bigseo. "Have 1.17M impression, 0.6 CTR. How can I improve my CTR?" October 26, 2026. [reddit.com/r/bigseo/comments/1xfo8z7/have_117m_impression_06_ctr_how_can_i_improve_my/](https://www.reddit.com/r/bigseo/comments/1xfo8z7/have_117m_impression_06_ctr_how_can_i_improve_my/). Accessed October 26, 2026.
5. Ryan Law, Ahrefs. "What is a Good Organic CTR? Real Website Benchmarks (July 2026)." Search Console data from 422,421 websites. June 22, 2026, updated monthly. *Vendor: sells SEO or analytics products.* [ahrefs.com/blog/what-is-a-good-ctr/](https://ahrefs.com/blog/what-is-a-good-ctr/). Accessed October 26, 2026.
6. Databox. "Organic and Paid CTR Benchmarks." Data contributed by over 4,800 companies; Google Search Console median CTR. Last updated October 26, 2026. *Vendor: sells SEO or analytics products.* [databox.com/benchmarks/ctr-benchmarks](https://databox.com/benchmarks/ctr-benchmarks). Accessed October 26, 2026.
7. Daniel Waisberg, Google Search Central Blog. "A deep dive into Search Console performance data filtering and limits." October 19, 2022. [developers.google.com/search/blog/2022/10/performance-data-deep-dive](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive). Accessed October 26, 2026.
8. Alex Szwabowicz, Measure Minds Group. "Google Search Console September 2025: Why Have Impressions Dropped & Rankings Improved?" September 16, 2025, updated November 19, 2025. *Vendor: sells SEO or analytics products.* [measuremindsgroup.com/gsc-impressions-dropped-rankings-improved](https://measuremindsgroup.com/gsc-impressions-dropped-rankings-improved). Accessed October 26, 2026.

Last updated: October 26, 2026. Related research: [all studies](https://stanislav-peev.com/research/).

---

Stanislav Peev - contact in writing only, no calls: [info@stanislav-peev.com](mailto:info@stanislav-peev.com) · [contact form](https://stanislav-peev.com/#contact)
