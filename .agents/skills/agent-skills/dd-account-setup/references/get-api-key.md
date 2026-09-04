# Step 4 — Turn the OAuth session into an API key (detail)

Backs **Step 4** in `SKILL.md`. Runs after Step 3 authenticated the user (OAuth Bearer
token in `${TMPDIR:-/tmp}/dd-oauth-$(id -u).token`, or a `DD_API_KEY`+`DD_APP_KEY` pair).
Produces a validated `DD_API_KEY` in `.env`. Display/wording rules are in `conventions.md`.

The OAuth token authenticates the user, but downstream instrumentation (e.g. LLM Observability) needs a **`DD_API_KEY`**. Use the Bearer token to confirm identity, then obtain a key — **retrieve** the org's most-recent key on an OAuth session (OAuth tokens cannot create keys), or **create** one when authenticating with an app key.

**1. Confirm identity + region.** First load the Bearer token Path B wrote to its `0600` file — shells don't persist between commands, so re-read it at the top of each block that needs it. A `403` here means the token is for a different region — back to Step 2.

```bash
TOKEN=$(cat "${TMPDIR:-/tmp}/dd-oauth-$(id -u).token")   # written by Path B Step 2 (inline exchange)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.${DD_SITE}/api/v2/current_user" \
  | grep -oE '"email"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1
```

**2. Get a `DD_API_KEY` and write it straight to `.env`.** How depends on the auth in hand — and the two cases are genuinely different:

- **OAuth Bearer (Path B/C):** **retrieve** the org's most-recent key — `GET /api/v2/api_keys?page[size]=1&sort=-created_at` → `GET /api/v2/api_keys/{id}` → `data.attributes.key`. **Do NOT `POST` to create** — minting an API key is not supported with an OAuth access token (the server rejects it), so it always fails. If the org has **zero** keys, or listing is role-denied, there is no OAuth create path → send the user to the org key page (they're already signed in). Reading keys is **not** gated by a separate scope — it follows the OAuth user's role, so no `api_keys_read` scope is needed.
- **API + APP key (`DD_API_KEY`+`DD_APP_KEY` present):** this path *can* `POST /api/v2/api_keys` to mint a fresh named key (an app key with `api_keys_write` is allowed to, unlike an OAuth token).

The block below branches on that and **prints the HTTP code of each step** so a failure is diagnosable (list-denied vs empty-org vs secret-denied), not a blanket "403". The secret is written straight to `.env`, never echoed. Send **exactly one** auth mechanism (never Bearer + API/APP together — that resolves to the API key's org).

```bash
TOKEN=$(cat "${TMPDIR:-/tmp}/dd-oauth-$(id -u).token" 2>/dev/null)
# Reload DD_* (env > .env.local > .env) so the app-key branch below sees a file-only DD_API_KEY/DD_APP_KEY.
for f in .env.local .env; do [ -f "$f" ] || continue; for k in DD_SITE DD_API_KEY DD_APP_KEY; do eval "[ -n \"\${$k:-}\" ]" && continue; v=$(grep -E "^$k=" "$f" | head -1 | cut -d= -f2- | sed 's/^["'\'']//;s/["'\'']$//'); [ -n "$v" ] && export "$k=$v"; done; done
envf=".env"
git ls-files --error-unmatch "$envf" >/dev/null 2>&1 && { echo "✗ $envf is git-tracked — use .env.local or untrack it first"; exit 1; }
git check-ignore -q "$envf" 2>/dev/null || printf '\n# Datadog local credentials\n.env\n' >> .gitignore
name="dd-account-setup-skill — $(basename "$PWD")"
esc(){ local s=$1; s=${s//\\/\\\\}; s=${s//\"/\\\"}; printf %s "$s"; }
key=""; outcome=""; keysrc=""; DDLOG="${TMPDIR:-/tmp}/dd-onboard-$(id -u).log"   # raw HTTP/URL machinery → log, clean lines → screen (conventions.md)
if [ -n "$TOKEN" ]; then
  auth=(-H "Authorization: Bearer $TOKEN")
  # OAuth: retrieve most-recent key (NO create — unsupported on OAuth tokens)
  who=$(curl -s "${auth[@]}" "https://api.${DD_SITE}/api/v2/current_user" | grep -oE '"email"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | cut -d'"' -f4)
  echo "AUTH SOURCE: OAuth session token from your Step-3 sign-in (…${TOKEN: -4}), authenticated as ${who:-<unknown>}." >> "$DDLOG"
  echo "▸ fetching your org's most-recent API key — signed in as ${who:-signed-in user} (not reusing any ambient DD_API_KEY)"
  # -g/--globoff: the query has page[size] — without it curl treats [ ] as glob syntax and aborts (exit 3) before sending.
  lresp=$(curl -sg -w $'\n%{http_code}' "${auth[@]}" "https://api.${DD_SITE}/api/v2/api_keys?page[size]=1&sort=-created_at"); lrc=$?
  lcode=$(printf '%s' "$lresp" | tail -1)
  # first "id" in the response is data[0].id — correct for this page[size]=1, sort=-created_at query (single key object, no preceding id field).
  kid=$(printf '%s' "$lresp" | grep -oE '"id"[[:space:]]*:[[:space:]]*"[a-f0-9-]{36}"' | head -1 | cut -d'"' -f4)
  kname=$(printf '%s' "$lresp" | grep -oE '"name"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | cut -d'"' -f4)
  echo "GET /api/v2/api_keys (list, most-recent first): HTTP ${lcode:-<none>}  (curl exit $lrc; key found: $([ -n "$kid" ] && echo "yes — id ${kid}, name \"${kname:-?}\"" || echo no))" >> "$DDLOG"
  if [ "$lrc" != 0 ] || ! printf %s "$lcode" | grep -qE '^[0-9]{3}$'; then
    outcome="TRANSPORT_ERROR (curl exit $lrc, no HTTP status — network/URL/proxy, NOT a permission problem)"
  elif [ "$lcode" = 200 ] && [ -n "$kid" ]; then
    gresp=$(curl -sg -w $'\n%{http_code}' "${auth[@]}" "https://api.${DD_SITE}/api/v2/api_keys/${kid}"); grc=$?
    gcode=$(printf '%s' "$gresp" | tail -1)
    key=$(printf '%s' "$gresp" | grep -oE '"key"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "GET /api/v2/api_keys/${kid} (reveal secret): HTTP ${gcode:-<none>} (curl exit $grc)" >> "$DDLOG"
    if [ -n "$key" ]; then outcome="retrieved existing key"; keysrc="Datadog backend (GET /api/v2/api_keys/${kid}) as ${who:-signed-in user}"
    else outcome="SECRET_DENIED (${gcode:-transport}) — could list keys but not reveal this one's secret"; fi
  elif [ "$lcode" = 200 ]; then outcome="EMPTY_ORG"
  elif printf %s "$lcode" | grep -qE '^(401|403|404)$'; then outcome="LIST_DENIED ($lcode)"
  else outcome="LIST_ERROR ($lcode — server/transient, NOT a permission problem; retry)"; fi
elif [ -n "$DD_API_KEY" ] && [ -n "$DD_APP_KEY" ]; then
  auth=(-H "DD-API-KEY: $DD_API_KEY" -H "DD-APPLICATION-KEY: $DD_APP_KEY")
  body='{"data":{"type":"api_keys","attributes":{"name":"'"$(esc "$name")"'"}}}'
  cresp=$(printf '%s' "$body" | curl -sg -w $'\n%{http_code}' -X POST "https://api.${DD_SITE}/api/v2/api_keys" "${auth[@]}" -H "Content-Type: application/json" --data-binary @-); crc=$?
  ccode=$(printf '%s' "$cresp" | tail -1)
  key=$(printf '%s' "$cresp" | grep -oE '"key"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | cut -d'"' -f4)
  echo "POST /api/v2/api_keys (create): HTTP ${ccode:-<none>} (curl exit $crc)" >> "$DDLOG"
  if [ -n "$key" ]; then outcome="created key \"$name\""; keysrc="Datadog backend (POST /api/v2/api_keys via your app key)"
  elif [ "$crc" != 0 ]; then outcome="TRANSPORT_ERROR (curl exit $crc — network/URL/proxy, NOT a permission problem)"
  else outcome="CREATE_DENIED (${ccode:-?})"; fi
else echo "No auth in hand — complete Step 3 first."; exit 1; fi

if [ -n "$key" ]; then
  echo "SOURCE OF KEY: $keysrc — value never printed; writing …${key: -4} to $envf now."
  ( umask 077; new="$envf.new"; grep -vE '^(DD_API_KEY|DD_SITE)=' "$envf" 2>/dev/null > "$new"
    printf 'DD_SITE=%s\nDD_API_KEY=%s\n' "$DD_SITE" "$key" >> "$new"; mv "$new" "$envf" )
  echo "$outcome (…${key: -4}) → written to $envf"
else
  echo "No key obtained (${outcome:-unknown}) → use the manual step below."
fi
unset key TOKEN auth lresp gresp cresp
```

Read the outcome, don't guess:
- **`retrieved existing key` / `created key`** → the secret is in `.env`; go to step 3. **You never see it** — intentional.
- **`EMPTY_ORG`** (list `200`, zero keys) → the org has no keys and OAuth can't create one. Not an error — send the user to make one (they're already signed in):
  > Your org has no API key yet, and I can't mint one from an OAuth session. Create one here: **`https://app.<DD_SITE>/organization-settings/api-keys`** → **+ New Key** → paste it back.
- **`LIST_DENIED`** (list `403`/`404`) → the OAuth user's role can't manage API keys in this org (common on managed/enterprise orgs like `@datadoghq.com`), or wrong region (identity check would also `403`). Same manual step — or an org admin grants key-management, or use an app key (the `DD_API_KEY`+`DD_APP_KEY` path above).
- **`SECRET_DENIED`** (list OK, `get` denied) → role can list but not reveal secrets. Manual step.
- **`LIST_ERROR`** (list returned `5xx` or another non-`401/403/404` status) → a server-side or transient error, **not** permissions. Retry; if it persists, check the Datadog status page and connectivity to `api.<DD_SITE>`. Do **not** tell the user their access was denied.
- **`CREATE_DENIED`** (app-key `POST` returned non-2xx) → the app key lacks `api_keys_write` or is for another region. Create one manually — same page as above: **`https://app.<DD_SITE>/organization-settings/api-keys`** → **+ New Key** → paste it back.
- **`TRANSPORT_ERROR`** (curl exited non-zero, **no** HTTP status) → not a permission problem: network, proxy, or a malformed URL (e.g. unescaped `[ ]` without `-g`). Re-run; if it persists, check connectivity/proxy to `api.<DD_SITE>`. Do **not** tell the user their key was denied.

In every manual case, when the user pastes a key, **don't echo it** — write it straight to `.env`: `printf 'DD_API_KEY=%s\n' '<pasted>' >> .env && chmod 600 .env` (after the same git-tracked/`.gitignore` guard as above).

**3. Load it from `.env`** (the actual `/api/v1/validate` check runs in **Step 5**): the secret lives in `.env` now — read it back for this shell; never paste or export the literal value.

```bash
# Load DD_* (env > .env.local > .env) — parse, don't source, so a crafted .env can't execute.
for f in .env.local .env; do [ -f "$f" ] || continue; for k in DD_SITE DD_API_KEY DD_APP_KEY; do eval "[ -n \"\${$k:-}\" ]" && continue; v=$(grep -E "^$k=" "$f" | head -1 | cut -d= -f2- | sed 's/^["'\'']//;s/["'\'']$//'); [ -n "$v" ] && export "$k=$v"; done; done
# App key, only if a downstream flow needs one: https://app.<DD_SITE>/organization-settings/application-keys
```

Never fabricate or poll for a key — create it via the API (written to `.env`), or wait for the user to paste one (also written to `.env`). The secret never transits the model or stdout.

> ↳ **Checklist:** once a validated key is in hand, tick **4. Get & validate an API key**, mark **5** ◔.
