---
name: page-speed-impact-review
description: Turns speed measurements into a conversion priority instead of a scoreboard, and says which specific asset to fix first. Use when a speed report has been run and nobody knows whether any of it is worth the engineering time.
---

# Page Speed Impact Review

## Use this skill when

- a measured speed report exists, from PageSpeed Insights, Lighthouse, Core Web Vitals field data or a real device test.
- a speed report has been run and nobody knows which line of it is worth engineering time.
- images or third-party tags were added and nobody measured what they cost.

This skill needs a measured report. Without one it names the tool to run and stops.

## Required input

- a measured speed report: PageSpeed Insights, Lighthouse, Core Web Vitals field data, or a real device test. Name the tool and whether the numbers are lab or field.
- the specific offending assets if the report names them: image sizes, blocking scripts, fonts, third-party tags.
- device split and the conversion rate per device, so priority can follow the money.
- **If no measured report exists, this skill does not run.** Say which tool to run and stop. An impression of slowness is not an input.

### If the data does not exist

Getting the report takes two minutes and there is no substitute for it.

- **Field data, which is what matters:** pagespeed.web.dev, enter the URL, and read the Core Web Vitals Assessment section at the top. That is real users at the 75th percentile. It only appears if the page has enough traffic; if it says there is not enough data, say so rather than substituting the lab score.
- **Lab data, for diagnosis:** the Lighthouse panel in Chrome DevTools, mobile preset, throttled. It names the LCP element and the largest assets, which is what turns a score into one fix.
- **Asset sizes:** the Network panel, sorted by size, with the cache disabled and the page reloaded.
- **No report and no way to run one:** stop. This is the one skill in the pack that has nothing to say without a measurement, and saying so is more useful than a plausible guess about a hero image.

Not for: mobile layout and interaction friction (`mobile-conversion-review`), or the Google Ads landing page experience rating (`google-ads-landing-page-experience-review`).

## Analysis workflow

1. Collect speed signals: Core Web Vitals, load time, mobile speed, script weight and observed drop-off.
2. Separate perceived speed blockers from actual conversion blockers.
3. Identify heavy scripts, media, third-party tags, forms or layout shifts likely to hurt paid traffic.
4. Compare speed issue severity with device mix and landing page conversion data.
5. Recommend speed fixes only where they plausibly affect conversion or tracking reliability.

## Decision rules

- Field data outranks lab data for prioritisation, and lab data outranks field data for diagnosis. Say which one each number is; a Lighthouse score is not what users experienced.
- Identify the LCP element before recommending anything. One oversized hero image is a single fix; a general speed programme is a quarter of engineering time.
- Layout shift is a conversion defect, not a technical one. Content moving under a thumb produces mis-taps on the elements that convert, so report it in those terms.
- Priority follows traffic share and conversion value, not the size of the number. A 5.8 second LCP on the 12 percent of traffic that is desktop is a smaller problem than a 3 second one on mobile.
- Never state a conversion lift from a speed change. Attribution needs everything else held still, and it never is. Say hypothesis.
- Do not recommend a rebuild, a framework change or a CDN purchase when the report points at three assets.

## Output format

| Metric | Value | Lab or field | Percentile | Offending asset | Fix | Effort |
|---|---|---|---|---|---|---|
| LCP / CLS / INP / TTFB / weight | As measured, with units | Lab / field | e.g. 75th | Named asset or unknown | The specific change | One asset / one template / engineering programme |

End with:

- `Highest-value single fix:` the one change, and the metric it moves
- `Traffic exposure:` device share carrying the worst numbers
- `Decision:` fix the named assets / measure field data first / escalate to engineering / ask for the report
- `Missing data:` what the report did not include
- No predicted conversion lift is given, and say why

## Practical example

User: "PageSpeed Insights on mobile: LCP 5.8s, field data, 75th percentile. CLS 0.24. Hero image is a 2.4MB uncompressed PNG. Three font files load before first paint. Mobile CVR 0.9 percent and mobile is 70 percent of traffic."

Assistant should note: LCP at 5.8s on the 75th percentile of field data means a quarter of real mobile visitors wait longer than that, and the 2.4MB hero PNG is almost certainly the LCP element, which makes this one fix rather than a programme of work; CLS at 0.24 means the layout moves under the visitor's thumb after paint, which produces mis-taps on exactly the elements that convert; 3 fonts blocking first paint compound the same problem.

Then: compressing and correctly sizing one image is the highest-value change available, and mobile carrying 70 percent of traffic is what makes it a business priority rather than a technical chore. What this refuses to give is a predicted conversion lift: attributing a CVR change to speed needs everything else held still, and it never is, so the effect on the 0.9 percent stays a hypothesis. Whether the PNG is genuinely the LCP element is unverified until the report names it; if it does not, that identification is the first thing to confirm.

## Guardrails

- Do not run without a measured report.
- Do not predict a conversion lift from a speed change.
- Do not recommend a rebuild or a purchase when named assets are the problem.
- Always say whether a number is lab or field.
