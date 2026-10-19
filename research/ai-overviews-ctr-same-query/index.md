---
title: "AI Overviews CTR: same query, one year later (2026)"
description: "How much do AI Overviews cut CTR? Same query, same position, a year apart: -28% with an AI Overview, -10% without. 280 queries, 13 sites."
url: "https://stanislav-peev.com/research/ai-overviews-ctr-same-query/"
lang: "en"
---

Research · Original data

# How much do AI Overviews cut your CTR? Same query, one year apart

By **Stanislav Peev**, SEO consultant & GEO specialist · Published **October 19, 2026** · 1,529 queries from 15 sites, each checked on a live mobile results page · [Download the data (CSV)](data-queries.csv) · 13 min read

-28%

**How much do AI Overviews cut click-through rate?** On the same query at the same position a year apart, CTR fell 28% where Google now shows an AI Overview, and changed by a statistically unclear -10% where it does not. That is 280 mobile queries from 13 sites, mostly in Bulgarian. I have not found another same-query study in a non-English market.

My data: Search Console, September 19 to October 16, 2025 vs 2026, with a mobile SERP check on October 19, 2026. 95% intervals: -36% to -18% with an AI Overview, -24% to +6% without. Points the same way as Ahrefs and a randomized field experiment, both on US data.

## Key takeaways

- **-28% vs -10%** - year-over-year CTR change on the same query at a stable position, with and without an AI Overview today (280 query pairs, 13 sites). Only the first is clearly different from zero, and the gap between the two groups is not itself statistically established
- **+54% impressions, -12% clicks** - what happened on the AI Overview queries. Most of the CTR drop is impressions growing while clicks shrink a little, which is exactly the "impressions but no clicks" pattern people keep asking about
- **-35%** - the CTR change for top-3 positions with an AI Overview, against -16% for positions 4-10. The top results lost more in this sample, though the intervals overlap
- **Being cited showed no sign of protecting CTR** - queries where the site was a source inside the AI Overview lost 32% of CTR, queries where it was not lost 24%. The intervals overlap
- **71%** - share of non-branded page-one queries that showed an AI Overview on mobile: 74% in Bulgarian, 55% in Slovak, 80% in English
- **19% vs 79%** - AI Overview rate on queries with a local map pack against queries without one. Local searches still mostly get the map, not the overview
- **4.7x the wrong way** - if you simply split Search Console queries into "with" and "without" an AI Overview, the AI Overview queries show 4.7 times the CTR. That comparison measures query types, not the AI Overview, and it is the most common mistake I see

## What's in this study

1. Why I ran this
2. How much CTR did queries with an AI Overview lose?
3. Why impressions went up while clicks went down
4. Which positions lost the most?
5. Does being cited in the AI Overview save the click?
6. How often do AI Overviews show in Bulgarian, Slovak and English?
7. Why the simple "with vs without" split gives the wrong answer
8. How to measure it on your own site
9. Calculator: your same-query CTR gap
10. Methodology and limitations
11. Frequently asked questions

## 1. Why I ran this

Search Console counts a click on an AI Overview link as an ordinary click and does not split it out, so site owners see rankings improve while clicks stay flat and cannot tell how much the AI Overview is to blame.

The question kept coming up in Reddit threads in the first half of October 2026. In r/localseo someone noted that Google says AI Overviews now show more links higher up, while Search Console still shows no separate click data for them. In r/SEO a B2B manufacturer's average position went from 17.7 to 11.7 and traffic did not move. Another r/SEO thread asked why a site gets impressions but almost no clicks. The answers repeated numbers from US studies, and nobody could say what happens in a smaller, non-English market.

Search Console's own documentation explains part of the blindness. A click on an external link in an AI Overview counts as a click, standard impression rules apply, and the whole AI Overview takes one position, so every link inside it shares that position (Google Search Console Help). You cannot filter those clicks out. What you can do is compare the same query with itself over time, which is what I did with the Search Console data of 15 sites I work on. I keep the sites anonymous; the [query-level file](data-queries.csv) has no query text and no site names.

## 2. How much CTR did queries with an AI Overview lose?

About 28%. For the same query at an average position that moved less than one place, mobile CTR fell from one year to the next by 28% on queries that show an AI Overview today, against -10% on queries that do not, and only the first change is clearly different from zero.

| Group (same query, stable position) | Queries | CTR change, Sep-Oct 2025 to Sep-Oct 2026 | 95% interval |
| --- | --- | --- | --- |
| AI Overview shown today | 203 | -28% | -36% to -18% |
| No AI Overview today | 77 | -10% | -24% to +6% |
| Bulgarian only, AI Overview | 179 | -31% | -40% to -21% |
| Bulgarian only, no AI Overview | 58 | -15% | -30% to +2% |

The change is the geometric mean of per-query CTR ratios, so one big query cannot drive it. The median query tells the same story: -32% with an AI Overview, -4% without. Seven of the eight sites with at least 7 query pairs lost CTR on their AI Overview queries, and the median site lost 41%. The one exception gained CTR on its 20 pairs.

AI Overview, all positions

-28%

AI Overview, top 3

-35%

AI Overview, site cited

-32%

AI Overview, site not cited

-24%

No AI Overview

-10%

The size fits what larger US studies found. Ahrefs compared 150,000 keywords with an AI Overview against 150,000 informational keywords without one and estimated that an AI Overview now goes with a 58% lower CTR for the top result, using December 2023 and December 2025 data (Ahrefs, vendor). A randomized experiment with 1,065 US desktop Chrome users found outbound organic clicks fell 39.8% when an AI Overview appeared (Agarwal and Sen, via PPC Land). My -28% is smaller, and two reasons are likely: I measure one year, not two, and some of these queries probably already had an AI Overview in autumn 2025, so part of the loss had happened before my baseline.

## 3. Why impressions went up while clicks went down

On the queries that show an AI Overview, impressions grew 54% while clicks fell 12%, so the CTR collapse is mostly a growing denominator. On queries without one, impressions and clicks fell together and CTR barely moved.

| Same-query pairs | Impressions 2025 | Impressions 2026 | Clicks 2025 | Clicks 2026 |
| --- | --- | --- | --- | --- |
| AI Overview today (203) | 66,383 | 101,955 (+54%) | 5,911 | 5,217 (-12%) |
| No AI Overview (77) | 101,081 | 72,931 (-28%) | 1,210 | 881 (-27%) |

+54%

More impressions for the same queries at the same positions, with fewer clicks. If your Search Console shows this shape, an AI Overview is the first thing to check.

203 query pairs, mobile, my data

I cannot tell from Search Console alone why the impressions grew, and I would not claim one cause. Two readings fit the data, and I cannot separate them. Demand for these informational queries may have grown, with the extra searchers getting their answer on the results page. And because an AI Overview link inherits the overview's position (Search Console Help), a site that appears both inside the overview and below it may collect impressions from people who never scroll to the blue link. Either way, the practical point is the same: "more impressions, same rank, no new clicks" can be a sign of an AI Overview, so check the live results page before you assume a technical fault.

## 4. Which positions lost the most?

The top three, in this sample, though the intervals overlap. With an AI Overview, CTR for queries in positions 1 to 3 fell 35%, while positions 4 to 10 fell 16% with an interval that crosses zero.

| Position band (AI Overview queries) | Queries | CTR change | 95% interval |
| --- | --- | --- | --- |
| Positions 1-3 | 115 | -35% | -44% to -24% |
| Positions 4-10 | 88 | -16% | -33% to +4% |

This matches the shape Ahrefs reported for US keywords, where the estimated loss falls from 58% at position 1 to 50.8% at position 2 and 32.6% at position 5 (Ahrefs). The top result had the most clicks to give away. If you rank first for an informational query, plan for the loss there first; that is also where a [reliable AI visibility measurement](https://stanislav-peev.com/research/ai-visibility-tracking-reliability/) matters more than a rank report.

## 5. Does being cited in the AI Overview save the click?

Not in this data. Where the site was one of the sources inside the AI Overview, CTR fell 32%; where it was not, CTR fell 24%. The intervals overlap, so being cited did not protect the click.

On the October snapshot, sites were cited in 47% of the AI Overviews that appeared for their queries, and the median overview listed 7 source links. A plain comparison makes citation look powerful: cited queries had a 5.9% CTR, uncited ones 2.3%. But cited queries also ranked higher. Comparing only queries in the top three, the gap shrinks to 12.2% against 9.0%, and the 95% interval for that ratio (0.91 to 2.30) includes no difference at all.

That is consistent with how people use the feature. Pew Research tracked 900 US adults and found that people who saw an AI summary clicked a link inside the summary on just 1% of visits, and clicked a regular result on 8% of visits against 15% when no summary appeared (Pew Research Center). A citation is a visibility win and worth having for brand reasons, as I found when testing [which pages AI answers cite](https://stanislav-peev.com/research/ai-citations-by-query-shape/). It is not a click guarantee.

## 6. How often do AI Overviews show in Bulgarian, Slovak and English?

Often. On October 19, 2026, an AI Overview appeared on 71% of the non-branded mobile queries where these sites rank on page one: 74% in Bulgarian, 55% in Slovak and 80% in English.

| Segment (non-branded, page one, mobile) | Queries | AI Overview shown |
| --- | --- | --- |
| All | 1,317 | 71% |
| Bulgarian | 922 | 74% |
| Slovak | 191 | 55% |
| English (UK and US) | 176 | 80% |
| Romanian (small sample) | 28 | 36% |
| Question queries ("how", "what", "why" and their equivalents) | 72 | 97% |
| One-word queries | 244 | 55% |
| Four words or more | 444 | 83% |
| Queries with a local map pack | 168 | 19% |
| Queries without a local map pack | 1,149 | 79% |
| Branded queries (excluded elsewhere) | 212 | 67% |

These are not shares of all searches. They are shares of the queries where these sites already get seen, which lean informational, so they run higher than the 18% of US searches with an AI summary in Pew's March 2025 panel (Pew) or the roughly 41% in the field experiment (Agarwal and Sen). The direction is the same as Pew's: longer queries and question queries trigger an overview far more often. Pew saw 8% for one- or two-word searches and 53% for ten words or more.

The local finding deserves its own line. When Google showed a map pack, it showed an AI Overview only 19% of the time. For a plumber or a dentist, the map is still the main battleground, which is why [who wins the map pack](https://stanislav-peev.com/research/google-review-concentration-home-services/) and [local SEO basics](https://stanislav-peev.com/services/small-business-seo/) matter more than chasing overview citations.

## 7. Why the simple "with vs without" split gives the wrong answer

Because AI Overview queries are not a random sample of queries. In a single snapshot, my AI Overview queries had 4.7 times the CTR of the rest, and even after matching by site, position and map pack they got 1.23 times the clicks you would expect, so a one-period split measures query types, not the overview.

| Position (snapshot, non-branded) | CTR with AI Overview | CTR without | Queries with / without |
| --- | --- | --- | --- |
| 1 | 20.5% | 9.0% | 104 / 20 |
| 2 | 11.2% | 6.3% | 99 / 17 |
| 3 | 5.1% | 5.0% | 57 / 13 |
| 4-5 | 3.7% | 2.2% | 158 / 60 |
| 6-10 | 1.6% | 0.5% | 518 / 271 |

Read naively, this table says AI Overviews double your CTR. They do not. The queries without an overview here are mostly short head terms, such as a single broad term, and local searches with a map pack. Those queries get huge impressions and tiny CTR for reasons that have nothing to do with AI. The fair test compares a query with itself, which is section 2. If a tool or a report shows you a with-vs-without split from one period, treat it as a description of your query mix, not as the cost of AI Overviews.

The same trap catches people comparing [AI referral traffic with organic traffic](https://stanislav-peev.com/research/ai-referral-traffic-conversion-vs-organic/): the groups differ before the feature does anything.

## 8. How to measure it on your own site

Export the same 28 days from this year and last year by query, keep queries whose average position moved less than one place, check which of them show an AI Overview today, and compare the CTR change of the two groups.

1. **Pick two identical windows a year apart**, for example September 19 to October 16 in both years, so seasonality cancels out. Filter to one country and one device; mobile and desktop SERPs differ.
2. **Export queries with impressions and clicks** for both windows. Drop branded queries; they behave differently and an AI Overview rarely stops someone who wants your site.
3. **Keep stable pairs**: at least 20 impressions in both windows and an average position within one place of last year. Otherwise you are measuring ranking changes.
4. **Check the SERP today** for each remaining query, in the right country and language and on the same device, and record whether an AI Overview shows. A rank tracker or SERP API that loads the overview does this; checking by hand works for a few dozen queries.
5. **Compare the CTR change** of the two groups, using the calculator below. The difference between them is a descriptive gap, not a clean measure of the effect: the no-overview group is a rough comparison group for everything else that changed in a year, not a true control.

If the gap is large and your top informational pages sit in the overview group, the work moves from ranking to what earns the click: content an overview cannot summarise in two lines, such as [original comparisons](https://stanislav-peev.com/research/competitor-comparison-pages-in-ai-answers/), tools and first-party data, and pages that convert the smaller, more decided group that still clicks. An [SEO audit](https://stanislav-peev.com/services/seo-audit/) that starts from this split is more useful than one that starts from average position.

## 9. Calculator: your same-query CTR gap

Enter totals for your stable query pairs, last year and this year, for queries that show an AI Overview today and for queries that do not.

AI Overview queries Queries without an AI Overview

Pre-filled with this study's totals, which give -43% and +1%. Pooled totals let a few large queries dominate, which is why the study itself reports per-query ratios (-28% and -10%). For your own site, the pooled figure is a quick first read. Nothing you type leaves your browser.

## 10. Methodology and limitations

Search Console data from 15 sites, mobile only, one country per site, compared with a DataForSEO mobile SERP check on October 19, 2026; the year-over-year test uses 280 stable query pairs from 13 sites.

- **Sites:** 15 small business, ecommerce and information sites I work on, in several verticals and four languages, most of them in Bulgarian. Names, verticals per site and query text are withheld.
- **Search Console:** query dimension, each site's top country, device = mobile, September 19 to October 16 in 2025 and 2026. Selection: at least 20 mobile impressions and average position 10.5 or better in 2026, up to 150 queries per site by impressions, 1,529 queries in total.
- **SERP check:** one Google mobile (Android) result page per query on October 19, 2026, through the DataForSEO SERP API with asynchronous AI Overview loading on, in the site's country and language. I recorded whether an AI Overview, a local pack or a featured snippet showed and whether the site was among the overview's sources.
- **Branded queries** (the site's name, or a brand the site sells) were tagged by keyword list and kept out of the main analysis: 212 queries, leaving 1,317.
- **Year-over-year pairs:** same query with at least 20 impressions in both windows and an average position within 1.0 of the previous year: 280 pairs (203 with an AI Overview today, 77 without). The change is the geometric mean of per-query CTR ratios with 0.5-click smoothing, with 95% bootstrap intervals from 4,000 resamples.
- **Biggest limitation:** I know whether a query shows an AI Overview today, not when it started. Queries that already had one in 2025 likely make my estimate smaller than the true effect. AI Overviews also vary by user and by day, and one snapshot per query will misclassify some.
- **Other limits:** 13 to 15 sites is a small and non-random sample, heavy on Bulgarian; the Slovak, English and Romanian slices are too small for their own conclusions. Other changes between 2025 and 2026, such as other SERP features or Google updates, hit both groups, which is why the no-overview group serves as a rough comparison group. This is observational data, not an experiment.
- **Data:** [data-queries.csv](data-queries.csv) (one row per non-branded query, anonymised) and [data-summary.json](data-summary.json) (every number on this page), CC BY 4.0. Planned refresh: spring 2027, with a second SERP snapshot to catch queries that gain or lose the overview.

## 11. Frequently asked questions

**How much do AI Overviews reduce click-through rate?**

In my data, about 28% on the same query at the same position from one year to the next, against about 10% for queries without an AI Overview, which is within noise. That covers 280 mobile query pairs from 13 sites, mostly Bulgarian, autumn 2025 vs autumn 2026. US studies point the same way: Ahrefs estimates 58% for the top result over two years, and a randomized field experiment found outbound organic clicks fell 39.8%.

**Does Search Console show clicks from AI Overviews?**

Yes, but not separately. Google's Search Console Help says a click on an external link in an AI Overview counts as a click, standard impression rules apply, and the whole overview takes a single position that every link inside it shares. There is no filter for those clicks, so the practical way to estimate the effect is to compare the same queries over time.

**Why do I get impressions but no clicks?**

One common reason is an AI Overview above your result. On the queries in this study that show one, impressions rose 54% year over year while clicks fell 12%, at unchanged positions. Check the live results page for your top queries before you look for a technical fault.

**Does being cited in an AI Overview bring the clicks back?**

No sign of it in this data. Queries where the site was cited inside the AI Overview lost 32% of CTR, queries where it was not lost 24%, and the difference is within noise. Pew Research found people click a link inside an AI summary on about 1% of visits. A citation helps visibility; it is not a click guarantee.

**How often do AI Overviews appear in Bulgarian or other smaller languages?**

Often, on the queries where these sites rank. On October 19, 2026 an AI Overview showed on 74% of the non-branded page-one mobile queries of the Bulgarian sites in this study, 55% for the Slovak sites and 80% for the English ones. Question queries got one 97% of the time; queries with a local map pack only 19%.

**Is comparing queries with and without an AI Overview a good way to measure the impact?**

Only if you compare each query with itself over time. In a single snapshot, my AI Overview queries had 4.7 times the CTR of the others, because the queries without an overview were mostly short head terms and local searches with naturally low CTR. A one-period split describes your query mix, not the cost of AI Overviews.

## Sources

1. r/localseo. "Google says AI Overviews/AI Mode now show more inline links higher up, but Search Console still won't show click data for them." October 15, 2026. [reddit.com/r/localseo/comments/1x7001m/google_says_ai_overviewsai_mode_now_show_more/](https://www.reddit.com/r/localseo/comments/1x7001m/google_says_ai_overviewsai_mode_now_show_more/). Accessed October 19, 2026.
2. r/SEO. "B2B manufacturing SEO: rankings are improving, but organic traffic has plateaued." October 16, 2026. [reddit.com/r/SEO/comments/1x7nb27/b2b_manufacturing_seo_rankings_are_improving_but/](https://www.reddit.com/r/SEO/comments/1x7nb27/b2b_manufacturing_seo_rankings_are_improving_but/). Accessed October 19, 2026.
3. r/SEO. "Why would a site get impressions but almost no clicks?" October 6, 2026. [reddit.com/r/SEO/comments/1wyrqqq/why_would_a_site_get_impressions_but_almost_no/](https://www.reddit.com/r/SEO/comments/1wyrqqq/why_would_a_site_get_impressions_but_almost_no/). Accessed October 19, 2026.
4. Google Search Console Help. "What are impressions, position, and clicks?" Section on AI Overviews and AI Mode. [support.google.com/webmasters/answer/7042828?hl=en](https://support.google.com/webmasters/answer/7042828?hl=en). Accessed October 19, 2026.
5. Ahrefs. "Update: AI Overviews reduce clicks by 58%." 300,000 keywords (150,000 with an AI Overview, 150,000 informational without), December 2023 vs December 2025. *Vendor: sells SEO products.* [ahrefs.com/blog/ai-overviews-reduce-clicks-update/](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/). Accessed October 19, 2026.
6. Pew Research Center. "Google users are less likely to click on links when an AI summary appears in the results." Browsing data of 900 US adults, March 2025. July 22, 2025. [pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/). Accessed October 19, 2026.
7. PPC Land. "Researchers find Google AI Overviews cut publisher clicks 39.8%." On Agarwal and Sen, "The Impact of Google AI Overviews on Publisher Traffic and User Experience: Evidence from a Field Experiment," SSRN, April 3, 2026, revised June 17, 2026. [ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/](https://ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/). Accessed October 19, 2026.

Last updated: October 19, 2026. Related research: [all studies](https://stanislav-peev.com/research/).

---

Stanislav Peev - contact in writing only, no calls: [info@stanislav-peev.com](mailto:info@stanislav-peev.com) · [contact form](https://stanislav-peev.com/#contact)
