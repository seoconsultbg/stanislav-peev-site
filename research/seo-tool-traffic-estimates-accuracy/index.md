---
title: "How accurate are SEO traffic estimates? 15 sites vs GSC"
description: "A keyword-based tool estimated 35% of real Search Console clicks on the median of 15 sites. Where totals matched, it was by accident. Data and a calculator."
url: "https://stanislav-peev.com/research/seo-tool-traffic-estimates-accuracy/"
lang: "en"
---

Research · Original data

# How accurate are SEO tool traffic estimates? 15 sites against Search Console

By **Stanislav Peev**, SEO consultant & GEO specialist · Published **November 2, 2026** · 15 sites, 101,141 real clicks, October 2026 · [Download the data (CSV)](data-sites.csv) · 12 min read

35%

**How accurate are SEO tool traffic estimates?** Not very, at least in my sample, which is mostly Bulgarian. On the median of 15 sites, a keyword-based estimator put organic traffic at 35% of the clicks Search Console recorded in October 2026. Across all 15 sites it estimated 48,720 visits against 101,141 real clicks. Where the total came close, it was mostly luck: the tool overestimated the keywords it knew and missed most of the others.

My data: Search Console clicks, each site's main country, October 1 to 30, 2026, against DataForSEO Labs estimates for the same country. Earlier studies for comparison: Ahrefs (49.52% median deviation, U.S.) and Screaming Frog (25 sites, mainly UK).

## Key takeaways

- **35% of real clicks** - the median estimate across 15 sites. Nine sites were estimated at less than half of their real traffic, two at less than a tenth
- **2.4 times too high** - the estimate for the 3,318 keywords that both the tool and Search Console knew: 47,109 estimated visits against 19,433 real clicks. 12 of the 15 sites were overestimated on these keywords
- **81% of clicks were invisible to the tool** - 40% came from anonymized queries that no keyword database can hold, and another 40% from named queries the tool did not list
- **Six "accurate" totals were accidents** - every site estimated within 25% of reality had its known keywords overestimated and its long tail missed. The two errors cancelled out
- **Small languages fare worst** - 9 of the 10 Bulgarian sites were estimated at under half of their clicks; all five Slovak, Romanian, UK and U.S. sites landed between 76% and 117%
- **The order of sites mostly holds** - rank correlation 0.71 between estimate and real clicks, close to what Ahrefs reported for the U.S., with some pairs badly wrong

## What's in this study

1. Why I ran this
2. What earlier studies found
3. How far off were the estimates?
4. Why an accurate total can still be wrong
5. What the tool cannot see
6. Can you still compare sites with it?
7. How to check a tool against your own data
8. Calculator: your correction factor
9. Methodology and limitations
10. Frequently asked questions

## 1. Why I ran this

A business owner asked on Reddit why Semrush and Ahrefs showed about a tenth of the traffic Search Console reported, and whether that meant their SEO agency was doing something wrong. The replies agreed the tools were unreliable, but nobody showed how unreliable, or in which direction.

The site had 20,000 to 30,000 monthly visits in GA4, Semrush estimated about one tenth of the Search Console figure, and neither tool showed keywords the owner could see ranking near the top (r/SEO, also posted in r/bigseo). The best reply explained the mechanism: the tools only know the queries in their own database and multiply volume by a modelled click rate. That is also how DataForSEO defines its metric: estimated traffic is the product of CTR and search volume across all the keywords a domain ranks for (DataForSEO, vendor).

So I measured it. I took 15 sites I work on, mostly in Bulgarian search, with some Slovak, Romanian, UK and U.S. traffic, and compared October 2026 Search Console clicks in each site's main country with the estimate for the same country from DataForSEO Labs. I keep the sites anonymous. The [per-site file](data-sites.csv) labels them Site A to Site O, from the most underestimated to the most overestimated.

## 2. What earlier studies found

The published tests are mostly English-language and several years old. They found typical errors of roughly 20% to 70%, and the one that tested small sites found them estimated worse.

| Study | Sample | Finding |
| --- | --- | --- |
| Ahrefs, 2022 | 1,635 sites, U.S. traffic | Median deviation 49.52% for Ahrefs, 68.36% for Semrush; correlation with GSC 0.76 and 0.74 |
| Authority Hacker, as cited by Ahrefs | 50 sites | Six tools compared; Ahrefs first, with a 22.5% average discrepancy |
| Screaming Frog, 2016 | 25 sites, mainly UK | Ahrefs 36% and Semrush 42% under on average; SimilarWeb 1% over |
| This study, 2026 | 15 sites, BG, SK, RO, UK, U.S. | Median estimate 35% of real clicks |

Two of these come from tool vendors. Ahrefs notes that its error depends heavily on the site and industry, from under 5% to more than 1,000% (Ahrefs, vendor). Screaming Frog found that for its three sites with under 10,000 organic visits, almost every tool's estimate was at least 40% wrong, and that one site living on long-tail local phrases was underestimated by all three (Screaming Frog, vendor). I found no published test for small-language markets like Bulgarian or Slovak, which is where most of my sample sits.

## 3. How far off were the estimates?

Far. The median site was estimated at 35% of its real clicks. Nine of the 15 sites were below half, six landed within 25% of reality, and only two were overestimated.

Site A (BG)

1.8%

Site B (BG)

5.9%

Site C (BG)

12%

Site D (BG)

24%

Site E (BG)

25%

Site F (BG)

27%

Site G (BG)

35%

Site H (BG)

35%

Site I (BG)

41%

Site J (SK)

76%

Site K (US)

80%

Site L (BG)

95%

Site M (RO)

100%

Site N (SK)

107%

Site O (UK)

117%

The worst case is the Reddit question in extreme form. Site A had 5,025 clicks in Bulgaria in October, from 258 different queries with at least one click. The tool listed one ranking keyword for it and estimated 92 visits, less than 2% of reality. Site B was estimated at 142 visits against 2,420 clicks.

| Market of the site | Sites | Real clicks | Estimate | Median estimate / real |
| --- | --- | --- | --- | --- |
| Bulgaria | 10 | 83,007 | 32,254 | 26% |
| Slovakia | 2 | 5,914 | 4,844 | 91% |
| Romania | 1 | 8,697 | 8,679 | 100% |
| United Kingdom | 1 | 327 | 381 | 117% |
| United States | 1 | 3,196 | 2,561 | 80% |

All nine of the lowest ratios belong to Bulgarian sites. Five non-Bulgarian sites are too few to call a pattern, but the direction fits what earlier tests suspected: a keyword database is thinner where fewer people search, so the estimate falls short. The next section shows why the near-perfect totals for the other markets should not reassure you.

## 4. Why an accurate total can still be wrong

Because the tool overestimated the keywords it knew and missed most of the others. On the 3,318 keywords both sources had, it estimated 2.4 times the real clicks. Every site whose total landed within 25% shows the same pattern.

2.4x

Estimated visits on keywords the tool and Search Console both knew: 47,109 estimated against 19,433 real clicks. On the median site the overestimate was 2.7 times, and 12 of 15 sites were over.

15 sites, exact keyword matches in each site's main country, my data

Take Site L. Its total estimate was 18,014 visits against 19,022 real clicks, 95% of reality, the kind of number that makes a tool look trustworthy. But 17,434 of those estimated visits sat on keywords that brought 4,559 real clicks in October. The other three quarters of its traffic came from searches the tool did not list. Site M, estimated at exactly 100%, follows the same pattern: 8,551 estimated visits on keywords that earned 3,178 clicks.

| Keyword-level check (897 keywords with an estimate of 5+ visits) | Keywords | Share |
| --- | --- | --- |
| Estimate more than double the real clicks | 756 | 84% |
| Estimate within half to double of real clicks | 112 | 12% |
| Estimate below half of real clicks | 29 | 3% |
| Of these, keywords with zero real clicks in October | 357 | 40% |

My data does not show why the per-keyword estimates run high, and part of it is how I matched them: clicks on a spelling variant of a keyword do not count toward it here. Two likely causes are inflated volumes for small markets and a click curve that assumes a clean results page. Real pages carry ads, maps, forums and AI Overviews; I measured how much an AI Overview alone takes in [my study of the same queries a year apart](https://stanislav-peev.com/research/ai-overviews-ctr-same-query/). The positions also differed: on keywords in both sources, the tool's rank and the Search Console average position had a median gap of under 1 to 8 places, depending on the site.

## 5. What the tool cannot see

Most of the traffic. Across the 15 sites, 81% of real clicks came from keywords the tool did not list. Half of that is anonymized queries that Google hides from every tool, the other half named queries missing from the tool's database.

| Where the 101,141 real clicks came from | Clicks | Share |
| --- | --- | --- |
| Keywords both the tool and Search Console list | 19,433 | 19% |
| Named queries in Search Console that the tool does not list | 40,936 | 40% |
| Anonymized queries (only in Search Console totals) | 40,772 | 40% |

Anonymized queries are searches not issued by more than a few dozen users over two to three months. Google leaves them out of the query table to protect privacy but keeps them in the totals (Google Search Central). A keyword database built from search volumes cannot contain them, so any tool will miss this part of a site, and it was large here: a median 48% of clicks per site. The same hidden share distorts CTR analysis, as I showed in [why site-wide CTR is low](https://stanislav-peev.com/research/why-site-wide-ctr-is-low/).

The named queries the tool missed are its own gap. On the median site, the tool listed 40% as many ranking keywords as the site had queries with at least one click, and the keywords it did list carried 37% of the clicks on named queries. Site E is a clear case: 1,917 queries with clicks in October and 100 keywords in the tool.

## 6. Can you still compare sites with it?

Roughly, and only within one market and one tool. The rank correlation between estimate and real clicks across my 15 sites was 0.71, near the 0.76 Pearson correlation Ahrefs reported for U.S. sites (a different measure). Single comparisons can be badly wrong.

A correlation of 0.71 means that a bigger site usually gets a bigger estimate. It does not mean any two sites will be ordered correctly. Site A, with 5,025 real clicks, was estimated at 92 visits; Site I, with 216 clicks, was estimated at 88. On the tool's numbers they were the same size. In reality, one had 23 times the other's traffic. Ahrefs makes the same point, framed in its own favor: the estimates are more consistent than they are accurate, especially within one industry (Ahrefs, vendor).

That is enough for a quick look at who leads a market. It is not enough to value a site you want to buy, to forecast what a client will get, or to judge whether an agency delivered. For those, ask for the Search Console data.

## 7. How to check a tool against your own data

Compare the tool's estimate for your own domain with your Search Console clicks for the same country and month. The ratio tells you how far to trust that tool in your market.

1. **Take 30 days of Search Console clicks** for your main country, web search only. Do not use GA4 all channels: as replies in the r/bigseo thread pointed out, Search Console counts only Google organic clicks, so compare it with the Organic Search channel in GA4.
2. **Look up your domain in the tool** for the same country and note its estimated monthly organic traffic and the number of keywords it says you rank for.
3. **Divide the estimate by your clicks.** Under 0.5 means the tool estimates less than half of your real clicks; that was 9 of my 15 sites.
4. **Count your queries with at least one click** in Search Console and compare with the tool's keyword count. A low share means it misses your long tail.
5. **Before trusting a "good" total**, open the tool's top keywords and compare each with Search Console clicks. If they are overestimated two or three times, the total is right by accident, as on Sites L and M.
6. **Use the ratio on competitors** in the same market and tool, as a rough correction, not a measurement.

If you are judging an agency, the tool gap is not evidence either way. Search Console clicks, the pages they land on, and the enquiries they bring are. An [SEO audit](https://stanislav-peev.com/services/seo-audit/) should start from that data, not from a third-party estimate.

## 8. Calculator: your correction factor

Enter your numbers for one country and one month.

Your site Keyword coverage (optional) Competitor (optional)

Pre-filled with Site G from this study. The competitor figure divides by your own ratio, so it assumes the tool misses the competitor's traffic as much as yours. Nothing you type leaves your browser.

## 9. Methodology and limitations

Search Console clicks for October 1 to 30, 2026, in each site's main country, against DataForSEO Labs estimates for the same country, collected on November 2, 2026.

- **Sites:** 15 small business, ecommerce and information sites I work on, with at least 100 clicks in their main country in October. Two more properties had too little data and were left out. Names, verticals and query text are withheld.
- **Real traffic:** Search Console clicks, web search, all devices, filtered to the country with the most clicks (Bulgaria for 10 sites, Slovakia for 2, Romania, the UK and the U.S. for one each). Country totals include anonymized queries; query rows do not, and no site reached the 25,000-row limit.
- **Estimates:** DataForSEO Labs (Google) domain overview for estimated monthly organic traffic and keyword counts, and ranked keywords for per-keyword estimates, using the same country and its main language. Ranked keywords were capped at the 1,000 keywords with the highest estimate, which affects two sites. Cost: 0.89 USD.
- **One provider:** I did not test Semrush or Ahrefs directly. Their databases and click models differ, so their errors will differ in size, though the earlier studies point the same way.
- **Matching:** keywords were matched by exact text after lowercasing and trimming spaces. Spelling variants and word-order changes do not match, which makes the keyword-level overestimate somewhat larger than it is.
- **Not like for like:** a tool estimate is a modelled monthly figure from a database snapshot; Search Console clicks are counted for a fixed window. Clicks are not sessions. Seasonality between the snapshot and October can move the ratio.
- **Limits:** 15 sites is a small, non-random sample, heavy on Bulgarian. Only five sites come from other markets, so the market comparison is a hint, not a finding.
- **Data:** [data-sites.csv](data-sites.csv) (one anonymized row per site) and [data-summary.json](data-summary.json) (every number on this page), CC BY 4.0.

## 10. Frequently asked questions

**How accurate are Semrush and Ahrefs traffic estimates?**

In published studies, typically off by about half, and much worse on some sites. Ahrefs' own 2022 study of 1,635 U.S. sites found a median deviation of 49.52% for Ahrefs and 68.36% for Semrush. In my 15 sites, a keyword-based estimator put traffic at a median 35% of real Search Console clicks, with a range from 1.8% to 117%.

**Why does Semrush or Ahrefs show much less traffic than Search Console?**

Mainly because the tool only knows some of your keywords. In my data, 81% of real clicks came from searches the tool did not list: 40% were anonymized queries that no keyword database can contain, and the rest were named queries missing from its database. Small-language markets were hit hardest: 9 of the 10 Bulgarian sites were estimated at less than half of their real clicks.

**If the tool's total matches my Search Console, is it accurate?**

Not necessarily. On the six sites where the total landed within 25% of reality, the tool overestimated the keywords it knew by 2.4 to 6.3 times, and missed the rest. The two errors cancelled out. On one site the estimate was 95% of real clicks, yet it assigned 17,434 visits to keywords that earned 4,559 clicks.

**Can I use traffic estimates to compare competitors?**

For a rough ranking within the same market and the same tool, yes. Across my 15 sites the rank correlation between estimate and real clicks was 0.71, close to the 0.76 Ahrefs reported. But individual pairs can be badly wrong: one site with 5,025 real clicks was estimated at 92 visits, while a site with only 216 clicks was estimated at 88.

**Which number should I trust to judge my SEO agency?**

Search Console clicks for organic search, and the Organic Search channel in GA4 for what visitors did next. Third-party estimates are models built from keyword volume and an assumed click curve, not measurements of your site. Compare GA4 organic sessions with GSC clicks, not GA4 all channels.

**Is there a way to calibrate a tool to my market?**

Yes. Pull 30 days of Search Console clicks for your main country, look up your own domain in the tool for the same country, and divide. That ratio is your correction factor for that tool and market. The calculator on this page does it and compares the result with the medians in this study.

## Sources

1. r/SEO. "GA4 and GSC show traffic, but Semrush and Ahrefs report much lower organic traffic. Is my SEO agency doing something wrong?" October 29, 2026. [reddit.com/r/SEO/comments/1xigrrm/ga4_and_gsc_show_traffic_but_semrush_and_ahrefs/](https://www.reddit.com/r/SEO/comments/1xigrrm/ga4_and_gsc_show_traffic_but_semrush_and_ahrefs/). Accessed November 2, 2026.
2. r/bigseo. Same question posted the same day, October 29, 2026. [reddit.com/r/bigseo/comments/1xigstu/ga4_and_gsc_show_traffic_but_semrush_and_ahrefs/](https://www.reddit.com/r/bigseo/comments/1xigstu/ga4_and_gsc_show_traffic_but_semrush_and_ahrefs/). Accessed November 2, 2026.
3. Tim Soulo, Ahrefs. "How Accurate Are the Search Traffic Estimations in Ahrefs? (New Research)." 1,635 websites, U.S. traffic. May 3, 2022. *Vendor: sells SEO or analytics products.* [ahrefs.com/blog/traffic-estimations-accuracy/](https://ahrefs.com/blog/traffic-estimations-accuracy/). Accessed November 2, 2026.
4. Patrick Langridge, Screaming Frog. "How Accurate Are Website Traffic Estimators?" 25 websites, mainly UK, Google Analytics data for February to April 2016. June 13, 2016. *Vendor: sells SEO or analytics products.* [screamingfrog.co.uk/how-accurate-are-website-traffic-estimators/](https://www.screamingfrog.co.uk/how-accurate-are-website-traffic-estimators/). Accessed November 2, 2026.
5. Daniel Waisberg, Google Search Central Blog. "A deep dive into Search Console performance data filtering and limits." October 19, 2022. [developers.google.com/search/blog/2022/10/performance-data-deep-dive](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive). Accessed November 2, 2026.
6. DataForSEO. "dataforseo_labs/google/domain_rank_overview/live" API documentation (definition of estimated traffic volume). *Vendor: sells SEO or analytics products.* [docs.dataforseo.com/v3/dataforseo_labs/google/domain_rank_overview/live/](https://docs.dataforseo.com/v3/dataforseo_labs/google/domain_rank_overview/live/). Accessed November 2, 2026.

Last updated: November 2, 2026. Related research: [all studies](https://stanislav-peev.com/research/).

---

Stanislav Peev - contact in writing only, no calls: [info@stanislav-peev.com](mailto:info@stanislav-peev.com) · [contact form](https://stanislav-peev.com/#contact)
