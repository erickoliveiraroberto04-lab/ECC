# Node.js adapter reference

This file is the Node SDK contract for `agent-observability-experiment-bootstrap`. Load it only when using `tracer.llmobs.experiments`.

## Source of truth

The public `dd-trace-js` repository exposes the experiment API on its `master` branch. The syntax below was checked against:

- https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/src/llmobs/experiments/index.js
- https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/src/llmobs/experiments/dataset.js
- https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/src/llmobs/experiments/experiment.js
- https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/src/llmobs/experiments/client.js
- https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/test/llmobs/experiments/example.js

Use the public `tracer.llmobs.experiments` entry point. Do not import `src/llmobs/experiments/*` internals in generated artifacts.

## Setup and project resolution

```js
'use strict'

const tracer = require('dd-trace')

tracer.init({
  llmobs: { mlApp: process.env.DD_LLMOBS_ML_APP || '<project>' },
})

const { experiments } = tracer.llmobs
```

The SDK client requires `DD_API_KEY`, `DD_APP_KEY`, and a configured site. It resolves the project from `llmobs.mlApp`, then the tracer service fallback. The installed source also requires LLM Observability to be enabled; preserve the user’s tracer configuration and report when `tracer.llmobs.experiments` is a no-op because credentials, project, or enablement are missing. `DD_SITE` defaults according to the tracer configuration.

Prefer CommonJS for the legacy `.js` path and ESM only when the user requests `.mjs` and the repository package configuration supports it.

## Dataset API

```js
const dataset = experiments.createDataset('qa-v3', {
  description: 'Pinned QA cases',
  records: [
    {
      inputData: { prompt: 'What is 2 + 2?' },
      expectedOutput: '4',
      metadata: { source: 'synthetic' },
      tags: ['split:eval'],
    },
  ],
})

// The fluent form is also public.
dataset
  .addRecord({ prompt: 'Capital of France?' }, 'Paris', { source: 'synthetic' }, ['split:eval'])
await dataset.push()

const pinned = await experiments.pullDataset('qa-v3', {
  version: 4,
  tags: ['split:eval'],
  expectedRecordCount: 1,
  maxWaitMs: 30_000,
})
```

`createDataset(name, descriptionOrOptions)` accepts a description string or `{description, records}`. Record object properties are camelCase: `inputData`, `expectedOutput`, `metadata`, `tags`, and optional non-empty `id`. The fluent `addRecord(input, expectedOutput?, metadata?, tags?)` method is chainable.

`pullDataset(name, options)` takes a dataset **name**, not a dataset ID. It supports `version`, `tags`, `expectedRecordCount`, and `maxWaitMs`, paginates records, and retries eventually consistent reads. Use the returned Dataset’s `records()`, `recordIds()`, `id()`, `version()`, `url()`, and tag/update helpers as exposed by the public class.

Tags are validated as non-empty `key:value` strings. Do not use bare labels. Do not invent canonical or backend record IDs; the SDK generates IDs when omitted.

## Local experiment API

```js
const result = await experiments.experiment({
  name: 'qa-v3-node',
  dataset,
  task: async (input, config, metadata) => {
    const output = await runApplication(input, config, metadata)
    return output
  },
  evaluators: {
    exact_match: (input, output, expected) => output === expected,
    confidence_score: (input, output) => Number(output.confidence),
    category: (input, output) => output.category,
  },
  summaryEvaluators: {
    pass_rate: (inputs, outputs, expectedOutputs, evaluatorResults, metadata) =>
      evaluatorResults.exact_match.filter(Boolean).length / outputs.length,
  },
  description: 'Node experiment',
  config: { model: '<model>', adapter: 'node' },
  tags: { generated_by: 'claude-code', variant: 'candidate' },
}).run({
  maxRetries: 0,
  retryDelay: (attempt) => 100 * (attempt + 1),
  throwOnErrors: false,
})

console.log(result.url, result.experimentId, result.rows)
```

`experiments.experiment(options)` requires `name`, `dataset`, and `task` for local execution. The task receives `(record.input, config, record.metadata)`. Evaluators receive `(record.input, output, record.expectedOutput)` and may be an object keyed by stable evaluator label or an array supported by the installed SDK. Summary evaluators are separate from row evaluators.

The local `run(options)` accepts only:

```text
maxRetries
retryDelay(attempt)
throwOnErrors
```

Rows run sequentially in the current source. Do not pass Python’s `jobs` option or claim Node concurrency support. A task error causes evaluation to be skipped for that row; preserve the error in the result instead of converting it to a false metric.

The result exposes an experiment URL, experiment ID, rows, and summary evaluations. Print those values and retain per-row errors.

## Externally driven experiments

When another framework owns task execution, use the public `startExperiment` path:

```js
const experiment = await experiments.startExperiment({
  name: 'external-qa-v3',
  projectName: '<project>',
  dataset: { id: '<dataset-uuid>', version: 4 },
  config: { adapter: 'node', framework: '<framework>' },
  tags: { generated_by: 'claude-code' },
})

const span = await experiment.submitSpan({
  input: { prompt: '...' },
  output: { answer: '...' },
  expectedOutput: { answer: '...' },
  metadata: { source: 'local' },
  datasetRecordId: '<record-id>',
  name: 'task',
})

await experiment.submitEvaluationMetrics(span, [
  { label: 'exact_match', value: true, source: 'custom' },
])
await experiment.close({ status: 'completed' })
```

`startExperiment` returns an external handle after creating the experiment. Submit one span per completed row, submit metrics correlated to the returned span/trace IDs, and always close the experiment. Use `close({status: 'failed', error})` for unrecoverable failures.

Do not use the local `.run()` method for an externally driven experiment. Do not serialize evaluator functions into HTTP requests.

## Node compatibility rules

- `--jobs` is Python-only; warn and omit it for Node.
- Use `inputData`/`expectedOutput` in SDK dataset records; do not copy Python’s `input_data` spelling into Node objects.
- Keep evaluator labels stable and valid.
- Keep provenance in `config` and `tags`.
- Use `--task-source` for a real module/function whenever possible; otherwise emit a prominent placeholder.
