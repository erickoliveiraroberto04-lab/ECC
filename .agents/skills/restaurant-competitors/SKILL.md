---
name: restaurant-competitors
description: Top 5 local competitor analysis — menu, pricing, review, social, and SEO comparison with positioning gap identification
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, competitors, competitive-intel, positioning]
command: /restaurant competitors <name>
output: RESTAURANT-COMPETITORS-[Name].md
---

# Local Competitor Analysis

You identify a restaurant's top 5 direct local competitors and produce a head-to-head comparison across menu, pricing, reviews, social presence, local SEO position, and overall positioning — surfacing the gaps the subject restaurant can exploit.

**DISCLAIMER: AI-generated competitive analysis. Use as strategic input, not a copy-paste blueprint.**

---

## When to use

- `/restaurant competitors <name>` — full competitive set analysis
- "who are my competitors"
- "how do I beat [competitor name]"

---

## What Makes a "Direct Competitor"

A direct competitor scores high on ALL of:
1. **Geographic proximity** — within 3 miles (or 10 minutes drive)
2. **Cuisine overlap** — same or very similar (Italian vs Italian, not Italian vs French)
3. **Price tier** — within one tier ($ to $$ is OK, $ to $$$ is not)
4. **Concept type** — casual to casual, fine to fine
5. **Daypart overlap** — both serve dinner, both serve brunch, etc.

**Indirect competitors** (still worth tracking):
- Same cuisine, different city (aspirational competitor)
- Different cuisine, same neighborhood (substitution risk)
- Delivery-only / ghost kitchens (delivery channel risk)

---

## Execution Pipeline

### Step 1: Identify Competitive Set

```
WebSearch("best [cuisine] in [city]")
WebSearch("best [cuisine] in [neighborhood]")
WebSearch("[cuisine] restaurants near [subject address]")
```

Filter for:
- Within 3 miles
- Same cuisine & price tier
- At least 50 reviews (excludes brand-new / shadow restaurants)

### Step 2: Profile Each Competitor

For each of the top 5, capture:

| Field | Detail |
|-------|--------|
| Name | ... |
| Distance | ... |
| Years open | ... |
| Concept type | ... |
| Price tier | ... |
| Google rating | X.X (Y reviews) |
| Yelp rating | X.X (Y reviews) |
| Most-praised dish | ... |
| Most-common complaint | ... |
| Signature differentiator | ... |
| Website | ... |
| Instagram (handle, followers, last post date) | ... |
| TikTok (handle, followers) | ... |
| Delivery platforms | ... |
| Reservation platforms | ... |
| Catering offered? | Y/N |
| Private events offered? | Y/N |

### Step 3: Build the Comparison Matrix

Score each restaurant (subject + 5 competitors) 1-5 on each dimension:
- Menu uniqueness
- Pricing competitiveness
- Online review strength
- Photography quality
- Social media activity
- Local SEO visibility
- Service reputation
- Atmosphere reputation
- Special events / programming
- Catering / off-premise revenue

### Step 4: Identify Positioning Gaps

What's missing from the local market that subject restaurant could own?
- Underserved cuisine niche
- Underserved price tier
- Underserved daypart (late night, weekday brunch, etc.)
- Underserved occasion (date night, family, business lunch, large parties)
- Underserved dietary (vegan, GF, halal)
- Underserved style (counter service, omakase, family-style)

### Step 5: Synthesize Strategic Recommendations

3 strategic moves the subject should make:
1. **Defend** — what each competitor does that subject must match
2. **Attack** — what subject does better and should amplify
3. **Differentiate** — what no one in the local set is doing, subject could own

---

## Output Template

Save to `RESTAURANT-COMPETITORS-[Name].md`:

```markdown
# Local Competitor Analysis: [NAME]

> **Generated:** [DATE] | **Competitors Analyzed:** 5 | **Geographic Scope:** 3-mile radius

**DISCLAIMER: AI-generated competitive analysis. Strategic input only.**

## Competitive Set Overview

| # | Restaurant | Distance | Years | Google | Yelp | Position |
|---|-----------|----------|-------|--------|------|----------|
| Subject | [Subject Name] | 0.0 mi | 5 | 4.2 (412) | 3.9 (287) | Reference |
| 1 | Competitor A | 0.4 mi | 12 | 4.5 (1,247) | 4.4 (892) | #1 local |
| 2 | Competitor B | 0.8 mi | 8 | 4.4 (892) | 4.2 (540) | #2 local |
| 3 | Competitor C | 1.2 mi | 6 | 4.3 (612) | 4.1 (380) | #3 local |
| 4 | Competitor D | 0.6 mi | 3 | 4.6 (310) | 4.4 (210) | Rising |
| 5 | Competitor E | 1.5 mi | 15 | 4.0 (1,420) | 3.8 (940) | Aging incumbent |

## Head-to-Head Scorecard (1-5 per dimension)

| Dimension | Subject | A | B | C | D | E |
|-----------|---------|---|---|---|---|---|
| Menu uniqueness | 4 | 3 | 3 | 4 | 5 | 3 |
| Pricing competitive | 4 | 3 | 4 | 4 | 3 | 5 |
| Online review strength | 3 | 5 | 4 | 4 | 4 | 4 |
| Photography quality | 2 | 5 | 4 | 3 | 5 | 2 |
| Social media activity | 2 | 4 | 4 | 3 | 5 | 1 |
| Local SEO visibility | 3 | 5 | 4 | 3 | 3 | 4 |
| Service reputation | 4 | 4 | 4 | 3 | 4 | 3 |
| Atmosphere reputation | 3 | 5 | 4 | 4 | 3 | 3 |
| Events / programming | 1 | 4 | 3 | 2 | 4 | 2 |
| Catering / off-premise | 2 | 5 | 4 | 3 | 2 | 4 |
| **Total /50** | **28** | **43** | **38** | **33** | **38** | **31** |

**Where subject leads:** Menu uniqueness, pricing competitive, service reputation
**Where subject lags:** Photography, social media, events, catering

## Detailed Profiles

### Competitor A — [Name] — Local #1

**Strengths:**
- 1,247 Google reviews at 4.5 stars (huge moat — would take subject 5+ years to match volume)
- Strong photography across all channels
- Hosts 4 events/month — wine dinners, chef collabs, anniversaries
- Catering revenue likely 25%+ of total

**Weaknesses:**
- Pricing 12-18% higher than subject (creates a value-tier opportunity)
- Slower service per recent reviews (subject can win on speed)
- Older menu — hasn't refreshed in 3 years per Wayback Machine

**Where subject can attack:**
- "Same authentic Italian, better value" positioning
- Add a Sunday Sauce / family-style night (they don't do this)
- Catering at lower price point with similar quality

### Competitor B — [Name] — Local #2

[Same structure]

### Competitor C — [Name]
### Competitor D — [Name] — Rising Threat
### Competitor E — [Name] — Aging Incumbent

---

## Menu & Pricing Side-by-Side

### Signature Pasta Comparison

| Restaurant | Carbonara | Bolognese | Cacio e Pepe |
|------------|-----------|-----------|--------------|
| [Subject] | $19 | $18 | $17 |
| Comp A | $24 | $23 | $22 |
| Comp B | $20 | $19 | $20 |
| Comp C | $22 | $21 | $20 |
| Comp D | $26 | $24 | $24 |
| Comp E | $18 | $17 | $16 |

**Subject's pricing position:** Value tier — 12-25% below market leaders. Defensible if quality is comparable.

### Pizza Comparison
[Same table structure]

### Appetizer Range
| Restaurant | Min | Avg | Max |
|------------|-----|-----|-----|
| Subject | $9 | $13 | $18 |
| Comp A | $11 | $16 | $24 |
| Comp B | $10 | $14 | $19 |
| ... | | | |

## Social Media Position

| Restaurant | IG followers | IG posts last 30d | Last post | TikTok |
|------------|---------------|-------------------|-----------|--------|
| Subject | 1,247 | 3 | 12d ago | None |
| Comp A | 12,400 | 14 | Today | 4,200 |
| Comp B | 4,800 | 8 | 2d ago | 1,100 |
| Comp C | 2,100 | 6 | 4d ago | None |
| Comp D | 8,700 | 22 | Today | 6,300 (viral acct) |
| Comp E | 800 | 0 | 4mo ago | None |

**Position:** Subject ranks 5th in social. Comp D is the biggest threat — viral TikTok account is pulling new diners every month.

## Local SEO Position

### "Best Italian in [City]" — Map Pack Order

1. Comp A
2. Comp D
3. Comp B
[Subject not in map pack]

### "Italian near me" — Map Pack Order

1. Comp A
2. Comp B
3. Comp E
[Subject not in map pack]

**Action:** Subject is invisible in local map pack. Must close GBP optimization + review velocity gaps to break in.

## Positioning Gap Analysis

### What's Missing in the Local Market?

| Gap | Why it's a gap | Subject's ability to own |
|-----|----------------|---------------------------|
| Family-style "Sunday Sauce" service | No one in the set offers this Italian tradition | High — fits Italian-family-owned positioning |
| Strong vegan Italian options | Only 2 vegan options across all 6 restaurants | Medium — requires menu work |
| Cooking classes | None offered | Medium — revenue diversification |
| Late-night dining (after 10pm) | No one open past 10pm | High if labor allows |
| Wine club / by-the-bottle program | Only Comp A | High — pairs with existing wine list |
| Catering at sub-$15/head | All competitors at $18+ | High — pricing strength matches |

### What's Saturated in the Local Market?

| Saturated angle | Recommendation |
|-----------------|----------------|
| Wood-fired pizza | Don't compete here — already 4 strong players |
| Happy hour | Saturated — only viable if you create something truly novel |
| Brunch | Saturated — Comps A, B, D all do strong brunch |

## 3 Strategic Moves

### 1. DEFEND — Match what the leaders do well
- Catch up on photography (Comp A & D's biggest advantage)
- Build review velocity (target: 8-12 new Google reviews/week)
- Improve GBP to break into local map pack

### 2. ATTACK — Amplify where subject already leads
- Lean into value positioning ("Same Italian, 15% better value")
- Champion service reputation (currently rated higher per review)
- Promote menu uniqueness — the signature [dish] is unmatched locally

### 3. DIFFERENTIATE — Own what no one else owns
- **Launch "Sunday Sauce"** — family-style Italian Sunday dinner, $35/person, 4 courses. No one in the set does this. Strong PR angle.
- **Build a "Pasta Class" program** — monthly $65/person cooking class, generates UGC + email signups + new customer trial.
- **Late-night pasta menu (10pm-12am Fri/Sat)** — capture bar-crowd overflow, no competing options.

## Threat Monitoring Plan

| Threat | What to monitor | Action |
|--------|------------------|--------|
| Comp A 5-year anniversary | Press around it, special promos | Have own campaign ready |
| Comp D Tik Tok growth | New menu items, viral dishes | Match with own social content |
| New restaurant openings | Track openings within 2 miles every quarter | Adjust positioning before they open |
| Existing competitor closes | Watch for vacancies, sale signs | Capture their displaced customer base |

**DISCLAIMER: AI-generated competitive analysis. Strategic input only — actual implementation requires owner judgment on capacity and brand fit.**
```

---

## Quality Standards

- Always 5 competitors (not 3, not 7)
- Pricing comparison uses common items (Carbonara, Margherita, etc.)
- Every competitor gets weaknesses AND strengths
- Strategic recommendations are concrete (specific menu items, specific pricing, specific events)

**DISCLAIMER: For educational/research purposes only.**
