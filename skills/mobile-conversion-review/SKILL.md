---
name: mobile-conversion-review
description: Diagnoses what breaks on a phone specifically: thumb reach, viewport competition, tap targets, keyboard behaviour and scroll cost. Use when the mobile conversion rate sits well below desktop and the layout is nominally responsive.
---

# Mobile Conversion Review

## Use this skill when

- device-split conversion data is available and mobile underperforms desktop by more than the offer or traffic mix explains.
- the mobile conversion rate sits well below desktop on a page that is nominally responsive.
- a sticky element, banner or chat widget was added and the mobile numbers moved.

This skill owns the device gap. Overlay timing and contrast belong to `popup-and-overlay-timing-review` and `accessibility-conversion-blocker-check`.

## Required input

- the page on a real mobile viewport: a screenshot at a stated width, or the URL plus the width tested.
- everything that occupies the mobile viewport on load: sticky header, cookie wall, chat bubble, sticky bar, and their heights.
- conversion rate by device, with sessions per device.
- tap target sizes and positions for the primary action and the form controls.
- optional: scroll depth by device, which is what confirms or kills most findings here.
- If only a desktop view is available, say the mobile findings are unverified. Reviewing a phone experience from a desktop screenshot is guessing.

### If the data does not exist

- **No device split:** GA4, Reports, then Tech, then Tech details, with Device category as the dimension and your key event as the metric. That is sessions and conversions per device in one table, which is the whole input for the gap.
- **No chrome heights:** open the page in Chrome's device toolbar at 390 by 664, Inspect each sticky element, and read its height from the box model. Add them up. Two minutes, and it is the number that most often explains the gap.
- **No scroll depth by device:** the same GA4 `scroll` event, with Device category as a secondary dimension. Blunt, and enough to confirm or kill the finding.
- **Cannot open the page yourself:** ask for a screen recording of a first visit on a phone, not a screenshot. The order things appear in is the finding and a still frame does not carry it.
- **Nothing at all:** do not report a device gap. Without sessions per device there is no gap, only an impression, and this skill's first decision rule refuses it.

Not for: overlay timing and which overlay to cut (`popup-and-overlay-timing-review`), or contrast and tap-target compliance (`accessibility-conversion-blocker-check`). This skill owns the device gap; those two own the mechanisms.

## Analysis workflow

1. Review mobile viewport first: load, hero clarity, CTA visibility, form usability, sticky elements and scroll depth.
2. Check tap targets, keyboard types, dropdowns, popups, cookie banners, chat widgets and layout shifts.
3. Compare mobile vs desktop conversion and engagement where data exists.
4. Flag mobile-specific blockers that desktop screenshots hide.
5. Recommend mobile-first fixes ranked by conversion risk and implementation effort.

## Diagnostic rubric

Use this table when the user provides mobile screenshots, recordings or device metrics:

| Area | Mobile evidence | Desktop comparison | Conversion risk | Fix priority |
|---|---|---|---|---|
| Hero / CTA / form / keyboard / popup / speed / sticky element / layout shift | Screenshot, metric, recording note or missing-data marker | Better / same / worse / unknown | High / Medium / Low | Fix now / test / monitor / ask for data |

Then call out:

- Hidden blocker: the issue that would be missed in a desktop-only review.
- Form risk: the field, keyboard, validation or step most likely to stop completion.
- Device split decision: whether the page needs a mobile-specific fix.

## Decision rules

- Establish the gap in numbers first: rate per device with sessions per device. Without both, there is no gap to explain, only an impression.
- Add up what the chrome consumes before content renders. Sticky header plus consent wall plus sticky bar routinely takes a third of a phone screen, and that is the most common cause of a device gap on a nominally responsive page.
- Responsive means the layout reflows. It does not mean the ask survives the reflow. Check specifically whether a primary action exists on the first mobile screen.
- The bottom-right corner is the easiest area for a thumb, and it is where chat widgets install themselves by default. Check what occupies it.
- A finding that would apply equally to desktop is not a mobile finding. Move it to the relevant skill rather than reporting it here.
- Weight findings by mobile's share of sessions. Mobile at 70 percent of traffic makes this the highest-value page problem present; mobile at 15 percent does not.
- Do not recommend a separate mobile page. That is a maintenance commitment and almost never the actual fix.

## Output format

| Device | Sessions | Conversions | Rate | Gap vs desktop |
|---|---|---|---|---|

Then:

| Mobile-specific defect | Evidence | Viewport cost | Thumb zone conflict | Fix |
|---|---|---|---|---|
| The defect | Measured height, screenshot note or missing-data marker | Approximate share of screen | Yes / no | The smallest change |

End with:

- `Is there an ask on the first mobile screen:` yes or no
- `Chrome consuming the viewport:` the sum, per element
- `Decision:` get an ask onto the first screen / reduce chrome / move the widget / pull scroll depth by device
- `Verification status:` measured on a real viewport, or unverified from a desktop view

## Practical example

User: "Mobile 68 percent of sessions, CVR 0.9 percent. Desktop 32 percent of sessions, CVR 3.4 percent. Page is responsive. Sticky header 90px, cookie banner 140px, chat bubble bottom right, primary CTA below a 400px hero image."

Assistant should note: on a common 667px viewport the sticky header plus the cookie banner consume roughly a third of the screen before any content renders, so the hero image pushes the primary CTA off the first screen entirely on mobile and not on desktop, which matches the split; the chat bubble sits in the bottom-right thumb zone where a sticky CTA would normally live, so the two compete for the easiest area to reach; responsive means the layout reflows, not that the ask survives the reflow. Then: mobile carries 68 percent of sessions and produces roughly a quarter of the desktop rate, so this is the highest-value page problem present, and the first fix is getting an ask onto the first mobile screen. Scroll depth by device was not supplied and would confirm the diagnosis.

## Guardrails

- Do not review mobile from a desktop screenshot without labelling it unverified.
- Do not report a defect here that applies equally to desktop.
- Do not recommend a separate mobile page.
- Do not state a device gap without sessions per device.
