---
name: conversion-leak-finder
description: Traces every way a visitor can leave the page without converting: outbound links, navigation, dead ends and paths that lead nowhere. Use when sessions are healthy, the offer is clear, and conversions still do not appear.
---

# Conversion Leak Finder

## Use this skill when

- the page's full link and navigation inventory is available, including anything that takes the visitor off the conversion path.
- a paid landing page carries the full site navigation and a long footer.
- outbound links to press, integrations or partners open in the same tab.

This skill looks at ways out of the page. Things that appear on top of the page belong to `popup-and-overlay-timing-review`.

## Required input

- every link on the page: header navigation, in-body links, footer, outbound links, and whether each opens in the same tab.
- the conversion path the page is supposed to produce, start to finish.
- what happens after each non-conversion click: another page, another site, a dead end with no route back.
- optional: exit pages, outbound click data, next-page paths.
- If the link inventory came from memory rather than from loading the page, say so. Footer and navigation links are the ones people forget they have.

### If the data does not exist

- **No link inventory:** in the browser Console, list every anchor's text, `href` and `target`. Any one-line snippet over `document.querySelectorAll('a')` does it, and the output pastes straight into this skill.
- **No exit data:** GA4 does not report exit links unless outbound click tracking is on, which it often is under enhanced measurement: Reports, then Engagement, then Events, and look for `click` with the `outbound` parameter. If it is missing, rank by structural exposure and say so.
- **Nothing at all:** count the links in the header and footer by eye on a paid landing page. If the header carries full site navigation, that is the finding and it needs no data to support it.

Not for: overlays that appear on top of the page (`popup-and-overlay-timing-review`), or whether the offer is convincing (`offer-clarity-diagnosis`).

## Analysis workflow

1. Map the page journey from ad click to hero, proof, objection handling, form, submit and thank-you step.
2. Use available data to locate leaks: bounce, scroll drop, CTA clicks, form starts, field errors and submits.
3. Classify each leak as message, offer, proof, UX, speed, form, tracking or traffic-quality related.
4. Prioritize leaks by business impact and confidence, not by visual preference.
5. Recommend the smallest test or fix for the top leak.

## Decision rules

- Count exits before diagnosing copy. A paid page carrying full site navigation offers a stranger many ways to leave before reading the offer, and closing that costs nothing to try.
- An outbound link opening in the same tab is an exit, not a citation. Press mentions and integrations are the usual offenders.
- Rank by structural exposure when there is no exit data, and say that is what you did. With exit data, rank by measured loss instead.
- A dead end is worse than an exit. A page the visitor reaches with no route back to the conversion is a leak that also wastes the click.
- Do not count every link as a leak. Links that serve the conversion, such as a pricing anchor or a proof detail, are part of the path.
- Do not recommend stripping navigation from pages that receive organic or branded traffic without saying that the recommendation is scoped to paid landing pages.

## Output format

| Exit | Type | Opens in | Where it leads | Serves the conversion | Verdict |
|---|---|---|---|---|---|
| Link or element | Navigation / in-body / footer / outbound | Same tab / new tab | Destination, or dead end | Yes / no | Keep / target-blank / remove on paid pages |

End with:

- `Exits above the offer:` the count
- `Dead ends:` the list, or none
- `Decision:` reduce navigation on paid pages / fix same-tab outbound links / remove dead ends / pull exit data
- `Ranking basis:` structural exposure or measured loss, stated explicitly
- `Missing data:` exit and outbound click data

## Practical example

User: "Paid landing page. Full site navigation in the header with 7 items, links to the blog and the careers page, a footer with 22 links, and three outbound links to press coverage that open in the same tab. Sessions 3800, conversions 41."

Assistant should note: a paid landing page carrying the full site navigation gives a visitor seven ways to leave before reading the offer, which is the largest leak on the list and the cheapest to close; three press links opening in the same tab hand the visitor to another domain with no route back, so those are exits rather than proof; 22 footer links on a page with one job is a navigation surface the page does not need. Then: the standard fix is a reduced header on paid pages and target-blank on any outbound link that must stay, ranked above copy work because it costs nothing to test. Exit-page data per link was not supplied, so the ranking is by structural exposure rather than measured loss.

## Guardrails

- Do not change the page, the navigation or any link.
- Do not treat every link as a leak.
- Scope navigation recommendations to paid landing pages, and say so.
- Say when the inventory came from memory instead of from loading the page.
