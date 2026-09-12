---
name: google-ads-landing-page-experience-review
description: Diagnoses a Below average Landing page experience rating in Google Ads and separates the page problems from the keyword problems. Use when Quality Score components show Below average on landing page experience, or when CPCs rise on keywords whose ads and page did not change.
---

# Google Ads Landing Page Experience Review

## Use this skill when

- the Landing page experience column reads Below average or Average and somebody wants to know what to change.
- CPCs crept up on keywords whose ads and page were untouched.
- one page serves many ad groups and the rating differs between them, which is a relevance problem rather than a page-quality problem.
- a page was redesigned and the rating moved, in either direction, and the cause needs naming.

Do not use this skill for conversion diagnosis. A page can be rated Above average and convert badly. `paid-traffic-message-match-audit` and the on-page skills own conversion.

## Required input

- the Google Ads export with, at minimum: keyword, ad group, final URL, Quality Score, and the three component columns including Landing page experience.
- impressions and cost per keyword, so findings can be ranked by what they cost.
- the landing page or pages: copy, headings, the offer, and whether the page is indexable and loads for a crawler.
- how many keywords and ad groups share each final URL.
- If only the aggregate Quality Score is available without the component columns, say so. The three components fail for different reasons and the aggregate cannot tell you which.

### If the data does not exist

The component columns are hidden by default, which is why most operators think they do not have them.

- **To add them:** Google Ads, then Campaigns, then Keywords, then the Columns button, then Modify columns, then Quality Score. Tick Landing page exp., Ad relevance and Exp. CTR alongside Quality Score. They appear as history columns, so also tick the historical versions if you want the trend.
- **No cost or impression columns:** add Cost and Impressions in the same panel. Without them the findings cannot be ranked by what they cost, and ranking by cost is most of this skill's value.
- **The columns show a dash:** that means too little serving data on those keywords, not a rating of zero. Say so; a dash is not a finding.
- **No access to the account:** ask the client for a keyword report as CSV with those columns, in one sentence. This is a read-only export and it is the least contentious thing you will ever ask a client for.

## Analysis workflow

1. Group the export by final URL. Rate each URL by weighted impressions and cost so the biggest bill comes first.
2. Within each URL, compare Landing page experience across ad groups. A rating that varies by ad group on one page is a keyword-to-page relevance problem, not a page defect.
3. For each low-rated group, check whether the page contains the query intent in its visible copy and headings, not just in a meta tag or a hidden accordion.
4. Check the mechanics Google measures and states publicly: relevant and original content, transparency about the business, ease of navigation, and load speed on mobile. Note which of the four the page fails, with evidence.
5. Check for the structural blockers: an interstitial on load, a page requiring a login, a page that redirects the crawler somewhere else, a final URL that no longer matches the page the user reaches.
6. Separate the keyword decisions from the page decisions. Some low-rated keywords should get a different page or leave the account; some pages need work.
7. Rank the recommendations by cost carried, not by how easy they are.

## Decision rules

- If the rating varies across ad groups pointing at the same URL, the page is not the defect. Say so plainly, and put the fix on keyword-to-page mapping.
- One page cannot be relevant to every query in a broad ad group. Splitting the group or building a second page is a legitimate answer, and it is a bigger job than a copy edit. Say which.
- Do not promise a Quality Score number after a change. Google recalculates on serving data over time. Any predicted rating is a hypothesis, always.
- Report load speed only from a measured source, and name it. An impression of slowness is not a finding.
- If the final URL and the page a user actually reaches differ, that is the first fix and everything else waits.
- Never recommend keyword stuffing the page to match the query. Recommend content that answers the query, and say the difference.

## Output format

| Final URL | Ad groups on it | Impressions | Cost | LP experience spread | Diagnosis | Fix owner |
|---|---|---|---|---|---|---|
| The URL | Count | Number | Number | The range across groups | Page defect / relevance mismatch / structural blocker | Page / account |

Then per page defect:

| Google's criterion | Status | Evidence | Recommended change |
|---|---|---|---|
| Relevant original content / transparency / navigation / mobile speed | Pass / fail / unknown | Quoted copy, measured number or missing-data marker | The smallest change |

End with:

- `Decision:` fix the page / remap keywords / split the ad group / fix the redirect first / ask for the component columns
- `Cost carried by low-rated keywords:` the number from the export
- `Missing data:` what would change the diagnosis

## Practical example

User pastes an export: 140 keywords, one final URL, Quality Score 3 to 7. Landing page experience is Below average on 61 keywords carrying 4200 of 6900 monthly spend, Average on the rest. The page is a generic homepage.

Assistant should note: one URL serving 140 keywords with the rating splitting between Below average and Average is a relevance spread, not a single page defect, so the first move is mapping which query themes sit in the Below average group; those 61 keywords carry 61 percent of spend, which is how the recommendations get ranked; a homepage as the final URL for specific commercial queries fails Google's relevant and original content criterion by construction, because the homepage answers no specific query fully. Then: the honest answer is dedicated pages per query theme, named as a bigger job than a copy edit, plus the note that no predicted Quality Score is offered because Google recalculates on serving data. Mobile speed is marked unknown because no measured number was supplied.

## Guardrails

- Do not change bids, keywords, ads or pages.
- Do not predict a Quality Score or a CPC after a change.
- Do not recommend keyword stuffing.
- Mark speed and any Google-side signal as unknown when it was not measured.
