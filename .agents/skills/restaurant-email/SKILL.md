---
name: restaurant-email
description: Email and SMS sequences — loyalty program emails, birthday emails, win-back campaigns, special event invites, abandoned cart for online orders
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, email-marketing, sms, loyalty, win-back, birthday]
command: /restaurant email <name>
output: RESTAURANT-EMAIL-[Name].md
---

# Email & SMS Sequence Library

You generate complete email + SMS sequences for a restaurant's full lifecycle marketing — welcome series, birthday flow, win-back campaigns, abandoned online order, event invitations, and loyalty program nudges.

**DISCLAIMER: AI-generated copy. Verify TCPA / CAN-SPAM compliance for SMS and email. Get express opt-in.**

---

## When to use

- `/restaurant email <name>` — full sequence library
- "loyalty emails for [name]"
- "birthday email flow"

---

## Why Email + SMS Matters

| Channel | Open Rate | Click Rate | Revenue per send |
|---------|-----------|------------|-------------------|
| Email (restaurant industry) | 20-25% | 2-3% | $0.15-$0.40 |
| SMS (restaurant industry) | 95-98% | 15-30% | $0.50-$2.00 |
| Push notification | 30-50% | 5-15% | $0.20-$0.60 |

A 5,000-person email list with one weekly send generates $750-$2,000/month for the restaurant. An SMS list of the same size = $2,500-$10,000/month.

The bottleneck: getting opt-ins. Every receipt, every reservation confirmation, every birthday card is an opt-in opportunity.

---

## The 7 Core Sequences

| Sequence | Trigger | # of touches | Goal |
|----------|---------|--------------|------|
| 1. Welcome Series | New email signup | 3 emails over 2 weeks | First visit / order |
| 2. Birthday Flow | Birthday in next 30 days | 3 touches (14d, 7d, day-of) | Birthday booking |
| 3. Win-Back | No order/visit in 60 days | 3 emails over 21 days | Re-engagement |
| 4. Abandoned Order | Started online order, didn't complete | 1 email + 1 SMS within 24hrs | Recover the order |
| 5. Event Invite | Live music, wine dinner, holiday | 3 emails leading up | RSVPs |
| 6. Post-Visit Thanks | Within 24hrs of visit | 1 email (low-pressure) | Review request + repeat visit |
| 7. Loyalty Program | Loyalty member status changes | Per milestone | Tier upgrade / redemption |

---

## Subject Line Frameworks

| Framework | Open Rate |
|-----------|-----------|
| Curiosity ("We added something to the menu...") | 28-35% |
| Personalization (uses name) | 26-32% |
| Offer ("Free dessert tonight only") | 25-30% |
| Urgency / FOMO ("3 tables left this Saturday") | 30-40% |
| Question ("What's your go-to order?") | 22-28% |
| Local ("Best brunch in [neighborhood] — proof inside") | 25-30% |

**Rules:**
- Subject under 40 chars for mobile preview
- Preview text (50-90 chars) reinforces the subject
- Skip emoji unless it fits the brand (works for casual, hurts fine dining)

---

## SMS Best Practices

- **Length:** Under 160 characters
- **Frequency:** Maximum 2-4 messages per month per subscriber
- **Time:** 10am-8pm only (TCPA)
- **Identity:** Always identify the business
- **Opt-out:** Always include "Reply STOP to unsubscribe"
- **Value:** Every message must deliver real value — never just "buy"

---

## Output Template

Save to `RESTAURANT-EMAIL-[Name].md`:

```markdown
# Email & SMS Sequence Library: [NAME]

> **Generated:** [DATE] | **Sequences:** 7 | **Total Touchpoints:** [N]

**DISCLAIMER: AI-generated copy. Verify TCPA / CAN-SPAM compliance. Get express opt-in.**

---

## Sequence 1 — Welcome Series

### Email 1 — Immediately after signup

**Subject:** Welcome to the family 🍝
**Preview:** Here's something to thank you for joining...

```
Hi [First Name],

Welcome to the [Restaurant] inner circle.

You're going to hear from us about new menu items, exclusive events, and the occasional behind-the-scenes story from our kitchen. Never spam. Promise.

As a thank-you, here's a free appetizer on your first visit:

[Show this email to your server — valid for 60 days]

We can't wait to feed you.

— [Owner Name], Owner
[Restaurant]
```

### Email 2 — 3 days later

**Subject:** The story behind our most popular dish
**Preview:** Why we'll never take this off the menu...

```
Hi [First Name],

3 days into our friendship and I want to introduce you to [Signature Dish].

[3-paragraph story about the dish — origin, ingredients, why it matters]

Come try it. Reservations below.

[CTA: Book a Table]

— [Owner Name]
```

### Email 3 — 10 days later (if no visit yet)

**Subject:** Did your free appetizer expire?
**Preview:** Quick reminder...

```
Hi [First Name],

Your free appetizer expires in 50 days, but I wouldn't wait.

Here's what's new this week:
• [New menu item]
• [Special event]
• [Reservation availability for the next 2 weekends]

[CTA: Reserve Now]

— [Owner]
```

---

## Sequence 2 — Birthday Flow

### Touch 1 — 14 days before birthday — EMAIL

**Subject:** Your birthday is coming up — here's something for it 🎂
**Preview:** A small gift from us...

```
Hi [First Name],

A little bird told us your birthday is in 2 weeks. So here's our gift to you:

🎂 Free dessert + champagne on the house when you celebrate at [Restaurant]
🎂 Personalized birthday card from the chef
🎂 Reserved seating

Reserve your birthday dinner — table is on us to set up, dessert is on us to enjoy.

[CTA: Book Birthday Dinner]

Happy almost-birthday!
— [Owner]
```

### Touch 2 — 7 days before birthday — SMS

```
[Restaurant]: Hey [Name], your birthday is next week! 🎂 We've still got Friday + Saturday open if you want to celebrate with us — dessert is on the house. Book here: [link]. Reply STOP to unsub.
```

### Touch 3 — Day of birthday — EMAIL

**Subject:** Happy birthday, [First Name]! 🎉
**Preview:** Today only...

```
Hi [First Name],

It's your day! Whether you've already got plans or you're still figuring it out, we just wanted to say happy birthday.

The free dessert offer is good through end of next week — no rush, no pressure.

Eat well today. Sleep in tomorrow.

— [Owner] & the [Restaurant] team
```

---

## Sequence 3 — Win-Back Campaign

### Email 1 — Day 60 since last visit/order

**Subject:** We miss you 💔
**Preview:** It's been a minute...

```
Hi [First Name],

It's been 2 months since you've been to [Restaurant]. We noticed.

A few things have changed since you last visited:
• [New dish #1]
• [New dish #2]
• [Anything else interesting]

Come back this week and we'll comp the appetizer of your choice. Just mention this email.

[CTA: Reserve a Table]

— [Owner]
```

### Email 2 — Day 75 (if no return)

**Subject:** Was it something we said?
**Preview:** Honest question...

```
Hi [First Name],

We notice when our regulars stop coming. We'd love to know — was there something about your last visit that didn't live up to the standard?

[Survey link — 3 questions, takes 30 seconds]

Or, if life just got busy, here's a small nudge: dinner for two, our dime, just reply to this email.

Either way, we want to hear from you.

— [Owner]
```

### Email 3 — Day 90 (last attempt)

**Subject:** Last note — and a small offer
**Preview:** Then I'll stop bothering you...

```
Hi [First Name],

If you're not into us anymore, no hard feelings — you can unsubscribe below and we won't take it personally.

But if you're still on the fence:

🍝 Free pasta dish with any entrée order through [date]
🍝 No code needed — just show this email
🍝 Valid for dine-in or takeout

Hope to see you again.

— [Owner]
```

---

## Sequence 4 — Abandoned Online Order

### Touch 1 — 1 hour after abandonment — SMS

```
[Restaurant]: Hey, you left some [signature item] in your cart 🍝 Still hungry? Complete in 60s: [link]. Reply STOP to unsub.
```

### Touch 2 — 4 hours later — EMAIL

**Subject:** Forgot something? 🍕
**Preview:** Your order is waiting...

```
Hi [First Name],

You started an order with us earlier today but didn't finish. We saved it for you:

[Cart contents]

Total: $XX.XX

Complete your order:
[CTA: Finish Order]

Need help? Hit reply or call us at [phone].

— [Restaurant]
```

---

## Sequence 5 — Event Invite (Wine Dinner Example)

### Email 1 — 21 days out

**Subject:** Wine dinner with [Vintner] — Mar 28
**Preview:** 30 seats only...

```
Hi [First Name],

Save the date: Friday, March 28th, 7pm. [Vintner] is joining us for a 5-course Tuscan wine pairing dinner.

The menu:
• [Course 1] paired with [Wine]
• [Course 2] paired with [Wine]
• ...

$95/person. 30 seats only. First come, first served.

[CTA: Reserve a Seat]

— [Owner]
```

### Email 2 — 7 days out

**Subject:** 8 seats left at the wine dinner
**Preview:** Last call...

```
Hi [First Name],

Quick update — only 8 seats remain at next Friday's wine dinner with [Vintner].

[Reminder of the menu]

[CTA: Grab the Last Seats]

— [Owner]
```

### Email 3 — Day before

**Subject:** See you tomorrow night!
**Preview:** Quick details...

```
Hi [First Name],

Quick reminder — tomorrow is the wine dinner.

📍 [Restaurant address]
🕖 7:00pm sharp (we start with the prosecco at 6:45)
👔 Dress: smart casual
🍷 5 courses + 5 pairings + 1 great evening

Can't wait to see you.

— [Owner]
```

---

## Sequence 6 — Post-Visit Thanks

### Email — Within 24 hours of visit

**Subject:** Thank you for dining with us
**Preview:** A small ask...

```
Hi [First Name],

Thanks for joining us at [Restaurant] last night. It means the world that you chose us.

If you have 30 seconds, we'd love a Google review — even one line helps a small family restaurant a lot.

[CTA: Leave a Google Review]

If something didn't live up to your expectations, please reply to this email directly — it goes to me (the owner), not a help desk.

See you again soon.

— [Owner]
```

---

## Sequence 7 — Loyalty Program Touchpoints

### When customer reaches 25 points

**Subject:** You just unlocked a free dessert 🎁
**Preview:** Enjoy on your next visit...

```
Hi [First Name],

You hit 25 points in our loyalty program. That's a free dessert on the house at your next visit.

Just mention "loyalty reward" to your server.

You're 25 points away from a free entrée. Keep going! 💪

[CTA: Reserve a Table]
```

### When customer reaches 50 points

**Subject:** Free entrée unlocked
**Preview:** ...

```
[Similar structure — celebrate the tier, nudge to the next tier]
```

### Tier Anniversary (1 year as VIP)

**Subject:** It's been a year 🎉
**Preview:** Thank you...

```
Hi [First Name],

A year ago today, you joined our VIP program. To say thanks for sticking with us:

• A signed cookbook from our chef
• A complimentary bottle of our house Chianti at your next dinner
• Our genuine gratitude

Just come by — Maria has it ready behind the host stand.

— [Owner] and the whole team
```

---

## SMS Quick-Send Library (Use Sparingly)

| Use Case | Sample SMS (under 160 char) |
|----------|------------------------------|
| Friday night reminder | [Restaurant]: 3 patio tables open tonight, 7-9pm. Reserve fast: [link]. STOP to unsub. |
| Today-only special | [Restaurant]: Today only — half-price wine bottles with dinner. See you tonight? STOP to unsub. |
| Event reminder | [Restaurant]: Tomorrow night — live jazz starts 7pm. No cover. See the menu: [link]. STOP to unsub. |
| Cart abandonment | [Restaurant]: Your [item] is still in the cart 🍝 Finish in 60s: [link]. STOP to unsub. |
| Birthday | [Restaurant]: 🎂 Birthday this week? Dessert is on us when you come in. Book: [link]. STOP to unsub. |
| Win-back | [Restaurant]: We miss you. Free app on your next visit — just show this. STOP to unsub. |

---

## Implementation Notes

### Tech Stack Recommendations
- **Email:** Klaviyo, Mailchimp, or Toast (if using Toast POS)
- **SMS:** Attentive, Postscript, or Klaviyo SMS
- **Customer data:** Toast / Square POS + loyalty integration
- **Birthdays:** Capture in reservation flow and POS

### Frequency Discipline
- Max 1 promotional email per week
- Max 2 SMS messages per month
- Transactional (confirmations, receipts) doesn't count

### Compliance Checklist
- ✓ Express opt-in for SMS (TCPA — written/digital agreement)
- ✓ Easy unsubscribe in every message
- ✓ Physical mailing address in email footer (CAN-SPAM)
- ✓ Honor opt-outs within 10 business days
- ✓ Birthday data captured with consent

## Revenue Projection

| List Size | Email-only Revenue/mo | + SMS Revenue/mo | Total |
|-----------|------------------------|-------------------|-------|
| 500 | $200 | $500 | $700 |
| 1,000 | $400 | $1,000 | $1,400 |
| 2,500 | $1,000 | $2,500 | $3,500 |
| 5,000 | $2,000 | $5,000 | $7,000 |
| 10,000 | $4,000 | $10,000 | $14,000 |

**Path to 5,000 subscribers in 12 months:** ~14 opt-ins per day. Achievable with receipt + reservation + Wi-Fi + loyalty enrollment.

**DISCLAIMER: AI-generated copy. Verify all promo offers are sustainable. Get legal review on TCPA / CAN-SPAM compliance before launching SMS.**
```

---

## Quality Standards

- Every sequence includes the full sequence (not just one email)
- SMS is under 160 chars and includes "STOP to unsub"
- Birthday flow respects opt-in
- Win-back has 3 attempts before stopping

**DISCLAIMER: For educational/research purposes only.**
