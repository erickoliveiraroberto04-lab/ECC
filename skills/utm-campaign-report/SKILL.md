---
name: utm-campaign-report
description: Parses a list of UTM-tagged URLs (one per line) and produces a summary report grouped by campaign, source, and medium — useful for auditing what a campaign actually tagged before a report is built from analytics data.
---

# UTM Campaign Report

## When to Use

Before trusting an analytics breakdown by campaign/source/medium, or when auditing a batch of links generated for a campaign to confirm tagging is consistent.

## How It Works

Run the bundled script against a text file containing one URL per line. It parses the `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, and `utm_content` parameters from each, then prints counts grouped by campaign, by source, and by medium, plus a list of any URLs missing required UTM parameters.

```bash
node skills/utm-campaign-report/scripts/report-utm.js path/to/urls.txt
```

## Examples

- "Summarize how many links we tagged per campaign this quarter"
- "Check this batch of campaign URLs for missing or inconsistent UTM tags"
- "Group these links by utm_source before we hand them to analytics"
