---
name: restaurant-photos
description: Food photography audit — reviews existing photos, identifies missing item photos, provides specific shot list with angles, lighting, and styling direction
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, photography, photos, food-styling, instagram]
command: /restaurant photos <name>
output: RESTAURANT-PHOTOS-[Name].md
---

# Food Photography Audit & Shot List

You audit a restaurant's existing food photography across Google Business Profile, Yelp, Instagram, website, and delivery platforms — then produce a concrete shot list of what's missing, what to reshoot, and how to brief a photographer.

**DISCLAIMER: AI-generated audit and creative direction.**

---

## When to use

- `/restaurant photos <name>` — full photo audit + shot list
- "do I need new food photos"
- "photography brief for [name]"

---

## Why Photography Matters (Revenue Math)

Industry data:
- GBP listings with 30+ photos get **2x clicks** vs listings with 10
- Instagram posts with food shots > 1k followers convert at **5-7%** vs lifestyle shots at 2-3%
- DoorDash menu items with photos sell **30-50%** more than items without
- 60% of diners say they choose restaurants based on Instagram photos

A typical 20-dish photo shoot ($1,500-$3,000) pays back in **8-14 days** at a 30-cover/day restaurant.

---

## Execution Pipeline

### Step 1: Inventory Existing Photos

For each platform, capture:
- **GBP photos** — count, categories (food/interior/team/exterior/menu), oldest, newest
- **Yelp photos** — same
- **Instagram grid** — last 30 posts, % food vs other
- **Website hero / menu photos**
- **Delivery platforms** — % of items with photos

### Step 2: Identify Missing Photos

Compare against menu. For each menu item, note:
- Has photo on website? Y/N
- Has photo on GBP? Y/N
- Has photo on DoorDash/Uber Eats? Y/N
- Has been featured on Instagram in last 90 days? Y/N

Items that need photos most urgently:
1. **Signature / Star items** — your highest-margin best-sellers
2. **Puzzles (low pop, high margin)** — photos lift these the most
3. **New menu additions** — never had a photo
4. **Seasonal items** — photos go stale

### Step 3: Audit Photo Quality

For each existing photo, score 1-10:
- **Lighting:** natural soft light? No harsh overhead fluorescent?
- **Composition:** rule of thirds? Negative space? Story?
- **Color:** food colors pop? No yellow cast from incandescent?
- **Styling:** clean plate edges? Garnishes intentional? Linens/textures?
- **Angle:** appropriate to the dish (overhead for pizzas/bowls, 3/4 for height items like burgers)?
- **Authenticity:** looks like the actual dish guests receive?
- **Consistency:** matches other photos in style?

### Step 4: Build Shot List

Structured shot list with:
- Item name
- Priority (Must-have / Should-have / Nice-to-have)
- Recommended angle
- Lighting note
- Styling note
- Use case (where the photo will be used)

---

## Angle Cheat Sheet by Dish Type

| Dish Type | Best Angle | Why |
|-----------|------------|-----|
| Pizza | Overhead (90°) | Shows full topping spread |
| Burger / sandwich | 3/4 angle (45°) | Shows height + cross-section |
| Pasta | 45° or overhead | 45° for height, overhead for sauce coverage |
| Salad | Overhead | Shows ingredient variety |
| Soup | 45° with steam | Steam adds appetite appeal |
| Steak / chops | 30° low angle | Emphasizes thickness |
| Cocktail | Eye-level (0°) or slight tilt | Shows glassware + garnish |
| Dessert (layered) | Cross-section or 45° | Shows layers |
| Charcuterie / spread | Overhead | Shows abundance |
| Tacos | 45° lined up | Shows fillings + tortilla |
| Sushi | Overhead grid | Shows precision + variety |
| Plated entrée (fine dining) | 30° low | Drama + chef plating |

---

## Lighting Notes

| Light Source | Use | Avoid |
|--------------|-----|-------|
| North-facing window, soft natural | Best for most food | n/a |
| Diffused softbox | Studio setup | Direct hard light |
| Golden hour patio | Beverages, outdoor concept | Direct sun harsh shadows |
| Restaurant interior lighting | Almost never works | Yellow / orange cast |
| Phone flash | Never | Flattens dimension |

**Pro tip:** Best food photos are taken between 10am-2pm next to a window with a white reflector card opposite.

---

## Styling Quick Wins

1. **Clean plate edges** — use a damp cloth, wipe rim before every shot
2. **Garnish for color** — fresh herbs, citrus, microgreens add the pop
3. **Steam matters** — add a quick blast from a kettle for hot dishes
4. **Surface texture** — wood boards, marble, linen, never flat formica
5. **Props minimal** — one fork, one napkin, one drink, no clutter
6. **Backlight liquids** — for cocktails, drinks, soup, put light behind glass
7. **Negative space** — let one corner be empty for text overlay use later

---

## Output Template

Save to `RESTAURANT-PHOTOS-[Name].md`:

```markdown
# Photography Audit & Shot List: [NAME]

> **Generated:** [DATE] | **Items Needing Photos:** [N] | **Photos to Reshoot:** [N]

**DISCLAIMER: AI-generated photography direction. Use as a creative brief for a food photographer.**

## Photo Inventory Snapshot

| Channel | Total Photos | Last 90 Days | Quality Avg | Coverage |
|---------|--------------|---------------|-------------|----------|
| Google Business Profile | X | X | X/10 | X% of menu items |
| Yelp | X | X | X/10 | X% |
| Instagram (last 30 posts) | X food / X other | X | X/10 | n/a |
| Website | X | X | X/10 | X% |
| DoorDash | n/a | n/a | n/a | X% of menu items |
| Uber Eats | n/a | n/a | n/a | X% |

## Missing Photo Inventory

Items with NO photos on any platform — these should be shot first:

| Item | Category | Margin | Priority |
|------|----------|--------|----------|
| Branzino al Forno | Entrée | High | Must-have |
| Veal Saltimbocca | Entrée | High | Must-have |
| Cannoli Trio | Dessert | High | Must-have |
| Bruschetta Trio | Appetizer | Med | Should-have |
| Affogato | Dessert | High | Should-have |

## Reshoot Candidates

Existing photos that hurt more than they help (under 5/10 quality):

| Item | Where | Current Quality | Issue |
|------|-------|-----------------|-------|
| Lasagna | GBP, Website | 3/10 | Yellow cast, flat lighting, dry-looking |
| Margherita Pizza | Yelp | 4/10 | Overhead but soggy-looking, no steam |
| Tiramisu | GBP | 4/10 | Bad cross-section, sloppy plating |

## Full Shot List (Priority Order)

### Must-Have (Shoot First)

**1. Margherita Pizza** (Signature, Star)
- **Use:** GBP cover, website hero, Instagram top-9
- **Angle:** Overhead (90°) on wooden peel
- **Lighting:** Natural soft light from window left, white reflector right
- **Styling:** Fresh basil on top after baking, drizzle of olive oil, slight char on crust visible
- **Props:** Wood peel, simple linen napkin, no other props
- **Why it matters:** Currently using poor Yelp photo as cover — Star item deserves hero treatment

**2. Branzino al Forno** (Puzzle — needs amplification)
- **Use:** Menu, GBP, Instagram feature
- **Angle:** 30° low angle to show whole fish presentation
- **Lighting:** Soft directional from behind to backlight skin crackle
- **Styling:** Whole fish on platter, lemon halves charred-side up, capers, parsley, single olive oil drizzle
- **Why it matters:** $32 item with zero photos — adding photo typically lifts this category 30-50%

**3. Veal Saltimbocca** (Puzzle)
- **Angle:** 45° showing sage and prosciutto on top
- ...

[Continue for all Must-have items]

### Should-Have (Round 2)

**6. Bruschetta Trio** (Appetizer)
- **Angle:** Overhead, three on a long board
- **Lighting:** Soft natural
- **Styling:** One classic tomato, one ricotta-honey, one mushroom-truffle — color contrast matters
- ...

### Nice-to-Have (Round 3)

**11. Affogato** (Dessert)
- ...

## Recommended Photo Mix Per Category

| Category | Target Count | Current | Gap |
|----------|--------------|---------|-----|
| Hero shots (signature items) | 8-10 | 4 | -4 |
| Full menu items | 100% of menu | 60% | -40% |
| Interior / ambiance | 5-7 | 8 | OK |
| Team / chef in action | 4-6 | 0 | -4 |
| Behind-the-scenes (kitchen, prep) | 5-8 | 0 | -5 |
| Drinks (wine, cocktails) | 6-8 | 2 | -4 |
| Exterior / signage | 2-3 | 3 | OK |
| Customer / atmosphere | 4-6 | 1 | -3 |

## Photographer Brief (Copy-paste ready)

**Project:** Food photography for [Restaurant Name]
**Concept:** [Cuisine] [Tier]
**Style direction:** Warm, natural light, editorial — think Bon Appétit's "Healthyish" column, not glossy commercial. Highlight craft and ingredients.
**Locations:** Restaurant kitchen + dining room window seat
**Shot count:** [X] hero items + [Y] supporting shots = ~[Z] final photos
**Deliverables:** RAW + edited (high-res for print + web-optimized social ratios)
**Aspect ratios needed:** 1:1 (Instagram), 4:5 (Instagram portrait), 16:9 (website hero), 9:16 (Stories/Reels)
**Budget range:** $1,500-$3,000 for 1-day shoot, 25-30 final images
**Recommended local resources:** Check Yelp/Instagram for local food photographers — look for restaurant clients in their portfolio

## Estimated ROI

| Effect | Conservative | Optimistic |
|--------|--------------|------------|
| GBP click lift (30+ photos) | +30% clicks | +100% clicks |
| Delivery item conversion lift | +20% sales on photographed items | +50% |
| Instagram follower lift | +200/mo | +500/mo |
| Estimated monthly revenue lift | +$2,500 | +$6,500 |

Payback period on a $2,500 shoot: **2-4 weeks**.

**DISCLAIMER: AI-generated creative direction. Adapt to the restaurant's concept tier and local photographer availability.**
```

---

## Quality Standards

- Every must-have item has angle + lighting + styling notes
- Photographer brief is copy-paste ready
- ROI projection included
- Aspect ratios specified for all use cases

**DISCLAIMER: For educational/research purposes only.**
