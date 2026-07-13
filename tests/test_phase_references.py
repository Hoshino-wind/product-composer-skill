import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


IMPLEMENTATION_HEADINGS = [
    "Principle",
    "Contents",
    "Functional delta",
    "Direction lock",
    "Design memory",
    "Artifact target and maturity",
    "Maturity claim rules",
    "Implementation inventory",
    "Locked/adaptable rules",
    "Change ledger",
    "Parity slices",
    "Target-device adaptation",
    "Final parity note",
]

REPAIR_HEADINGS = [
    "Principle",
    "Contents",
    "Baseline evidence",
    "Loop budget",
    "Diagnosis",
    "Repair axes",
    "Patch one vertical slice",
    "Verification",
    "Decision protocol",
    "Stop conditions",
    "Output shape",
]

VERIFICATION_HEADINGS = [
    "Principle",
    "Contents",
    "Command discovery",
    "Functional checks",
    "State checks",
    "Accessibility checks",
    "Target-device and localization checks",
    "Visual checks",
    "Concept parity",
    "Scanner",
    "Evidence classes",
    "Artifact maturity",
    "Evidence report",
    "Verification gaps",
]


class PhaseReferenceTests(unittest.TestCase):
    def read_sections(self, name, expected_headings):
        text = (ROOT / "references" / name).read_text(encoding="utf-8")
        sections = self.parse_h2_sections(text)
        self.assertEqual(
            expected_headings,
            [title for title, _ in sections],
            f"{name} must preserve the phase contract as ordered H2 sections",
        )
        return text, dict(sections)

    def parse_h2_sections(self, text):
        sections = []
        current_title = None
        current_lines = []
        fence_marker = None

        for line in text.splitlines():
            fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if fence:
                marker = fence.group(1)
                trailing_content = fence.group(2)
                marker_character = marker[0]
                marker_length = len(marker)
                if fence_marker is None:
                    fence_marker = (marker_character, marker_length)
                elif (
                    fence_marker[0] == marker_character
                    and marker_length >= fence_marker[1]
                    and not trailing_content.strip()
                ):
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

    def parse_markdown_table(self, section):
        rows = []
        for line in section.splitlines():
            stripped = line.strip()
            if not (stripped.startswith("|") and stripped.endswith("|")):
                continue
            cells = []
            current = []
            escaped = False
            for character in stripped[1:-1]:
                if escaped:
                    current.append(character)
                    escaped = False
                elif character == "\\":
                    escaped = True
                elif character == "|":
                    cells.append("".join(current).strip())
                    current = []
                else:
                    current.append(character)
            if escaped:
                current.append("\\")
            cells.append("".join(current).strip())
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            rows.append(cells)

        self.assertGreaterEqual(len(rows), 2, "expected a header and data rows")
        width = len(rows[0])
        self.assertTrue(
            all(len(row) == width for row in rows),
            "every table row must preserve the header width",
        )
        return rows[0], rows[1:]

    def assert_labeled_record(self, section, expected_fields):
        fields = re.findall(
            r"^\s*-\s*([^:\r\n]+):\s*(.*?)\s*$",
            section,
            re.MULTILINE,
        )
        names = [name.strip() for name, _ in fields]
        self.assertEqual(
            expected_fields,
            names,
            "labeled record fields must be complete and in causal order",
        )
        self.assertEqual(len(names), len(set(names)), "record fields must be unique")
        record = {}
        for name, value in fields:
            name = name.strip()
            with self.subTest(field=name):
                self.assertTrue(value.strip(), f"{name!r} must have a relationship value")
            record[name] = value.strip()
        return record

    def assert_terms(self, section, terms):
        for term in terms:
            with self.subTest(term=term):
                self.assertIn(term, section)

    def assert_unique_keyed_table(
        self,
        section,
        expected_header,
        expected_keys,
        required_nonempty_columns,
    ):
        header, rows = self.parse_markdown_table(section)
        self.assertEqual(expected_header, header)
        keys = [row[0] for row in rows]
        self.assertEqual(
            expected_keys,
            keys,
            "keyed table rows must be complete and in contract order",
        )
        self.assertEqual(len(keys), len(set(keys)), "table keys must be unique")
        column_indexes = [header.index(column) for column in required_nonempty_columns]
        for row in rows:
            with self.subTest(key=row[0]):
                for index in column_indexes:
                    self.assertTrue(
                        row[index].strip(),
                        f"{row[0]!r} must define {header[index]!r}",
                    )
        return {row[0]: dict(zip(header[1:], row[1:])) for row in rows}

    def test_h2_parser_requires_matching_fence_marker_and_opening_length(self):
        text = "\n".join([
            "````markdown",
            "## Hidden inside long fence",
            "```",
            "## Still hidden after short fence",
            "~~~~",
            "## Still hidden after other marker",
            "````",
            "## Visible",
            "visible body",
        ])

        self.assertEqual(
            [("Visible", "visible body")],
            self.parse_h2_sections(text),
        )

    def test_h2_parser_rejects_closing_fence_with_trailing_content(self):
        text = "\n".join([
            "````markdown",
            "## Hidden before false close",
            "````not-a-closing-fence",
            "## Hidden after false close",
            "````",
            "## Visible",
            "visible body",
        ])

        self.assertEqual(
            [("Visible", "visible body")],
            self.parse_h2_sections(text),
        )

    def test_implementation_requires_functional_delta(self):
        _, sections = self.read_sections(
            "implementation-fidelity.md",
            IMPLEMENTATION_HEADINGS,
        )

        functional_rows = self.assert_unique_keyed_table(
            sections["Functional delta"],
            ["Functional delta", "Required record", "Acceptance evidence"],
            [
                "Workflow",
                "Data",
                "Permissions",
                "Error recovery",
                "Irreversible actions",
                "Accessibility",
            ],
            ["Required record", "Acceptance evidence"],
        )
        self.assertIn("user-visible transition", functional_rows["Workflow"]["Required record"])
        self.assertIn("source of truth", functional_rows["Data"]["Required record"])
        self.assertIn("authorization", functional_rows["Permissions"]["Required record"])
        self.assertIn("rollback", functional_rows["Irreversible actions"]["Required record"])

        self.assert_terms(sections["Direction lock"], ["Locked", "Adaptable"])
        self.assertIn("Design memory", sections["Design memory"])
        self.assertIn("Change ledger", sections["Change ledger"])
        self.assertIn("Parity slices", sections["Parity slices"])

        self.assert_unique_keyed_table(
            sections["Change ledger"],
            ["Decision", "Baseline", "Implemented delta", "Evidence", "Owner"],
            ["direction", "workflow", "data", "target-device", "accessibility"],
            ["Baseline", "Implemented delta", "Evidence", "Owner"],
        )
        self.assert_unique_keyed_table(
            sections["Parity slices"],
            ["Parity slice", "Behavior", "State", "Viewport", "Evidence", "Status"],
            ["primary task", "critical recovery", "permission boundary"],
            ["Behavior", "State", "Viewport", "Evidence", "Status"],
        )

    def test_blocked_implementation_preserves_selected_route_and_exact_r3(self):
        _, sections = self.read_sections(
            "implementation-fidelity.md",
            IMPLEMENTATION_HEADINGS,
        )

        self.assert_terms(sections["Functional delta"], [
            "An implementation-authorized new UI does not require a pre-accepted concept",
            "selected or explicitly inference-authorized `DirectionContract`",
            "complete Functional delta before the first slice",
            "For accepted-concept work, stop if the concept is unavailable",
            "selected Implement / Surface / Modifier window",
            "exactly Implement / Product / Image + Reference-led",
            "Every other Implement route",
            "selected Surface and Modifier owners",
            "Record Asset truth and Verify needs as named gaps",
            "open Asset truth after the current window closes",
            "missing media materially constrains proof, claims, accessibility, or composition",
            "even when no file exists",
            "Open Verify only after the required verifiable input or environment exists",
        ])

    def test_artifact_maturity_claims_are_evidence_gated(self):
        _, sections = self.read_sections(
            "implementation-fidelity.md",
            IMPLEMENTATION_HEADINGS,
        )
        maturity = sections["Artifact target and maturity"]
        rows = self.assert_unique_keyed_table(
            maturity,
            ["Artifact target", "Allowed claim", "Matching evidence", "Promotion boundary"],
            ["recipe", "preview", "runnable starter", "tested golden", "template"],
            ["Allowed claim", "Matching evidence", "Promotion boundary"],
        )
        self.assert_terms(rows["recipe"]["Allowed claim"], ["non-runnable", "direction metadata"])
        self.assert_terms(rows["preview"]["Allowed claim"], ["visual evidence", "without behavior claims"])
        self.assert_terms(rows["runnable starter"]["Allowed claim"], ["executable skeleton", "basic interaction"])
        self.assert_terms(rows["tested golden"]["Matching evidence"], [
            "named scenario", "applicable acceptance checks", "runtime", "rendered evidence",
        ])
        self.assert_terms(rows["template"]["Matching evidence"], [
            "manifest", "entrypoint", "replaceable-input contract",
            "origin/license record", "smoke test", "rendered evidence",
        ])

        rules = sections["Maturity claim rules"]
        self.assertIn("Do not promote an artifact without matching evidence.", rules)
        self.assertIn("A recipe or preview must not be described as a production template.", rules)

    def test_repair_is_surface_only_and_evidence_driven(self):
        text, sections = self.read_sections(
            "repair-rendered-ui.md",
            REPAIR_HEADINGS,
        )
        self.assertNotIn("skill loop", text.lower())
        self.assertNotIn("routing/references/tests", text.lower())

        self.assert_terms(sections["Baseline evidence"], [
            "rendered evidence", "behavioral baseline", "target project",
            "scenario", "viewport", "known gap",
        ])
        self.assertIn("one repair axis", sections["Loop budget"])
        axes = self.assert_unique_keyed_table(
            sections["Repair axes"],
            ["Repair axis", "Diagnose", "Patch boundary", "Verify with"],
            ["shape", "arrange", "typeset", "colorize", "distill", "harden", "asset", "motion"],
            ["Diagnose", "Patch boundary", "Verify with"],
        )
        self.assertIn("hierarchy", axes["shape"]["Diagnose"])
        self.assertIn("reading order", axes["arrange"]["Diagnose"])
        self.assertIn("reduced motion", axes["motion"]["Verify with"])

        decisions = [
            "Continue: [next weakest axis] because [new evidence]",
            "Stop: contract satisfied because [evidence]",
            "Escalate: design contract must change because [reason]",
            "Block: verification cannot run because [missing input or environment]",
            "Handoff: [Implementation or responsible owner] because [functional baseline failed, post-patch baseline was not restored, or repair budget exhausted with verified defect remaining]",
        ]
        decision_lines = {
            line.strip()
            for line in sections["Decision protocol"].splitlines()
            if line.strip()
        }
        for decision in decisions:
            with self.subTest(decision=decision):
                self.assertIn(decision, decision_lines)
        self.assert_terms(
            sections["Stop conditions"],
            ["Continue", "Stop", "Escalate", "Block", "Handoff"],
        )

    def test_repair_without_task_scoped_baseline_selects_no_axis_and_blocks(self):
        _, sections = self.read_sections(
            "repair-rendered-ui.md",
            REPAIR_HEADINGS,
        )
        self.assert_terms(sections["Baseline evidence"], [
            "Until both task-scoped rendered evidence and a behavioral baseline exist",
            "select no repair axis",
            "not even provisionally or tentatively",
            "make no diagnosis",
            "Block and name the missing evidence",
            "missing-baseline Block stays inside Repair plus the selected Surface owner set",
            "two active owners for Product or Brand and three for Hybrid",
            "Do not open Verify when the baseline is missing",
            "record verification as a later gap",
            "Before opening any Stage or Gate owner or searching the workspace",
            "determine whether the request supplies both task-scoped rendered evidence and a behavioral baseline",
            "If either input is absent, stop owner selection immediately",
            "do not search the checkout or temporary directories",
            "Block from the Repair / Surface owners alone",
        ])

    def test_repair_iteration_record_preserves_the_causal_chain(self):
        _, sections = self.read_sections(
            "repair-rendered-ui.md",
            REPAIR_HEADINGS,
        )
        iteration = self.assert_labeled_record(
            sections["Patch one vertical slice"],
            [
                "entry functional gate",
                "selected repair axis",
                "bounded vertical slice",
                "baseline scenario",
                "baseline viewport",
                "rerun scenario",
                "rerun viewport",
                "evidence",
                "decision",
            ],
        )
        self.assert_terms(iteration["entry functional gate"], [
            "pass with behavioral evidence",
            "Handoff to Implementation",
        ])
        self.assertIn("exactly one", iteration["selected repair axis"])
        self.assertIn("one", iteration["bounded vertical slice"])
        self.assertIn("same as baseline scenario", iteration["rerun scenario"])
        self.assertIn("same as baseline viewport", iteration["rerun viewport"])
        self.assert_terms(iteration["evidence"], ["behavioral", "rendered"])
        self.assert_terms(iteration["decision"], [
            "exactly one", "Continue", "Stop", "Escalate", "Block", "Handoff",
        ])

        rerun = self.assert_unique_keyed_table(
            sections["Verification"],
            ["Rerun relationship", "Baseline", "Required match", "New evidence"],
            ["scenario", "viewport", "behavior", "rendered surface"],
            ["Baseline", "Required match", "New evidence"],
        )
        self.assertIn("same named scenario", rerun["scenario"]["Required match"])
        self.assertIn("same viewport", rerun["viewport"]["Required match"])
        self.assertIn("behavioral evidence", rerun["behavior"]["New evidence"])
        self.assertIn("rendered evidence", rerun["rendered surface"]["New evidence"])

    def test_repair_decisions_are_exhaustive_and_handoff_out_of_scope_work(self):
        _, sections = self.read_sections(
            "repair-rendered-ui.md",
            REPAIR_HEADINGS,
        )
        protocol = sections["Decision protocol"]
        decisions = self.assert_unique_keyed_table(
            protocol,
            ["Decision", "Select when", "Required record", "Forbidden claim"],
            ["Continue", "Stop", "Escalate", "Block", "Handoff"],
            ["Select when", "Required record", "Forbidden claim"],
        )
        self.assert_terms(decisions["Continue"]["Select when"], [
            "repair budget remains",
            "verified surface defect remains",
            "no post-patch regression is active",
            "same functional baseline was restored",
        ])
        self.assertIn("budget is exhausted", decisions["Continue"]["Forbidden claim"])
        self.assertIn("unreverted regression", decisions["Continue"]["Forbidden claim"])
        self.assertIn("contract is satisfied", decisions["Stop"]["Select when"])
        self.assertIn("remaining defect", decisions["Stop"]["Forbidden claim"])
        self.assertIn("design contract must change", decisions["Escalate"]["Select when"])
        self.assert_terms(decisions["Block"]["Select when"], [
            "verification cannot run", "missing input or environment",
        ])
        self.assert_terms(decisions["Handoff"]["Select when"], [
            "entry functional baseline fails",
            "repair budget is exhausted",
            "verified surface defect remains",
            "post-patch regression cannot be reverted",
            "functional baseline cannot be restored",
        ])
        self.assert_terms(decisions["Handoff"]["Required record"], [
            "Implementation with behavioral evidence",
            "responsible owner for budget or authority",
            "failure evidence",
            "rollback evidence",
        ])
        self.assertIn(
            "Select exactly one decision; the five states are mutually exclusive and exhaustive for Repair.",
            protocol,
        )

        handoffs = self.assert_unique_keyed_table(
            sections["Stop conditions"],
            ["Handoff case", "Required owner", "Evidence to preserve", "Must not claim"],
            [
                "entry functional baseline fails",
                "post-patch regression not restored",
                "budget exhausted with verified surface defect",
            ],
            ["Required owner", "Evidence to preserve", "Must not claim"],
        )
        self.assertIn("Implementation", handoffs["entry functional baseline fails"]["Required owner"])
        self.assertIn(
            "Implementation or responsible owner",
            handoffs["post-patch regression not restored"]["Required owner"],
        )
        self.assert_terms(
            handoffs["post-patch regression not restored"]["Evidence to preserve"],
            ["failure evidence", "rollback evidence", "baseline rerun"],
        )
        self.assertIn(
            "Continue Repair",
            handoffs["post-patch regression not restored"]["Must not claim"],
        )
        self.assertIn(
            "budget or authority",
            handoffs["budget exhausted with verified surface defect"]["Required owner"],
        )

    def test_repair_rolls_back_post_patch_regression_before_decision(self):
        _, sections = self.read_sections(
            "repair-rendered-ui.md",
            REPAIR_HEADINGS,
        )
        verification = sections["Verification"]
        rollback = self.assert_labeled_record(
            verification,
            [
                "regression observed",
                "affected behavior",
                "patch reverted",
                "baseline rerun",
                "baseline restored",
                "failure evidence",
                "rollback evidence",
                "next owner or decision",
            ],
        )
        self.assert_terms(rollback["regression observed"], [
            "current bounded slice", "functional", "data", "permission", "accessibility",
        ])
        self.assertIn("same functional baseline", rollback["affected behavior"])
        self.assert_terms(rollback["patch reverted"], [
            "stop Repair", "revert the current bounded slice",
        ])
        self.assert_terms(rollback["baseline rerun"], [
            "same functional baseline", "after rollback",
        ])
        self.assertIn("yes or no", rollback["baseline restored"])
        self.assertIn("regression", rollback["failure evidence"])
        self.assert_terms(rollback["rollback evidence"], ["revert", "baseline rerun"])
        self.assert_terms(rollback["next owner or decision"], [
            "restored and repair budget remains -> Continue",
            "restored and repair budget is exhausted -> Handoff",
            "cannot revert or restore -> Handoff to Implementation or responsible owner",
        ])
        self.assertIn(
            "Complete the Rollback record before selecting a decision.",
            verification,
        )

    def test_verification_covers_public_behavior_and_visual_quality(self):
        _, sections = self.read_sections("verification.md", VERIFICATION_HEADINGS)

        self.assert_terms(sections["Functional checks"], ["Workflow", "Data", "behavioral evidence"])
        self.assert_terms(sections["State checks"], ["loading", "empty", "error", "permission"])
        self.assert_terms(sections["Accessibility checks"], [
            "keyboard", "focus order", "semantic structure", "touch target", "reduced motion",
        ])
        self.assert_terms(sections["Target-device and localization checks"], [
            "declared target-device scope", "PC-only", "long text",
        ])
        self.assertIn("visual parity", sections["Visual checks"])
        self.assertIn("scanner warnings are evidence prompts", sections["Scanner"])

        evidence = sections["Evidence classes"]
        evidence_rows = self.assert_unique_keyed_table(
            evidence,
            ["Evidence class", "Proves", "Does not prove", "Required locator"],
            [
                "behavioral evidence",
                "rendered evidence",
                "structural evidence",
                "provenance evidence",
                "judgment evidence",
                "verification gap",
            ],
            ["Proves", "Does not prove", "Required locator"],
        )
        self.assertIn("workflow", evidence_rows["behavioral evidence"]["Proves"])
        self.assertIn("rendered result", evidence_rows["rendered evidence"]["Proves"])
        self.assertIn("origin", evidence_rows["provenance evidence"]["Proves"])
        for hard_rule in [
            "Map every acceptance check to exactly one evidence class.",
            "Screenshots do not prove workflow behavior.",
            "Source inspection does not prove rendering.",
            "Static strings do not prove aesthetic quality.",
            "Inference is not evidence.",
            "Runtime browser/device evidence belongs to the target project verification loop; package CI must not pretend it rendered a project it did not run.",
        ]:
            with self.subTest(hard_rule=hard_rule):
                self.assertIn(hard_rule, evidence)

        maturity_rows = self.assert_unique_keyed_table(
            sections["Artifact maturity"],
            ["Artifact target", "Minimum verification", "Forbidden overclaim"],
            ["recipe", "preview", "runnable starter", "tested golden", "template"],
            ["Minimum verification", "Forbidden overclaim"],
        )
        self.assertIn("behavior claims", maturity_rows["preview"]["Forbidden overclaim"])
        self.assertIn("runtime and rendered evidence", maturity_rows["tested golden"]["Minimum verification"])
        self.assert_terms(sections["Artifact maturity"], [
            "Verify plus the selected Surface owners",
            "two active owners for Product or Brand and three for Hybrid",
            "sequential window of at most three",
            "Never create a verification gap merely to avoid a required owner",
            "A supplied static preview is validation evidence input, not Image work",
            "does not activate the Image modifier or open image-concepts.md",
            "explicitly asks to generate, direct, or repair imagery",
            "When a validation-only overclaim prompt includes an existing, missing, or inaccessible preview, choose Asset truth as the claim owner",
            "The maturity table already covers template and tested-golden packaging/runtime gaps",
            "open implementation-fidelity.md in a later window only when an implementation-owned claim needs evidence beyond this table",
            "Route and owner selection precede all modifier-owner loading",
            "Do not open image-concepts.md merely to decide whether a supplied static preview counts as Image",
            "Static preview plus validation-only intent resolves that decision before reference loading",
        ])
        self.assertIn(
            "node scripts/ui-pattern-scan.mjs ./src",
            sections["Scanner"],
        )

        self.assert_unique_keyed_table(
            sections["Evidence report"],
            ["Acceptance check", "Evidence class", "Evidence locator", "Result", "Notes"],
            ["[exact acceptance check]"],
            ["Evidence class", "Evidence locator", "Result", "Notes"],
        )
        self.assertIn("verification gap", sections["Verification gaps"])

    def test_verification_discovers_repo_local_commands_and_reports_not_run(self):
        _, sections = self.read_sections("verification.md", VERIFICATION_HEADINGS)
        command_section = sections["Command discovery"]
        record = self.assert_labeled_record(
            command_section,
            [
                "repo-local instructions",
                "repo-local manifests",
                "repo-local scripts",
                "selected command",
                "working directory",
                "scenario and environment",
                "run status",
                "evidence locator",
                "Not run reason",
                "decision",
            ],
        )
        self.assertIn("Pass, Fail, or Not run", record["run status"])
        self.assertIn("missing input or environment", record["Not run reason"])
        self.assertIn("omit non-applicable checks", record["Not run reason"])
        self.assertIn("Block", record["decision"])

        statuses = self.assert_unique_keyed_table(
            command_section,
            ["Run status", "Meaning", "Required record", "Allowed decision"],
            ["Pass", "Fail", "Not run"],
            ["Meaning", "Required record", "Allowed decision"],
        )
        self.assertIn("do not relabel", statuses["Fail"]["Allowed decision"])
        self.assertIn("missing input or environment", statuses["Not run"]["Required record"])
        self.assertIn("Block", statuses["Not run"]["Allowed decision"])

    def test_verification_functional_checks_preserve_the_complete_delta(self):
        _, sections = self.read_sections("verification.md", VERIFICATION_HEADINGS)
        rows = self.assert_unique_keyed_table(
            sections["Functional checks"],
            ["Functional check", "Required observation", "Behavioral evidence", "Failure owner"],
            ["Workflow", "Data", "Permissions", "Error recovery", "Irreversible actions"],
            ["Required observation", "Behavioral evidence", "Failure owner"],
        )
        self.assertIn("user-visible transition", rows["Workflow"]["Required observation"])
        self.assertIn("source of truth", rows["Data"]["Required observation"])
        self.assertIn("authorization", rows["Permissions"]["Required observation"])
        self.assertIn("recovered state", rows["Error recovery"]["Required observation"])
        self.assertIn("rollback", rows["Irreversible actions"]["Required observation"])

    def test_verification_concept_parity_record_is_traceable(self):
        _, sections = self.read_sections("verification.md", VERIFICATION_HEADINGS)
        record = self.assert_labeled_record(
            sections["Concept parity"],
            [
                "locked decision",
                "adaptable mechanic",
                "change ledger entry",
                "parity slice",
                "parity evidence",
                "decision owner",
            ],
        )
        self.assertIn("DirectionContract field", record["locked decision"])
        self.assertIn("engineering constraint", record["adaptable mechanic"])
        self.assert_terms(record["change ledger entry"], ["baseline", "delta", "owner"])
        self.assert_terms(record["parity evidence"], [
            "same scenario", "same viewport", "behavioral", "rendered",
        ])


if __name__ == "__main__":
    unittest.main()
