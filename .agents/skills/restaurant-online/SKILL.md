---
name: restaurant-online
description: Online presence audit — Google Business Profile completeness, Yelp listing quality, website assessment, online ordering setup, third-party platform presence
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, online-presence, gbp, yelp, website, ordering]
command: /restaurant online <name>
output: RESTAURANT-ONLINE-[Name].md
---

# Online Presence Audit

You audit a restaurant's full digital footprint across Google Business Profile, Yelp, the restaurant's website, third-party delivery platforms (Uber Eats, DoorDash, Grubhub), reservation platforms (OpenTable, Resy), and social presence — then score each and provide a prioritized fix list.

**DISCLAIMER: AI-generated audit based on publicly observable data.**

---

## When to use

- `/restaurant online <name>` — full presence audit
- "audit my Google Business Profile"
- "how does my restaurant look online"

---

## Execution Pipeline

### Step 1: Gather URLs

```
WebSearch("[name] [city] google business profile")
WebSearch("[name] [city] yelp")
WebSearch("[name] [city] website")
WebSearch("[name] [city] doordash ubereats grubhub")
WebSearch("[name] [city] opentable resy")
```

### Step 2: Audit Google Business Profile (GBP)

GBP is the #1 source of new restaurant customers in 2026. Audit checklist:

| Element | Best Practice | Score (1-10) |
|---------|---------------|--------------|
| Business name | Exact match across all platforms | ... |
| Categories | Primary + 2-4 secondary categories | ... |
| Hours | Accurate, includes special hours | ... |
| Phone | Direct restaurant line (not third-party) | ... |
| Address | Exact and accurate | ... |
| Website URL | Live and functional | ... |
| Menu link | Direct to menu page | ... |
| Reservation link | Direct to OpenTable/Resy/own | ... |
| Order link | Direct to online ordering | ... |
| Description | 750 char max, includes cuisine + signature dish + USP | ... |
| Photos | 30+ photos, 80% food/interior, last 90 days activity | ... |
| Photo categories | Logo, cover, interior, food, team | ... |
| Posts | At least 1 post/week | ... |
| Q&A | All questions answered by owner | ... |
| Attributes | All applicable (wheelchair, parking, kid-friendly, etc.) | ... |
| Service areas | Defined if delivery offered | ... |
| Products | Top 10 menu items as products | ... |

### Step 3: Audit Yelp Listing

| Element | Best Practice | Score (1-10) |
|---------|---------------|--------------|
| Business owner verified | Yes | ... |
| Cover photo | High-quality food or interior | ... |
| Photos | 50+ photos | ... |
| Menu | Uploaded and current | ... |
| Hours | Accurate | ... |
| About / specialties section | Filled with story + signatures | ... |
| Attributes | All applicable | ... |
| Reservation integration | OpenTable / Yelp Reservations enabled | ... |
| Order integration | Yelp Delivery enabled | ... |

### Step 4: Audit Website

| Element | Best Practice | Score (1-10) |
|---------|---------------|--------------|
| Mobile-responsive | Yes (60%+ of traffic is mobile) | ... |
| Page speed | Under 3 seconds load | ... |
| Menu | Current and downloadable | ... |
| Online ordering | First-party or third-party widget | ... |
| Reservations | First-party or OpenTable widget | ... |
| Contact info | Phone, address, hours visible | ... |
| Photos | High-quality, recent | ... |
| About / story | Owner/chef story present | ... |
| Press / awards | Featured if available | ... |
| Gift cards | Sellable online | ... |
| Email signup | Newsletter or loyalty | ... |
| Social links | Instagram, Facebook, TikTok | ... |
| Schema markup | Restaurant schema for Google rich results | ... |

### Step 5: Audit Delivery Platforms

For each (Uber Eats, DoorDash, Grubhub):

| Element | Check |
|---------|-------|
| Listed? | Y/N |
| Star rating | X.X |
| Hours match GBP | Y/N |
| Menu fully populated | Y/N |
| Photos on menu items | %  |
| Pricing markup over dine-in | % |
| Response to reviews | %  |

### Step 6: Audit Reservation Platforms

| Platform | Listed? | Avg Wait Time | Reviews | Notes |
|----------|---------|---------------|---------|-------|
| OpenTable | ... | ... | ... | ... |
| Resy | ... | ... | ... | ... |
| Yelp Reservations | ... | ... | ... | ... |
| Tock | ... | ... | ... | ... |

### Step 7: NAP Consistency Check

Compare Name / Address / Phone across:
- Google Business Profile
- Yelp
- Website
- Facebook
- Apple Maps
- Bing Places
- TripAdvisor
- Yellow Pages

Even 1 mismatched character (St vs Street, suite # variation) hurts local SEO.

---

## Output Template

Save to `RESTAURANT-ONLINE-[Name].md`:

```markdown
# Online Presence Audit: [NAME]

> **Generated:** [DATE] | **Presence Score:** [X]/100

**DISCLAIMER: AI-generated audit based on publicly observable data.**

## Presence Snapshot

| Channel | Score | Status |
|---------|-------|--------|
| Google Business Profile | X/100 | [Strong / Mixed / Weak / Critical] |
| Yelp | X/100 | ... |
| Website | X/100 | ... |
| Delivery Platforms | X/100 | ... |
| Reservation Platforms | X/100 | ... |
| Social Media | X/100 | ... |

## Google Business Profile Audit

### Completeness Checklist
[Full GBP checklist table from Step 2 with each item rated]

### Critical Gaps
1. [Specific missing element + revenue impact]
2. ...

### Quick Wins (under 10 min each)
1. Add online order link (currently missing) — capture customers searching from Google
2. Add 10 more photos (currently 12, target 30+) — listings with 30+ photos get 2x clicks
3. Reply to 4 unanswered Q&A questions
4. Update hours to include special holiday hours

## Yelp Listing Audit
[Same structure as GBP]

## Website Audit

### What Works
- ...

### What Needs Fixing
| Issue | Impact | Effort | Fix |
|-------|--------|--------|-----|
| Site is not mobile-responsive | 60% of visitors bounce | High | Rebuild on Squarespace/Wix ($500-2000) or use a restaurant template |
| No online ordering | Losing $X,XXX/mo | Med | Add ChowNow, Toast, or own platform |
| No reservations | Friction in booking | Low | Add OpenTable or Resy widget |
| Schema markup missing | No rich results in Google | Med | Add Restaurant + Menu schema |

## Delivery Platform Audit

| Platform | Listed | Stars | Reviews | Menu Complete | Notes |
|----------|--------|-------|---------|---------------|-------|
| DoorDash | Yes | 4.4 | 412 | 87% | Add 5 missing items, photo 6 |
| Uber Eats | Yes | 4.2 | 287 | 75% | Update prices (12% higher than dine-in feels excessive) |
| Grubhub | No | — | — | — | Consider adding (lower fees in some markets) |

## Reservation Platform Audit

| Platform | Listed | Avg Reviews | Notes |
|----------|--------|-------------|-------|
| OpenTable | Yes | 4.5 (87 reviews) | Strong presence |
| Resy | No | — | Consider for fine-dining positioning |

## NAP Consistency Report

| Source | Name | Address | Phone | Match? |
|--------|------|---------|-------|--------|
| Google | Bella Italia Trattoria | 1240 Main St | 555-1234 | Reference |
| Yelp | Bella Italia | 1240 Main Street | 555-1234 | Address mismatch ("Street" vs "St") |
| Website | Bella Italia Trattoria | 1240 Main St, Ste B | 555-1234 | Address mismatch (missing suite on Google) |
| Facebook | Bella Italia Trattoria | 1240 Main St | (555) 123-4567 | Phone formatting only — OK |

**NAP grade: B-** — 2 small mismatches will dilute local search authority. Fix: standardize on the exact format used on the lease/business license.

## Online Presence Score Breakdown

| Sub-Dimension | Score | Notes |
|---------------|-------|-------|
| Google Business Profile | X/20 | ... |
| Yelp Listing Quality | X/20 | ... |
| Website Quality | X/20 | ... |
| Third-Party Platform Coverage | X/20 | ... |
| NAP & Citation Health | X/20 | ... |
| **Total** | **X/100** | |

## Prioritized Action List (Top 10)

1. **Add online ordering to GBP** — 5 min — captures Google search demand
2. **Upload 18 more photos to GBP** — 30 min — listings with 30+ photos get 2x clicks
3. **Reply to 4 unanswered Q&A questions** — 15 min — boosts engagement signal
4. **Standardize NAP across all platforms** — 60 min — local SEO authority
5. **Enable Yelp Reservations** — 10 min — captures Yelp discovery traffic
6. **Add Restaurant schema markup to website** — 1 hour — rich results in Google
7. **Add weekly GBP post (specials, events)** — 10 min/week — keeps profile active
8. **Verify business on Apple Maps** — 1 day approval — captures iOS users
9. **Update DoorDash menu to 100% photo coverage** — 30 min — lifts order conversion 20-30%
10. **Add gift card sales to website** — 2 hours — captures holiday gifting + cash flow

## Estimated Revenue Impact

| Fix | Monthly Lift |
|-----|--------------|
| Online ordering on GBP | +$2,000-$4,000 |
| GBP photo expansion | +$800-$1,500 |
| Yelp Reservations | +$500-$1,000 |
| DoorDash photo completion | +$1,200-$2,500 |
| Gift card sales | +$300-$800 |
| **Total estimated lift** | **+$4,800-$9,800/month** |

**DISCLAIMER: AI-generated audit. Always verify with the owner before changing platform settings.**
```

---

## Quality Standards

- Every audit element gets a 1-10 score
- Every critical gap has a revenue impact estimate
- Recommendations sorted by impact / effort
- NAP consistency check is exhaustive — every platform

**DISCLAIMER: For educational/research purposes only.**
