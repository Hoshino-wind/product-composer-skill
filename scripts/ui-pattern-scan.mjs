#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const strict = args.includes("--strict");
const positional = args.filter((arg) => arg !== "--strict");
const root = path.resolve(positional[0] || process.cwd());

function fail(error) {
  console.error(JSON.stringify({ error }, null, 2));
  process.exit(2);
}

const ignoredDirs = new Set([
  ".git",
  "node_modules",
  "dist",
  "build",
  ".next",
  ".nuxt",
  ".svelte-kit",
  "coverage",
  "out",
  "vendor",
]);

const textExtensions = new Set([
  ".astro",
  ".css",
  ".html",
  ".js",
  ".jsx",
  ".mjs",
  ".cjs",
  ".mdx",
  ".scss",
  ".ts",
  ".tsx",
  ".mts",
  ".cts",
  ".vue",
  ".svelte",
]);

const checks = [
  {
    id: "purple-blue-gradient",
    severity: "warn",
    pattern:
      /(from-(purple|violet|fuchsia|indigo)-\d{2,3}[^\r\n]{0,140}to-(blue|sky|cyan)-\d{2,3})|(linear-gradient\([^)]*(purple|violet|fuchsia|indigo)[^)]*(blue|sky|cyan)[^)]*\))/i,
    message: "Possible generic purple/blue gradient identity.",
  },
  {
    id: "decorative-orb",
    severity: "warn",
    pattern: /\b(orb|blob|bokeh)\b|blur-3xl|blur-\[|radial-gradient/i,
    message: "Possible decorative orb/blob/background effect.",
  },
  {
    id: "oversized-radius",
    severity: "info",
    pattern: /\brounded-(3xl|full|\[[^\]]*(3rem|48px|999px)[^\]]*\])/i,
    message: "Large radius detected; ensure it fits the product surface.",
  },
  {
    id: "generic-saas-copy",
    severity: "info",
    pattern: /\b(unlock|seamless|transform|all-in-one|powerful platform|supercharge|revolutionize)\b/i,
    message: "Possible generic SaaS copy.",
  },
  {
    id: "viewport-scaled-type",
    severity: "warn",
    pattern: /(text-\[[^\]]*(vw|dvw|cqw)[^\]]*\])|(font-size\s*:\s*[^;]*(vw|dvw|cqw))/i,
    message: "Viewport-scaled type detected; avoid it in product UI.",
  },
  {
    id: "pure-black-white",
    severity: "info",
    pattern: /(#000000|#000\b|#fff\b|#ffffff|rgb\(0\s+0\s+0\)|rgb\(255\s+255\s+255\))/i,
    message: "Pure black/white token detected; verify contrast and visual tone.",
  },
  {
    id: "lorem-placeholder",
    severity: "warn",
    pattern: /lorem ipsum|placeholder text|sample copy/i,
    message: "Placeholder copy detected.",
  },
  {
    id: "flowchart-aesthetic",
    severity: "info",
    pattern: /\b(flowchart|node graph|dag|edge|connector|mermaid)\b/i,
    message:
      "Flowchart or node-graph language detected; verify it is not carrying the whole aesthetic.",
  },
];

function compareText(left, right) {
  if (left < right) return -1;
  if (left > right) return 1;
  return 0;
}

function walk(dir, files = []) {
  const entries = fs
    .readdirSync(dir, { withFileTypes: true })
    .sort((left, right) => compareText(left.name, right.name));

  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (!ignoredDirs.has(entry.name)) {
        walk(path.join(dir, entry.name), files);
      }
      continue;
    }

    if (entry.isFile() && textExtensions.has(path.extname(entry.name))) {
      files.push(path.join(dir, entry.name));
    }
  }
  return files;
}

function lineForIndex(text, index) {
  return (text.slice(0, index).match(/\r\n?|\n/g)?.length || 0) + 1;
}

if (!fs.existsSync(root)) {
  fail("Input path does not exist");
}

let inputStats;
try {
  inputStats = fs.statSync(root);
} catch {
  fail("Unable to inspect input path");
}

if (!inputStats.isDirectory()) {
  fail("Input path must be a directory");
}

let files;
try {
  files = walk(root);
} catch {
  fail("Unable to scan input directory");
}

const findings = [];
for (const file of files) {
  const relativeFile = path.relative(root, file).split(path.sep).join("/");
  let text;
  try {
    text = fs.readFileSync(file, "utf8");
  } catch {
    fail(`Unable to read source file: ${relativeFile}`);
  }

  for (const check of checks) {
    const match = check.pattern.exec(text);
    if (match) {
      findings.push({
        id: check.id,
        severity: check.severity,
        file: relativeFile,
        line: lineForIndex(text, match.index),
        message: check.message,
      });
    }
  }
}

findings.sort(
  (left, right) =>
    compareText(left.file, right.file) ||
    left.line - right.line ||
    compareText(left.id, right.id),
);

console.log(
  JSON.stringify(
    {
      schemaVersion: 1,
      root,
      checkedFiles: files.length,
      findingCount: findings.length,
      findings,
    },
    null,
    2,
  ),
);

const hasWarnings = findings.some((finding) => finding.severity === "warn");
process.exitCode = strict && hasWarnings ? 1 : 0;
