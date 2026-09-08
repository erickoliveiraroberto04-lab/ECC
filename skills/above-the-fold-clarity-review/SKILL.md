---
name: above-the-fold-clarity-review
description: Judges what a visitor can actually understand and do in the first screen, before any scroll. Use when bounce is high, when a page was redesigned, or when the hero has to carry cold traffic that knows nothing about the brand.
---

# Above The Fold Clarity Review

## Use this skill when

- a screenshot or URL of the first screen is available and bounce, scroll start rate or CVR suggests visitors leave before reading anything.
- a redesign shipped and nobody checked what survives on a phone-sized viewport.
- a consent banner, sticky bar or chat widget was added and the first screen shrank.

This skill judges only what is visible without scrolling. Everything below that belongs to another skill.

## Required input

- a screenshot or URL of the first screen, on mobile and on desktop, since they crop differently.
- anything that overlays that screen on load: cookie wall, sticky header, chat bubble, promo bar.
- who the traffic is and whether they arrive knowing the brand.
- optional but useful: bounce rate, scroll start rate, time on page.
- If only a desktop screenshot exists, say so and mark every mobile statement as unverified. Most traffic is mobile, so a desktop-only review is half a review.

Not for: reading the hero elements as one argument (`hero-section-diagnosis`), or judging the offer's substance (`offer-clarity-diagnosis`).

## Analysis workflow

1. Evaluate whether a first-time visitor can identify audience, problem, outcome, offer and next step within 3 seconds.
2. Check headline, subheadline, visual, CTA, proof and form visibility together, not separately.
3. Flag ambiguity, jargon, hidden offer, weak contrast, competing CTAs and unclear next step.
4. Compare mobile and desktop above-the-fold experiences if both are available.
5. Recommend a revised information hierarchy, not a full page rewrite unless the first screen cannot be salvaged.

## Decision rules

- Judge only what is visible without scrolling, including whatever the overlays cover. A hero measured on an empty viewport is a hero nobody sees.
- The three-second test has one pass condition: a stranger can say what the thing is and who it is for. Everything else on the screen is secondary.
- A first screen whose only action is "Learn more" makes no ask. Report that as a finding, not as a CTA.
- If the visible area differs between mobile and desktop by more than a section, treat them as two different first screens and report both.
- Do not call a first screen cluttered. Count the competing elements and report the count.
- Bounce rate alone cannot rank these findings. Without scroll or engagement data, say the ranking is judgement.

## Output format

| Element | Visible on mobile | Visible on desktop | Does it answer what / who / next | Verdict |
|---|---|---|---|---|
| Headline, subhead, visual, CTA, proof, overlay | Yes / no / partially covered | Yes / no | Which of the three questions it answers | Keep / rewrite / move up / remove |

End with:

- `What a stranger knows after three seconds:` one sentence, written from the screen alone
- `Viewport consumed by overlays:` approximate share, per device
- `Decision:` rewrite the hero / remove an overlay / move an element up / ask for data
- `Missing data:` what would turn the ranking from judgement into measurement

## Practical example

User supplies a desktop and a mobile screenshot of the first screen: a full-width video background, a headline reading Growth, unlocked., a subhead of three lines in light grey, a Learn more button. Mobile viewport 390 by 664, with a 64px sticky header and a cookie banner 210px tall at the bottom. Bounce 68 percent, scroll start rate not available.

Assistant should note: after three seconds a first-time visitor knows the page is about growth and nothing else, because the headline names no product, audience or outcome; the only action offered is Learn more, which asks for a scroll rather than a decision, so the first screen makes no ask at all; on mobile the sticky header and cookie banner take 274 of 664 points, which is 41 percent of the viewport, leaving the subhead and the button competing for what is left.

Then: the hero owes one sentence naming what the thing does and for whom. What this cannot conclude is the ranking of those three defects against each other, because scroll start rate was not supplied and 68 percent bounce alone cannot separate "left before reading" from "read and left". The 41 percent figure is measured from the supplied dimensions; the video's effect on load is unverified, since no speed report came with it.

## Guardrails

- Do not review the page below the fold here.
- Do not assess a mobile first screen from a desktop screenshot.
- Do not use the words cluttered, clean or modern. Count things instead.
- Say plainly when the ranking of findings is judgement rather than measurement.
