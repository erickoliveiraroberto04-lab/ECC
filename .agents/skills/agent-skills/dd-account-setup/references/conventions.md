# Display & wording conventions (all steps)

These rules govern *how every step in `SKILL.md` talks to the user and renders progress*.
Read this once before Step 1; apply it to every step, every reprint.

## Presentation contract — show the user a clean surface, not the machinery

The commands in `SKILL.md` are the *engine*; they are not what the user should read. Raw `curl` bodies,
JSON, and HTTP codes are noise. Follow this contract so every step looks the same and the screen
stays calm:

- **Emit only clean status lines**, one per meaningful transition, using this fixed vocabulary:
  `▸` doing · `✓` done · `⚠` warning (recoverable) · `✗` failed (needs a decision) · `🔑` credential card.
- **Send noise to a log, not the screen.** Every noisy command appends verbose output to
  `DDLOG="${TMPDIR:-/tmp}/dd-onboard-$(id -u).log"` (`>>"$DDLOG" 2>&1`) and echoes only a clean
  line. The blocks in the steps already print clean lines — when you add a `curl`, redirect its body to
  `$DDLOG` and echo a `▸`/`✓`/`✗` line, never the raw response.
- **Details on demand.** If the user asks "why" / "show details" (or a step fails), then — and only
  then — surface the relevant tail: `tail -n 30 "$DDLOG"`.
- **Never** put a secret (key, token, password) in a status line or the log echo — only `…last4`.
- **Never** dump machine detail to the screen: raw OAuth scope lists, HTTP `Location:`/redirect
  headers, JSON bodies, and full response dumps go to `$DDLOG` — echo only a one-line `✓`/`✗`. (Both
  bit a real run: a 40-scope wall and a `Location: /signup/setup` line leaked onto the user's screen.)
- When you paraphrase a step for the user, describe the *outcome* ("Signed in as X on US1"), not
  the tool call ("ran curl …"). Do not narrate Bash invocations.

## Ask with the host's native UI — never letter-entry

For **every** choice (region, and the connect method), use the host's **native question UI**
(Claude Code `AskUserQuestion`; the equivalent in Codex/Cursor) so the user picks from an
up/down-navigable selector. **Never ask the user to type a letter or number to choose** ("enter A",
"press 1") — the letters below (A/B/C) are internal labels for *you* to map paths, not a prompt to
show. Each native option's visible label is the human wording (e.g. "Use my existing credentials",
"Sign in", "Create a new account"). Only fall back to a numbered text menu when no native picker
exists at all; even then, still let the user reply in words, not a bare letter.

## Show a live progress checklist

This flow has five steps and it branches, so **keep the user oriented with a checklist.** Post it when Step 1 begins (right after the preflight board), then **reprint the whole list at each step transition.** Never put a secret (key, token, password) in the list.

**Marker rules — the same on every line, every reprint (a real run corrupted this):**
- Exactly one marker set: `●` done · `◔` current · `○` todo · `⊘` skipped · `✖` failed. Every line is `- <glyph> <number>.` — **no bare `a.` / `b.` / `2.`**.
- **Top-level steps are always numbered `1.`–`5.`**; Path-C sub-items are lettered `a.`/`b.`/`c.` and **indented under step 3**. Never renumber a top-level step as a letter or swap the two — that conflation is exactly what broke the last run (`a. Detect … ◔ 2. Confirm … c. Authenticate`).
- A completed step shows `●`, not a bare letter. Re-emit the full 5-line list each time; don't hand-edit a prior copy.

Canonical shape to copy (fill the markers, keep the numbers/letters fixed):
```
**Datadog account setup**
- ● 1. Detect existing credentials
- ● 2. Confirm region / site
- ◔ 3. Authenticate
- ○ 4. Get & validate an API key
- ○ 5. Ready — hand off
```

Each step in `SKILL.md` ends with a `↳ Checklist:` cue telling you what to flip.

Interactive baseline:

```
**Datadog account setup**
- ◔ 1. Detect existing credentials
- ○ 2. Confirm region / site
- ○ 3. Authenticate
- ○ 4. Get & validate an API key
- ○ 5. Ready — hand off
```

Adapt it to the path actually taken:

- **Headless (Step H)** — collapse to two: `Check DD_API_KEY / DD_APP_KEY / DD_SITE` → `Validate & hand off`.
- **Existing key already valid (Path A)** — steps 3–4 collapse to one: `3. Validate the existing key`.
- **Create account in the terminal (Path C)** — expand step 3 so signup is legible, e.g. mid-flow:

```
- ● 1. Detect existing credentials
- ● 2. Confirm region / site
- ◔ 3. Create account & sign in
  - ● a. Create the org (email + password)
  - ◔ b. Verify email code
  - ○ c. Sign in via OAuth
- ○ 4. Get & validate an API key
- ○ 5. Ready — hand off
```

Tick an item only when its outcome is real — check "Confirm region" after the user confirms (not when you suggest one), and "Authenticate" after a token/key is in hand (not when the browser opens).
