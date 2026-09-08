---
name: popup-and-overlay-timing-review
description: Reviews every popup, banner, chat bubble and cookie wall that fires on a landing page and decides which ones are stealing the primary conversion. Use when a page has several overlays, when a new one was added, or when mobile converts far worse than desktop for no structural reason.
---

# Popup And Overlay Timing Review

## Use this skill when

- the page carries more than one interruption: exit intent, timed modal, cookie wall, chat bubble, sticky bar, notification prompt.
- someone added an overlay to hit an email target and nobody checked what it did to the primary conversion.
- mobile converts much worse than desktop and the layout itself is fine, which points at overlays covering the viewport.
- a tool was installed by one team and its overlay competes with another team's CTA.

`conversion-leak-finder` looks for exits and dead ends in the page flow. This skill looks only at things that appear on top of the page and interrupt it.

## Required input

- the full inventory: every overlay, what triggers it, on which pages, on which devices, and which tool serves it.
- what each overlay asks for, and which conversion it counts towards.
- the page's primary conversion, stated explicitly.
- any numbers per overlay: impressions, capture rate, dismissals, and the primary conversion rate with and without it if that was ever measured.
- If the inventory was assembled from memory rather than by loading the page, say so. Overlays installed by other teams are routinely forgotten.

### If the data does not exist

Nobody has ever measured the primary conversion rate with and without each overlay. That is the normal case, and it is why this skill reports unknown rather than guessing.

- **No per-overlay numbers:** the deliverable is the test plan, not a verdict. Name the one overlay to switch off first, for how long, and which single number to watch. Pick the overlay that covers the most viewport, because it is the cheapest to justify turning off.
- **No capture numbers either:** ask the tool that serves the overlay; every one of them reports impressions and captures. If it cannot, that is worth knowing about the tool.
- **You cannot load the page yourself:** ask for a screen recording of a first visit on a phone, not a screenshot. The order and timing of the overlays is the finding, and a still frame does not carry it.

## Analysis workflow

1. Load the page on mobile and desktop and record what fires, in what order, with what delay, and how much of the viewport each one covers.
2. For each overlay, name the conversion it serves and whether that conversion is the page's primary one or a secondary capture.
3. Identify collisions: two overlays that can be on screen together, an overlay that covers the primary CTA, an overlay that fires before the visitor has read the offer.
4. Check the cookie or consent wall separately. It fires first, it is usually not optional, and everything else has to work around it.
5. Estimate the cost side honestly: an overlay that captures emails at a measured rate may still lose primary conversions, and unless someone measured the primary rate both ways, the net is unknown. Say unknown rather than assuming positive.
6. Check the timed and exit triggers against how long the page takes to read. A modal that fires before a first-time visitor could plausibly have read the offer interrupts comprehension rather than rescuing an exit. Estimate reading time from the word count, say which count you used, and mark the estimate as an estimate; this pack has no measured reading-speed figure and does not pretend to.
7. Recommend per overlay: keep, retime, restrict to a device or page, subordinate to the primary CTA, or remove.

## Decision rules

- An overlay that covers the primary CTA is a defect, not a trade-off.
- An overlay that fires before the offer has been read is asking a stranger for a commitment. Retime it to a scroll or engagement trigger rather than a timer.
- If nobody measured the primary conversion rate with and without the overlay, the net effect is unknown. Report it as unknown and name the test rather than declaring the overlay harmful or harmless.
- Two overlays that can co-occur on mobile is a blocker. Mobile viewports do not have room for a negotiation.
- Do not recommend removing a consent wall. Recommend making it smaller, faster to dismiss, or non-blocking where the law allows, and say that the legal requirement is out of scope for this skill.
- Never count captured emails as a win without naming what the primary conversion did in the same period.

## Output format

| Overlay | Tool | Trigger | Device | Viewport covered | Conversion it serves | Verdict |
|---|---|---|---|---|---|---|
| Name | The tool serving it | Timer, scroll, exit, always | Mobile / desktop / both | Approximate share | Primary / secondary / none | Keep / retime / restrict / subordinate / remove |

End with:

- `Collisions:` overlays that can appear together, and on which device
- `Covering the primary CTA:` the list, or none
- `Decision:` remove / retime / measure first / ask for data
- `Missing data:` usually the primary conversion rate measured with and without

## Practical example

User: "Cookie wall on load. Chat bubble bottom right always on. Email modal at 8 seconds. Exit intent modal on desktop. Sticky discount bar. Primary conversion is a demo request. Email modal captures 240 a month."

Assistant should note: on a mobile viewport the cookie wall plus the sticky bar plus the chat bubble leave a narrow band of readable page, and the 8 second modal fires inside it, so three of five overlays can be on screen with the offer; the chat bubble sits in the same corner most sticky CTAs use, which is worth checking against the demo button's position; the 8 second timer needs checking against the page's word count rather than asserted on, and if the offer runs longer than roughly two sentences the timer beats the reader to it, which makes a scroll trigger the smaller fix. On the 240 captured emails: without the demo request rate measured with and without the modal, the net is unknown, and that measurement is the recommended next step rather than a verdict. The consent wall's existence is out of scope; only its size and dismissal cost are in scope.

## Guardrails

- Do not disable, install or reconfigure any overlay or tool.
- Do not give legal advice about consent requirements.
- Do not declare an overlay net positive or negative without the primary conversion measured both ways.
- Say when the inventory came from memory rather than from loading the page.
