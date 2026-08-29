/**
 * Tests for scripts/gemini-generate-image.js
 */

const assert = require('assert');
const path = require('path');
const { execFileSync } = require('child_process');

const SCRIPT = path.join(__dirname, '..', '..', 'scripts', 'gemini-generate-image.js');
const {
  parseArgs,
  buildRequestBody,
  extractImageData,
} = require(SCRIPT);

function run(args = [], envOverrides = {}) {
  const env = { ...process.env, ...envOverrides };
  delete env.GEMINI_API_KEY;
  Object.assign(env, envOverrides);

  try {
    const stdout = execFileSync('node', [SCRIPT, ...args], {
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe'],
      env,
      timeout: 10000,
    });
    return { code: 0, stdout, stderr: '' };
  } catch (error) {
    return {
      code: error.status || 1,
      stdout: error.stdout || '',
      stderr: error.stderr || '',
    };
  }
}

function test(name, fn) {
  try {
    fn();
    console.log(`  ✓ ${name}`);
    return true;
  } catch (error) {
    console.log(`  ✗ ${name}`);
    console.log(`    Error: ${error.message}`);
    return false;
  }
}

function runTests() {
  console.log('\n=== Testing gemini-generate-image.js ===\n');

  let passed = 0;
  let failed = 0;

  if (test('--help prints usage and exits 0', () => {
    const result = run(['--help']);
    assert.strictEqual(result.code, 0, result.stderr);
    assert.ok(result.stdout.includes('Generate an image with the Gemini API'));
  })) passed++; else failed++;

  if (test('no arguments prints usage and exits 0', () => {
    const result = run([]);
    assert.strictEqual(result.code, 0, result.stderr);
    assert.ok(result.stdout.includes('Usage:'));
  })) passed++; else failed++;

  if (test('missing GEMINI_API_KEY exits 1 with a clear message', () => {
    const result = run(['a red fox in snow']);
    assert.strictEqual(result.code, 1);
    assert.ok(result.stderr.includes('GEMINI_API_KEY'), result.stderr);
  })) passed++; else failed++;

  if (test('parseArgs returns prompt and default output path', () => {
    const options = parseArgs(['a cat wearing a hat']);
    assert.strictEqual(options.prompt, 'a cat wearing a hat');
    assert.strictEqual(options.outputPath, 'generated-image.png');
  })) passed++; else failed++;

  if (test('parseArgs honors a custom output path', () => {
    const options = parseArgs(['a cat wearing a hat', 'out/cat.png']);
    assert.strictEqual(options.outputPath, 'out/cat.png');
  })) passed++; else failed++;

  if (test('buildRequestBody wraps the prompt as Gemini contents', () => {
    const body = buildRequestBody('a cat wearing a hat');
    assert.deepStrictEqual(body, {
      contents: [{ parts: [{ text: 'a cat wearing a hat' }] }],
    });
  })) passed++; else failed++;

  if (test('extractImageData reads inlineData from the response', () => {
    const response = {
      candidates: [
        {
          content: {
            parts: [{ inlineData: { data: 'YWJj', mimeType: 'image/png' } }],
          },
        },
      ],
    };
    const result = extractImageData(response);
    assert.deepStrictEqual(result, { data: 'YWJj', mimeType: 'image/png' });
  })) passed++; else failed++;

  if (test('extractImageData throws when no image part is present', () => {
    assert.throws(
      () => extractImageData({ candidates: [{ content: { parts: [{ text: 'no image' }] } }] }),
      /did not contain image data/
    );
  })) passed++; else failed++;

  console.log(`\nResults: Passed: ${passed}, Failed: ${failed}`);
  process.exit(failed > 0 ? 1 : 0);
}

runTests();
