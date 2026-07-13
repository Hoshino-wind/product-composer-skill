import ast
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
BANNED_FILES = {
    "setup.py", "setup.cfg", "pyproject.toml", "Pipfile", "Pipfile.lock",
    "poetry.lock", "uv.lock", "pdm.lock", "pdm.toml",
    "conda-lock.yml", "conda-lock.yaml",
    "package.json", "package-lock.json", "npm-shrinkwrap.json",
    "pnpm-lock.yaml", "pnpm-workspace.yaml", "yarn.lock", "bun.lock", "bun.lockb",
}
BANNED_FILE_PATTERNS = (
    re.compile(r"requirements.*\.(?:txt|in)\Z", re.IGNORECASE),
    re.compile(r"environment(?:[-_.].*)?\.(?:yml|yaml)\Z", re.IGNORECASE),
)
BANNED_DIRS = {"node_modules", ".yarn", ".venv", "venv", "vendor"}
INSTALL_PATTERN = re.compile(
    r"\b(?:(?:python(?:3(?:\.\d+)*)?|py)\s+-m\s+(?:pip|pip3)\s+install"
    r"|(?:pip|pip3)\s+install"
    r"|npm\s+(?:install|i|in|ins|inst|insta|instal|isnt|isnta|isntal|isntall|add|"
    r"ci|clean-install|install-clean|ic|cit)"
    r"|pnpm\s+(?:install|i|add)"
    r"|yarn(?:\s+(?:install|add)|\s+--(?:immutable|immutable-cache|frozen-lockfile)"
    r"|(?=[ \t]*(?:$|[\r\n;&|])))"
    r"|bun\s+(?:install|i|add)"
    r"|poetry\s+(?:install|add)"
    r"|pdm\s+(?:install|sync|add)"
    r"|uv\s+(?:sync|add|pip\s+install))\b"
)
JS_EXTENSIONS = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".mts", ".cts"}
JS_SPECIFIER = re.compile(
    r'(?:from\s+|import\s*\(|require\s*\(|import\s+)["\']([^"\']+)["\']'
)
VERIFIED_ACTION_REFS = {
    "actions/checkout": "34e114876b0b11c390a56381ad16ebd13914f8d5",
    "actions/setup-python": "a26af69be951a213d495a4c3e4e4022e16d87065",
    "actions/setup-node": "49933ea5288caeca8642d1e84afbd3f7d6820020",
}
EXPECTED_ACTION_COUNTS = {
    "actions/checkout": 3,
    "actions/setup-python": 2,
    "actions/setup-node": 1,
}


class DependencyBoundaryTests(unittest.TestCase):
    def repository_paths(self):
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        return [
            ROOT / raw.decode("utf-8")
            for raw in result.stdout.split(b"\0")
            if raw and (ROOT / raw.decode("utf-8")).exists()
        ]

    def assert_repository_mutation_rejected(self, relative_path, content, boundary):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            candidate = temp_root / relative_path
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_text(content, encoding="utf-8")
            with (
                patch(f"{__name__}.ROOT", temp_root),
                patch.object(self, "repository_paths", return_value=[candidate]),
                self.assertRaises(AssertionError),
            ):
                boundary()

    def test_no_dependency_manifests_or_vendored_directories(self):
        failures = []
        for path in self.repository_paths():
            relative = path.relative_to(ROOT)
            if any(part in BANNED_DIRS for part in relative.parts):
                failures.append(str(relative))
            if path.is_file() and (
                path.name in BANNED_FILES
                or any(pattern.fullmatch(path.name) for pattern in BANNED_FILE_PATTERNS)
            ):
                failures.append(str(relative))
        self.assertEqual(failures, [])

    def test_manifest_detector_rejects_common_python_and_node_variants(self):
        manifests = [
            "setup.py",
            "setup.cfg",
            "requirements.txt",
            "requirements-dev.txt",
            "requirements.in",
            "requirements-dev.in",
            "pyproject.toml",
            "Pipfile",
            "Pipfile.lock",
            "poetry.lock",
            "uv.lock",
            "pdm.lock",
            "pdm.toml",
            "environment.yml",
            "environment.yaml",
            "environment-dev.yml",
            "conda-lock.yml",
            "conda-lock.yaml",
            "package.json",
            "package-lock.json",
            "npm-shrinkwrap.json",
            "pnpm-lock.yaml",
            "pnpm-workspace.yaml",
            "yarn.lock",
            "bun.lock",
            "bun.lockb",
        ]
        for manifest in manifests:
            with self.subTest(manifest=manifest):
                self.assert_repository_mutation_rejected(
                    manifest,
                    "temporary dependency mutation\n",
                    self.test_no_dependency_manifests_or_vendored_directories,
                )

    def test_vendored_yarn_cache_is_rejected(self):
        self.assert_repository_mutation_rejected(
            ".yarn/cache/example.zip",
            "vendored dependency\n",
            self.test_no_dependency_manifests_or_vendored_directories,
        )

    def test_python_uses_standard_library_or_local_modules(self):
        local_modules = {path.stem for path in ROOT.glob("*.py")}
        local_modules |= {path.name for path in ROOT.iterdir() if path.is_dir()}
        allowed = set(sys.stdlib_module_names) | local_modules
        failures = []
        for path in self.repository_paths():
            if path.suffix != ".py":
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    names = [alias.name.split(".")[0] for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    names = [node.module.split(".")[0]]
                else:
                    continue
                failures += [f"{path.relative_to(ROOT)}:{name}" for name in names if name not in allowed]
        self.assertEqual(failures, [])

    def test_node_uses_builtin_or_relative_imports(self):
        failures = []
        for path in self.repository_paths():
            if path.suffix not in JS_EXTENSIONS:
                continue
            for specifier in JS_SPECIFIER.findall(path.read_text(encoding="utf-8")):
                if not specifier.startswith(("node:", "./", "../")):
                    failures.append(f"{path.relative_to(ROOT)}:{specifier}")
        self.assertEqual(failures, [])

    def test_node_import_detector_scans_jsx_and_tsx(self):
        for extension in [".jsx", ".tsx"]:
            with self.subTest(extension=extension):
                self.assert_repository_mutation_rejected(
                    f"component{extension}",
                    'import React from "react";\n',
                    self.test_node_uses_builtin_or_relative_imports,
                )

    def test_ci_has_no_dependency_install_step(self):
        workflows_dir = ROOT / ".github" / "workflows"
        validation_workflow = workflows_dir / "validate.yml"
        self.assertTrue(validation_workflow.is_file(), "missing .github/workflows/validate.yml")

        configurations = {
            *workflows_dir.glob("*.yml"),
            *workflows_dir.glob("*.yaml"),
        }
        actions_dir = ROOT / ".github" / "actions"
        if actions_dir.is_dir():
            configurations.update(actions_dir.rglob("action.yml"))
            configurations.update(actions_dir.rglob("action.yaml"))
        configurations = sorted(configurations)
        self.assertIn(validation_workflow, configurations)
        failures = []
        for configuration in configurations:
            match = INSTALL_PATTERN.search(configuration.read_text(encoding="utf-8"))
            if match:
                failures.append(f"{configuration.relative_to(ROOT)}:{match.group(0)}")
        self.assertEqual(failures, [])

    def test_ci_boundary_rejects_missing_validation_workflow(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch(f"{__name__}.ROOT", Path(temp_dir)):
                with self.assertRaises(AssertionError):
                    self.test_ci_has_no_dependency_install_step()

    def test_ci_boundary_scans_every_workflow(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            workflows = Path(temp_dir) / ".github" / "workflows"
            workflows.mkdir(parents=True)
            (workflows / "validate.yml").write_text("name: safe\n", encoding="utf-8")
            (workflows / "release.yaml").write_text("- run: npm install\n", encoding="utf-8")
            with patch(f"{__name__}.ROOT", Path(temp_dir)):
                with self.assertRaises(AssertionError):
                    self.test_ci_has_no_dependency_install_step()

    def test_ci_boundary_scans_local_composite_actions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            workflows = temp_root / ".github" / "workflows"
            workflows.mkdir(parents=True)
            (workflows / "validate.yml").write_text("name: safe\n", encoding="utf-8")
            action = temp_root / ".github" / "actions" / "bootstrap" / "action.yml"
            action.parent.mkdir(parents=True)
            action.write_text(
                "runs:\n  using: composite\n  steps:\n    - shell: bash\n"
                "      run: npm add example\n",
                encoding="utf-8",
            )
            with patch(f"{__name__}.ROOT", temp_root):
                with self.assertRaises(AssertionError):
                    self.test_ci_has_no_dependency_install_step()

    def test_install_detector_covers_common_ci_commands(self):
        install_commands = {
            "pip install example",
            "pip3 install example",
            "python -m pip install example",
            "python3 -m pip install example",
            "py -m pip install example",
            "npm install",
            "npm i",
            "npm in",
            "npm ins",
            "npm inst",
            "npm insta",
            "npm instal",
            "npm isnt",
            "npm isnta",
            "npm isntal",
            "npm isntall",
            "npm add example",
            "npm ci",
            "npm clean-install",
            "npm install-clean",
            "npm ic",
            "npm cit",
            "pnpm install",
            "pnpm i",
            "pnpm add example",
            "yarn",
            "yarn --immutable",
            "yarn --immutable-cache",
            "yarn --frozen-lockfile",
            "yarn install",
            "yarn add example",
            "bun install",
            "bun i",
            "bun add example",
            "poetry install",
            "poetry add example",
            "pdm install",
            "pdm sync",
            "pdm add example",
            "uv sync",
            "uv pip install example",
            "uv add example",
        }
        for command in install_commands:
            with self.subTest(command=command):
                self.assertIsNotNone(INSTALL_PATTERN.search(command))

    def test_validation_workflow_is_least_privilege_and_pinned(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(
            encoding="utf-8"
        )
        self.assertRegex(workflow, r"(?m)^permissions:\n  contents: read$")
        self.assertNotRegex(workflow, r"(?m)^\s+[a-z-]+:\s+write\s*$")

        for action, expected_sha in VERIFIED_ACTION_REFS.items():
            with self.subTest(action=action):
                refs = re.findall(
                    rf"(?m)^\s*- uses: {re.escape(action)}@([^\s#]+)",
                    workflow,
                )
                self.assertEqual(EXPECTED_ACTION_COUNTS[action], len(refs))
                self.assertEqual({expected_sha}, set(refs))
                self.assertTrue(all(re.fullmatch(r"[0-9a-f]{40}", ref) for ref in refs))

        checkout_sha = VERIFIED_ACTION_REFS["actions/checkout"]
        checkout_steps = re.findall(
            rf"(?m)^      - uses: actions/checkout@{checkout_sha}(?:\s+#.*)?\n"
            r"        with:\n"
            r"          persist-credentials: false$",
            workflow,
        )
        self.assertEqual(3, len(checkout_steps))

        timeouts = re.findall(r"(?m)^    timeout-minutes: ([1-9][0-9]*)$", workflow)
        self.assertEqual(3, len(timeouts))
        self.assertTrue(all(int(timeout) <= 30 for timeout in timeouts))


if __name__ == "__main__":
    unittest.main()
