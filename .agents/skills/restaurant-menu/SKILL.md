---
name: restaurant-menu
description: Menu engineering analysis — item placement, description quality, pricing psychology, upsell opportunities, photo presence, Kasavana matrix (Stars/Plowhorses/Puzzles/Dogs)
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, menu, engineering, kasavana, pricing]
command: /restaurant menu <url-or-name>
output: RESTAURANT-MENU-[Name].md
---

# Menu Engineering Analysis

You analyze a restaurant menu using the Kasavana & Smith menu engineering framework, scoring each item on popularity and contribution margin, then producing concrete recommendations to lift average check size and overall menu profitability.

**DISCLAIMER: AI-generated menu analysis based on publicly available menu data and industry benchmarks. The restaurant owner should verify item-level cost and sales data.**

---

## When to use

- `/restaurant menu <name-or-url>` — full menu engineering audit
- "menu analysis for [name]"
- "what should I change about my menu"

---

## The Kasavana & Smith Matrix

Every menu item plots on a 2x2 grid:

| | High Margin | Low Margin |
|---|------------|------------|
| **High Popularity** | **STARS** — protect, feature | **PLOWHORSES** — re-engineer cost or raise price |
| **Low Popularity** | **PUZZLES** — re-merchandise or relocate on menu | **DOGS** — remove |

**Definitions:**
- **Margin** = menu price - food cost
- **Popularity** = % of category orders > category mean

---

## Execution Pipeline

### Step 1: Acquire Menu

Sources in priority order:
1. Restaurant website (most accurate)
2. Google Business Profile menu
3. Yelp menu
4. Third-party (Uber Eats, DoorDash) — note prices may include markup
5. Photos of physical menu

```
WebSearch("[name] [city] menu prices")
WebSearch("[name] [city] menu pdf")
```

### Step 2: Catalog Every Item

For each item capture:
- Category (appetizer / entrée / side / dessert / drink)
- Name
- Description (full text)
- Price
- Photo present Y/N
- Position in category (1st, 2nd, 3rd, etc.)
- Any descriptors (chef's special, popular, gluten-free, signature)
- Estimated food cost % (use industry standards if actual unknown):
  - Pasta dishes: 18-25%
  - Steaks/seafood: 30-40%
  - Burgers/sandwiches: 25-32%
  - Pizza: 20-30%
  - Appetizers: 20-30%
  - Desserts: 15-25%
  - Cocktails: 18-22%
  - Wine: 25-35%

### Step 3: Apply Kasavana Matrix

For each item, estimate:
- **Contribution margin** = price - (price × est. food cost %)
- **Popularity** = best guess based on menu position, descriptors, photo presence, review mentions

Plot each item as Star / Plowhorse / Puzzle / Dog.

### Step 4: Score 5 Sub-Dimensions

| Dimension | What to Check | Score (0-20) |
|-----------|---------------|--------------|
| Menu Structure & Layout | Categories logical? Length appropriate? Star placement in golden triangle? | ... |
| Description Quality | Sensory language, origin stories, ingredient highlights, length 15-30 words? | ... |
| Pricing Psychology | Charm pricing ($14.95 vs $15)? Decoy items? Anchoring (high-price first)? Currency symbols dropped? | ... |
| Photo Presence | Photos for high-margin items? Quality? Consistency? | ... |
| Upsell / Combo Engineering | Add-ons, combos, dessert nudges, drink pairings, sides upgrades? | ... |

### Step 5: Identify Quick Wins

The 5 highest-leverage menu changes:
1. Reposition Stars to the golden triangle (top-right, top-left, first item in category)
2. Rewrite descriptions for Plowhorses to boost margin perception
3. Re-merchandise Puzzles with photos and "chef's pick" badges
4. Remove or replace Dogs (free up real estate)
5. Add 2-3 strategic combos / add-ons for 8-12% ticket lift

---

## Pricing Psychology Reference

| Tactic | When to use | Example |
|--------|-------------|---------|
| Charm pricing (.95, .99) | Casual / value-driven concepts | $14.95 vs $15.00 |
| Round pricing (whole dollars) | Premium / fine dining | "32" vs "$32.00" |
| Drop currency symbols | Removes "spending" psychology | "Burger 16" |
| Decoy effect | Anchor a premium item to make others look reasonable | $48 ribeye makes $32 strip steak feel cheap |
| Bracket pricing | 3 price tiers per category (low/mid/high) — mid sells most | $12 / $18 / $26 |
| Avoid price columns | Right-aligned price columns invite price comparison | Inline price after description |
| Avoid dollar signs | Especially in fine dining | $14 → 14 |

---

## Description Quality Rubric

A great menu description (15-30 words):

✅ Uses sensory language (crispy, slow-braised, hand-rolled, charred)
✅ Names 2-3 key ingredients
✅ Mentions origin or technique (Sicilian, wood-fired, 36-month aged)
✅ Hints at preparation (chef's signature, family recipe)
✅ Differentiates from competitors

❌ Generic ("delicious chicken with vegetables")
❌ Just a list of components
❌ Over 40 words (decision fatigue)
❌ Under 8 words for items > $20 (feels cheap)

---

## Golden Triangle / Eye Tracking

Eye-tracking studies show diners read menus in this pattern:

```
1. Top-right corner  ← place 2 highest-margin items here
2. Top-left corner   ← place signature / story-driven items here
3. Center            ← middle ground
4. Bottom-left
5. Bottom-right      ← place items you want LESS attention on
```

Within categories: first item gets 20% more attention. Last item gets 15% more attention. Middle items get the least.

---

## Output Template

Save to `RESTAURANT-MENU-[Name].md`:

```markdown
# Menu Engineering Analysis: [NAME]

> **Generated:** [DATE] | **Menu Score:** [X]/100 | **Total Items Analyzed:** [N]

**DISCLAIMER: AI-generated menu analysis. Verify item-level cost data with the owner.**

## Menu Health Snapshot

| Metric | Value | Industry Benchmark |
|--------|-------|---------------------|
| Total items | X | 20-30 (sweet spot) |
| Avg item price | $X.XX | ... |
| Items with photos | X% | 30-50% (digital), 0-20% (print) |
| Avg description length | X words | 15-30 words |
| Estimated avg food cost | X% | 28-32% |
| Pricing strategy | [Charm / Round / Mixed] | ... |

## Kasavana Matrix Distribution

| Quadrant | Item Count | % of Menu |
|----------|------------|-----------|
| Stars (high pop, high margin) | X | X% |
| Plowhorses (high pop, low margin) | X | X% |
| Puzzles (low pop, high margin) | X | X% |
| Dogs (low pop, low margin) | X | X% |

## Item-by-Item Analysis

### Entrées

| Item | Price | Est. Margin | Pop. | Classification | Recommendation |
|------|-------|-------------|------|----------------|----------------|
| Spaghetti Carbonara | $19 | $14.25 | High | Star | Move to top-right of menu; add chef story |
| Lasagna | $17 | $11.50 | High | Plowhorse | Raise to $18.50 (price elasticity weak here) |
| Branzino | $32 | $22.40 | Low | Puzzle | Add photo, badge "Chef's Pick" |
| Caesar Salad Entrée | $14 | $9.80 | Low | Dog | Remove or convert to half-portion side |

### Appetizers, Sides, Desserts
[same table structure]

## 5 Quick-Win Recommendations

### 1. Reposition Stars to the Golden Triangle
- Move Spaghetti Carbonara to top-right position
- Move Margherita Pizza (signature) to top-left
- Expected impact: +5-8% category sales lift

### 2. Rewrite Plowhorse Descriptions
- Current Lasagna description: "Traditional lasagna with meat sauce." (8 words)
- Suggested: "Hand-layered with Bolognese braised 6 hours, fresh ricotta, and Grana Padano — Nonna Maria's recipe since 1962." (20 words)
- Expected impact: support price increase from $17 → $18.50 without complaints

### 3. Re-Merchandise Puzzles
- Branzino — add photo + "Chef's Pick" badge
- Veal Saltimbocca — pair with house Chianti as a "Tuscany Tasting"
- Expected impact: 30-50% lift in low-pop high-margin item sales

### 4. Remove or Convert Dogs
- Caesar Salad Entrée — remove (low margin, cannibalizes appetizer Caesar)
- Three Cheese Ravioli — replace with seasonal special slot
- Expected impact: freed menu real estate + lower waste

### 5. Add 3 Strategic Add-ons
- "Make it a Bolognese" — add ground beef to any pasta for $4 (90%+ margin)
- "Truffle upgrade" — shaved truffle on any pasta for $7
- "Tiramisu duo" — small tasting + espresso for $8
- Expected ticket lift: +$3.50/cover = +$X,XXX/month at current covers

## Pricing Psychology Audit

| Element | Current State | Recommendation |
|---------|---------------|----------------|
| Charm vs round pricing | Mixed | Standardize on round (concept is mid-premium) |
| Currency symbols | Used | Drop "$" — less price-focus |
| Price alignment | Right-aligned column | Move to inline at end of description |
| Decoy item | None | Add $42 Ribeye to anchor entrée prices down |

## Photo Audit

| Item | Has Photo? | Should It? |
|------|------------|------------|
| Carbonara (Star) | Yes | Yes — keep |
| Branzino (Puzzle) | No | YES — add immediately |
| Lasagna (Plowhorse) | Yes | Yes — but quality is poor, reshoot |
| Caesar (Dog) | No | No — being removed |

## Menu Score Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Structure & Layout | X/20 | ... |
| Description Quality | X/20 | ... |
| Pricing Psychology | X/20 | ... |
| Photo Presence | X/20 | ... |
| Upsell / Combo Engineering | X/20 | ... |
| **Total** | **X/100** | |

## Revenue Impact Projection

If the 5 quick wins are implemented:
- Avg check size lift: +$2.80 (8.5%)
- At [N] daily covers × 30 days: **+$X,XXX/month revenue lift**
- No change in food cost % expected

## What to Implement First

1. **This week:** Move Stars to golden triangle (zero cost, just menu redesign)
2. **This week:** Add 3 strategic add-ons (zero food cost change)
3. **Within 2 weeks:** Rewrite Plowhorse descriptions, raise prices
4. **Within 30 days:** Reshoot photos for Puzzles + signature items
5. **Within 60 days:** Full menu reprint with all changes

**DISCLAIMER: AI-generated analysis. Always verify item-level food cost and sales mix data with the owner before raising prices or removing items.**
```

---

## Quality Standards

- Every item gets a classification (no skipping)
- Every recommendation includes a revenue impact estimate
- Pricing recommendations consider local competition and concept tier
- Photo recommendations factor in cost ($500-$2,000 for a 20-item shoot)

**DISCLAIMER: For educational/research purposes only. AI-generated.**
