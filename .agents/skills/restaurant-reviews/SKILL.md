---
name: restaurant-reviews
description: Multi-platform review analysis — pulls Yelp/Google/TripAdvisor reviews, identifies recurring complaints, sentiment patterns, response rate, and rating trajectory
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, reviews, reputation, sentiment, yelp, google]
command: /restaurant reviews <name>
output: RESTAURANT-REVIEWS-[Name].md
---

# Restaurant Reviews Analysis

You analyze a restaurant's review profile across all major platforms — Google, Yelp, TripAdvisor, OpenTable, and third-party delivery apps — and produce a structured report identifying recurring complaints, recurring praises, owner response performance, and rating trajectory over time.

**DISCLAIMER: AI-generated analysis based on publicly available reviews. Always verify with the restaurant owner.**

---

## When to use

- `/restaurant reviews <name>` — full multi-platform review breakdown
- "analyze reviews for [name]"
- "what are people saying about [name]"

---

## Execution Pipeline

### Step 1: Locate Listings

```
WebSearch("[name] [city] google reviews")
WebSearch("[name] [city] yelp")
WebSearch("[name] [city] tripadvisor")
WebSearch("[name] [city] doordash ubereats grubhub reviews")
```

Capture for each platform:
- URL
- Star rating
- Review count
- Owner verified Y/N
- Last owner response date

### Step 2: Read Recent Reviews

Read the 20 most recent reviews on each platform (last 90 days where possible). Categorize each as:
- Positive (4-5 stars)
- Neutral (3 stars)
- Negative (1-2 stars)

### Step 3: Theme Extraction

Build two lists by tallying common phrases:

**Top 5 Recurring Complaints** — categories like:
- Slow service / long wait
- Cold food / quality issues
- Pricing / portion size
- Noise level / atmosphere
- Parking / location
- Staff attitude
- Cleanliness
- Online ordering / delivery problems
- Bathroom / facilities
- Reservation / wait list

**Top 5 Recurring Praises**:
- Specific dish names (signature items)
- Specific staff names (servers, chef, host)
- Atmosphere / ambiance
- Value
- Service speed (positive)
- Authenticity / quality

### Step 4: Owner Response Analysis

For the last 50 reviews across platforms:
- % of negative reviews with owner reply
- % of positive reviews with owner reply (yes, this matters)
- Average response time (days)
- Response quality: templated vs personalized vs absent

Industry benchmark: top-decile restaurants respond to 100% of negative reviews within 48 hours.

### Step 5: Rating Trajectory

Look at rating over time (use the rating history shown on Yelp / Google or infer from recent vs older reviews):
- 12-month trend: improving / flat / declining
- Inflection points: any sudden drops or jumps
- Recent 30-day score vs all-time average

### Step 6: Cross-Platform Comparison

| Platform | Stars | Count | Last Owner Reply | Response Rate (neg) |
|----------|-------|-------|------------------|---------------------|
| Google | ... | ... | ... | ... |
| Yelp | ... | ... | ... | ... |
| TripAdvisor | ... | ... | ... | ... |

Identify gaps: e.g., 4.4 on Google but 3.6 on Yelp = perception gap to investigate.

---

## Output Template

Save to `RESTAURANT-REVIEWS-[Name].md`:

```markdown
# Reviews & Reputation Analysis: [NAME]

> **Generated:** [DATE] | **Composite Rating:** [X.X] stars | **Total Reviews:** [N]

**DISCLAIMER: AI-generated review analysis. Always verify with the restaurant owner.**

## Cross-Platform Snapshot

| Platform | Stars | Reviews | Owner Verified | Response Rate (Neg) | Last Owner Reply |
|----------|-------|---------|----------------|---------------------|------------------|
| Google | ... | ... | ... | ... | ... |
| Yelp | ... | ... | ... | ... | ... |
| TripAdvisor | ... | ... | ... | ... | ... |
| DoorDash | ... | ... | n/a | n/a | n/a |

**Perception Gap Notes:** [Any large gaps between platforms and likely reason]

## Rating Trajectory (12 Months)

- **Trend:** [Improving / Stable / Declining]
- **Inflection points:** [Any sudden changes and likely cause]
- **Recent 30 days vs all-time:** [Comparison]

## Top 5 Recurring Complaints

1. **[Theme]** — appears in ~X% of negative reviews. Example quote: "..." Action: [specific fix]
2. **[Theme]** — ...
3. ...

## Top 5 Recurring Praises

1. **[Theme]** — appears in ~X% of positive reviews. Example quote: "..." Action: [how to amplify]
2. ...

## Owner Response Performance

| Metric | Current | Industry Benchmark | Gap |
|--------|---------|---------------------|-----|
| Negative response rate | X% | 100% within 48hr | -X% |
| Positive response rate | X% | 30%+ | ... |
| Average response time | X days | <48 hours | ... |
| Response quality | [Personal/Template/Absent] | Personal | ... |

## Unanswered Critical Reviews (Last 90 Days)

[List up to 10 unanswered 1-2 star reviews with quote + date + platform. These need responses NOW.]

## Reviews Score

| Sub-Dimension | Score | Rationale |
|---------------|-------|-----------|
| Star Rating | X/20 | ... |
| Review Volume & Recency | X/20 | ... |
| Owner Response Rate | X/20 | ... |
| Sentiment Pattern | X/20 | ... |
| Rating Trajectory | X/20 | ... |
| **Total** | **X/100** | |

## Recommended Actions This Week

1. Respond to all unanswered 1-star reviews (see list above). Template provided in `/restaurant respond [name]`.
2. ...
3. ...

## 30-Day Outlook

If owner responds to all backlogged negative reviews and resolves the top complaint, expect:
- Star rating lift: +0.1 to +0.3
- Revenue impact: estimated +$X,XXX/month at current covers
```

---

## Quality Standards

- Quote actual review text where possible
- Use percentages not vague terms ("32% of negatives" not "many negatives")
- Always include the example quote for each theme
- Always flag unanswered critical reviews — these are the highest-priority lift
- Connect every recommendation to a revenue number

**DISCLAIMER: For educational/research purposes only. AI-generated analysis.**
