---
name: restaurant-ads
description: Facebook/Instagram ad copy variations — 10+ ad copy variants across happy hour, lunch, weekend brunch, catering, birthday/anniversary angles with A/B testing framework
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, ads, facebook, instagram, meta, paid-social]
command: /restaurant ads <name>
output: RESTAURANT-ADS-[Name].md
---

# Facebook & Instagram Ad Copy Variations

You generate 10+ ad copy variations for a restaurant across all major use cases (happy hour, lunch traffic, weekend brunch, catering, birthdays, takeout, new menu launch) with A/B testing framework, audience targeting, budget recommendations, and creative direction.

**DISCLAIMER: AI-generated ad copy. Final ads must comply with Meta's Advertising Standards. Test small budgets before scaling.**

---

## When to use

- `/restaurant ads <name>` — full Meta ad copy set
- "Facebook ads for [name]"
- "Instagram ads for my restaurant"

---

## The 10 Core Restaurant Ad Angles

| # | Angle | When to use | Goal |
|---|-------|-------------|------|
| 1 | **Happy Hour** | Slow weekday hours | Fill 4-6pm |
| 2 | **Lunch Specials** | Lunch undertraffic | Fill lunch covers |
| 3 | **Weekend Brunch** | Saturday/Sunday | Brunch differentiation |
| 4 | **Catering / Office Lunch** | B2B revenue | Corporate orders |
| 5 | **Special Occasions** | Birthdays, anniversaries | Reservations |
| 6 | **Takeout / Delivery** | Compete with delivery apps | Direct online orders |
| 7 | **New Dish / Menu Launch** | Seasonal menu change | Drive curiosity |
| 8 | **Loyalty / Repeat Visit** | Customer retention | Get them back |
| 9 | **First-Time Visit** | New customer acquisition | Trial offer |
| 10 | **Event / Live Music** | Wednesday wine night, Friday jazz | Event RSVPs |

---

## Ad Copy Formulas

### PAS (Problem-Agitate-Solution)
"Stuck eating sad desk lunches? [Agitate the boredom]. [Restaurant] delivers fresh [cuisine] to your office in 30 minutes."

### AIDA (Attention-Interest-Desire-Action)
"Best carbonara in Austin. [I] Hand-rolled pasta, 18-month Pecorino. [D] $19 and your week just got better. [A] Reserve below."

### BAB (Before-After-Bridge)
"Tired of the same chain restaurants? Imagine a place where your server knows your name and the chef is the owner. That's [Restaurant]. [CTA]."

### "Magic 3" (Hook + Proof + Offer)
"[Hook attention-grabber] [Proof — review quote or specific fact] [Offer — what you want them to do]"

---

## Audience Targeting Matrix

| Campaign Goal | Audience | Geo | Age | Interests |
|---------------|----------|-----|-----|-----------|
| New customers (general) | Lookalike of customer email list | 5-mile radius | 25-55 | Fine dining, foodie, cooking |
| First-time visit | Cold — people who haven't visited | 3-mile radius | 28-65 | [Cuisine] cuisine, restaurants |
| Lunch traffic | Workers near restaurant | 1-mile radius weekdays 10am-2pm | 25-55 | n/a |
| Catering | LinkedIn-style B2B | 10-mile radius | 30-60 | HR managers, office managers, EA |
| Brunch | Weekend leisure | 5-mile radius weekends | 25-50 | Brunch, Sunday Funday, mimosas |
| Birthday | "Upcoming birthday this month" | 10-mile radius | 25-65 | n/a |
| Anniversary | "Newlywed", "Engaged" + "Anniversary" interests | 10-mile radius | 25-65 | n/a |
| Repeat customer | Customer email list / SMS list | n/a | n/a | n/a |
| Lapsed customer | Email list minus last-30-day customers | n/a | n/a | n/a |

---

## Budget Framework

| Restaurant Size | Monthly Ad Budget | Daily Spread |
|-----------------|-------------------|--------------|
| Small (1 location, < $1M revenue) | $300-$800/mo | $10-$25/day |
| Mid (1 location, $1-3M revenue) | $1,000-$2,500/mo | $35-$80/day |
| Large (multi-location or > $3M) | $3,000-$10,000/mo | $100-$330/day |

**Allocation:**
- 60% to proven-winner ad sets
- 30% to A/B tests on new copy/creative
- 10% to retargeting

---

## Execution Pipeline

### Step 1: Gather Context

```
WebSearch("[name] [city] menu specials")
WebSearch("[name] [city] events happy hour")
WebSearch("[name] [city] catering")
```

Gather:
- Signature dishes (these go in the ads)
- Existing specials / events
- Price tier
- Hours
- Catering offered?
- Existing review quotes (great for social proof)

### Step 2: Generate Ads

For each of the 10 angles, generate 2 copy variants = 20 total ads.

---

## Output Template

Save to `RESTAURANT-ADS-[Name].md`:

```markdown
# Facebook & Instagram Ad Copy: [NAME]

> **Generated:** [DATE] | **Ad Variants:** 20+ | **Use Cases:** 10

**DISCLAIMER: AI-generated ad copy. Comply with Meta's Advertising Standards. Test before scaling.**

## Quick-Start Recommendation

Based on this restaurant's profile, start with:
1. **Angle:** [Most-fit angle based on the data]
2. **Audience:** [Recommended target]
3. **Budget:** [Recommended starting daily spend]
4. **Test:** 2 copy variants × 2 creatives × 14 days

---

## Ad #1 — Happy Hour Push

**Audience:** 2-mile radius, ages 25-55, M-F evenings
**Budget:** $15-$25/day
**Goal:** Conversions (reservations) or Traffic (online orders)

### Variant A — PAS Formula

> Stop drinking $14 cocktails. 🍸
>
> Every weekday 4-6pm at [Restaurant]:
> • $7 wines by the glass
> • $5 select beers
> • $8 small plates (the burrata is unreal)
>
> Plus — actual sunlight. We have a patio.
>
> Tap below to claim your spot.

**CTA:** Reserve Now

### Variant B — Social Proof + Specifics

> "Best happy hour I've had in 5 years in Austin." — Karen B., Google review
>
> $7 wine. $5 beer. $8 small plates. Mon-Fri 4-6pm at [Restaurant].
>
> The burrata is what gets people talking. Come find out why.

**CTA:** Get Directions

---

## Ad #2 — Lunch Specials

### Variant A — Speed-of-Service Hook

> 30-minute lunch break? We got you.
>
> $14 lunch combos at [Restaurant]:
> ✓ Pasta + side salad + drink
> ✓ Out in under 25 minutes
> ✓ Or order ahead for curbside
>
> Mon-Fri only. Tap to order.

**CTA:** Order Now

### Variant B — FOMO Angle

> Your coworkers are already here.
>
> $14 lunch specials Mon-Fri. Office orders welcome.
>
> [Restaurant] — your new lunch spot.

**CTA:** See Menu

---

## Ad #3 — Weekend Brunch

### Variant A — Aspirational

> Your Sunday upgraded. ☕🥂
>
> Brunch at [Restaurant], Sat-Sun 10am-2pm:
> • Bottomless mimosas $25
> • Wood-fired huevos rancheros
> • Garden patio
>
> Reservations recommended.

**CTA:** Book Brunch

### Variant B — Specific Dish Hero

> The breakfast pizza everyone's posting about.
>
> Egg, pancetta, arugula, hollandaise.
>
> Saturday & Sunday only at [Restaurant]. Don't sleep on this.

**CTA:** Reserve

---

## Ad #4 — Catering / Office Lunch (B2B)

### Variant A — ROI Pitch for Office Managers

> Cater your next office lunch from [Restaurant].
>
> Why offices choose us:
> ✓ $15/person catering menus
> ✓ Free delivery within 5 miles
> ✓ Vegetarian, vegan, GF options
> ✓ 24-hour notice required
>
> Email catering@[domain].com or tap below.

**CTA:** Get a Quote

### Variant B — Testimonial-Led

> "Our team asks for [Restaurant] every Friday." — Jen, HR @ [Tech Company]
>
> Corporate lunch catering from $15/head. Hot, delivered, on time.

**CTA:** See Menus

---

## Ad #5 — Special Occasions (Birthday / Anniversary)

### Variant A — Birthday-Targeted

> Birthday this month?
>
> Celebrate at [Restaurant]. The birthday guest gets:
> ✓ Free dessert on the house
> ✓ Reserved seating
> ✓ Personalized card from the chef
>
> Reserve below — tell us it's a birthday.

**CTA:** Book Birthday Dinner

### Variant B — Anniversary

> 30 years of marriage. 30 years of finding new restaurants.
>
> Make this one the new tradition.
>
> Anniversary tasting menu at [Restaurant]: 5 courses, wine pairing, $95/person.

**CTA:** Reserve

---

## Ad #6 — Takeout / Skip the Delivery App Fees

### Variant A — Anti-DoorDash

> DoorDash adds $8 in fees. We don't.
>
> Order direct from [Restaurant] — same menu, same price, no service fees.
>
> Free pickup. Ready in 25 min.

**CTA:** Order Direct

### Variant B — Loyalty Angle

> Order direct and get points.
>
> Every $10 you spend at [Restaurant].com = 1 free dish in the future.
>
> Why pay delivery apps when you can earn rewards?

**CTA:** Start Earning

---

## Ad #7 — New Dish / Menu Launch

### Variant A — Limited-Time Hook

> [Chef's Name] just dropped the new winter menu.
>
> Available 6 weeks only:
> • [New dish 1]
> • [New dish 2]
> • [New dish 3]
>
> Reserve before it's gone.

**CTA:** See Menu

### Variant B — Behind-the-Scenes

> Why we added this dish to our menu (and why we'll never take it off):
>
> [Restaurant chef] tells the story →

**CTA:** Watch Video

---

## Ad #8 — Loyalty / Win-Back

### Variant A — "We Miss You"

> It's been 90 days since your last visit to [Restaurant]. 💔
>
> Come back this week and dessert is on us.
>
> No code needed. Just mention this ad.

**CTA:** Reserve

### Variant B — New Reasons

> Last time you were here, the menu was different.
>
> See what's new at [Restaurant] — 6 dishes added since you last visited.

**CTA:** See Updates

---

## Ad #9 — First-Time Visit Offer

### Variant A — Trial Offer

> First time at [Restaurant]? 🆕
>
> Free appetizer with any entrée order.
>
> Show this ad to your server. Valid through [date]. New guests only.

**CTA:** Get Directions

### Variant B — Curiosity Hook

> 4.6 stars. 487 reviews. Family-owned since 2014.
>
> If you haven't tried [Restaurant] yet — what are you waiting for?

**CTA:** See Reviews

---

## Ad #10 — Event / Live Music Night

### Variant A — Specific Event

> Live jazz + carbonara every Wednesday.
>
> [Musician name] takes the stage at 7pm. Menu specials all night. No cover.
>
> Reservations recommended (we fill up).

**CTA:** Reserve

### Variant B — Recurring Theme

> The best Wednesday night in [neighborhood]:
> 🎷 Live jazz 7-10pm
> 🍝 Half-price pasta
> 🍷 Wine flights $15
>
> Every Wednesday at [Restaurant].

**CTA:** Book Now

---

## A/B Testing Framework

### What to Test
1. **Hook (first line):** PAS vs Social Proof vs Specific Number
2. **CTA:** "Reserve" vs "Book Now" vs "Order Direct"
3. **Creative:** Food shot vs People-eating shot vs Owner/chef portrait
4. **Audience:** Lookalike vs Interest-based vs Geo-narrow
5. **Format:** Single image vs Carousel vs Reel/video

### Test Setup
- Budget per test: $50-$100
- Duration: 7-14 days
- Sample size: 1,000+ impressions per variant before drawing conclusions
- Metric: Click-through rate (CTR) + cost per conversion (CPA)

### Winning Metrics
- CTR > 1.5% (good), > 2.5% (great)
- CPA under $15 for reservations
- CPA under $25 for catering inquiries
- ROAS (return on ad spend) > 3x

---

## Creative Direction

| Ad Type | Best Format | Aspect Ratio |
|---------|-------------|---------------|
| Happy hour | Single image (drinks/people) | 1:1 or 4:5 |
| Brunch | Carousel (3-4 dish photos) | 1:1 |
| Catering | Single image (spread / variety) | 1:1 |
| Special occasion | Reel (15s atmosphere video) | 9:16 |
| Takeout | Single image (takeout bag handoff) | 4:5 |
| Win-back | Carousel (3 new dishes) | 1:1 |
| Live music | Reel (event clip) | 9:16 |

## Restaurant Ad Compliance Checklist

- ✓ No claims like "best in the city" without proof
- ✓ Prices accurate at time of ad
- ✓ Health/dietary claims (gluten-free, vegan) accurate
- ✓ No misleading photos (must reflect actual dishes)
- ✓ Alcohol ads only target 21+ in US
- ✓ Disclaimers for "while supplies last" / "limited time"

**DISCLAIMER: AI-generated ad copy. Verify Meta Ad Policy compliance. Local liquor laws apply to alcohol-related ads.**
```

---

## Quality Standards

- Each angle has 2 distinct copy variants
- Each ad includes audience + budget + CTA
- All claims verifiable
- A/B testing framework is concrete

**DISCLAIMER: For educational/research purposes only.**
