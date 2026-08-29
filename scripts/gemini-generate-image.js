#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const DEFAULT_MODEL = 'gemini-2.5-flash-image';
const API_BASE = 'https://generativelanguage.googleapis.com/v1beta/models';

function usage() {
  return [
    'Generate an image with the Gemini API.',
    '',
    'Usage:',
    '  node scripts/gemini-generate-image.js "<prompt>" [output-path]',
    '',
    'Requires GEMINI_API_KEY in the environment.',
    'Defaults output to generated-image.png in the current directory.'
  ].join('\n');
}

function parseArgs(argv) {
  if (argv.includes('--help') || argv.includes('-h') || argv.length === 0) {
    return { help: true };
  }

  const [prompt, outputPath] = argv;
  if (!prompt || prompt.startsWith('-')) {
    throw new Error('Expected a prompt as the first argument');
  }

  return { prompt, outputPath: outputPath || 'generated-image.png' };
}

function buildRequestBody(prompt) {
  return {
    contents: [{ parts: [{ text: prompt }] }],
  };
}

function extractImageData(responseBody) {
  const parts = (responseBody && responseBody.candidates &&
    responseBody.candidates[0] && responseBody.candidates[0].content &&
    responseBody.candidates[0].content.parts) || [];
  const imagePart = parts.find(part => part.inlineData && part.inlineData.data);
  if (!imagePart) {
    throw new Error('Gemini response did not contain image data');
  }

  return {
    data: imagePart.inlineData.data,
    mimeType: imagePart.inlineData.mimeType || 'image/png',
  };
}

async function generateImage(prompt, apiKey, model = DEFAULT_MODEL) {
  const url = `${API_BASE}/${model}:generateContent?key=${encodeURIComponent(apiKey)}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(buildRequestBody(prompt)),
  });

  const body = await response.json();
  if (!response.ok) {
    const message = (body && body.error && body.error.message) ||
      `Gemini API request failed (${response.status})`;
    throw new Error(message);
  }

  return extractImageData(body);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    console.log(usage());
    return;
  }

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY is not set. Add it to your environment and try again.');
  }

  const { data, mimeType } = await generateImage(options.prompt, apiKey);
  const outputPath = path.resolve(process.cwd(), options.outputPath);
  fs.writeFileSync(outputPath, Buffer.from(data, 'base64'));
  console.log(`Saved ${mimeType} image to ${outputPath}`);
}

module.exports = { usage, parseArgs, buildRequestBody, extractImageData, generateImage };

if (require.main === module) {
  main().catch(error => {
    console.error(error.message);
    process.exit(1);
  });
}
