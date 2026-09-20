---
title: "How reliable is AI visibility tracking? A 60-query experiment - Stanislav Peev"
description: "I ran the same 4 buyer questions 60 times across ChatGPT, Gemini and Perplexity. Which engine you track moved a brand's measured AI visibility 2.3x more than the model's own randomness. Original data, methodology and limitations."
url: "https://stanislav-peev.com/research/ai-visibility-tracking-reliability/"
lang: "en"
---

Research · AI Search Data

# How reliable is AI visibility tracking? I ran the same queries 60 times

By **Stanislav Peev**, SEO consultant & GEO specialist · Published **August 17, 2026** · Original experiment · 8 min read

2.3×

Which AI engine you track moved a brand's measured visibility about 2.3 times more than the model's own run-to-run randomness. Same category, same day, same questions - the engine, not the model's noise, decided the answer.

Source: this experiment - 60 queries across ChatGPT, Gemini and Perplexity, August 17, 2026

## Key takeaways

- **2.3×** - engines disagreed with each other about 2.3 times more than a single engine wavered between identical repeats (cross-engine set distance 0.50 vs within-engine 0.22)
- **78%** - even repeating one prompt on one model five times, the single top recommendation held only ~78% of the time; the fuller list churned ~22%
- **0% vs 100%** - for one buyer question, Asana was recommended in every Perplexity answer and in none of the ChatGPT or Gemini answers, the same day
- **t0ggles** - two of three engines handed that same question entirely to little-known tools (t0ggles, TeamEasy) that the third engine never named once
- **90% vs ~28%** - Trello looked dominant on Perplexity and marginal on the other two; the same brand ranks differently on each engine, not noisily around one truth
- **60 queries**, 3 engines, 4 questions, one category, one day - raw data published under CC BY 4.0

## What's in this report

1. What I measured, in one paragraph
2. Same model, same question, five times: the list still moves
3. Engines disagree 2.3x more than one engine wavers
4. The clearest case: two engines recommend a tool the third never mentions
5. The same brand ranks differently on every engine
6. Is your AI visibility report trustworthy? A 6-point test
7. Methodology
8. Limitations
9. FAQ
10. Get the data

## 1. What I measured, in one paragraph

I picked one category - project management software - and four buyer questions a real customer would type. I ran each question five times, unchanged, on three web-connected AI engines, in one sitting. That is 60 answers. For each answer I logged which brands were named and in what order, then measured how much the result moved: between identical repeats on one engine, and between the three engines.

The point was not to rank project management tools. It was to test the thing every AI-visibility dashboard quietly assumes: that a weekly "you were mentioned in X% of answers" number is a stable measurement. If the same question, asked the same way, on the same day, produces a different answer each time, then a lot of what those dashboards report as movement is not movement at all. Full method and the raw answers are below.

## 2. Same model, same question, five times: the list still moves

Repeating an identical prompt five times on a single engine, the set of recommended brands changed by about 22% on average (Jaccard distance). The single top pick was more stable - it held about 78% of the time - but in one cell out of five, even the first-named brand changed between identical runs.

Top-1 recommendation stable

~78%

Full recommended set stable

~78%

Within-engine, across 5 identical repeats. Set instability 0.22 means the named set differs by ~22% run to run.

The pattern underneath the average matters. Mainstream leaders locked in fast: for "what project management software should a small team use?", Perplexity named the same four tools in all five runs (instability 0.00). The churn lived at the bottom of the list and in the long tail - a fifth or sixth tool that appears in one run and vanishes in the next. A second, quieter driver was **answer length**: the same question sometimes returned a five-tool comparison and sometimes a one-line recommendation. When the answer shortened, every brand except the winner disappeared - so a tracker counting "mentions" records a brand as absent purely because the model was terse that time, not because its ranking changed.

1 in 5

In one prompt-and-engine cell out of five, even the top recommendation flipped between identical repeats - for example ClickUp on three runs, Asana on two, same question, same engine, minutes apart.

This experiment, 2026

## 3. Engines disagree 2.3x more than one engine wavers

Within one engine, the recommended set moved ~22% between identical repeats. Between the three engines, it moved ~50%. The engine you choose to track determines the result about 2.3 times more than the model's own randomness does.

Within one engine (repeat noise)

0.22

Between three engines

0.50

Mean Jaccard distance between recommended sets. Higher = more disagreement. 0 = identical, 1 = no overlap.

This is the finding that should change how the reports are read. An AI-visibility score has **two independent layers of instability**: the model is not deterministic between identical runs, and the models do not agree with each other. The second layer is more than twice the size of the first. A dashboard that blends ChatGPT, Gemini and Perplexity into one "AI visibility" percentage is averaging over the largest source of variance in the whole measurement and reporting the average as if it were a single fact. The divergence was widest exactly where buyers make decisions: for the two most specific, most commercial questions, cross-engine distance reached 0.60 and 0.67 - close to no overlap at all.

## 4. The clearest case: two engines recommend a tool the third never mentions

For "recommend a project management platform for a small remote team", the three engines did not just rank tools differently - they recommended different companies entirely. Perplexity named only mainstream tools. ChatGPT and Gemini named only two little-known ones, and named them almost every time.

| Engine | Who it recommended for "small remote team" |
| --- | --- |
| Perplexity Sonar | Asana, ClickUp, Trello, Monday.com, Basecamp |
| ChatGPT (GPT-4o, web) | t0ggles, TeamEasy |
| Gemini 2.5 Flash (web) | t0ggles, TeamEasy (all 5 runs identical) |

t0ggles and TeamEasy are niche tools with landing pages written for exactly this phrasing (t0ggles.com/for/small-teams, teameasy.app). Two of the three engines handed the entire recommendation to them and never mentioned a single mainstream brand; Perplexity did the reverse and never mentioned them. The overlap between engines on this question was almost zero (cross-engine distance 0.67). Read as visibility: **Asana's AI visibility for this query was 100% on one engine and 0% on the other two, on the same afternoon.** Read as opportunity: a small, focused tool can own two of three answer engines for a real buyer query while the category leaders are invisible - which is the whole case for [generative engine optimization](https://stanislav-peev.com/#geo) as a distinct discipline from ranking.

## 5. The same brand ranks differently on every engine

Across all 20 answers per engine, a brand's mention rate was not a noisy estimate of one underlying popularity. It was a different number on each engine - often a reversal, not a wobble.

| Brand | Perplexity | ChatGPT | Gemini |
| --- | --- | --- | --- |
| ClickUp | 100% | 65% | 75% |
| Trello | 90% | 25% | 30% |
| Asana | 85% | 50% | 50% |
| Monday.com | 80% | 45% | 55% |
| Notion | 15% | 40% | 70% |
| Basecamp | 15% | 30% | 70% |
| Zoho Projects | 0% | 45% | 45% |
| Linear | 0% | 25% | 45% |
| t0ggles | 0% | 25% | 25% |
| TeamEasy | 0% | 20% | 25% |

Read the rows, not the columns. Trello looks like a category leader on Perplexity (90%) and a bit player on the other two (~28%). Notion and Basecamp are the mirror image: near-invisible on Perplexity (15%), dominant on Gemini (70%). Zoho Projects and Linear do not exist for Perplexity at all and are real presences on the other two. If your AI-visibility program optimizes for the engine your report happens to sample, you can move a number while your actual buyers - on a different engine - see none of it. This is why I baseline [AI visibility per engine](https://stanislav-peev.com/services/) and never as a single blended score.

## 6. Is your AI visibility report trustworthy? A 6-point test

You do not need to run this experiment yourself to judge a report. Tick every statement that is true of the AI-visibility number you were handed - by a tool or an agency.

**0/6** checked - tick each statement that is true of your report.

Six out of six is a report you can act on. Three to five, and the number is directional at best - useful for the very top of the answer, unreliable below it. Below three, you are being sold a trend line drawn through noise. None of this makes AI visibility unmeasurable; it makes it measurable only with a method that respects how much the answers move.

## 7. Methodology

One category was used as a testbed: project management software. Four buyer-intent prompts were fixed in advance: "what project management software should a small team use?", "best project management tool for a 10-person startup?", "which project management app should my team pick in 2026?", and "recommend a project management platform for a small remote team." Each prompt was sent five times, unchanged, to three web-connected models, all in a single session on August 17, 2026: Perplexity Sonar, OpenAI GPT-4o and Google Gemini 2.5 Flash, each with web search enabled, routed through one OpenRouter key. That is 4 prompts x 3 models x 5 repeats = 60 answers.

For every answer, brand names were extracted against a fixed dictionary and recorded in order of first mention. Three metrics were computed. **Within-engine set instability**: the mean pairwise Jaccard distance between the five repeat sets for a given prompt and engine (0 = identical every run, 1 = no overlap). **Cross-engine set distance**: the mean pairwise Jaccard distance between the three engines' combined sets for a given prompt. **Top-1 stability**: the share of repeats whose first-named brand equals the most common first-named brand in that cell. Every raw answer, with timestamp, is published so the numbers can be recomputed or challenged. A browser cross-check on the consumer Perplexity interface the same day reproduced the same instability pattern.

## 8. Limitations

This is a directional experiment, not a benchmark. The effect is unmistakable at this size, but the exact figures should not be quoted as universal constants - they are a floor, measured under favorable conditions.

Four honest caveats. First, scope: one category, four prompts, five repeats, one day and the API's default location. Enough to show the direction and the rough magnitude; not enough to attach a confidence interval to any single brand's number - that needs more repeats and more categories. Second, the models were queried through OpenRouter's web plugin, which is not identical to the consumer ChatGPT, Gemini and Perplexity apps (no personalization, memory or app-specific UI). That means this measures the *floor* of the noise; the consumer surfaces most buyers use are at least this variable, usually more. Third, brand extraction used a fixed dictionary, so a tool outside it would read as zero mentions - the dictionary was expanded to include t0ggles and TeamEasy after they first appeared. Fourth, this is not a ranking of project management tools; the category is only a testbed for the measurement question. I will extend this to more categories and higher repeat counts, and update this page with the harder numbers.

## 9. Frequently asked questions

**How many prompts do I need for a reliable AI visibility check?**

More than one engine, and more than a handful of repeats. Repeating the same prompt five times on one model still moved the full recommended set by about 22% and flipped the top pick in one cell out of five. Mainstream leaders stabilize fast; everything below the top and every smaller brand needs several repeats per engine before the number means anything.

**Does it matter which AI engine I track?**

More than anything else here. The three engines disagreed about 2.3 times more than a single engine wavered between identical runs. A blended "AI visibility" score hides which of those two effects it is actually reporting - track ChatGPT, Gemini and Perplexity separately.

**Why does an AI visibility tool give a different number every week?**

Two reasons. The models are non-deterministic, so identical prompts return different sets minutes apart. And answer length varies, so a brand drops out of a shorter answer without any change in ranking. A weekly move below the top position, measured on few repeats, is usually noise, not a trend.

**Is a single blended AI visibility score meaningful?**

Only for the very top of the answer. Top-1 recommendations for mainstream brands were about 78% stable, so a headline leader is fairly trustworthy. Below the top, and for any smaller brand, a one-number score with no per-engine breakdown and no repeat count reports more certainty than the data supports.

**Which is more reliable: ChatGPT, Gemini or Perplexity?**

They are different rankings, not noisy copies of one. Perplexity concentrated on four mainstream tools; Gemini rated Notion and Basecamp far higher; both GPT-4o and Gemini surfaced query-optimized long-tail tools Perplexity never named. The engine that matters is the one your buyers use.

**Can I trust an AI visibility report from a vendor?**

Ask two things: is it per engine, and how many repeats per prompt? A single blended score with no repeat count averages over run-to-run noise and engine disagreement and presents the average as a trend. Use the 6-point test above before acting on any AI-visibility number.

## 10. Get the data

### Full dataset, CC BY 4.0

All 60 raw answers with timestamps, plus the computed per-cell and per-engine metrics. Recompute the numbers, challenge them, or replicate the method on your own category.

[data-summary.json](https://stanislav-peev.com/research/ai-visibility-tracking-reliability/data-summary.json) - metrics, prompts, per-engine mention rates
[data-raw.jsonl](https://stanislav-peev.com/research/ai-visibility-tracking-reliability/data-raw.jsonl) - every answer, one JSON object per line

Citing this page: link to this URL. If you replicate it on another category or at higher repeat counts, [email me](mailto:info@stanislav-peev.com?subject=AI%20visibility%20stability%20-%20replication) and I'll add it here.

Published: August 17, 2026. Original experiment by [Stanislav Peev](https://stanislav-peev.com/). This is a directional first run; I will extend it to more categories and higher repeat counts and update this page with the harder numbers. Method or figures look off? [Email me](mailto:info@stanislav-peev.com?subject=AI%20visibility%20experiment%20-%20feedback) - the raw data is published so it can be checked.

## Want an AI visibility baseline that isn't just noise?

I run AI-visibility baselines and GEO programs measured per engine, on real buyer prompts, with enough repeats to tell signal from noise - so you know where ChatGPT, Gemini and Perplexity actually place you. Describe your situation in a few sentences and I'll reply personally with an honest first read. No calls, no meetings.

[See GEO services](https://stanislav-peev.com/services/) [Email me](mailto:info@stanislav-peev.com?subject=AI%20visibility%20baseline%20inquiry)

- **Email** [info@stanislav-peev.com](mailto:info@stanislav-peev.com)
- **LinkedIn** [in/stanislav-peev-seo](https://www.linkedin.com/in/stanislav-peev-seo/)
- **Based in** Bratislava, Slovakia - working worldwide

---

Stanislav Peev - contact in writing only, no calls: [info@stanislav-peev.com](mailto:info@stanislav-peev.com) · [contact form](https://stanislav-peev.com/#contact)
