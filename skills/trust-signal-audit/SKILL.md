---
name: trust-signal-audit
description: Reviews whether the page answers the questions a cautious buyer asks before handing over data or money: who runs this, what happens to my data, what if it goes wrong. Use when a form or checkout is about to ship, or when form abandonment is high on an otherwise clear page.
---

# Trust Signal Audit

## Use this skill when

- the page asks for personal data, payment or a call, and the copy around that ask is available for review.
- the page asks for card details, personal data or a document upload.
- abandonment concentrates at the payment or submit step rather than earlier.

This skill diagnoses from absence, at the moment of the ask. It does not assess whether any policy is legally sufficient.

## Required input

- what the page asks for: personal data, payment details, a call, a document upload.
- the copy immediately around that ask, which is the only place these signals do work.
- what the page says about the company: legal entity, address, who is behind it, how to reach a human.
- terms the buyer needs before committing: refund policy, cancellation, data handling, contract length, what happens after they submit.
- optional: abandonment rate at the ask, and where in the flow it happens.
- If the page's ask cannot be identified, ask which conversion is being reviewed. Trust signals are only assessable relative to a specific commitment.

Not for: judging testimonials and proof quality (`social-proof-strength-audit`), or form mechanics (`form-friction-finder`).

## Analysis workflow

1. Inventory trust signals: company info, privacy, security, reviews, proof, guarantees, certifications and contact routes.
2. Match trust signals to the risk the visitor feels at the conversion point.
3. Identify missing trust signals for sensitive forms, high-consideration offers or technical claims.
4. Flag trust signals that are generic, buried or disconnected from the main objection.
5. Recommend trust additions or placement changes near decision points.

## Decision rules

- Position is the whole finding. A refund policy in the footer does not answer a hesitation that happens at the card field. Report distance from the ask, not presence on the site.
- The bigger the commitment, the more the absence costs. A missing legal entity on a newsletter signup is nothing; on a checkout it is disqualifying.
- A contact form as the only support route signals that nobody will answer quickly. Name it, because first-time buyers weigh it heavily.
- Trust defects are diagnosed from absence, not from performance data. You can state that a needed answer is missing without any conversion number, and you should say that is how you concluded it.
- Do not describe a missing policy as a conversion percentage. Say which question goes unanswered at which moment.
- Compliance and legal adequacy are out of scope. Whether a policy exists and is reachable at the ask is in scope; whether it is legally sufficient is not.

## Output format

| Question a cautious buyer asks | Answered on the page | Distance from the ask | Commitment at stake | Severity |
|---|---|---|---|---|
| Who runs this / what happens to my data / what if it goes wrong / when will someone contact me / can I get my money back | Yes / no / only in the footer / only in a linked policy | Adjacent / same screen / elsewhere on the site / nowhere | The specific ask | Disqualifying / costly / minor |

End with:

- `Unanswered at the moment of the ask:` the list
- `Decision:` move terms next to the ask / add a real support route / name the legal entity / ask for data
- `Out of scope:` legal sufficiency of any policy
- `Missing data:` abandonment position, if it would change the ranking

## Practical example

User: "Checkout page. No refund policy visible, no company name or address, privacy policy in the footer only, no security indicators near the card fields, support contact is a form. Cart abandonment at payment step is 71 percent."

Assistant should note: at the moment a card number is typed the page shows no refund terms, no legal entity and no support channel with a human on the end, so every reason to hesitate is unanswered exactly where hesitation happens; a privacy policy reachable only from the footer is not an answer at the point of the ask; a contact form as the only support route signals nobody will answer quickly, which matters most to a first-time buyer. Then: 71 percent abandonment at the payment step is where the money leaves, and the fix is placing refund terms, entity identity and a real support route adjacent to the card fields rather than elsewhere on the site. Whether these lift completion is a hypothesis to measure; trust defects are diagnosed from absence, not from performance data.

## Guardrails

- Do not give legal or compliance advice, and do not assess whether a policy is adequate.
- Do not draft policy text. Say what question needs answering.
- Do not convert a missing trust signal into a predicted lift.
- Say plainly that these findings come from absence rather than from performance data.
