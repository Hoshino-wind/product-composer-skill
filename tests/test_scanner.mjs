import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const root = path.resolve(import.meta.dirname, "..");
const scanner = path.join(root, "scripts", "ui-pattern-scan.mjs");
const permissionChecksUnavailable =
  process.platform === "win32" ||
  (typeof process.getuid === "function" && process.getuid() === 0);

function withFixture(files, run) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "product-composer-scan-"));
  try {
    for (const [name, content] of Object.entries(files)) {
      const target = path.join(dir, name);
      fs.mkdirSync(path.dirname(target), { recursive: true });
      fs.writeFileSync(target, content, "utf8");
    }
    return run(dir);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
}

function scan(args, options = {}) {
  return spawnSync(process.execPath, [scanner, ...args], {
    encoding: "utf8",
    ...options,
  });
}

function parseOutput(result) {
  assert.equal(result.signal, null);
  assert.equal(result.error, undefined);
  return JSON.parse(result.stdout);
}

test("matches same-line Tailwind purple-blue gradient", () => {
  withFixture(
    { "app.tsx": 'const c = "from-purple-500 bg-gradient-to-r to-blue-500";' },
    (dir) => {
      const result = scan([dir]);
      assert.equal(result.status, 0);
      const output = parseOutput(result);
      assert.equal(output.schemaVersion, 1);
      assert.equal(output.findings[0].id, "purple-blue-gradient");
      assert.equal(output.findings[0].line, 1);
    },
  );
});

test("does not join gradients across line endings", () => {
  for (const lineEnding of ["\n", "\r\n", "\r"]) {
    withFixture(
      {
        "app.tsx": `from-purple-500${lineEnding}gap${lineEnding}to-blue-500`,
      },
      (dir) => {
        const output = parseOutput(scan([dir]));
        assert.equal(
          output.findings.some((item) => item.id === "purple-blue-gradient"),
          false,
        );
      },
    );
  }
});

test("reports the source line for each line-ending style", () => {
  for (const lineEnding of ["\n", "\r\n", "\r"]) {
    withFixture(
      { "app.tsx": `const ok = true;${lineEnding}lorem ipsum` },
      (dir) => {
        const output = parseOutput(scan([dir]));
        const finding = output.findings.find(
          (item) => item.id === "lorem-placeholder",
        );
        assert.equal(finding.line, 2);
      },
    );
  }
});

test("supports modern JavaScript and TypeScript module extensions", () => {
  withFixture(
    {
      "a.mjs": "const ok = true;",
      "b.cjs": "const ok = true;",
      "c.mts": "const ok = true;",
      "d.cts": "const ok = true;",
    },
    (dir) => {
      const output = parseOutput(scan([dir]));
      assert.equal(output.checkedFiles, 4);
    },
  );
});

test("walks nested source directories and ignores dependency and VCS directories", () => {
  withFixture(
    {
      "nested/app.tsx": "lorem ipsum",
      "node_modules/package/index.tsx": "lorem ipsum",
      ".git/hooks/example.tsx": "lorem ipsum",
      "notes.txt": "lorem ipsum",
    },
    (dir) => {
      const output = parseOutput(scan([dir]));
      assert.equal(output.checkedFiles, 1);
      assert.deepEqual(
        output.findings.map((item) => item.file),
        ["nested/app.tsx"],
      );
    },
  );
});

test("sorts files and findings by stable relative paths", () => {
  withFixture(
    {
      "z.tsx": "lorem ipsum",
      "nested/b.tsx": "lorem ipsum",
      "a.tsx": "lorem ipsum",
    },
    (dir) => {
      const first = parseOutput(scan([dir]));
      const second = parseOutput(scan([dir]));
      assert.deepEqual(first, second);
      assert.deepEqual(
        first.findings.map((item) => item.file),
        ["a.tsx", "nested/b.tsx", "z.tsx"],
      );
    },
  );
});

test("sorts findings in one file by line and rule ID", () => {
  withFixture({ "app.tsx": "lorem ipsum\nblur-3xl" }, (dir) => {
    const output = parseOutput(scan([dir]));
    assert.deepEqual(
      output.findings.map(({ id, line }) => ({ id, line })),
      [
        { id: "lorem-placeholder", line: 1 },
        { id: "decorative-orb", line: 2 },
      ],
    );
  });
});

test("accepts directory paths containing spaces", () => {
  withFixture({}, (dir) => {
    const spaced = path.join(dir, "directory with spaces");
    fs.mkdirSync(spaced);
    fs.writeFileSync(path.join(spaced, "app.tsx"), "const ok = true;", "utf8");
    const result = scan([spaced]);
    assert.equal(result.status, 0);
    assert.equal(parseOutput(result).root, path.resolve(spaced));
  });
});

test("uses the current working directory when no directory is provided", () => {
  withFixture({ "app.tsx": "const ok = true;" }, (dir) => {
    const result = scan([], { cwd: dir });
    assert.equal(result.status, 0);
    const output = parseOutput(result);
    assert.equal(output.root, fs.realpathSync(dir));
    assert.equal(output.checkedFiles, 1);
  });
});

test("emits the versioned JSON result schema", () => {
  withFixture({ "app.tsx": "const ok = true;" }, (dir) => {
    const result = scan([dir]);
    assert.equal(result.status, 0);
    const output = parseOutput(result);
    assert.deepEqual(Object.keys(output), [
      "schemaVersion",
      "root",
      "checkedFiles",
      "findingCount",
      "findings",
    ]);
    assert.equal(output.schemaVersion, 1);
    assert.equal(output.root, path.resolve(dir));
    assert.equal(output.checkedFiles, 1);
    assert.equal(output.findingCount, 0);
    assert.deepEqual(output.findings, []);
  });
});

test("flushes JSON results larger than the pipe buffer", () => {
  const content = [
    "from-purple-500 to-blue-500",
    "orb",
    "rounded-3xl",
    "unlock",
    "text-[1vw]",
    "#000",
    "lorem ipsum",
    "flowchart",
  ].join("\n");
  const files = Object.fromEntries(
    Array.from({ length: 100 }, (_, index) => [`file-${index}.tsx`, content]),
  );

  withFixture(files, (dir) => {
    const result = scan([dir]);
    assert.equal(result.status, 0);
    const output = parseOutput(result);
    assert.equal(output.checkedFiles, 100);
    assert.equal(output.findingCount, 800);
  });
});

test("non-strict scans return zero when warnings exist", () => {
  withFixture({ "app.tsx": "lorem ipsum" }, (dir) => {
    const result = scan([dir]);
    assert.equal(result.status, 0);
    assert.equal(parseOutput(result).findingCount, 1);
  });
});

test("strict mode returns one for warnings", () => {
  withFixture({ "app.tsx": "lorem ipsum" }, (dir) => {
    assert.equal(scan(["--strict", dir]).status, 1);
    assert.equal(scan([dir, "--strict"]).status, 1);
  });
});

test("strict mode returns zero without warnings", () => {
  withFixture({ "app.tsx": "const ok = true;" }, (dir) => {
    assert.equal(scan(["--strict", dir]).status, 0);
  });
});

test("strict mode does not fail for informational findings", () => {
  withFixture({ "app.tsx": "rounded-3xl" }, (dir) => {
    const result = scan(["--strict", dir]);
    assert.equal(result.status, 0);
    const output = parseOutput(result);
    assert.equal(output.findingCount, 1);
    assert.equal(output.findings[0].severity, "info");
  });
});

test("file input returns controlled JSON error", () => {
  withFixture({ "app.tsx": "const ok = true;" }, (dir) => {
    const result = scan([path.join(dir, "app.tsx")]);
    assert.equal(result.status, 2);
    assert.equal(result.stdout, "");
    assert.equal(JSON.parse(result.stderr).error, "Input path must be a directory");
  });
});

test("missing input returns controlled JSON error", () => {
  const missing = path.join(
    os.tmpdir(),
    `product-composer-scan-missing-${process.pid}-${Date.now()}`,
  );
  const result = scan([missing]);
  assert.equal(result.status, 2);
  assert.equal(result.stdout, "");
  assert.equal(JSON.parse(result.stderr).error, "Input path does not exist");
});

test(
  "filesystem traversal errors return controlled JSON",
  { skip: permissionChecksUnavailable },
  () => {
    withFixture({ "blocked/app.tsx": "lorem ipsum" }, (dir) => {
      const blocked = path.join(dir, "blocked");
      fs.chmodSync(blocked, 0o000);
      try {
        const result = scan([dir]);
        assert.equal(result.status, 2);
        assert.equal(result.stdout, "");
        assert.equal(typeof JSON.parse(result.stderr).error, "string");
      } finally {
        fs.chmodSync(blocked, 0o700);
      }
    });
  },
);

test(
  "filesystem read errors return controlled JSON",
  { skip: permissionChecksUnavailable },
  () => {
    withFixture({ "blocked.tsx": "lorem ipsum" }, (dir) => {
      const blocked = path.join(dir, "blocked.tsx");
      fs.chmodSync(blocked, 0o000);
      try {
        const result = scan([dir]);
        assert.equal(result.status, 2);
        assert.equal(result.stdout, "");
        assert.equal(
          JSON.parse(result.stderr).error,
          "Unable to read source file: blocked.tsx",
        );
      } finally {
        fs.chmodSync(blocked, 0o600);
      }
    });
  },
);
