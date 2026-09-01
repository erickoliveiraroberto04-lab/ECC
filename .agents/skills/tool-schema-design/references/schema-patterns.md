# Tool schema patterns

Read this reference when choosing parameter shapes, separating tools, or specifying mutations.

## Boundaries

Create separate tools when operations have different:

- permissions or confirmation requirements;
- side effects or retry semantics;
- required parameter sets;
- latency or cost expectations;
- user intents that need distinct selection descriptions.

Keep one tool when a small enum selects behavior with identical safety and data requirements. Avoid exposing raw backend endpoints solely because they already exist.

## Parameter patterns

- Use `type: object` at the parameter root.
- Set `additionalProperties: false` when supported.
- Put every indispensable property in `required`; do not require fields with safe defaults.
- Use ISO 8601 strings with an explicit timezone for instants.
- Include units in names such as `timeout_seconds` or descriptions.
- Use opaque identifiers instead of free-form names for mutations after a lookup step.
- Set `minLength`, `maxLength`, `minimum`, `maximum`, `minItems`, and `maxItems` where the domain has real bounds.
- Use `enum` only for a closed set controlled by the implementation.
- Prefer shallow objects. Use `oneOf` only when the provider supports it reliably and branches are distinguishable.

## Mutation contract

Define these alongside the schema:

| Concern | Required decision |
| --- | --- |
| Authorization | Server-derived actor, tenant, and scope |
| Confirmation | Trigger, preview, expiry, and confirmation token |
| Idempotency | Key source, retention window, and duplicate result |
| Retry | Retryable error codes and backoff |
| Partial success | Per-item status and compensating action |
| Audit | Actor, operation, target, policy result, and timestamp |

Never make `confirmed: true` supplied by the model the sole proof of user confirmation.

## Example function definition

```json
{
  "name": "get_order_status",
  "description": "Get the current status of one order by opaque ID. Use after identifying the order; do not use to edit or cancel it.",
  "parameters": {
    "type": "object",
    "additionalProperties": false,
    "properties": {
      "order_id": {
        "type": "string",
        "description": "Opaque order identifier returned by order lookup.",
        "minLength": 1
      }
    },
    "required": ["order_id"]
  }
}
```

## Error envelope

Return stable codes and a safe message:

```json
{"ok":false,"error":{"code":"AUTHORIZATION_DENIED","message":"The caller cannot access this order.","retryable":false}}
```

Do not return stack traces, credentials, internal policy text, or unrelated records. Include structured field errors for invalid input and an operation identifier for ambiguous timeouts.

## Validator scope

`scripts/validate_tool_schema.py` accepts a direct function definition or a `{"type":"function","function":{...}}` wrapper. It returns `structurally_valid: false` for common JSON-shape errors. Without `--strict`, review warnings do not change a structurally valid exit status. With `--strict`, any warning returns exit `1`; `strict_pass` reports the same disposition in JSON. Invalid JSON or unreadable input returns `2`.

Strict review findings include:

- tool names or string parameters that expose free-form command, shell, script, or code execution;
- caller-controlled privilege/elevation flags and credential- or secret-looking parameters;
- URL, URI, host, endpoint, file, directory, or path strings without an enum, restrictive pattern, or other closed constraint;
- missing or permissive `additionalProperties` on objects;
- missing `maxLength`/required `minLength` on ordinary free-form strings, missing item bounds on arrays, and missing numeric bounds on obviously limit-like fields.

These are conservative heuristics. A finding can require documented runtime controls rather than a schema-only fix, and a clean result cannot detect semantic mismatches, hidden implementation behavior, authorization flaws, sandbox escapes, SSRF/path traversal behind apparently bounded inputs, or provider-specific incompatibility. Treat `structurally_valid` as shape validation and `strict_pass` as a review checklist result—not a safety certification. The target runtime and implementation tests remain authoritative.
