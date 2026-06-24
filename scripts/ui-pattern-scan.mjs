#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const root = path.resolve(process.argv[2] || process.cwd());
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
  ".mdx",
  ".scss",
  ".ts",
  ".tsx",
  ".vue",
  ".svelte",
]);

const checks = [
  {
    id: "purple-blue-gradient",
    severity: "warn",
    pattern:
      /(from-(purple|violet|fuchsia|indigo)-\d{2,3}[^\\n]{0,140}to-(blue|sky|cyan)-\d{2,3})|(linear-gradient\([^)]*(purple|violet|fuchsia|indigo)[^)]*(blue|sky|cyan)[^)]*\))/i,
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

function walk(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
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
  return text.slice(0, index).split("\n").length;
}

if (!fs.existsSync(root)) {
  console.error(JSON.stringify({ error: `Path not found: ${root}` }, null, 2));
  process.exit(2);
}

const findings = [];
for (const file of walk(root)) {
  const text = fs.readFileSync(file, "utf8");
  for (const check of checks) {
    const match = check.pattern.exec(text);
    if (match) {
      findings.push({
        id: check.id,
        severity: check.severity,
        file: path.relative(root, file),
        line: lineForIndex(text, match.index),
        message: check.message,
      });
    }
  }
}

console.log(
  JSON.stringify(
    {
      root,
      checkedFiles: walk(root).length,
      findingCount: findings.length,
      findings,
    },
    null,
    2,
  ),
);

process.exit(findings.some((finding) => finding.severity === "warn") ? 1 : 0);
