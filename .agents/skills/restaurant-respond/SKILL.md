---
name: restaurant-respond
description: Generate personalized review responses for negative, neutral, and positive reviews — empathetic, professional, conversion-focused with platform-specific tone
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, reviews, responses, reputation, replies]
command: /restaurant respond <name>
output: RESTAURANT-RESPONSES-[Name].md
---

# Review Response Generator

You generate professional, empathetic, and conversion-focused responses to a restaurant's recent reviews — negative, neutral, and positive — with platform-appropriate tone (Yelp formal-public, Google warm-personal, TripAdvisor traveler-focused).

**DISCLAIMER: AI-generated draft responses. Owner should review before posting.**

---

## When to use

- `/restaurant respond <name>` — generate drafts for unanswered reviews
- "draft responses for [name]"
- "reply to bad reviews"

---

## The Response Framework (HEART)

For negative reviews, every reply follows the **HEART** structure:

| Letter | Meaning | Example |
|--------|---------|---------|
| **H** — Hear them | Acknowledge their experience without defensiveness | "Thank you for taking the time to share this feedback, Sarah." |
| **E** — Empathize | Express understanding of how they felt | "We're truly sorry the service felt rushed during your anniversary dinner — that's the opposite of the experience we aim for." |
| **A** — Apologize | Genuine, specific apology — no "but" | "We apologize for falling short." |
| **R** — Resolve | What you've done or will do | "We've reviewed the timing with our team and re-trained on pacing for special occasions." |
| **T** — Take it offline | Invite them back, give a direct contact | "Please reach out to Maria at maria@bellaitalia.com — we'd love to host you again on us." |

### Positive Reviews Framework (THANKS)

| Letter | Meaning | Example |
|--------|---------|---------|
| **T** — Thanks | Genuine thank-you, use their name | "Thank you so much, James!" |
| **H** — Highlight | Echo something specific they mentioned | "So glad the carbonara hit the spot — that's our chef Antonio's signature." |
| **A** — Acknowledge staff | Name the staff they mentioned (or thank the team) | "I'll pass this along to Maria — she'll be thrilled." |
| **N** — Next visit | Subtle nudge to come back | "Save room for the tiramisu next time!" |
| **K** — Keep it short | 2-4 sentences max for positives | |
| **S** — Sign off | Owner name or "The [Restaurant] Team" | "— Marco, Owner" |

### Neutral / 3-Star Framework

Acknowledge the mixed experience, address the specific issue mentioned, invite a return visit. Don't be defensive about the parts they enjoyed.

---

## Execution Pipeline

### Step 1: Identify Reviews That Need Responses

Use WebSearch or read `RESTAURANT-REVIEWS-[Name].md` if it exists. Prioritize:
1. Unanswered negative reviews (last 90 days) — URGENT
2. Unanswered neutral reviews (last 90 days)
3. Recent positive reviews that mentioned staff by name
4. Older negative reviews with no response (within last 12 months)

### Step 2: Gather Context for Each Review

Capture:
- Platform (Yelp / Google / TripAdvisor)
- Reviewer name
- Star rating
- Date
- Verbatim review text
- Any specific dishes, staff, or incidents mentioned
- Whether this is a first-time or repeat reviewer

### Step 3: Generate Draft Response

Use the HEART or THANKS framework. Adapt tone by platform:

| Platform | Tone | Length | CTA Style |
|----------|------|--------|-----------|
| Yelp | More formal, public-facing — assume future customers reading | 4-6 sentences | Email contact, not phone |
| Google | Warm, personal, can be slightly longer | 3-5 sentences | Email or "ask for [owner] next visit" |
| TripAdvisor | Traveler-focused, hospitality language | 4-6 sentences | "We hope to welcome you back" |
| DoorDash / UberEats | Short, focused on the delivery/order issue | 2-3 sentences | Refund/credit offer, not store visit |

### Step 4: Output Format

Save to `RESTAURANT-RESPONSES-[Name].md`:

```markdown
# Review Response Drafts: [NAME]

> **Generated:** [DATE] | **Draft Count:** [N]

**DISCLAIMER: AI-generated drafts. The owner should personalize signoff, verify facts, and post.**

---

## Negative Reviews — RESPOND FIRST

### Review #1 — Google — 1 star — Sarah K. — Mar 15, 2026

**Original review:**
> "Waited 45 minutes for our food on a quiet Tuesday night and when it came the pasta was cold. Server seemed annoyed when I mentioned it. Will not be back."

**Draft response:**
> Sarah, thank you for taking the time to share this — and I'm genuinely sorry. A 45-minute wait on a Tuesday is unacceptable, and cold pasta is on us, full stop. I've spoken with the kitchen and floor team about pacing on slower nights, and we've reviewed the way we handle remake requests. I'd love the chance to make this right. Please email me directly at marco@bellaitalia.com — dinner is on me whenever you're ready to give us another try.
> — Marco, Owner

**Why this works:** Specific (45 min, cold pasta), accountable ("on us, full stop"), shows action taken, names the owner, offers a concrete return offer.

---

### Review #2 — Yelp — 2 stars — David M. — Mar 8, 2026

**Original:** ...

**Draft response:** ...

---

## Neutral Reviews

### Review #5 — Google — 3 stars — Linda T. — Feb 22, 2026

**Original:** "Food was good but really loud — couldn't hear my date."

**Draft response:**
> Thank you, Linda. We've heard this feedback from a few guests recently and we're actively working on sound dampening in the main dining room (acoustic panels installed last month, more coming). For your next visit, ask to be seated in the back room near the wine wall — it's our quietest spot. Hope to see you again soon.
> — The Bella Italia Team

---

## Positive Reviews — DON'T SKIP THESE

Replying to positives signals an engaged owner and lifts your visibility in algorithm signals. Aim for 30%+ response rate on positives.

### Review #8 — Google — 5 stars — James P. — Mar 12, 2026

**Original:** "Best carbonara I've had outside of Rome. Our server Maria was an absolute delight."

**Draft response:**
> Thank you so much, James! Chef Antonio will be thrilled to hear his carbonara is getting the Rome comparison — that's the highest praise. I'll pass this along to Maria right away. Save room for the tiramisu next visit!
> — Marco, Owner

---

## Bulk Response Template Library

For when the owner wants to handle response volume themselves, here are reusable templates with placeholders:

### Negative — Service Issue
```
[Name], thank you for taking the time to share this. A [specific issue] is not the experience we want for anyone, and we're sorry we let you down. We've [specific action taken]. Please email me at [owner-email] — we'd love the chance to make it right.
— [Owner], Owner
```

### Negative — Food Quality
```
[Name], we're truly sorry the [dish] didn't meet the standard you and we expect. Our [chef name] has reviewed [specific corrective action]. We'd love a second chance — please reach out at [owner-email] and we'll make it up to you.
— [Owner]
```

### Positive — Generic
```
Thank you so much, [Name]! [Specific echo of what they mentioned]. [Staff thank-you if applicable]. We can't wait to welcome you back!
— [Owner / Team]
```

### Positive — Mentioned Staff by Name
```
[Name], thanks for the lovely note! [Staff] will be over the moon — I'm sharing this with the team at our pre-shift meeting. See you again soon!
— [Owner]
```

---

## Posting Order Recommendation

1. Negative reviews from last 30 days — TODAY
2. Negative reviews from days 31-90 — within 48 hours
3. Neutral reviews from last 30 days — within 1 week
4. Recent positives that mentioned staff by name — within 2 weeks
5. Set up a recurring 15-minute weekly slot for ongoing review responses

## Rules

- **Never argue** in public, even if the reviewer is wrong. Take it offline.
- **Never reveal private info** (dietary issues, complaints lodged privately).
- **Never use templates verbatim** — always personalize with at least one specific detail from the review.
- **Sign with a name** when possible — "The Team" is the absolute fallback.
- **For 1-star reviews older than 12 months**, a late reply still helps — it signals an active, caring owner to future readers.

**DISCLAIMER: AI-generated draft responses. The restaurant owner should review and personalize before posting.**
```

---

## Quality Standards

- Each response must include at least one specific detail from the review
- Owner contact info must be real (the owner provides it before drafting)
- Never promise free food/refunds in public — always move that offer to email/phone
- Keep apologies genuine — no "we're sorry you feel that way" non-apologies
- Match the reviewer's energy: if they wrote 2 sentences, don't reply with 8

**DISCLAIMER: AI-generated drafts for review by the owner.**
