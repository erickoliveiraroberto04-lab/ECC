---
name: landing-page-triage
description: Starts here when a landing page gets traffic and does not convert and nobody knows why. Use when the problem is not yet diagnosed, when you do not know which check to run first, or when someone wants a full page audit and would otherwise get twenty five separate opinions.
---

# Landing Page Triage

The start-here skill. It runs no diagnosis of its own. It establishes what evidence actually exists, then names at most three skills to run, in order, and says what to do when the evidence is thin.

Run this first. A page has many plausible causes for the same symptom, and running every check produces twenty five findings ranked by nothing.

## Use this skill when

- the page gets traffic and does not convert, and the cause is genuinely unknown.
- someone asks for a full landing page audit.
- there are several theories in the room and no way to choose between them.
- you have this pack installed and no idea which of its skills applies.

Do not use this skill when the problem is already named. If the question is "why do people abandon the form", go straight to `form-friction-finder`. Triage is for the undiagnosed case, and running it on a diagnosed one wastes a step.

## Required input

Nothing. This skill's job is to find out what you have.

Ask these five questions, in this order, and stop asking as soon as the answers point somewhere:

1. **What is the page's one conversion, and how many did it get last month?** A raw count, not a rate.
2. **Where does the traffic come from, and can you split the conversions by source?** Cold paid, retargeting, branded search, email, organic.
3. **What is the conversion rate on mobile versus desktop, with sessions for each?**
4. **Does the page have a form, and do you know how many people start it versus finish it?**
5. **Do you have the ad copy that points at this page, and have you read it next to the page recently?**

If the user cannot answer a question, that is an answer. Write down which of the five are unavailable, because the missing ones change what can be concluded, and say so before recommending anything.

## Analysis workflow

1. Collect the five answers. Record the counts, not the rates; a rate with no denominator hides the sample size.
2. Establish whether there is a conversion problem at all. A page with 3 conversions from 90 sessions has a sample size problem, not necessarily a page problem, and the honest first recommendation is to wait for volume or check tracking.
3. Apply the routing table below in order and stop at the first row whose condition is met. The rows are ordered by how often each cause turns out to be the real one, and by how cheap the check is.
4. Name at most three skills. Say what each will need as input, and say plainly which of those inputs the user has already told you they do not have.
5. Name the one measurement worth adding this week if a key input was missing. One, not a list.
6. State explicitly which skills you are **not** running and why. This is the point of triage: the unrun checks are the deliverable as much as the run ones.

## Routing table

Stop at the first row that matches.

| If | Then run, in order | Because |
|---|---|---|
| Mobile rate is far below desktop, and mobile carries most sessions | `mobile-conversion-review`, then `popup-and-overlay-timing-review`, then `accessibility-conversion-blocker-check` | The device gap has three usual causes and they are cheap to separate |
| Conversions split very differently by source | `traffic-temperature-match-review`, then `paid-traffic-message-match-audit` | One page is serving audiences that need different arguments |
| Form starts greatly exceed form finishes | `form-friction-finder`, then `trust-signal-audit`, then `lead-form-sales-handoff-check` | Everyone who started intended to finish, so look at mechanics before motivation |
| Volume of leads is fine and sales says they are weak | `lead-form-sales-handoff-check`, then `traffic-temperature-match-review` | This is a qualification problem wearing a conversion problem's clothes |
| Bounce is high and few people scroll at all | `above-the-fold-clarity-review`, then `hero-section-diagnosis` | They are leaving before any argument gets made |
| People scroll and read and still do not act | `offer-clarity-diagnosis`, then `cta-clarity-check`, then `objection-map-builder` | The page is understood and unconvincing, which is a different failure |
| The page asks for money or card details | `trust-signal-audit`, then `pricing-page-clarity-review` | At the ask, unanswered hesitation is the dominant cause |
| A speed report exists and looks bad | `page-speed-impact-review` | One measured report turns into one prioritised fix |
| Google Ads shows Below average landing page experience | `google-ads-landing-page-experience-review` | Often the finding is keyword mapping, not the page |
| Spend is about to increase | `landing-page-scale-readiness-check`, then `traffic-temperature-match-review` | The current rate was measured on traffic that is about to change |
| A test just finished and someone wants to ship the winner | `landing-page-ab-test-readout` | Run the arithmetic before the decision |
| None of the above, and no data beyond a conversion count | `paid-traffic-message-match-audit`, then `offer-clarity-diagnosis` | Cheapest pair that needs no analytics, and the two most common real causes |

## Decision rules

- Three skills maximum. A triage that recommends eight has not triaged.
- Never route on a rate alone. 4 percent from 25 sessions and 4 percent from 25 000 are different situations and only one of them supports a decision.
- If the monthly conversion count is in single digits, say that no page diagnosis will be conclusive at that volume, and name checking tracking as the first move.
- If the user has none of the five inputs, do not run a diagnosis from the page alone. Route to the two skills that need no analytics, and name the single measurement to add this week.
- If two rows both match, take the higher one and say the other is next. Do not merge them.
- Never produce findings in this skill. Handing back a diagnosis here defeats the routing and produces the twenty-five-opinion output triage exists to prevent.

## Output format

| Answer | Value | Available |
|---|---|---|
| Monthly conversions, traffic split, device split, form starts and finishes, ad copy | The count, or not available | Yes / no |

Then:

| Order | Skill | What it needs from you | You have it |
|---|---|---|---|
| 1, 2, 3 | Skill name | The specific input | Yes / no / partly |

End with:

- `Routed on:` which row of the table matched, quoted
- `Not running:` the skills deliberately skipped, and the one-line reason
- `Add this week:` the single measurement worth having next time, or none needed
- `What no skill here can conclude:` given the missing inputs, stated plainly

## Practical example

User: "Our page gets about 3000 sessions a month from Meta and Google. Maybe 20 demo requests. It feels like the copy is wrong but honestly we do not know. I can get numbers out of GA4 if I have to but I do not have anything to hand."

Assistant should not diagnose. It should ask the five questions, and on this answer establish: 20 conversions from 3000 sessions is roughly 0.67 percent, enough volume to diagnose but a small enough numerator that any segment split will be thin; no device split, no source split and no form data supplied; ad copy not confirmed as read against the page.

Then route on the last row of the table, because none of the specific conditions can be checked yet: run `paid-traffic-message-match-audit` first, since it needs only the ad and the page and it catches the most common real cause, then `offer-clarity-diagnosis`, which needs only the copy. Both are answerable today with zero analytics work.

Not running: everything device-related and everything form-related, because the inputs that would justify them are unavailable, and guessing at a device gap without sessions per device is how a page gets rebuilt for the wrong reason.

Add this week: conversion rate by device with sessions for each. It is one GA4 report, it takes minutes, and it is the single split that most often relocates the whole diagnosis.

What no skill here can conclude: whether the problem is the page at all. With 20 conversions a month, a tracking defect and a genuine conversion problem look identical, and the copy hunch stays a hunch until the split data arrives.

## Guardrails

- Do not diagnose. Route.
- Do not recommend more than three skills.
- Do not route on a rate without its denominator.
- Do not treat a hunch from the user as evidence. Record it as a hypothesis to test, and route on the data instead.
- Say which skills you are not running, every time.
