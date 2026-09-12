---
name: responsive-breakpoint-audit
description: Scans a CSS file's media queries and reports the actual breakpoint set in use, flagging inconsistent or oddly-specific values that suggest ad-hoc fixes instead of a deliberate breakpoint system.
---

# Responsive Breakpoint Audit

## When to Use

When a site's responsive behavior feels inconsistent across pages, or before standardizing a stylesheet onto a small, deliberate set of breakpoints.

## How It Works

Run the bundled script against a `.css` file. It extracts every `@media` query's width conditions, lists the distinct breakpoint values in use, and flags values that are close to a common breakpoint but not exactly it (e.g. `767px` vs. the more standard `768px`), which usually means the value was picked to patch one bug rather than chosen deliberately.

```bash
node skills/responsive-breakpoint-audit/scripts/audit-breakpoints.js path/to/styles.css
```

## Examples

- "List every breakpoint actually used in this stylesheet"
- "Are our media query breakpoints consistent, or did they grow ad hoc?"
- "Audit this CSS for near-duplicate breakpoint values"
