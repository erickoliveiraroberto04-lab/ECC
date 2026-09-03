---
name: restaurant-pricing
description: Competitive pricing analysis — compares menu prices against local competitors, identifies underpriced items leaving money on the table and overpriced items hurting sales
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, pricing, competitive, menu, margin]
command: /restaurant pricing <name>
output: RESTAURANT-PRICING-[Name].md
---

# Competitive Pricing Analysis

You compare a restaurant's menu prices against direct local competitors of the same cuisine and price tier, then surface specific items that are underpriced (leaving margin on the table) or overpriced (hurting volume).

**DISCLAIMER: AI-generated competitive pricing analysis. The restaurant owner should verify with full P&L data before changing prices.**

---

## When to use

- `/restaurant pricing <name>` — full competitive pricing comparison
- "are my prices right"
- "how does my pricing compare"

---

## Execution Pipeline

### Step 1: Identify Direct Competitors

Find 5-7 restaurants within 3 miles that match:
- Same cuisine
- Same price tier ($, $$, $$$, $$$$)
- Similar concept (casual / fine / fast-casual)

```
WebSearch("best [cuisine] near [neighborhood] [city]")
WebSearch("[cuisine] restaurants similar to [subject name] [city]")
```

### Step 2: Capture Competitor Menus

For each competitor, capture pricing on:
- 3-5 signature / most-ordered dishes
- A common reference dish present at most concepts (e.g., for Italian: spaghetti & meatballs, margherita pizza, caesar salad)
- Appetizer price range (min/avg/max)
- Entrée price range
- Dessert price range
- Glass of house wine / beer / cocktail prices

### Step 3: Build Pricing Comparison Matrix

For each subject menu item, compare to competitor equivalents:

| Subject Item | Subject Price | Comp Avg | Comp Range | Position |
|--------------|---------------|----------|------------|----------|
| Margherita Pizza | $16 | $18.50 | $15-$22 | Underpriced |
| Lasagna | $17 | $19.20 | $17-$22 | Slightly under |
| Carbonara | $19 | $18.40 | $16-$21 | At market |
| Ribeye | $42 | $48.00 | $42-$58 | Underpriced |
| Tiramisu | $11 | $9.50 | $8-$11 | Overpriced |

### Step 4: Identify Underpriced Items (Leaving Money on Table)

Items more than 8% below competitor average WITHOUT a deliberate value-positioning reason. For each:
- Recommend new price
- Calculate revenue lift at current volume
- Consider price elasticity risk

### Step 5: Identify Overpriced Items (Hurting Volume)

Items more than 10% above competitor average WITHOUT clear premium justification. For each:
- Recommend new price OR
- Recommend description/photo upgrade to justify premium OR
- Recommend repositioning as a "premium tier" item

### Step 6: Beverage Pricing Audit

Beverage margins (70-85%) dwarf food margins (60-72%). Critical to get right:
- House wine glass: typical 22-30% of bottle cost
- Beer (draft): aim for 22-25% pour cost
- Cocktails: 18-22% liquor cost
- Soft drinks / coffee: 5-15% cost

---

## Output Template

Save to `RESTAURANT-PRICING-[Name].md`:

```markdown
# Competitive Pricing Analysis: [NAME]

> **Generated:** [DATE] | **Items Analyzed:** [N] | **Competitors:** [N]

**DISCLAIMER: AI-generated competitive pricing analysis. Verify with full P&L before changing prices.**

## Pricing Position Snapshot

| Category | Subject Avg | Comp Avg | Position |
|----------|-------------|----------|----------|
| Appetizers | $X.XX | $X.XX | [Under/At/Over] |
| Entrées | $X.XX | $X.XX | [Under/At/Over] |
| Desserts | $X.XX | $X.XX | [Under/At/Over] |
| Wine (glass) | $X.XX | $X.XX | [Under/At/Over] |
| Cocktails | $X.XX | $X.XX | [Under/At/Over] |

**Overall pricing position:** [Premium / At-market / Value]

## Competitive Set

| Competitor | Distance | Cuisine | Tier | Sample Avg Entrée |
|------------|----------|---------|------|--------------------|
| Competitor A | 0.4 mi | Italian | $$ | $20.50 |
| Competitor B | 0.8 mi | Italian | $$ | $22.00 |
| Competitor C | 1.2 mi | Italian | $$$ | $28.00 |
| Competitor D | 0.6 mi | Italian | $$ | $19.80 |
| Competitor E | 1.5 mi | Italian | $$ | $21.20 |

## Underpriced Items — Recommended Price Increases

| Item | Current | Comp Avg | New Price | Monthly Lift* |
|------|---------|----------|-----------|---------------|
| Margherita Pizza | $16 | $18.50 | $18 | +$XXX |
| Ribeye | $42 | $48 | $46 | +$XXX |
| House Cabernet (glass) | $9 | $11.50 | $11 | +$XXX |
| Tiramisu | n/a | n/a | n/a | n/a |

*Assuming current volume holds (low elasticity). Total est. monthly lift: **+$X,XXX/month**

## Overpriced Items — Recommended Actions

| Item | Current | Comp Avg | Action | Rationale |
|------|---------|----------|--------|-----------|
| Tiramisu | $11 | $9.50 | Drop to $9.95 OR add anchor item ($14 Cannoli Trio) | Currently the menu's price ceiling on desserts |
| Chicken Parm | $26 | $22 | Drop to $24 + upgrade photo | Current price hurts volume; signature item should be a hero |

## Item-by-Item Comparison

### Pasta Category

| Item | [Subject] | Comp A | Comp B | Comp C | Comp D | Comp E | Position |
|------|-----------|--------|--------|--------|--------|--------|----------|
| Carbonara | $19 | $20 | $18 | $24 | $17 | $20 | At market |
| Bolognese | $18 | $19 | $19 | $26 | $18 | $19 | At market |
| ... |

### Pizza Category
[same table structure]

### Entrée Category
[same table structure]

### Beverage Category
[same table structure]

## Price Elasticity Notes by Category

| Category | Elasticity | Implication |
|----------|------------|-------------|
| Pasta | Low (signature items) | Can raise 5-8% without volume loss |
| Pizza | Medium | Raise 3-5%, monitor mix shift |
| Steaks | Low at premium tier | Can raise to comp average |
| Desserts | High (impulse) | Keep at or below comp average |
| House wine | Low | Raise to comp average |
| Cocktails | Low (specialty) | Can raise 8-12% on signatures |

## Hidden Margin Opportunities

1. **Glass pours from premium bottles:** Currently selling $50 bottle wines at $14/glass = 28% pour cost. Industry target = 22-25%. Raise to $16/glass = +$2/glass at current volume.

2. **Add a "Premium Tier" anchor:** A $48 Tomahawk steak would pull diners up to your existing $32 strip — no need to lower the strip.

3. **Daily / weekly special pricing flexibility:** Sunday Sauce, Wednesday Wine Night, Friday Live Music — can absorb 8-12% price premium with "specialty experience" positioning.

4. **Modifier / upgrade pricing:** Currently $0 for substitutions. Could charge $2-4 for protein upgrades, $3 for truffle/lobster, $5 for premium wine pairing.

## Recommended Implementation Sequence

| When | Action | Risk |
|------|--------|------|
| Week 1 | Raise underpriced beverages (wine glass +$2, cocktails +$1) | Low — guests rarely compare drink prices |
| Week 2 | Add 3 high-margin add-ons / upgrades | Zero risk |
| Week 3 | Update menu prices on undermarked entrées | Low — most items raising <10% |
| Week 4-6 | Add premium-tier anchor item | Low — additive, not replacing |
| Month 2 | Reprice overpriced items down + upgrade descriptions | Low — guests notice price drops |

## Total Revenue Lift Estimate

| Source | Estimated Monthly Lift |
|--------|------------------------|
| Underpriced item adjustments | +$X,XXX |
| Beverage repricing | +$X,XXX |
| New add-ons / upgrades | +$X,XXX |
| Overpriced corrections (volume recovery) | +$X,XXX |
| **Total** | **+$XX,XXX/month** |

Annualized: **+$XXX,XXX/year** with zero food cost change.

**DISCLAIMER: All estimates assume current volume holds within 2-3%. AI-generated — verify with full sales mix data before changing prices.**
```

---

## Quality Standards

- Compare to at least 5 direct competitors
- All recommendations include estimated revenue lift
- Consider price elasticity per category
- Flag risk level on every recommendation
- Never recommend a price change > 12% in one move

**DISCLAIMER: For educational/research purposes only. AI-generated competitive analysis.**
