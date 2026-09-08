---
name: cta-clarity-check
description: Checks whether each call to action states the next step plainly, and whether the page is asking for one thing or quietly asking for five. Use when clicks on the primary action are low, or when a page has accumulated buttons over time.
---

# Cta Clarity Check

## Use this skill when

- every CTA label and its position on the page are available, and the primary action is getting fewer clicks than the traffic and scroll data suggest it should.
- buttons accumulated over a year and nobody removed any.
- the same action carries two different labels in two places on the page.

This skill reviews the asks the page makes. Which ask it *should* make belongs to `trial-vs-demo-path-decision`.

## Required input

- every CTA on the page: exact label, position, visual weight, and whether it is a button, a link or a form.
- which single conversion is the primary one, stated explicitly by the user.
- any secondary asks living on the page: newsletter field, chat, download, demo video.
- optional: clicks per CTA, which is what turns this from a structural review into a measured one.
- If the primary conversion is not stated, ask. Without it there is no way to tell a competing CTA from a supporting one.

### If the data does not exist

- **No per-CTA clicks:** this is the normal case, because it requires each button to be tagged. Say the finding about which CTA absorbs attention is unavailable, and run the rest, since duplicate labels and four equal-weight commitments are read off the page.
- **To get them:** the cheapest route is giving each CTA a distinct destination or query string and reading the destination traffic. The proper route is a GTM click trigger per button, which is a developer task, not a page fix.
- **No conversion count at all:** run it anyway. Counting the asks on the first screen is the finding, and it needs nothing.

Not for: which ask the page should be making (`trial-vs-demo-path-decision`), or overlays that interrupt the page (`popup-and-overlay-timing-review`).

## Analysis workflow

1. List every CTA and classify its job: primary conversion, secondary education, navigation or support.
2. Check whether CTA text states the next step and matches the offer commitment.
3. Identify competing CTAs, vague verbs, inconsistent labels and CTA placement gaps.
4. Compare CTA promise with form, thank-you page and follow-up expectation.
5. Recommend CTA copy, hierarchy or placement changes.

## Decision rules

- Count the commitments offered at equal visual weight on the first screen. More than one and the page has not decided; a visitor resolves that by choosing none.
- Two labels for the same action is a defect twice over: it splits the click data and makes the primary action look weaker than it is. Unify the wording before concluding anything from per-CTA numbers.
- A label that states no next step ("Learn more", "Explore") costs a click and promises nothing. Say what the visitor expects to happen after each label.
- Subordinate is not the same as absent. Secondary paths belong as text links, not as buttons competing with the primary one.
- Without per-CTA click data you cannot say which CTA is absorbing attention. Say that, and name pulling it as the next step.
- Do not propose CTA copy in isolation from the commitment. A label promising less than the form asks for is a message-match break, and that belongs to the message match skill.

## Output format

| CTA | Label | Position | Visual weight | Commitment it implies | Serves the primary conversion | Verdict |
|---|---|---|---|---|---|---|
| Each one | Verbatim | Where | Primary / equal / subordinate | What the visitor expects next | Yes / no | Keep / relabel / subordinate / remove |

End with:

- `Commitments offered on the first screen:` the count and the list
- `Duplicate labels for one action:` the pairs, or none
- `Decision:` unify labels / subordinate the secondary paths / relabel / pull per-CTA data first
- `Missing data:` per-CTA clicks, and what they would change

## Practical example

User: "Above the fold: Get started, Watch demo, Talk to sales, and a newsletter field. Mid page: Learn more twice. Footer: Contact us. Sticky bar says Try it now. Primary conversion is a paid signup. 4400 sessions last month, 26 signups. No per-CTA click data."

Assistant should note: the first screen offers 4 different commitments at equal visual weight, so the page has not decided what it wants and a visitor resolves that by choosing none of them; Get started and Try it now are 2 labels for the same action, which splits the click data across two names and makes the primary action look weaker than it is; Learn more appears twice mid-page and states no next step, so it costs a click and promises nothing. Counting everything, the page makes 8 asks for 1 primary conversion.

Then: one primary label used consistently, the other paths demoted to text links, and the newsletter field moved off the first screen. What this cannot conclude is which of the 8 currently absorbs the attention, because no per-CTA click data was supplied, and that is the one measurement to pull before rewriting anything. 26 signups from 4400 sessions is 0.59 percent; whether label unification moves it is a hypothesis, not a forecast.

## Guardrails

- Do not change the page or the CTAs.
- Do not conclude which CTA wins attention without per-CTA data.
- Do not write a label that promises less or more than the form actually asks for.
- Do not claim a click-through lift.
