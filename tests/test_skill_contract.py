import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
METADATA = ROOT / "agents" / "openai.yaml"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
SCENARIOS = ROOT / "examples" / "scenarios" / "product-composer-routing.md"
TOMBSTONE = ROOT / "references" / "task-router.md"
DIRECTION_SYSTEM = ROOT / "references" / "direction-system.md"

EXPECTED_DESCRIPTION = (
    "Use when creating or substantially redesigning UI where visual direction, aesthetic "
    "judgment, asset-family art direction, image-concept generation, accepted-design fidelity, "
    "rendered repair, or artifact-maturity or visual-parity judgment materially affects the result."
)

EXPECTED_REFERENCES = {
    "direction-system.md",
    "product-surfaces.md",
    "brand-experiences.md",
    "frontier-interactions.md",
    "asset-context.md",
    "image-concepts.md",
    "implementation-fidelity.md",
    "repair-rendered-ui.md",
    "chinese-aesthetic.md",
    "react-motion.md",
    "reference-translation.md",
    "verification.md",
}

EXPECTED_HEADINGS = [
    "Principle",
    "Creative Core",
    "Route",
    "Design Contract",
    "Owner Matrix",
    "Reference Windows",
    "Phase Outcomes",
    "Frame",
    "Verify",
    "Hard Gates",
    "Optional Scanner",
]

EXPECTED_OWNERS = {
    ("Phase", "Explore"): (
        "references/direction-system.md",
        "references/verification.md",
    ),
    ("Phase", "Implement"): ("references/implementation-fidelity.md",),
    ("Phase", "Repair"): ("references/repair-rendered-ui.md",),
    ("Surface", "Product"): ("references/product-surfaces.md",),
    ("Surface", "Brand"): ("references/brand-experiences.md",),
    ("Surface", "Hybrid"): (
        "references/product-surfaces.md",
        "references/brand-experiences.md",
    ),
    ("Modifier", "Data"): ("references/product-surfaces.md",),
    ("Modifier", "Frontier"): ("references/frontier-interactions.md",),
    ("Modifier", "Cultural"): ("references/chinese-aesthetic.md",),
    ("Modifier", "Image"): ("references/image-concepts.md",),
    ("Modifier", "Motion"): ("references/react-motion.md",),
    ("Modifier", "Reference-led"): ("references/reference-translation.md",),
    ("Gate", "Asset truth"): ("references/asset-context.md",),
    ("Stage", "Verify"): ("references/verification.md",),
}

LEGACY_RUNTIME_REFERENCES = {
    "task-router.md",
    "style-family-router.md",
    "chinese-aesthetic-design.md",
    "visual-direction.md",
    "hero-page-experience.md",
    "taste-calibration.md",
    "direction-matrix-builder.md",
    "concept-to-implementation-lock.md",
    "asset-context-protocol.md",
    "design-memory-consistency.md",
    "visual-quality-rubric.md",
    "loop-engineer.md",
    "image-generation-aesthetic-calibration.md",
    "interaction-grammar.md",
    "ant-design-product-values.md",
    "content-judgment.md",
    "desire-minimalism-psychology.md",
    "market-calibration.md",
    "signature-aesthetic-systems.md",
    "react-bits-motion-layer.md",
    "execution-discipline.md",
    "anti-patterns.md",
}


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")
        cls.sections = cls.parse_heading_sections(cls.text, level=2)
        cls.section_map = dict(cls.sections)

    @staticmethod
    def parse_heading_sections(text, level):
        sections = []
        current_title = None
        current_lines = []
        fence_marker = None
        heading_pattern = re.compile(rf"^ {{0,3}}#{{{level}}}[ \t]+(.+?)\s*$")

        for line in text.splitlines():
            fence = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
            if fence:
                marker = fence.group(1)[0]
                if fence_marker is None:
                    fence_marker = marker
                elif fence_marker == marker:
                    fence_marker = None
                if current_title is not None:
                    current_lines.append(line)
                continue

            heading = heading_pattern.match(line) if fence_marker is None else None
            if heading:
                if current_title is not None:
                    sections.append((current_title, "\n".join(current_lines)))
                current_title = heading.group(1)
                current_lines = []
            elif current_title is not None:
                current_lines.append(line)

        if current_title is not None:
            sections.append((current_title, "\n".join(current_lines)))
        return sections

    @staticmethod
    def parse_markdown_table(section):
        rows = []
        for line in section.splitlines():
            stripped = line.strip()
            if not (stripped.startswith("|") and stripped.endswith("|")):
                continue
            cells = [cell.strip() for cell in stripped[1:-1].split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            rows.append(cells)

        if not rows:
            raise AssertionError("expected a markdown table")
        width = len(rows[0])
        if not all(len(row) == width for row in rows):
            raise AssertionError("table rows must have equal width")
        return rows[0], rows[1:]

    @staticmethod
    def get_labeled_field(section, field):
        matches = re.findall(
            rf"(?mi)^-\s*{re.escape(field)}\s*:\s*(.*?)\s*$",
            section,
        )
        if len(matches) != 1:
            raise AssertionError(f"expected one {field!r} field, found {len(matches)}")
        return matches[0]

    def owner_rows(self):
        header, rows = self.parse_markdown_table(self.section_map["Owner Matrix"])
        self.assertEqual(["Axis", "Value", "Owner reference"], header)
        parsed = {}
        for axis, value, owner_cell in rows:
            key = (axis, value)
            self.assertNotIn(key, parsed, f"duplicate owner row: {key}")
            parsed[key] = tuple(re.findall(r"references/[a-z0-9-]+\.md", owner_cell))
        return parsed

    def direction_contract_fields(self):
        text = DIRECTION_SYSTEM.read_text(encoding="utf-8")
        sections = dict(self.parse_heading_sections(text, level=2))
        record = re.search(
            r"```text\nDirectionContract\n(.*?)\n```",
            sections["Direction Contract"],
            re.DOTALL,
        )
        self.assertIsNotNone(record)
        fields = tuple(re.findall(r"(?m)^([A-Za-z][A-Za-z -]+):", record.group(1)))
        self.assertTrue(fields)
        self.assertEqual(len(fields), len(set(field.casefold() for field in fields)))
        return fields

    def test_frontmatter_is_trigger_only_and_covers_runtime_entry_cases(self):
        match = re.match(r"\A---\n(.*?)\n---\n", self.text, re.DOTALL)
        self.assertIsNotNone(match)
        fields = {}
        for line in match.group(1).splitlines():
            key, value = line.split(":", 1)
            fields[key] = value.strip().strip('"')
        self.assertEqual({"name", "description"}, set(fields))
        self.assertEqual("product-composer", fields["name"])
        self.assertEqual(EXPECTED_DESCRIPTION, fields["description"])
        for route_instruction in ["phase", "surface", "modifier", "route"]:
            self.assertNotIn(route_instruction, fields["description"].casefold())

    def test_runtime_sections_and_context_budget_are_bounded(self):
        self.assertEqual(EXPECTED_HEADINGS, [title for title, _ in self.sections])
        raw = SKILL.read_bytes()
        self.assertLessEqual(len(raw.splitlines()), 200)
        self.assertLessEqual(len(raw), 16 * 1024)

    def test_creative_core_is_positive_and_shared_across_ui_and_assets(self):
        core = self.section_map["Creative Core"]
        for term in [
            "creative director as well as a contract governor",
            "positive visual thesis before applying anti-defaults",
            "truth constrain claims, not imagination",
            "content, control, proof, space, and time",
            "attention, silhouette, proportion, rhythm, and silence",
            "fixed anchors", "one controlled tension or exploration axis",
            "layout, type, image, material, and motion as one visual grammar",
            "selection and deletion part of taste", "inspectable target context",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, core)

    def test_route_axes_have_total_unique_owner_coverage(self):
        route = self.section_map["Route"]
        self.assertIn(
            "Design read and direction parameters are Design Contract fields, not route axes",
            route,
        )
        enums = {
            "Phase": tuple(self.get_labeled_field(route, "Phase").split(" | ")),
            "Surface": tuple(self.get_labeled_field(route, "Surface").split(" | ")),
            "Modifier": tuple(self.get_labeled_field(route, "Modifiers").split(" | ")),
        }
        self.assertEqual(("Explore", "Implement", "Repair"), enums["Phase"])
        self.assertEqual(("Product", "Brand", "Hybrid"), enums["Surface"])
        self.assertEqual(
            ("Data", "Frontier", "Cultural", "Image", "Motion", "Reference-led"),
            enums["Modifier"],
        )

        owners = self.owner_rows()
        self.assertEqual(EXPECTED_OWNERS, owners)
        for axis, values in enums.items():
            self.assertEqual(set(values), {value for row_axis, value in owners if row_axis == axis})

        self.assertEqual(
            ("references/product-surfaces.md", "references/brand-experiences.md"),
            owners[("Surface", "Hybrid")],
        )
        combined = (
            owners[("Phase", "Implement")]
            + owners[("Surface", "Product")]
            + owners[("Modifier", "Data")]
        )
        self.assertEqual(
            ["references/implementation-fidelity.md", "references/product-surfaces.md"],
            list(dict.fromkeys(combined)),
        )
        self.assertNotIn(("Modifier", "Asset truth"), owners)
        self.assertEqual(("references/asset-context.md",), owners[("Gate", "Asset truth")])

    def test_design_contract_is_one_record_with_direction_projection(self):
        section = self.section_map["Design Contract"]
        self.assertIn("Design Contract is the only runtime record.", section)
        self.assertIn("Every owner reads and updates this same record.", section)
        preamble = section.split("###", 1)[0]
        fields = set(re.findall(r"(?m)^- ([A-Za-z][A-Za-z /-]+):", preamble))
        self.assertEqual({
            "Route",
            "DirectionContract projection",
            "Experience architecture and region model",
            "Workflow and required states",
            "Truth and provenance ledger",
            "Artifact target and maturity",
            "Functional delta",
            "Locked and adaptable decisions",
            "Acceptance checks",
        }, fields)

        subsections = dict(self.parse_heading_sections(section, level=3))
        self.assertEqual(["DirectionContract Projection", "Stage Handoff"], list(subsections))
        self.assertIn("not a second record", subsections["DirectionContract Projection"])
        projection_header, projection_rows = self.parse_markdown_table(
            subsections["DirectionContract Projection"]
        )
        self.assertEqual(["DirectionContract field", "Design Contract field"], projection_header)
        source_fields = self.direction_contract_fields()
        self.assertEqual(
            [field.casefold() for field in source_fields],
            [row[0].casefold() for row in projection_rows],
        )
        self.assertEqual(
            [field.casefold() for field in source_fields],
            [row[1].casefold() for row in projection_rows],
        )
        self.assertEqual(
            len(projection_rows),
            len({row[0].casefold() for row in projection_rows}),
        )

        handoff_header, handoff_rows = self.parse_markdown_table(
            subsections["Stage Handoff"]
        )
        self.assertIn(
            "Every stage summary updates the same Design Contract",
            subsections["Stage Handoff"],
        )
        self.assertEqual(["Handoff record", "Preservation rule"], handoff_header)
        self.assertEqual([
            [
                "Design Contract",
                "all fields, including the complete DirectionContract projection",
            ]
        ], handoff_rows)

    def test_phase_outcomes_branch_and_stop_instead_of_falling_into_build(self):
        self.assertIn("Phase Outcomes", self.section_map)
        self.assertIn(
            "directly for the validation-only Explore entry",
            self.section_map["Verify"],
        )
        section = self.section_map["Phase Outcomes"]
        self.assertEqual(
            "direction-only | implementation-authorized | rendered-repair | validation-only",
            self.get_labeled_field(section, "Entry intent"),
        )
        self.assertNotIn("Entry intent", self.section_map["Route"])
        header, rows = self.parse_markdown_table(section)
        self.assertEqual([
            "Trigger class", "Entry intent", "Phase", "Owner",
            "Required input or evidence", "Output", "Mutation or stop",
        ], header)
        self.assertEqual([
            [
                "new UI or substantial-redesign direction", "direction-only", "Explore",
                "references/direction-system.md", "framed inputs",
                "updated Design Contract plus selected direction",
                "stop; enter Implement only with explicit user authorization",
            ],
            [
                "new UI or substantial-redesign implementation", "implementation-authorized", "Implement",
                "references/direction-system.md plus references/implementation-fidelity.md",
                "explicit authorization to infer or select direction, framed inputs, and complete Functional delta",
                "selected or inferred DirectionContract, implemented vertical slice, and updated Design Contract",
                "select or infer direction and complete Functional delta before the first slice; then Verify",
            ],
            [
                "image concept", "direction-only", "Explore",
                "references/direction-system.md plus references/image-concepts.md",
                "framed inputs plus image eligibility",
                "updated Design Contract plus image concept",
                "stop; enter Implement only with explicit user authorization",
            ],
            [
                "accepted concept implementation", "implementation-authorized", "Implement",
                "references/implementation-fidelity.md",
                "complete Functional delta plus locked direction",
                "implemented vertical slice plus updated Design Contract",
                "Verify; enter Repair only from observed failure",
            ],
            [
                "rendered repair", "rendered-repair", "Repair",
                "references/repair-rendered-ui.md",
                "rendered evidence plus observed failure",
                "one evidence-backed repair axis plus updated Design Contract",
                "continue, stop, escalate, or block; stop without new evidence",
            ],
            [
                "artifact maturity or visual parity validation", "validation-only", "Explore",
                "references/verification.md plus necessary claim owner",
                "inspectable artifact or claim",
                "Evidence report plus verification gaps",
                "no mutation; do not enter Build, Implement, or Repair",
            ],
        ], rows)
        self.assertEqual(6, len({row[0] for row in rows}))
        self.assertEqual({"Explore", "Implement", "Repair"}, {row[2] for row in rows})
        validation_rows = [row for row in rows if row[1] == "validation-only"]
        self.assertEqual(1, len(validation_rows))
        self.assertEqual("Explore", validation_rows[0][2])
        self.assertEqual("Evidence report plus verification gaps", validation_rows[0][5])
        self.assertEqual(
            "no mutation; do not enter Build, Implement, or Repair",
            validation_rows[0][6],
        )
        self.assertIn("exactly one Phase and one Surface", section)
        self.assertIn("within the normal reference-window budget", section)
        self.assertNotIn("Commit -> Build", self.text)

        authorized = [row for row in rows if row[1] == "implementation-authorized"]
        self.assertEqual(2, len(authorized))
        self.assertTrue(all(row[2] == "Implement" for row in authorized))
        self.assertIn("selected or inferred DirectionContract", authorized[0][5])
        self.assertIn("complete Functional delta", authorized[0][4])
        self.assertIn("before the first slice", authorized[0][6])

    def test_reference_windows_have_one_exact_r3_exception(self):
        self.assertIn("Reference Windows", self.section_map)
        section = self.section_map["Reference Windows"]
        self.assertEqual(
            "owner documents open in the current window",
            self.get_labeled_field(section, "Active references"),
        )
        self.assertEqual("3", self.get_labeled_field(section, "Normal maximum"))
        self.assertEqual(
            "write decisions into the complete Design Contract, then unload all owner documents",
            self.get_labeled_field(section, "Window close"),
        )
        self.assertEqual(
            "open sequential windows of at most 3; never omit an owner",
            self.get_labeled_field(section, "Owner overflow"),
        )
        self.assertEqual("R3 only", self.get_labeled_field(section, "Exception set"))

        header, rows = self.parse_markdown_table(section)
        self.assertEqual(["Exception", "Initial route", "Active owner references", "Count"], header)
        self.assertEqual(1, len(rows))
        exception, route, owner_cell, count = rows[0]
        self.assertEqual("R3", exception)
        self.assertEqual(
            "Implement / Product / Image + Reference-led / accepted image concept",
            route,
        )
        self.assertEqual("4", count)
        self.assertEqual([
            "implementation-fidelity.md",
            "product-surfaces.md",
            "image-concepts.md",
            "reference-translation.md",
        ], re.findall(r"[a-z0-9-]+\.md", owner_cell))
        self.assertNotIn("verification.md", owner_cell)
        for escape_hatch in [
            "if one stage needs more than",
            "more than three owners",
            "record the exception",
            "why every owner changes behavior",
        ]:
            self.assertNotIn(escape_hatch, section.casefold())

    def test_hard_gate_priority_and_aesthetic_override_are_explicit(self):
        self.assertIn("Hard Gates", self.section_map)
        section = self.section_map["Hard Gates"]
        header, rows = self.parse_markdown_table(section)
        self.assertEqual(["Priority", "Rule"], header)
        self.assertEqual(["1", "2", "3", "4"], [row[0] for row in rows])
        self.assertEqual(
            "product correctness; state clarity; accessibility; reversibility; "
            "truth and provenance; license boundaries",
            rows[0][1],
        )
        self.assertEqual(
            "infer from evidence; no universal default; never override locked decisions",
            self.get_labeled_field(section, "Direction parameters"),
        )
        self.assertEqual(
            "require context and an override condition; popularity alone never creates a ban",
            self.get_labeled_field(section, "Aesthetic anti-defaults"),
        )
        self.assertIn(
            "source signals, visible consequences, fixed anchors, and one exploration axis",
            self.get_labeled_field(section, "Creative-core gate"),
        )
        self.assertIn(
            "do not allocate media by screen count",
            self.get_labeled_field(section, "Media-led implementation gate"),
        )
        self.assertIn(
            "do not code a media- or scroll-led website until its archetype",
            self.get_labeled_field(section, "Experience architecture gate"),
        )
        art_repair = self.get_labeled_field(section, "Art-direction repair gate")
        for term in [
            "diagnose the lowest failure",
            "Form, Proportion, Memory, or repeated structure",
            "otherwise repair one axis",
            "full/thumbnail/crop/blurred-label",
            "preserve truth/mission",
        ]:
            self.assertIn(term, art_repair)

        interaction = self.get_labeled_field(section, "Interaction-causality gate")
        for term in [
            "if direction promises a primary interaction",
            "living object",
            "input -> response -> durable consequence -> handoff -> fallback",
            "Utility filters/accordions may remain but do not count",
            "use one state machine",
        ]:
            self.assertIn(term, interaction)

    def test_composition_divergence_gate_rejects_theme_only_reskins(self):
        section = self.section_map["Hard Gates"]
        gate = self.get_labeled_field(section, "Composition-divergence gate")
        for term in [
            "new UI or substantial redesign",
            "three structurally different candidates",
            "copy, palette, assets, or card styling",
            "nearby or accepted outputs",
            "at least four fingerprint axes",
            "at least two structural axes",
            "composition family or experience architecture",
            "explicit continuity evidence",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, gate)

    def test_runtime_evidence_gates_and_reference_first_are_section_bound(self):
        design = self.section_map["Design Contract"]
        frame = self.section_map["Frame"]
        verify = self.section_map["Verify"]
        self.assertIn("Do not implement an image concept until Functional delta is complete", design)
        self.assertIn("Generated or inferred material is not factual proof", design)
        self.assertIn("Inspect a supplied reference before proposing a direction", frame)
        self.assertIn("Reference-first does not automatically add Reference-led", frame)
        sequence = (
            "website archetype and route scope -> content beats -> region geometry and scroll model -> "
            "media palette and many-to-many mapping -> motion grammar and per-region choreography -> "
            "typography and interaction -> implementation"
        )
        self.assertIn(sequence, frame)
        self.assertIn("A hero is the opening experience inside a route", frame)
        self.assertIn("not required to be one `100vh` section", frame)
        self.assertIn("A content beat is not a screen", frame)
        self.assertIn("One asset may persist across several beats", frame)
        self.assertIn("trace the complete route from opener to footer or interaction endpoint", frame)
        self.assertIn("A first-viewport screenshot can establish composition only", frame)
        self.assertIn("artifact maturity", verify)
        self.assertIn("visual parity", verify)
        self.assertIn("matching evidence", verify)
        self.assertIn("explicitly PC-only", verify)
        self.assertIn(
            "Do not label a recipe or preview as a runnable starter, tested golden, "
            "or production template without matching evidence",
            verify,
        )
        self.assertIn("node scripts/ui-pattern-scan.mjs ./src", self.section_map["Optional Scanner"])

    def test_reference_index_is_exact_unique_and_resolvable(self):
        linked = set(re.findall(r"references/([a-z0-9-]+\.md)", self.text))
        self.assertEqual(EXPECTED_REFERENCES, linked)
        for name in linked:
            with self.subTest(reference=name):
                self.assertTrue((ROOT / "references" / name).is_file())

    def test_public_surfaces_neutralize_the_legacy_runtime(self):
        authority_line = "Runtime authority: root `SKILL.md` only."
        public_guides = {
            README_EN: README_EN.read_text(encoding="utf-8"),
            README_ZH: README_ZH.read_text(encoding="utf-8"),
            SCENARIOS: SCENARIOS.read_text(encoding="utf-8"),
        }
        for path, text in public_guides.items():
            with self.subTest(path=path.name):
                self.assertIn(authority_line, text)
                for legacy_name in LEGACY_RUNTIME_REFERENCES:
                    self.assertNotIn(legacy_name, text)
                self.assertNotIn("## Reference Map", text)
                self.assertNotIn("Expected routing:", text)
                self.assertNotIn("Work mode:", text)
                self.assertNotIn("test_skill_guidance_structure.py", text)

        scenario_sections = self.parse_heading_sections(public_guides[SCENARIOS], level=2)
        self.assertEqual(
            ["Runtime Authority", "Example 1: Explore", "Example 2: Accepted Image Concept"],
            [title for title, _ in scenario_sections],
        )

        self.assertFalse(TOMBSTONE.exists())

    def test_metadata_prompt_is_phase_neutral_and_aligned(self):
        metadata = METADATA.read_text(encoding="utf-8")
        match = re.search(r'^  default_prompt: "([^"]+)"$', metadata, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(
            "Use $product-composer to direct this UI and asset task, choose its phase and surface, "
            "and produce the appropriate evidence-backed outcome.",
            match.group(1),
        )
        self.assertNotIn("implement", match.group(1).casefold())
        self.assertNotIn("build", match.group(1).casefold())

    def test_runtime_does_not_maintain_itself(self):
        lowered = self.text.casefold()
        self.assertNotIn("skill loop", lowered)
        self.assertNotIn("improve this skill's routing", lowered)
        self.assertNotIn("repository maintenance", lowered)


if __name__ == "__main__":
    unittest.main()
