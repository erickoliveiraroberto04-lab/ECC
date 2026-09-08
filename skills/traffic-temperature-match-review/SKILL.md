---
name: traffic-temperature-match-review
description: Checks whether one landing page is being asked to serve cold prospecting, warm retargeting and branded search at the same time, and what that costs. Use when a page performs on one source and collapses on another, or when a new channel was pointed at an existing page.
---

# Traffic Temperature Match Review

## Use this skill when

- one page receives several sources and the conversion rate between them differs by more than the page can explain.
- a new channel was launched and pointed at whichever page already existed.
- branded search and cold prospecting share a page, and someone is averaging their conversion rate into one number.
- a page was built for one audience and quietly became the default destination for everything.

`paid-traffic-message-match-audit` compares one ad to one page. This skill compares the page against the intent temperature of every source hitting it.

## Required input

- traffic by source with sessions and conversions per source, not just the total.
- what each source knows on arrival: has the visitor heard of the brand, seen the product, been to the site before, searched for a solution or been interrupted mid-scroll.
- the page as it stands: what it assumes the visitor already knows, what it explains, and what it asks for.
- the conversion definition, and whether it is the same event for every source.
- If conversions are only available in aggregate, say so. An averaged rate across temperatures hides both the working source and the broken one.

### If the data does not exist

Conversions by source is the one input this skill genuinely cannot do without.

- **In GA4:** Reports, then Acquisition, then Traffic acquisition. Set the primary dimension to Session source / medium and add your key event as the metric. That gives sessions and conversions per source in one table, which is exactly the input.
- **If your conversion is not a GA4 key event:** use the platform's own numbers per channel (Meta Ads Manager and Google Ads report their own conversions) and say explicitly that the two platforms count differently and may double-count the same person.
- **If conversion happens off-site**, in a CRM or a booking tool: export the last 100 records and tally by the source field, if there is one. If there is not, that is the finding, and the fix is a hidden source field on the form.
- **Nothing at all:** do not run this skill. Its entire value is the split, and a blended number is what it exists to refuse. Say that plainly and route to a skill that works from the page itself.

## Analysis workflow

1. Tabulate every source with sessions, conversions and rate, and sort by volume. Note where a single source dominates the average.
2. Assign each source a temperature: cold, warm, branded or existing-relationship, and write what that visitor knows at the moment they land.
3. Read the page's opening as each of those visitors. Note what a cold visitor needs that is missing and what a branded visitor is forced to read that they already know.
4. Check the ask against each temperature. The same commitment is reasonable from a branded searcher and unreasonable from a cold interrupted scroller.
5. Look for the averaging trap: recompute the rate with the dominant source removed, and say which kind of dominant you mean, because the answer differs. Here branded search dominates conversions while cold traffic dominates sessions, and removing one gives 1.70 percent where removing the other gives 5.03 percent. State the basis every time.
6. Decide per source: the page fits, the page needs a section the source requires, or the source needs a different page.
7. If splitting the page is the answer, name the cost honestly: another page to maintain, another test to run, and traffic thin enough that neither version may reach significance.

## Decision rules

- Never report a single conversion rate for a page served by multiple temperatures without also reporting it by source. The average is the least useful number available.
- Recompute the overall rate from the per-source counts before anything else. If it does not match the number the user quoted, that discrepancy is the first finding and everything downstream waits for it.
- A branded searcher forced through a cold-traffic argument is a real cost, not a harmless one. It shows up as time on page and a lower rate than branded traffic should produce.
- If a source has too few sessions to have a stable rate, say so and do not rank it. Small-sample rates invite confident wrong decisions.
- Splitting a page is a maintenance commitment. Recommend it only when the volume per variant can support a decision, and say what volume would be needed.
- Do not recommend personalisation tooling as the fix. Recommend the page change, and mention tooling only if the team already runs it.
- If conversions are defined differently per source, stop and fix the definition first. Everything else is measuring two things.

## Output format

| Source | Sessions | Conversions | Rate | Temperature | What the visitor knows | Page fit |
|---|---|---|---|---|---|---|
| Named source | Number | Number | Percent, or "small sample" | Cold / warm / branded / existing | One line | Fits / needs a section / needs its own page |

Then:

- `Rate without the dominant source:` the number, the basis used (sessions or conversions), and what it changes
- `What a cold visitor is missing:` the list
- `What a branded visitor is forced to read:` the list

End with:

- `Decision:` keep one page / add a section / build a second page / fix the conversion definition / ask for data
- `Volume needed to support a split:` the honest number, or unknown
- `Missing data:` what would change the verdict

## Practical example

User: "Landing page does 2.8 percent overall. Sources: branded search 1200 sessions 61 conversions, Meta cold prospecting 3400 sessions 42 conversions, retargeting 400 sessions 18 conversions, newsletter 90 sessions 6 conversions. The page opens with a long explanation of what the category is, then asks to book a call."

Assistant should start with the reconciliation, not the diagnosis: the supplied sources total 5090 sessions and 127 conversions, which is 2.50 percent, not the 2.8 percent stated, so either a source is missing from the list or the two figures come from different date ranges. That gets resolved before any per-source finding is trusted, because this is the exact discrepancy the skill exists to catch. Then the honest split: 5.08 percent branded, 1.24 percent cold, 4.50 percent retargeting, and the newsletter's 90 sessions is a small sample that should not be ranked. Rate with the dominant source by conversions (branded search) removed: 1.70 percent, 66 conversions of 3890 sessions. Cold traffic is 66.8 percent of sessions and 33.1 percent of conversions, so it carries the volume and the problem: an interrupted scroller is asked to book a call after a category explanation, with no lower-commitment step, while branded searchers read a category explanation they do not need. Then: add a lower-commitment path for cold traffic and move the specific offer above the category explanation, with a second page named as the alternative and the volume it would need to be decidable.

## Guardrails

- Do not average across temperatures without also reporting the split.
- Do not rank a source with too few sessions to be stable.
- Do not recommend personalisation software as the fix.
- Do not change traffic routing, campaigns or the page.
