# Orchestration patterns

Read this reference when deciding whether to delegate, selecting a topology, or defining handoffs.

## Topology selection

| Pattern | Use for | Avoid when |
| --- | --- | --- |
| Coordinator and specialists | Distinct domains with one integration owner | The coordinator cannot verify specialist outputs |
| Map-reduce | Independent items with the same output schema | Items share mutable state or depend on prior results |
| Planner and executor | Fragile sequences that benefit from an explicit plan | The plan becomes stale after every action |
| Worker and reviewer | High-risk artifacts with objective review criteria | Reviewer independence is not possible |
| Bounded debate | A consequential choice with credible competing hypotheses | More evidence, not more opinion, is needed |
| Pipeline | Stable stage-to-stage transformation | Failures require frequent backward edits |

Start with the fewest agents that expose real parallelism. One integrator must own the final result.

## Task contract

Define each task with:

- `id`: stable machine-readable identifier.
- `owner`: one accountable agent or role.
- `description`: bounded action and non-goals.
- `depends_on`: task identifiers whose outputs are required.
- `output_contract`: artifact, format, evidence, and acceptance conditions.
- `writes`: exact files, records, branches, or systems the task may mutate.
- `tags`: lowercase risk tags. Use `consequential`, `deploy`, or `external-mutation` when applicable.
- `approval_ref`: approval-point ID; required for any of those three risk tags.
- `timeout_seconds`: positive number no greater than 86,400.
- `max_attempts`: integer from 1 through 10.
- `retry_backoff_seconds`: optional number from 0 through 3,600.
- `retry_contract`: required by strict validation when `max_attempts` is greater than 1; name idempotency or status-check behavior and retryable errors.

Each approval point has `id`, `before_task`, and `reason`. A tagged task's `approval_ref` must resolve to an approval point whose `before_task` is that same task.

`scripts/validate_plan.py` returns `structurally_valid: false` for malformed fields, unresolved dependencies or approvals, cycles, invalid bounds, or missing approval references on tagged work. It reports exact same-target parallel write conflicts as warnings. Without `--strict`, warnings do not change exit status; with `--strict`, any warning returns exit `1`. `strict_pass` shows whether the same document would pass strict mode. Exit `2` is reserved for unreadable or invalid JSON input. These checks cover declared structure, not runtime behavior or effective authorization.

Example task and approval:

```json
{
  "id": "deploy-preview",
  "owner": "release-agent",
  "description": "Deploy the approved preview build.",
  "depends_on": ["test-build"],
  "output_contract": "Preview URL and deployment log.",
  "writes": ["preview-environment"],
  "tags": ["deploy", "external-mutation"],
  "approval_ref": "approve-preview",
  "timeout_seconds": 900,
  "max_attempts": 1
}
```

```json
{"id":"approve-preview","before_task":"deploy-preview","reason":"A human must approve the external deployment."}
```

## Handoff contract

Require downstream-readable fields:

1. Status: completed, partial, failed, or blocked.
2. Result: concise answer or artifact locations.
3. Evidence: tests, sources, logs, or diffs.
4. State changes: exact resources created or modified.
5. Assumptions and uncertainty.
6. Risks, approvals needed, and recommended next step.

Do not accept “done” as a handoff. Do not expose hidden chain-of-thought; request conclusions and evidence.

## Shared-state rules

- Prefer immutable artifacts and append-only event records.
- Assign one writer per mutable target.
- Use explicit versions and compare-and-swap for shared records.
- Keep task status separate from task content.
- Cancel dependents when their required input is invalidated.
- Make retries idempotent or attach a unique operation key.

## Stop conditions

Stop or collapse the orchestration when the objective is met, a required approval is denied, the critical dependency is unavailable, budget is exhausted, repeated results add no evidence, or coordination time exceeds the remaining sequential work.
