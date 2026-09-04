# Regions & IP auto-detection (Step 2)

Reference tables for Step 2 in `SKILL.md`: the allowed sites, their app/signup base
URLs, and the country→region mapping used when `DD_SITE` is unset. The decision logic
(validate `DD_SITE`, else IP-detect and confirm) lives in Step 2 itself.

## Region reference

| Region | `DD_SITE` | App / signup base URL |
|--------|-----------|-----------------------|
| 🇺🇸 US1 — East (Virginia) | `datadoghq.com` | `https://app.datadoghq.com` |
| 🇺🇸 US3 — West (Oregon) | `us3.datadoghq.com` | `https://us3.datadoghq.com` |
| 🇺🇸 US5 — Central (Ohio) | `us5.datadoghq.com` | `https://us5.datadoghq.com` |
| 🇪🇺 EU1 — Europe (Frankfurt) | `datadoghq.eu` | `https://app.datadoghq.eu` |
| 🇯🇵 AP1 — Japan (Tokyo) | `ap1.datadoghq.com` | `https://ap1.datadoghq.com` |
| 🇦🇺 AP2 — Australia (Sydney) | `ap2.datadoghq.com` | `https://ap2.datadoghq.com` |
| 🇬🇧 UK1 — United Kingdom (London) | `uk1.datadoghq.com` | `https://uk1.datadoghq.com` |

The API host is uniformly `https://api.${DD_SITE}`.

The full allowed-site list (for validating a supplied `DD_SITE`) is exactly:

`datadoghq.com` · `us3.datadoghq.com` · `us5.datadoghq.com` · `datadoghq.eu` · `ap1.datadoghq.com` · `ap2.datadoghq.com` · `uk1.datadoghq.com`

## Country → region mapping (IP auto-detection)

Given the ISO 3166-1 alpha-2 country code from `https://ipinfo.io/json`, suggest this region. **On no match, timeout, or error → default to US1 (`datadoghq.com`).**

| Suggested region | `DD_SITE` | Country codes |
|------------------|-----------|---------------|
| 🇺🇸 US1 — East (Virginia) | `datadoghq.com` | US, CA, MX, PR, VI, BR, AR, CL, CO, PE, VE, EC, BO, PY, UY |
| 🇪🇺 EU1 — Europe (Frankfurt) | `datadoghq.eu` | DE, FR, IT, ES, NL, BE, AT, CH, PT, SE, NO, DK, FI, PL, CZ, RO, HU, GR, BG, HR, SK, LT, LV, EE, SI, LU, MT, CY, IL, AE, SA, ZA, EG, NG, KE, TR, IN, PK, BD, LK |
| 🇯🇵 AP1 — Japan (Tokyo) | `ap1.datadoghq.com` | JP, KR, TW, HK, SG, TH, MY, PH, VN, ID, CN |
| 🇦🇺 AP2 — Australia (Sydney) | `ap2.datadoghq.com` | AU, NZ, FJ, PG |
| 🇬🇧 UK1 — United Kingdom (London) | `uk1.datadoghq.com` | GB, IE |

Notes:
- There is no country routing to US3 or US5; those are chosen manually. Only suggest the five regions above from IP, and let the user pick US3/US5 explicitly if they want them.
- The suggestion is a *default*, not a decision. Always let the user override — region is permanent once an account exists.
