---
name: restaurant-report-pdf
description: Generate a professional PDF restaurant report by scanning RESTAURANT-*.md files in current directory and running the bundled Python ReportLab generator
version: 1.0.0
author: AI Restaurant Team
tags: [restaurant, pdf, report, reportlab, deliverable]
command: /restaurant report-pdf
output: RESTAURANT-REPORT.pdf
---

# Restaurant PDF Report Generator

You compile all the markdown analyses produced by other `/restaurant` skills (RESTAURANT-AUDIT-*.md, RESTAURANT-REVIEWS-*.md, RESTAURANT-MENU-*.md, etc.) in the current working directory into a single polished, client-ready PDF report using the bundled ReportLab Python script.

**DISCLAIMER: AI-generated report. Owner should review before sending to clients.**

---

## When to use

- `/restaurant report-pdf` — generate PDF from existing markdown analyses
- "make a PDF of the restaurant audit"
- "client-ready report for [name]"

---

## Execution Pipeline

### Step 1: Scan Current Directory

List all `RESTAURANT-*.md` files in the cwd:

```bash
ls RESTAURANT-*.md
```

Recognize these files:
- `RESTAURANT-AUDIT-[Name].md` — main audit (highest priority)
- `RESTAURANT-REVIEWS-[Name].md`
- `RESTAURANT-MENU-[Name].md`
- `RESTAURANT-PRICING-[Name].md`
- `RESTAURANT-ONLINE-[Name].md`
- `RESTAURANT-PHOTOS-[Name].md`
- `RESTAURANT-SOCIAL-[Name].md`
- `RESTAURANT-SEO-[Name].md`
- `RESTAURANT-ADS-[Name].md`
- `RESTAURANT-EMAIL-[Name].md`
- `RESTAURANT-COMPETITORS-[Name].md`
- `RESTAURANT-RESPONSES-[Name].md`

### Step 2: Extract Key Data

From each markdown file, extract:
- Restaurant name (from filename or top-of-file)
- Date
- Score (if applicable)
- Top findings
- Top recommendations
- Tables of data

Assemble into a single JSON payload like:

```json
{
  "restaurant_name": "Bella Italia Trattoria",
  "city": "Austin, TX",
  "cuisine": "Italian",
  "date": "2026-05-20",
  "overall_score": 64,
  "categories": {
    "Reviews & Reputation": {"score": 68, "weight": "25%"},
    "Menu & Pricing": {"score": 72, "weight": "20%"},
    "Online Presence": {"score": 55, "weight": "20%"},
    "Marketing & Engagement": {"score": 48, "weight": "15%"},
    "Local Competition": {"score": 70, "weight": "20%"}
  },
  "reviews": {...},
  "menu": {...},
  "online": {...},
  "competitors": [...],
  "action_plan": [...]
}
```

### Step 3: Write Temp JSON

Save extracted data to `/tmp/restaurant_data.json`.

### Step 4: Run PDF Generator

```bash
python3 ~/.claude/skills/restaurant/scripts/generate_restaurant_pdf.py /tmp/restaurant_data.json RESTAURANT-REPORT.pdf
```

### Step 5: Confirm Output

Verify `RESTAURANT-REPORT.pdf` exists in cwd. Report path back to user.

---

## If No Markdown Files Exist

If no `RESTAURANT-*.md` files are present, do one of:

**Option A: Demo mode**
```bash
python3 ~/.claude/skills/restaurant/scripts/generate_restaurant_pdf.py --demo
```
Generates `RESTAURANT-REPORT-sample.pdf` with sample data.

**Option B: Prompt the user**
Tell the user no analyses are present in the current directory, and suggest running `/restaurant audit <name>` first.

---

## PDF Structure (what the bundled script produces)

| Page | Content |
|------|---------|
| 1 | Cover — restaurant name, city, cuisine, score gauge, grade, signal |
| 2 | Score dashboard — bar chart of 5 categories + table |
| 3 | Reviews & reputation — star ratings table, top complaints, top praises |
| 4 | Menu engineering — Kasavana matrix, item analysis, pricing |
| 5 | Online presence — GBP, Yelp, website, delivery audit |
| 6 | Marketing recommendations — social cadence, ad angles, email sequences |
| 7 | Competitor comparison — head-to-head scorecard, positioning gaps |
| 8 | 90-day action plan — Week 1 / Days 8-30 / Days 31-90 |
| 9 | Revenue opportunity summary + disclaimer |

---

## Customizations Available

When calling the script, you can override defaults via the JSON:
- `accent_color` — defaults to warm red (#e74c3c)
- `agency_name` — defaults to "AI Restaurant Team"
- `agency_logo_path` — optional logo file path
- `client_name` — restaurant name (filename-safe)

---

## Output Validation

After running, confirm:
- File exists
- File size > 50KB (smaller = error)
- File is valid PDF (first 4 bytes = `%PDF`)

Report back:
```
PDF generated: ./RESTAURANT-REPORT.pdf
Pages: 9
File size: 287 KB
Restaurant: Bella Italia Trattoria
Health Score: 64/100 (Grade: B — Average)
```

---

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `reportlab not installed` | Missing dependency | Run `pip install reportlab` |
| `JSON parsing error` | Bad extraction from MD | Re-run with `--demo` to verify script works |
| `Permission denied` | cwd not writable | Move to a writable directory |
| `No restaurant data found` | No RESTAURANT-*.md files | Suggest running `/restaurant audit` first |

**DISCLAIMER: AI-generated report. Owner should review before sending to clients.**
