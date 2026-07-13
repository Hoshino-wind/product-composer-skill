import re
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_REFERENCES = {
    "asset-context.md",
    "brand-experiences.md",
    "chinese-aesthetic.md",
    "direction-system.md",
    "frontier-interactions.md",
    "image-concepts.md",
    "implementation-fidelity.md",
    "product-surfaces.md",
    "react-motion.md",
    "reference-translation.md",
    "repair-rendered-ui.md",
    "verification.md",
}

EXPECTED_TEST_FILES = {
    "test_aesthetic_references.py",
    "test_cross_axis_routing.py",
    "test_dependency_boundary.py",
    "test_image_prompt_compiler.py",
    "test_modifier_references.py",
    "test_phase_references.py",
    "test_provenance.py",
    "test_reference_integrity.py",
    "test_scanner.mjs",
    "test_skill_contract.py",
}

OLD_REFERENCES = {
    "ant-design-product-values.md",
    "anti-patterns.md",
    "asset-context-protocol.md",
    "chinese-aesthetic-design.md",
    "concept-to-implementation-lock.md",
    "content-judgment.md",
    "design-memory-consistency.md",
    "desire-minimalism-psychology.md",
    "direction-matrix-builder.md",
    "execution-discipline.md",
    "hero-page-experience.md",
    "image-generation-aesthetic-calibration.md",
    "interaction-grammar.md",
    "loop-engineer.md",
    "market-calibration.md",
    "react-bits-motion-layer.md",
    "reference-dna-extraction.md",
    "signature-aesthetic-systems.md",
    "style-family-router.md",
    "task-router.md",
    "taste-calibration.md",
    "ui-generation-operating-model.md",
    "visual-direction.md",
    "visual-quality-rubric.md",
}

EXPECTED_DISCOVERY_ROWS = [
    ["D1", "Create a distinctive SaaS homepage", "yes"],
    ["D2", "Substantially redesign an Ant Design dashboard", "yes"],
    ["D3", "Generate an art-directed UI image concept", "yes"],
    ["D4", "Implement an accepted visual concept without losing direction", "yes"],
    ["D5", "Repair a rendered first viewport that remains generic", "yes"],
    ["D6", "Change one button padding value", "no"],
    ["D7", "Review backend database indexes", "no"],
    ["D8", "Translate a document", "no"],
    ["D9", "Audit an existing UX flow without requesting redesign", "no"],
    ["D10", "Fix a local TypeScript error unrelated to visual direction", "no"],
    [
        "D11",
        "Create a personal portfolio direction from real content without inventing proof",
        "yes",
    ],
    [
        "D12",
        "Validate whether a recipe and preview qualify as a production template",
        "yes",
    ],
    [
        "D13",
        (
            "Create a routine settings screen entirely within an established design system, "
            "with no art-direction or fidelity decision"
        ),
        "no",
    ],
]

EXPECTED_ROUTING_ROWS = [
    [
        "R1 vague SaaS homepage",
        "Explore",
        "Brand",
        "none",
        "direction-system.md, brand-experiences.md, asset-context.md",
        "none",
        "3",
    ],
    [
        "R2 existing Ant Design dashboard redesign",
        "Explore",
        "Product",
        "Data",
        "direction-system.md, product-surfaces.md",
        "none",
        "2",
    ],
    [
        "R3 accepted image concept implementation",
        "Implement",
        "Product",
        "Image, Reference-led",
        (
            "implementation-fidelity.md, product-surfaces.md, image-concepts.md, "
            "reference-translation.md"
        ),
        "phase + surface + two behavior-changing modifiers",
        "4",
    ],
    [
        "R4 physical product page without photography",
        "Explore",
        "Brand",
        "Image",
        "direction-system.md, brand-experiences.md, image-concepts.md",
        "none",
        "3",
    ],
    [
        "R5 autonomous agent monitoring surface",
        "Explore",
        "Product",
        "Frontier, Data",
        "direction-system.md, product-surfaces.md, frontier-interactions.md",
        "none",
        "3",
    ],
    [
        "R6 Chinese cultural homepage",
        "Explore",
        "Brand",
        "Cultural",
        "direction-system.md, brand-experiences.md, chinese-aesthetic.md",
        "none",
        "3",
    ],
    [
        "R7 screenshot-led implementation",
        "Implement",
        "Product",
        "Reference-led",
        "implementation-fidelity.md, product-surfaces.md, reference-translation.md",
        "none",
        "3",
    ],
    [
        "R8 repair weak brand first viewport",
        "Repair",
        "Brand",
        "none",
        "repair-rendered-ui.md, brand-experiences.md",
        "none",
        "2",
    ],
    [
        "R9 personal portfolio without visual reference",
        "Explore",
        "Brand",
        "none",
        "direction-system.md, brand-experiences.md, asset-context.md",
        "none",
        "3",
    ],
    [
        "R10 recipe and preview requested as production template",
        "Explore",
        "Brand",
        "none",
        "verification.md, brand-experiences.md",
        "none",
        "2",
    ],
    [
        "R11 hybrid product launch with account workflow",
        "Explore",
        "Hybrid",
        "none",
        "direction-system.md, product-surfaces.md, brand-experiences.md",
        "none",
        "3",
    ],
]

ENGLISH_SECTIONS = [
    "Positioning",
    "When To Use",
    "Runtime Model",
    "What The Skill Preserves",
    "Package Map",
    "Scanner",
    "Validation",
    "License",
]

CHINESE_SECTIONS = [
    "Positioning",
    "什么时候使用",
    "运行模型",
    "保留的能力",
    "文件结构",
    "Scanner",
    "验证",
    "License",
]

VALIDATION_COMMANDS = [
    'python3 -B "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$PWD"',
    "python3 -B -m unittest discover -s tests -p 'test_*.py' -v",
    "node --test tests/test_scanner.mjs",
]


class ReferenceIntegrityTests(unittest.TestCase):
    def assert_exact_file_inventory(self, directory, expected, ignored_parts=frozenset()):
        actual = {
            str(path.relative_to(directory))
            for path in directory.rglob("*")
            if path.is_file()
            and not (set(path.relative_to(directory).parts) & set(ignored_parts))
        }
        self.assertEqual(actual, expected)

    def read_required(self, path):
        self.assertTrue(path.is_file(), f"required file is missing: {path.relative_to(ROOT)}")
        return path.read_text(encoding="utf-8")

    def public_paths(self):
        paths = [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "README.zh-CN.md"]
        paths += [ROOT / "references" / name for name in sorted(EXPECTED_REFERENCES)]
        paths += sorted((ROOT / "examples").glob("**/*.md"))
        return paths

    def public_text(self):
        return "\n".join(self.read_required(path) for path in self.public_paths())

    def parse_tables(self, path):
        text = self.read_required(path)
        groups = []
        current = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                current.append(stripped)
            elif current:
                groups.append(current)
                current = []
        if current:
            groups.append(current)

        tables = []
        for group in groups:
            self.assertGreaterEqual(len(group), 3, f"incomplete table in {path.name}")
            rows = [
                [cell.strip() for cell in line[1:-1].split("|")]
                for line in group
            ]
            width = len(rows[0])
            self.assertTrue(
                all(len(row) == width for row in rows),
                f"table rows must preserve {width} columns in {path.name}",
            )
            self.assertTrue(
                all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]),
                f"second table row must be a separator in {path.name}",
            )
            data_rows = rows[2:]
            for row_number, row in enumerate(data_rows, start=1):
                self.assertTrue(
                    all(row),
                    f"table row {row_number} has an empty cell in {path.name}",
                )
            tables.append((rows[0], data_rows))
        return tables

    def h2_sections(self, path):
        return re.findall(r"(?m)^## ([^#\r\n].*?)\s*$", self.read_required(path))

    def test_runtime_links_every_reference_directly_and_resolves_targets(self):
        skill = self.read_required(ROOT / "SKILL.md")
        linked_targets = set(re.findall(r"references/([a-z0-9-]+\.md)", skill))
        self.assertEqual(EXPECTED_REFERENCES, linked_targets)
        self.assertEqual(len(EXPECTED_REFERENCES), len(linked_targets))
        for name in sorted(linked_targets):
            with self.subTest(reference=name):
                self.assertTrue((ROOT / "references" / name).is_file())

    def test_reference_directory_is_exact(self):
        references = ROOT / "references"
        self.assert_exact_file_inventory(references, EXPECTED_REFERENCES)

    def test_reference_inventory_rejects_nested_or_non_markdown_payloads(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            for name in EXPECTED_REFERENCES:
                (references / name).write_text("owner\n", encoding="utf-8")
            nested = references / "legacy" / "payload.txt"
            nested.parent.mkdir()
            nested.write_text("legacy\n", encoding="utf-8")
            with self.assertRaises(AssertionError):
                self.assert_exact_file_inventory(references, EXPECTED_REFERENCES)

    def test_contract_test_inventory_is_exact(self):
        tests = ROOT / "tests"
        self.assert_exact_file_inventory(tests, EXPECTED_TEST_FILES, {"__pycache__"})

    def test_contract_test_inventory_rejects_a_missing_core_test(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            tests = Path(temp_dir)
            for name in EXPECTED_TEST_FILES - {"test_skill_contract.py"}:
                (tests / name).write_text("test\n", encoding="utf-8")
            with self.assertRaises(AssertionError):
                self.assert_exact_file_inventory(tests, EXPECTED_TEST_FILES)

    def test_old_reference_names_are_absent_from_public_runtime(self):
        text = self.public_text()
        for name in OLD_REFERENCES:
            self.assertNotIn(name, text)

    def test_runtime_package_has_required_files(self):
        required = {
            ".github/workflows/validate.yml",
            "SKILL.md",
            "agents/openai.yaml",
            "scripts/compile-image-prompt.py",
            "scripts/ui-pattern-scan.mjs",
            "evals/source-ledger.json",
            "tests/test_provenance.py",
            "tests/test_dependency_boundary.py",
        }
        required |= {f"tests/{name}" for name in EXPECTED_TEST_FILES}
        required |= {f"references/{name}" for name in EXPECTED_REFERENCES}
        actual = {
            str(path.relative_to(ROOT))
            for path in ROOT.rglob("*")
            if path.is_file()
        }
        self.assertTrue(required <= actual, sorted(required - actual))

    def test_public_surface_has_no_legacy_routes_or_machine_paths(self):
        text = self.public_text()
        self.assertNotIn("/Users/", text)
        self.assertNotIn("~/.codex/skills/product-composer", text)
        for name in sorted(OLD_REFERENCES):
            with self.subTest(legacy_reference=name):
                self.assertNotIn(name, text)
        for phrase in ["## Reference Map", "Expected routing:", "Work mode:"]:
            with self.subTest(legacy_route_phrase=phrase):
                self.assertNotIn(phrase, text)

    def test_public_guides_do_not_duplicate_complete_route_tables(self):
        paths = [
            ROOT / "README.md",
            ROOT / "README.zh-CN.md",
            ROOT / "examples" / "scenarios" / "product-composer-routing.md",
        ]
        forbidden_table_fragments = [
            "| Axis | Value | Owner reference |",
            "| ID | Phase | Surface | Modifiers | Initial active references |",
            "Phase: Explore | Implement | Repair",
            "Modifiers: Data | Frontier | Cultural | Image | Motion | Reference-led",
        ]
        for path in paths:
            text = self.read_required(path)
            for fragment in forbidden_table_fragments:
                with self.subTest(path=path.name, fragment=fragment):
                    self.assertNotIn(fragment, text)

    def test_long_references_have_early_contents_map(self):
        for name in sorted(EXPECTED_REFERENCES):
            path = ROOT / "references" / name
            lines = self.read_required(path).splitlines()
            if len(lines) > 100:
                with self.subTest(reference=name):
                    self.assertEqual(1, lines[:40].count("## Contents"))

    def test_metadata_matches_runtime_scope(self):
        metadata = self.read_required(ROOT / "agents" / "openai.yaml")
        self.assertIn("$product-composer", metadata)
        self.assertNotIn("localize", metadata.casefold())

    def test_discovery_scenarios_are_exact_unique_and_well_formed(self):
        path = ROOT / "evals" / "discovery-scenarios.md"
        tables = self.parse_tables(path)
        self.assertEqual(1, len(tables))
        header, rows = tables[0]
        self.assertEqual(["ID", "Prompt summary", "Activate"], header)
        self.assertEqual(3, len(header))
        keys = [row[0] for row in rows]
        self.assertEqual(len(keys), len(set(keys)), "discovery IDs must be unique")
        self.assertEqual(EXPECTED_DISCOVERY_ROWS, rows)
        self.assertEqual(
            {"yes"},
            {rows[index - 1][2] for index in [1, 2, 3, 4, 5, 11, 12]},
        )
        self.assertEqual(
            {"no"},
            {rows[index - 1][2] for index in [6, 7, 8, 9, 10]},
        )

    def test_routing_scenarios_are_exact_unique_and_respect_budget(self):
        path = ROOT / "evals" / "routing-scenarios.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(
            "R3, R4, R6, R7, R10, and R11 close the initial owner window before opening a later Asset truth window",
            text,
        )
        self.assertIn("does not change the selected Phase or Surface", text)
        tables = self.parse_tables(path)
        self.assertEqual(1, len(tables))
        header, rows = tables[0]
        self.assertEqual(
            [
                "ID",
                "Phase",
                "Surface",
                "Modifiers",
                "Initial active references",
                "Documented exception",
                "Count",
            ],
            header,
        )
        self.assertEqual(7, len(header))
        keys = [row[0].split()[0] for row in rows]
        self.assertEqual(len(keys), len(set(keys)), "routing IDs must be unique")
        self.assertEqual(EXPECTED_ROUTING_ROWS, rows)
        parsed = []
        for row in rows:
            key = row[0].split()[0]
            self.assertRegex(row[6], r"^\d+$")
            count = int(row[6])
            active = [name.strip() for name in row[4].split(",")]
            self.assertEqual(count, len(active), f"declared count differs for {key}")
            self.assertEqual(len(active), len(set(active)), f"duplicate owner for {key}")
            if key == "R10":
                self.assertIn("verification.md", active)
                self.assertEqual("Explore", row[1])
            else:
                self.assertNotIn("verification.md", active)
            for name in active:
                with self.subTest(route=key, reference=name):
                    self.assertIn(name, EXPECTED_REFERENCES)
                    self.assertTrue((ROOT / "references" / name).is_file())
            parsed.append((key, row[5], count))

        over_budget = [key for key, _, count in parsed if count > 3]
        self.assertEqual(["R3"], over_budget)
        r3 = [item for item in parsed if item[0] == "R3"]
        self.assertEqual(1, len(r3), "R3 must appear exactly once")
        self.assertEqual(("R3", "phase + surface + two behavior-changing modifiers", 4), r3[0])
        for key, exception, count in parsed:
            if key == "R3":
                continue
            self.assertLessEqual(count, 3, key)
            self.assertEqual("none", exception, key)

    def test_readmes_share_the_final_public_contract(self):
        readmes = [
            (
                ROOT / "README.md",
                ENGLISH_SECTIONS,
                "The package does not claim to include a runnable starter, tested golden, "
                "or production template.",
                "is repository provenance evidence; it is not a runtime reference.",
            ),
            (
                ROOT / "README.zh-CN.md",
                CHINESE_SECTIONS,
                "本包不声称包含 runnable starter、tested golden 或 production template。",
                "是仓库的 provenance evidence，不是 runtime reference。",
            ),
        ]
        for path, expected_sections, maturity_disclaimer, provenance_role in readmes:
            text = self.read_required(path)
            with self.subTest(path=path.name):
                self.assertEqual(expected_sections, self.h2_sections(path))
                self.assertIn("Runtime authority: root `SKILL.md` only.", text)
                self.assertIn("validation-only", text)
                self.assertIn("(evals/source-ledger.json)", text)
                self.assertIn("(evals/discovery-scenarios.md)", text)
                self.assertIn("(evals/routing-scenarios.md)", text)
                for term in ["recipe", "preview", "runnable starter", "tested golden", "template"]:
                    self.assertRegex(text, rf"(?mi)^- \*\*{re.escape(term)}\*\*[:：]\s*\S")
                self.assertIn(maturity_disclaimer, text)
                self.assertIn(provenance_role, text)
                for command in VALIDATION_COMMANDS:
                    self.assertIn(command, text)

    def test_public_evaluation_links_resolve_and_scenarios_stay_compact(self):
        links = {
            ROOT / "README.md": [
                "evals/source-ledger.json",
                "evals/discovery-scenarios.md",
                "evals/routing-scenarios.md",
            ],
            ROOT / "README.zh-CN.md": [
                "evals/source-ledger.json",
                "evals/discovery-scenarios.md",
                "evals/routing-scenarios.md",
            ],
            ROOT / "examples" / "scenarios" / "product-composer-routing.md": [
                "../../evals/discovery-scenarios.md",
                "../../evals/routing-scenarios.md",
            ],
        }
        for source, targets in links.items():
            text = self.read_required(source)
            for target in targets:
                with self.subTest(source=source.name, target=target):
                    self.assertEqual(1, text.count(f"({target})"))
                    self.assertTrue((source.parent / target).resolve().is_file())

        scenario = ROOT / "examples" / "scenarios" / "product-composer-routing.md"
        self.assertEqual(
            ["Runtime Authority", "Example 1: Explore", "Example 2: Accepted Image Concept"],
            self.h2_sections(scenario),
        )
        self.assertEqual(2, self.read_required(scenario).count("Prompt:"))


if __name__ == "__main__":
    unittest.main()
