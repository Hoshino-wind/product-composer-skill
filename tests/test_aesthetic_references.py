import re
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DIRECTION_HEADINGS = [
    "Principle", "Contents", "Design Read", "Aesthetic Derivation", "Direction Contract",
    "Direction Parameters", "Style Families", "Taste Contract",
    "Shared Visual Grammar", "Composition Families", "Experience Architecture", "Direction Orthogonality",
    "Typography And Palette Judgment", "Generic-Default Test",
    "Override Conditions", "Quality Score", "Repair Selection",
    "Common Failures",
]

PRODUCT_HEADINGS = [
    "Principle", "Contents", "Priority Order",
    "Product Object And Task Order", "Navigation And Contextual Actions",
    "Forms Tables Filters And Drawers", "State And Permission Clarity",
    "Data Grammar", "Density And Content Judgment", "3D Eligibility Gate",
    "Technical Surface Rules", "Acceptance Checks",
]

BRAND_HEADINGS = [
    "Principle", "Contents", "Content-Truth Questions",
    "Reference-First Decision", "Website Archetype And Experience Scope",
    "Content And Region Model",
    "First-Viewport Contract",
    "Media Choreography Gate", "Product Proof And Belief Timing",
    "Page Rhythm And Continuation",
    "Desire Mechanisms", "Signature System", "Conversion Path",
    "Market Calibration Discipline", "Acceptance Checks",
]


class AestheticReferenceTests(unittest.TestCase):
    def parse_h2_sections(self, text):
        sections = []
        current_title = None
        current_lines = []
        fence_marker = None

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

            heading = None
            if fence_marker is None:
                heading = re.match(r"^ {0,3}##[ \t]+(.+?)\s*$", line)

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

    def assert_h2_structure(self, relative_path, expected_headings):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        sections = self.parse_h2_sections(text)
        actual_headings = [title for title, _ in sections]
        self.assertEqual(expected_headings, actual_headings)
        return dict(sections)

    def assert_terms(self, relative_path, terms):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        self.assertTrue(
            self.parse_h2_sections(text),
            "reference must contain real H2 sections outside fenced code blocks",
        )
        for term in terms:
            with self.subTest(path=relative_path, term=term):
                self.assertIn(term, text)

    def test_keyword_dump_does_not_satisfy_structure_contract(self):
        terms = [
            "Design read", "Visual thesis",
            "Composition variance", "Motion energy", "Information density",
            "Taste contract", "Style family", "Direction orthogonality",
            "Deletion rule", "dominant silhouette", "generic-default",
            "Override condition",
        ]
        collapsed = " ".join(terms) + "\n```markdown\n" + "\n".join([
            "## Principle", "## Contents", "## Design Read",
            "## Direction Contract", "## Direction Parameters",
        ]) + "\n```\n"

        for term in terms:
            self.assertIn(term, collapsed)

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "keyword-dump.md"
            path.write_text(collapsed, encoding="utf-8")
            with self.assertRaises(AssertionError):
                self.assert_terms(path, terms)
            with self.assertRaises(AssertionError):
                self.assert_h2_structure(path, DIRECTION_HEADINGS)

    def test_direction_system_preserves_art_direction_judgment(self):
        self.assert_terms("references/direction-system.md", [
            "Design read", "Visual thesis",
            "Aesthetic derivation", "attention strategy", "visual genre",
            "Composition variance", "Motion energy", "Information density",
            "Taste contract",
            "Style family",
            "Direction orthogonality",
            "Deletion rule",
            "dominant silhouette",
            "generic-default",
            "Override condition",
        ])

    def test_direction_system_has_required_h2_sections_once_in_order(self):
        self.assert_h2_structure(
            "references/direction-system.md",
            DIRECTION_HEADINGS,
        )

    def test_direction_contract_keeps_required_fields_in_its_section(self):
        sections = self.assert_h2_structure(
            "references/direction-system.md",
            DIRECTION_HEADINGS,
        )
        contract = sections["Direction Contract"]
        required_fields = [
            "Design read", "Visual thesis", "user mission",
            "aesthetic stance", "tension pair", "visual genre", "attention strategy",
            "dominant silhouette", "composition family",
            "experience architecture", "page rhythm and continuity",
            "Composition variance", "Motion energy", "Information density",
            "material language", "image-world thesis", "palette roles", "type roles",
            "signature detail", "justified risk", "restraint",
            "fixed anchors", "exploration axis",
            "anti-defaults", "Override condition", "Deletion rule",
        ]

        for field in required_fields:
            with self.subTest(field=field):
                occurrences = re.findall(
                    rf"(?m)^{re.escape(field)}:",
                    contract,
                )
                self.assertEqual(1, len(occurrences))

        anti_defaults = re.search(r"(?m)^anti-defaults:\s*(.+)$", contract)
        self.assertIsNotNone(anti_defaults)
        for relationship in [
            "pattern", "task context", "why weak", "override evidence",
        ]:
            self.assertIn(relationship, anti_defaults.group(1))
        self.assertRegex(contract, r"(?m)^Override condition:")

        derivation = sections["Aesthetic Derivation"]
        for term in [
            "source signal", "inferred meaning", "visible consequence",
            "affected DirectionContract field", "alternative rejected and why",
            "first focal point", "one tension pair", "artist, studio, or work name",
            "fixed anchors", "one exploration axis", "adjectives without visible consequences",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, derivation)

        grammar = sections["Shared Visual Grammar"]
        for term in [
            "UI consequence", "Image or asset consequence", "attention strategy",
            "dominant silhouette", "tension pair", "material language",
            "page rhythm and continuity", "fixed anchors and exploration axis",
            "Share causal rules, not a sticker layer",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, grammar)

        architecture = sections["Experience Architecture"]
        self.assertIn("Composition family describes relationships inside one region", architecture)
        self.assertIn("content beats, region geometry, interaction states, media, and handoffs", architecture)
        self.assertIn("A beat may be shorter than, equal to, or longer than a viewport", architecture)
        self.assertIn("Region geometry record", architecture)
        self.assertIn("incomplete if it shows only the first viewport", architecture)

    def test_direction_parameters_and_overrides_keep_their_relationships(self):
        sections = self.assert_h2_structure(
            "references/direction-system.md",
            DIRECTION_HEADINGS,
        )
        parameters = sections["Direction Parameters"]

        self.assertRegex(
            parameters,
            r"(?m)^\| Parameter \| 1 \| 3 \| 5 \| Infer from \|$",
        )
        for parameter, one, three, five in [
            ("Composition variance", "stable", "balanced", "expressive"),
            ("Motion energy", "static", "responsive", "choreographed"),
            ("Information density", "sparse", "balanced", "compressed"),
        ]:
            with self.subTest(parameter=parameter):
                self.assertRegex(
                    parameters,
                    re.compile(
                        rf"^\| {re.escape(parameter)} \| {one} \| {three} \| {five} \|",
                        re.MULTILINE,
                    ),
                )

        self.assertRegex(
            parameters,
            re.compile(r"\bno (?:global|universal) default\b", re.IGNORECASE),
        )
        self.assertRegex(
            parameters,
            re.compile(
                r"\b(?:do not|must not|never)\b[^\n]*\broute axes\b",
                re.IGNORECASE,
            ),
        )

        generic_default = sections["Generic-Default Test"]
        table_rows = [
            line for line in generic_default.splitlines() if line.startswith("|")
        ]
        self.assertGreaterEqual(len(table_rows), 3)
        header = [cell.strip() for cell in table_rows[0].strip("|").split("|")]
        self.assertEqual([
            "Anti-default",
            "Task context that makes it weak",
            "Required override evidence",
        ], header)
        for row in table_rows[2:]:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            self.assertEqual(3, len(cells))
            self.assertTrue(all(cells))

        override = sections["Override Conditions"]
        self.assertIn("Override condition", override)
        self.assertIn("evidence predicate", override)
        self.assertIn("contract fields it changes", override)

    def test_product_surfaces_prioritize_real_work(self):
        self.assert_terms("references/product-surfaces.md", [
            "task correctness -> interaction clarity -> information architecture -> visual expression",
            "natural task order",
            "certainty",
            "contextual actions",
            "dense-with-air",
            "Data grammar",
            "3D eligibility gate",
        ])

    def test_product_surfaces_has_required_h2_sections_once_in_order(self):
        self.assert_h2_structure(
            "references/product-surfaces.md",
            PRODUCT_HEADINGS,
        )

    def test_product_priority_and_3d_gate_are_section_bound(self):
        sections = self.assert_h2_structure(
            "references/product-surfaces.md",
            PRODUCT_HEADINGS,
        )
        priority = sections["Priority Order"]
        self.assertEqual(
            "task correctness -> interaction clarity -> information architecture -> visual expression",
            priority.splitlines()[0],
        )

        gate = sections["3D Eligibility Gate"]
        self.assertIn("all three conditions are true", gate)
        for condition in [
            r"user task depends on spatial geometry",
            r"readings or controls anchor to real regions",
            r"assets and performance permit[^\n]*\b3D\b",
        ]:
            with self.subTest(condition=condition):
                self.assertRegex(gate, re.compile(condition, re.IGNORECASE))
        self.assertRegex(
            gate,
            re.compile(
                r"^If any condition fails, select tables, comparison, charts, maps, or calm native product UI\.",
                re.MULTILINE,
            ),
        )

    def test_brand_experiences_preserve_proof_and_desire(self):
        self.assert_terms("references/brand-experiences.md", [
            "first-viewport",
            "product proof",
            "reason to continue",
            "desire mechanism",
            "signature system",
            "Content And Region Model",
            "Content-truth questions",
            "Audience", "Proof", "Trust", "Next action or continuation",
            "Do not invent metrics",
        ])

    def test_brand_experiences_has_required_h2_sections_once_in_order(self):
        self.assert_h2_structure(
            "references/brand-experiences.md",
            BRAND_HEADINGS,
        )

    def test_brand_truth_reference_and_region_rules_are_section_bound(self):
        sections = self.assert_h2_structure(
            "references/brand-experiences.md",
            BRAND_HEADINGS,
        )
        truth = sections["Content-Truth Questions"]
        for label in [
            "Introduced", "Audience", "Core content object", "Proof", "Trust",
            "Next action or continuation",
        ]:
            with self.subTest(label=label):
                self.assertEqual(
                    1,
                    len(re.findall(rf"(?m)^- {re.escape(label)}:", truth)),
                )
        self.assertRegex(truth, r"(?m)^- Introduced: What or who ")
        self.assertIn(
            "Do not invent metrics, testimonials, clients, links, awards, project outcomes",
            truth,
        )
        for term in [
            "keep the selected Hybrid Surface",
            "close the current window",
            "hand off to Asset truth even when no file exists",
            "resume from the updated Design Contract",
            "without replacing Product or Brand ownership",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, truth)
        self.assertNotIn("Do not open Asset truth while", truth)

        reference_first = sections["Reference-First Decision"]
        self.assertIn("follow it before offering alternatives", reference_first)
        self.assertIn("complete route from opener to footer or interaction endpoint", reference_first)
        self.assertIn("Case trace", reference_first)
        self.assertIn("rare, well-observed mechanism", reference_first)
        self.assertIn(
            "Offer `2–3` previews only when direction is genuinely unresolved.",
            reference_first,
        )

        choreography = sections["Media Choreography Gate"]
        ordered_steps = [
            "`website archetype and route scope`", "`content beats`",
            "`region geometry and scroll model`", "`media palette and many-to-many mapping`",
            "`motion grammar and per-region choreography`",
            "`typographic voice and interaction`", "`implementation`",
        ]
        positions = [choreography.index(step) for step in ordered_steps]
        self.assertEqual(sorted(positions), positions)
        for term in [
            "One content beat may use no external media or several synchronized media",
            "One asset may persist through several beats",
            "screen count or independent-source count",
            "Media choreography record", "semantic text",
            "poster, loading, failure, reduced-motion, and static fallback",
        ]:
            with self.subTest(term=term):
                self.assertIn(term, choreography)

        region_model = sections["Content And Region Model"]
        self.assertIn(
            "A beat may be shorter than, equal to, or longer than a viewport.",
            region_model,
        )
        self.assertIn("Experience architecture", region_model)
        self.assertIn("Region record", region_model)
        self.assertIn("intrinsic | subviewport | viewport | overviewport/pinned", region_model)
        scope = sections["Website Archetype And Experience Scope"]
        self.assertIn("opener or hero", scope)
        self.assertIn("route or page experience", scope)
        self.assertIn("multi-route website", scope)
        self.assertIn("Hero does not mean one `100vh` section", scope)
        self.assertIn("PC-only", scope)

if __name__ == "__main__":
    unittest.main()
