# Python adapter reference

This file is the Python SDK contract for `agent-observability-experiment-bootstrap`. Load it only when the Python SDK is the selected adapter.

## Source of truth

The public `dd-trace-py` repository exposes the experiment API on its `main` branch. The syntax below was checked against:

- https://github.com/DataDog/dd-trace-py/blob/main/ddtrace/llmobs/_llmobs.py
- https://github.com/DataDog/dd-trace-py/blob/main/ddtrace/llmobs/_experiment.py
- https://github.com/DataDog/dd-trace-py/blob/main/ddtrace/llmobs/__init__.py
- https://github.com/DataDog/dd-trace-py/blob/main/tests/llmobs/test_experiments.py

Use public imports only. Never import `ddtrace.llmobs._experiment`, `_llmobs`, or other private modules in generated artifacts.

## Setup

```python
import os
from ddtrace.llmobs import LLMObs

LLMObs.enable(
    api_key=os.getenv("DD_API_KEY"),
    app_key=os.getenv("DD_APPLICATION_KEY") or os.getenv("DD_APP_KEY"),
    site=os.getenv("DD_SITE", "datadoghq.com"),
    project_name="<project>",
    agentless_enabled=True,
)
```

`LLMObs.enable` accepts `project_name`, `site`, `api_key`, `app_key`, `agentless_enabled`, and the tracing/service options shown in `_llmobs.py`. The generated artifact should read credentials from the environment or an approved `.env` loader and must never embed literal keys.

## Dataset API

Use keyword arguments so generated code is resilient to positional-order mistakes.

```python
records = [
    {
        "input_data": {"prompt": "What is 2 + 2?"},
        "expected_output": "4",
        "metadata": {"source": "synthetic"},
        "tags": ["split:eval"],
    },
]

dataset = LLMObs.create_dataset(
    dataset_name="<dataset>",
    project_name="<project>",
    description="<description>",
    records=records,
    bulk_upload=False,
    deduplicate=True,
)

pinned = LLMObs.pull_dataset(
    dataset_name="<dataset>",
    project_name="<project>",
    version=4,
    tags=["split:eval"],
)
```

Current signatures:

```python
LLMObs.pull_dataset(
    dataset_name: str,
    project_name: str | None = None,
    version: int | None = None,
    tags: list[str] | None = None,
) -> Dataset

LLMObs.create_dataset(
    dataset_name: str,
    project_name: str | None = None,
    description: str = "",
    records: list[DatasetRecordNew] | None = None,
    bulk_upload: bool = False,
    deduplicate: bool = True,
) -> Dataset
```

New records use `input_data`, optional `expected_output`, `metadata`, `tags`, and optional user-defined `id`. Records returned from a remote dataset use `record_id`; do not fabricate that field for new records. Tags must be non-empty `key:value` strings.

`Dataset` exposes `append(record)`, `extend(records)`, `push(deduplicate=True, create_new_version=True, bulk_upload=None)`, and tag/update/delete helpers. `push()` mutates the remote dataset and may create a new version. Explain that operation before generating it.

For CSV input, use the actual helper rather than inventing a generic CSV loader:

```python
LLMObs.create_dataset_from_csv(
    csv_path="./data/eval.csv",
    dataset_name="<dataset>",
    input_data_columns=["prompt"],
    expected_output_columns=["answer"],
    metadata_columns=["source"],
    csv_delimiter=",",
    description="<description>",
    project_name="<project>",
    deduplicate=True,
    id_column=None,
)
```

`expected_output_columns`, `metadata_columns`, and `id_column` are optional. Preserve a runtime CSV path rather than embedding CSV contents unless the user explicitly requests conversion.

## Experiment API

The synchronous factory has this public shape:

```python
from ddtrace.llmobs import LLMObs


def task(input_data, config, metadata=None):
    return run_application(input_data, config, metadata)


def exact_match(input_data, output_data, expected_output):
    return output_data == expected_output


def aggregate(inputs, outputs, expected_outputs, evaluators_results):
    return sum(bool(value) for value in evaluators_results["exact_match"]) / len(outputs)

experiment = LLMObs.experiment(
    name="<experiment>",
    task=task,
    dataset=dataset,
    evaluators=[exact_match],
    description="<purpose>",
    project_name="<project>",
    tags={"adapter": "python", "generated_by": "claude-code"},
    config={"purpose": "<purpose>", "model": "<model>"},
    summary_evaluators=[aggregate],
    runs=1,
)

result = experiment.run(
    jobs=10,
    raise_errors=False,
    sample_size=None,
    max_retries=0,
)
print(result)
```

Current factories:

```python
LLMObs.experiment(
    name, task, dataset, evaluators, description="", project_name=None,
    tags=None, config=None, summary_evaluators=None, runs=1,
) -> SyncExperiment

LLMObs.async_experiment(
    name, task, dataset, evaluators, description="", project_name=None,
    tags=None, config=None, summary_evaluators=None, runs=1,
) -> Experiment
```

Function evaluators receive `(input_data, output_data, expected_output)`. Summary evaluators receive `(inputs, outputs, expected_outputs, evaluators_results)`. Class evaluators must use the public `BaseEvaluator`, `BaseAsyncEvaluator`, `BaseSummaryEvaluator`, or `BaseAsyncSummaryEvaluator` contracts from `ddtrace.llmobs`.

The sync wrapper exposes `run(jobs=1, raise_errors=False, sample_size=None, max_retries=0, retry_delay=None)`. Async `Experiment.run` defaults to `jobs=10`; both accept a callable `retry_delay(attempt)`. Do not map Node's sequential run to Python's `jobs` behavior without stating the difference.

Task and evaluator errors remain distinct from false values. `raise_errors=False` preserves row-level errors in the result; use `raise_errors=True` only when the caller requests fail-fast behavior.

## Evaluator results and remote evaluators

For diagnostic context, use the public `EvaluatorResult`:

```python
from ddtrace.llmobs import EvaluatorResult

def quality(input_data, output_data, expected_output):
    score = 1.0 if output_data == expected_output else 0.0
    return EvaluatorResult(
        value=score,
        reasoning="Exact comparison",
        assessment="pass" if score else "fail",
        metadata={"criterion": "exact_match"},
        tags={"category": "accuracy"},
    )
```

`RemoteEvaluator`, `EvaluatorContext`, `LLMJudge`, and provider-specific classes are public exports, but load their dedicated reference only when selected. Do not claim a remote evaluator exists by name without checking the organization/backend.

## Python compatibility rules

Preserve the legacy behavior of this skill:

- default adapter is Python;
- default format is `.py`, with optional `.ipynb`;
- `--jobs` maps only to `experiment.run(jobs=N)`;
- local JSON is validated and PII-scrubbed before embedding;
- `--dataset` and `--dataset-name` are mutually exclusive;
- no dataset produces a small runnable inline sample;
- task discovery is bounded to `--app-root`, excludes tests/build/vendor trees, and never silently replaces a discovered callable with a placeholder; and
- the generated artifact retains the purpose, provider, evaluator style, dataset identity, and next-step sections used by the legacy Python workflow.

## Python public symbol map

Generated code must use public exports from `ddtrace.llmobs`:

| Import | Public capability |
|---|---|
| `LLMObs` | `enable`, dataset creation/CSV import/pull, synchronous and asynchronous experiments. |
| `EvaluatorResult` | Value plus reasoning, assessment, metadata, and tags for diagnostic metrics. |
| `EvaluatorContext` and `SummaryEvaluatorContext` | Context objects for class-based row and summary evaluators. |
| `BaseEvaluator` and `BaseAsyncEvaluator` | Stateful row evaluator contracts. |
| `BaseSummaryEvaluator` and `BaseAsyncSummaryEvaluator` | Stateful summary evaluator contracts. |
| `RemoteEvaluator` and `EvaluatorContext` | Server-side evaluator integration when configured in the organization. |
| `LLMJudge` | Inline LLM-as-judge support when the selected evaluator reference confirms its installed signature. |

Never import `_experiment`, `_llmobs`, `_evaluators`, or any other underscore-prefixed implementation module in generated code. The implementation links above are evidence for the contract, not import paths.

## Legacy Python invocation contract

The legacy command name and Python defaults remain supported:

```text
/agent-observability-experiment-bootstrap
  [--purpose TEXT] [--format py|ipynb]
  [--dataset PATH | --dataset-name NAME] [--dataset-version N]
  [--project-name NAME] [--evaluator-style function|class|remote]
  [--jobs N] [--output PATH] [--task-source module:function]
  [--placeholder-task] [--app-root PATH] [--env-file PATH]
```

Python-specific defaults and meanings:

| Option | Default | Python behavior |
|---|---|---|
| `--format` | `py` | Emit one runnable `.py` file or an `.ipynb` notebook. |
| `--dataset` | none | Read a local JSON or CSV dataset. With neither dataset flag, emit a runnable three-record inline sample. |
| `--dataset-name` | none | Pull an existing Datadog dataset by name at runtime. Mutually exclusive with `--dataset`. |
| `--dataset-version` | latest | Pin the version used by `LLMObs.pull_dataset`; ignored without `--dataset-name`. |
| `--project-name` | `experiment-<service-name>` | Resolve from Python project metadata or the application root; use `experiment-sdk-default` only as a last resort. |
| `--evaluator-style` | `function` | Select plain functions, public evaluator classes, or remote evaluators. Load only the selected evaluator reference. |
| `--jobs` | `10` | Pass only to the Python `experiment.run(jobs=N)` call. |
| `--output` | `./experiments/experiment.<ext>` | Derive `.py` or `.ipynb` from `--format` when omitted. |
| `--task-source` | auto-discovered | Explicit `<dotted.module.path>:<function>` override for task discovery. |
| `--placeholder-task` | off | Opt out of discovery and emit the clearly marked generic task. This is the only normal path where `TODO(user)` is allowed in the task section. |
| `--app-root` | project metadata directory or cwd | Hard boundary for Python source discovery. |
| `--env-file` | none | Bake one or more explicit absolute `.env` paths into the generated loader; shell variables still win. |

Do not prompt for optional defaults. Always resolve a non-empty purpose from `--purpose`, the request, or a focused question before selecting the task and evaluators.

## Python project and purpose resolution

If `--project-name` is omitted, resolve a stable name in this order:

1. `pyproject.toml` `[project].name` or `[tool.poetry].name`.
2. `setup.cfg` `[metadata].name`.
3. The first `name="..."` argument in `setup.py`.
4. `package.json` `name` when the Python app lives in a mixed-language repository.
5. The current directory basename, lowercased and slugified.

Prefix the resolved service name with `experiment-`, but do not duplicate an existing `experiment-` prefix. If nothing resolves, use `experiment-sdk-default` and warn that `--project-name` should be supplied. Embed the resolved value in the artifact; do not emit a runtime cwd lookup because the artifact may run from another directory.

Purpose resolution order:

1. Use `--purpose` verbatim.
2. Extract a clear purpose from the invocation and confirm it.
3. Ask one focused question with seed choices such as output accuracy, tool-call correctness, structured output, retrieval faithfulness, or regression testing.

The purpose is reasoning context, not a fixed taxonomy. Carry it into the file header, task-wrapper decisions, evaluator semantics, experiment `description`, `config`, `tags`, and completion report. For tool/agent purposes, prefer candidates exposing tool calls or agent spans; for retrieval purposes, prefer candidates exposing retrieved context; for schema purposes, prefer structured-output call sites; for regression purposes, prefer deterministic evaluators.

## Python dataset ingestion

For `--dataset`:

- Require a top-level JSON array and validate each record as `input_data`, optional `expected_output`, optional `metadata`, optional `tags`, and optional user-defined `id`.
- Scrub obvious PII and credential-like strings before embedding JSON records. Cover email, phone, SSN, and API-key patterns, replace matches with typed redaction markers, and report affected record indices.
- For JSON, embed sanitized records inline so the artifact is self-contained.
- For CSV, preserve the runtime path and emit `LLMObs.create_dataset_from_csv`; do not embed CSV contents unless explicitly requested. Auto-detect input columns from `prompt|input|query|question` and expected columns from `expected|gold|truth|answer` when the user has not specified them.
- Preserve metadata and tags. Every tag must be a non-empty `key:value` string; namespace bare source labels instead of passing malformed tags to the SDK.

For `--dataset-name`:

- Emit `LLMObs.pull_dataset(dataset_name=..., project_name=..., version=...)` and let the SDK fetch it when the artifact runs.
- Do not call Datadog during code generation, scrub remote records locally, or invent a `--dataset-id` workaround. If the user has only a UI ID, ask them to resolve the dataset name in the UI.
- State whether the artifact uses the latest version or a pinned version.

The SDK owns remote record IDs, canonical IDs, dataset versioning, push diffing, and bulk thresholds. Never generate UUIDs or fabricate `record_id`/`canonical_id` fields. Explain that `Dataset.push()` mutates the remote dataset before generating code that calls it.

## Python task discovery and wrapper generation

Unless `--task-source` or `--placeholder-task` is supplied, discover the real LLM entry point. Resolve the app root from `--app-root`, otherwise from the project metadata file used for project resolution, otherwise cwd. Refuse `/` or `~` as an unresolved root. Bound the scan to that tree and respect `.gitignore`; exclude `node_modules`, `.venv`, `venv`, `__pycache__`, `.git`, `dist`, `build`, `target`, `vendor`, `third_party`, tests, fixtures, and notebooks. If the scan would inspect an unusually large tree, narrow the root rather than scanning indiscriminately.

Search Python files for these call sites and walk upward to their enclosing `def` or `async def`:

| Signal | Examples |
|---|---|
| OpenAI | `openai.chat.completions.create`, `client.chat.completions.create`, `openai.completions.create` |
| Anthropic | `client.messages.create`, `Anthropic(...).messages.create` |
| LiteLLM | `litellm.completion`, `litellm.acompletion` |
| LangChain | `.invoke`, `ChatOpenAI`, `ChatAnthropic`, `LLMChain` |
| LlamaIndex | `from llama_index`, `as_query_engine`, `as_chat_engine` |
| Gemini/Vertex | `GenerativeModel(...).generate_content` |
| Bedrock | `boto3.client("bedrock-runtime").invoke_model` |
| Instrumented code | `@LLMObs.llm`, `@LLMObs.agent`, `@LLMObs.workflow`, `@LLMObs.task`, `@workflow`, `@agent` |

Record each candidate's file, line, function name, async status, signature, enclosing class, and provider. Rank candidates with these signals:

- canonical names such as `generate`, `chat`, `complete`, `respond`, `answer`, `handle_request`, `process_query`, `run`, `predict`, `infer`, `query`, `agent_loop`, or `main`: +5;
- one or two typed `str`/`dict` parameters: +3;
- an LLM, workflow, or agent decorator: +5;
- top-level module function: +2;
- application-like module (`main`, `app`, `api`, `handlers`, `server`, `routes`, `agent`, `bot`, `chat`): +3;
- agent/service class method: +2;
- private helper with other candidates present: −3;
- examples/scripts/notebooks: −2;
- multiple LLM call sites in the same function: +1;
- a purpose-aligned shape: a soft +3–5 bias.

Show the top three candidates and use the first unless the user chooses another. If no candidate exists, emit a one-line note and use placeholder semantics; never invent an import and never silently replace a discovered callable with a placeholder.

Adapt the selected callable to the SDK task contract `task_fn(input_data: dict, config: dict, metadata: dict | None) -> Any`:

- One scalar parameter: pass the sole matching input value.
- Multiple parameters: map by parameter name, then use input-value order only with an explicit assumption comment.
- A dict parameter or `**kwargs`: pass the input mapping through.
- A `config`, `model`, or `temperature` parameter: pass the corresponding value from `config` rather than dropping it.
- An async callable: either use `LLMObs.async_experiment` consistently or wrap it with `asyncio.run` for a synchronous experiment. Do not mix sync and async execution accidentally.
- A class method: import the class and instantiate it lazily; add a constructor-arguments note when required arguments cannot be inferred.

Add a source comment naming the module, function, source location, purpose, and adaptation. If the purpose needs tool calls, retrieved documents, or intermediate state, preserve those fields only when the selected function actually returns them. If it returns only text, emit a note explaining what richer return shape would be useful; never invent one or modify application source.

Scan the selected function and immediate same-module calls for side effects. Warn when it reads non-credential environment variables, calls external non-provider HTTP endpoints, accesses databases, writes files, or invokes tools. Do not remove or rewrite those side effects.

## Python environment setup and provider loading

Required Datadog credentials are `DD_API_KEY` and either `DD_APPLICATION_KEY` or `DD_APP_KEY`; `DD_SITE` defaults to `datadoghq.com`. Provider credentials are conditional on the discovered task and must not be asserted speculatively.

Emit the shipped `references/python/env_setup_template.py` rather than reimplementing the loader. It must:

1. Load explicit `--env-file` overrides first.
2. Search the generated file directory, cwd, parent directories, and `~/.datadog/credentials`.
3. Preserve shell variables over values loaded from files.
4. Avoid a `python-dotenv` dependency.
5. Redact values from diagnostics and assert only keys actually required by the wired task.

Load only the matching provider reference:

| Detected task SDK | Reference |
|---|---|
| OpenAI or Azure OpenAI | `references/python/providers/openai.md` |
| Anthropic | `references/python/providers/anthropic.md` |
| LiteLLM | `references/python/providers/litellm.md` |
| LangChain | `references/python/providers/langchain.md`, then its underlying provider guidance |
| LlamaIndex | `references/python/providers/llamaindex.md` |
| Gemini or Vertex | `references/python/providers/gemini.md` |
| AWS Bedrock | `references/python/providers/bedrock.md` |
| Custom/unknown | No fabricated assert; emit a clear user TODO for required keys. |

Always pass `site=os.getenv("DD_SITE", "datadoghq.com")` to `LLMObs.enable`. Never embed keys, use a literal secret, overwrite an exported shell value, or assert provider keys unrelated to the task.

## Python evaluator selection

Load exactly one evaluator-style reference under `references/python/evaluator-styles/`. The style controls the API surface; the purpose controls evaluator semantics:

- `function`: plain functions for most experiments; trivial checks may return bool/float, richer checks should return `EvaluatorResult`.
- `class`: public `BaseEvaluator`/`BaseAsyncEvaluator` implementations with `evaluate` returning `EvaluatorResult`.
- `remote`: public `RemoteEvaluator` instances only when the evaluator name exists or the user will configure it in Datadog; do not invent organization-specific names.

Default accuracy experiments should use two or three metrics such as exact match, a richer rule-based check, and an optional judge. Tool purposes should inspect structured tool calls when present. Retrieval purposes require retrieved context. Structured-output purposes should parse and validate the required schema. Regression purposes should favor deterministic exact/near-match thresholds over an LLM judge.

Any non-trivial evaluator should populate `value`, `reasoning`, and `assessment` in `EvaluatorResult`, with optional `metadata` and `tags`. Keep row-level evaluators separate from summary evaluators. Evaluator errors must remain errors; never convert an exception into a false or passing value. Add a `TODO(user)` customization note to evaluator logic where appropriate, but do not put that marker in a successfully discovered task wrapper.

Every `LLMObs.experiment` call must carry the resolved purpose and provenance in `description`, `config`, and `tags`, including `generated_by=claude-code`, the skill name, adapter, dataset identity/version, and task source where available.

## Python artifact structure and validation

Keep the historical Python section ordering in both formats:

```text
0. Header docstring: name, generation time, purpose, provider, task source.
1. Environment setup: inline loader, credential assertions, shell precedence.
2. LLMObs.enable(): explicit credentials, site, project, agentless mode.
3. Dataset: inline records, CSV loader, or remote pull.
4. Task function: real imported callable and signature adapter, or marked placeholder.
5. Evaluators: selected style, purpose-driven semantics, labels and rubrics.
6. Experiment: dataset/task/evaluators, description, config, tags, provenance.
7. Run: jobs/retries/error policy; print the experiment URL.
8. Results: inspect rows and summary metrics, preserving task/evaluator errors.
```

For `.py`, use `from __future__ import annotations`, clear section banners, typed task/evaluator signatures, and one blank line between sections. For `.ipynb`, emit valid notebook JSON with one markdown and one code cell per section, `nbformat` 4, a Python 3 kernel, null execution counts, and empty outputs.

Run `python -m py_compile` for `.py`. For `.ipynb`, parse JSON and require non-empty markdown/code cells. Report missing toolchains without pretending validation passed.

The generated Python artifact must not:

- import `ddtrace.llmobs._experiment`, `_llmobs`, or any private module;
- generate UUIDs or client-owned `record_id`/`canonical_id` values;
- manually implement SDK dataset push, JSON:API, status, or HTTP calls;
- embed literal credentials or unsanitized PII;
- silently collapse task/evaluator errors into false metrics; or
- emit a placeholder when a real callable was discovered.

## Python completion report

After generation, report:

```text
Generated SDK experiment: Python/<py|ipynb>
Path: <path>
Purpose: "<resolved purpose>"
Project: <project>
Dataset: <source>, version=<version or latest>
Task function source: <module:function | placeholder>
Evaluators: <labels and style>
SDK calls: LLMObs.enable, dataset operation, LLMObs.experiment, experiment.run
Validation: <py_compile or notebook JSON result>
Result link: <URL after run, or pending>

Next steps:
1. Confirm the discovered task source and adaptation.
2. Set Datadog and provider credentials via shell or a discoverable .env.
3. Review evaluator semantics and TODO notes.
4. Run `python <path>` or open the notebook.
5. Inspect row-level errors before trusting aggregate metrics.
```

## Python telemetry beacon (legacy invocation)

For the legacy Python invocation, preserve the startup-beacon behavior when a Datadog backend is available:

1. Generate one eight-character hexadecimal invocation ID before the first backend call.
2. If the user explicitly requests `--backend pup`, run the pup beacon.
3. Otherwise use the Datadog MCP beacon when the corresponding LLM Observability MCP tool is available.
4. If neither backend is available, skip silently or print one informational line.
5. Beacon failure is non-fatal and must never block local code generation.
6. Prefix MCP telemetry intent with `skill:agent-observability-experiment-bootstrap[<invocation_id>]`; use the `:start` suffix for the startup call.

Do not expose or persist the beacon response payload.

## Python notebook patterns

Use the public reference notebooks as style templates:

| Notebook | Pattern |
|---|---|
| `00-basic-datasets.ipynb` | Dataset create, append, and push lifecycle. |
| `01-basic-experiments.ipynb` | Minimal inline-record experiment with simple evaluators. |
| `02-extra-data.ipynb` | CSV dataset, multi-value task output, and confidence metrics. |
| `04-multi-span-experiments.ipynb` | Multi-step LLM pipeline inside one task. |
| `07-remote-evaluators.ipynb` | Remote evaluator and transform function usage. |

Reference: https://github.com/DataDog/llm-observability/tree/main/experiments/notebooks. Keep one markdown cell and one code cell per generated section, with `nbformat` 4 metadata and no fabricated execution outputs.

## Python documentation and operating rules

Use these public references when the selected SDK contract or feature is not covered here:

| Topic | URL |
|---|---|
| Agent Observability overview | https://docs.datadoghq.com/llm_observability/ |
| Setup and site selection | https://docs.datadoghq.com/llm_observability/setup/ |
| Instrumentation | https://docs.datadoghq.com/llm_observability/instrumentation/ |
| Python SDK reference | https://docs.datadoghq.com/llm_observability/instrumentation/sdk/ |
| Experiments | https://docs.datadoghq.com/llm_observability/experiments/ |
| Evaluations | https://docs.datadoghq.com/llm_observability/evaluations/ |
| Custom LLM-as-a-judge | https://docs.datadoghq.com/llm_observability/evaluations/custom_llm_as_a_judge_evaluations/ |
| Managed evaluations | https://docs.datadoghq.com/llm_observability/evaluations/managed_evaluations/ |
| Monitoring | https://docs.datadoghq.com/llm_observability/monitoring/ |
| Terms and glossary | https://docs.datadoghq.com/llm_observability/terms/ |
| Evaluation developer guide | https://docs.datadoghq.com/llm_observability/guide/evaluation_developer_guide/ |
| Claude Code skills guide | https://docs.datadoghq.com/llm_observability/guide/claude_code_skills/ |
| LLM Observability MCP server | https://docs.datadoghq.com/llm_observability/mcp_server/ |
| Reference notebooks | https://github.com/DataDog/llm-observability/tree/main/experiments/notebooks |

When the feature is not covered here, fetch the most specific documentation page rather than guessing symbols or behavior, and cite it when answering the user. Keep the Python adapter SDK-only: no manual HTTP transport, no manual JSON:API envelopes, no generated IDs, no dependency on `python-dotenv`, and no generated requirements or project metadata file. Print the install command instead. Do not modify `dd-trace-py` or application source while updating this skill.
