import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CrossAxisRoutingTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_frontmatter_materiality_and_ordinary_creation_exclusion(self):
        skill = self.read("SKILL.md")
        description = re.search(r'^description: "([^"]+)"$', skill, re.MULTILINE)
        self.assertIsNotNone(description)
        self.assertIn("materially affects the result", description.group(1))

        discovery = self.read("evals/discovery-scenarios.md")
        rows = [
            [cell.strip() for cell in line.strip("|").split("|")]
            for line in discovery.splitlines()
            if re.match(r"^\| D\d+ ", line)
        ]
        self.assertEqual(13, len(rows))
        self.assertEqual(
            [
                "D13",
                "Create a routine settings screen entirely within an established design system, with no art-direction or fidelity decision",
                "no",
            ],
            rows[-1],
        )

    def test_authorized_new_ui_has_a_legal_implement_route(self):
        skill = self.read("SKILL.md")
        implementation = self.read("references/implementation-fidelity.md")
        self.assertIn(
            "Entry intent: direction-only | implementation-authorized | rendered-repair | validation-only",
            skill,
        )
        self.assertIn(
            "| new UI or substantial-redesign implementation | implementation-authorized | Implement | references/direction-system.md plus references/implementation-fidelity.md |",
            skill,
        )
        self.assertIn("selected or inferred DirectionContract", skill)
        self.assertIn("complete Functional delta", skill)
        self.assertIn("before the first slice", skill)
        self.assertIn("does not require a pre-accepted concept", implementation)
        self.assertIn("complete Functional delta before the first slice", implementation)
        self.assertIn(
            "An explicit screenshot, reference-parity, or reference-fidelity implementation "
            "uses the accepted-concept path even when the referenced artifact is unavailable; "
            "do not open direction-system.md to replace it",
            skill,
        )

    def test_redesign_without_mutation_or_reference_authority_stays_explore(self):
        skill = self.read("SKILL.md")
        asset = self.read("references/asset-context.md")

        self.assertIn(
            "Create, design, or redesign alone selects direction-only Explore; "
            "Implement requires an explicit request to build, implement, edit target code, "
            "or otherwise mutate the target project",
            skill,
        )
        self.assertIn(
            "Preserving an existing design system, product workflow, or interaction convention "
            "does not add Reference-led",
            skill,
        )
        self.assertIn(
            "Reference-led requires a supplied or accepted visual reference, or an explicit "
            "parity or fidelity target",
            skill,
        )
        self.assertIn(
            "A missing target UI, source tree, or rendered baseline is a Frame or verification "
            "gap, not an Asset truth input unless the task supplies or explicitly requires it "
            "as a media artifact or proof object",
            skill,
        )
        self.assertIn(
            "Do not open Asset truth merely because a screenshot, render, or media object could "
            "be useful evidence",
            asset,
        )
        self.assertIn(
            "The task or selected direction must make that object material to proof, factual "
            "claims, accessibility, or composition",
            asset,
        )
        self.assertIn(
            "Direction-only Explore is not a change-producing output and stops without opening "
            "Verify",
            skill,
        )
        self.assertIn(
            "Acceptance reporting alone does not open Verify; keep future checks and named gaps "
            "in the Design Contract",
            skill,
        )

    def test_shared_owners_preserve_the_selected_surface_and_exact_r3(self):
        cultural = self.read("references/chinese-aesthetic.md")
        repair = self.read("references/repair-rendered-ui.md")
        implementation = self.read("references/implementation-fidelity.md")
        verification = self.read("references/verification.md")

        self.assertNotIn("Explore / Brand / Cultural", cultural)
        self.assertIn("selected Surface", cultural)
        self.assertNotIn("Repair / Brand window", repair)
        self.assertIn("selected Surface owner set", repair)
        self.assertIn("two active owners for Product or Brand and three for Hybrid", repair)

        self.assertIn(
            "exactly Implement / Product / Image + Reference-led",
            implementation,
        )
        self.assertIn("Every other Implement route", implementation)
        self.assertIn("selected Surface and Modifier owners", implementation)

        self.assertIn("Verify plus the selected Surface owners", verification)
        self.assertIn("three for Hybrid", verification)
        self.assertIn("sequential window of at most three", verification)
        self.assertIn("Never create a verification gap merely to avoid a required owner", verification)

    def test_data_modifier_requires_material_data_semantics(self):
        skill = self.read("SKILL.md")
        self.assertIn(
            "Add Data only when value or record semantics—such as comparison, monitoring, "
            "analysis, source, freshness, provenance, or risk—materially change decisions, "
            "states, or evidence",
            skill,
        )
        self.assertIn(
            "Dashboard work adds Data when its requested purpose is analytics, monitoring, "
            "comparison, provenance, or risk, because value and record semantics then define "
            "the surface",
            skill,
        )
        self.assertIn(
            "An analytics label on a generic workspace or onboarding flow alone does not "
            "add Data",
            skill,
        )
        self.assertIn(
            "A rendered-repair request resolves its baseline gate before inferring any "
            "Modifier",
            skill,
        )
        self.assertIn(
            "When task-scoped rendered evidence or the behavioral baseline is missing, "
            "stay in Repair plus the selected Surface with no inferred Modifiers",
            skill,
        )

    def test_missing_media_hands_off_to_asset_truth_without_a_file(self):
        asset = self.read("references/asset-context.md")
        brand = self.read("references/brand-experiences.md")
        image = self.read("references/image-concepts.md")
        cultural = self.read("references/chinese-aesthetic.md")
        implementation = self.read("references/implementation-fidelity.md")

        self.assertIn("Missing relevant media is itself an Asset truth input", asset)
        self.assertIn("even when no file exists", asset)
        for text in [brand, image, cultural]:
            with self.subTest(owner=text.splitlines()[0]):
                self.assertIn("hand off to Asset truth even when no file exists", text)
                self.assertNotIn("Do not open Asset truth while", text)
        self.assertIn("open Asset truth after the current window closes", implementation)
        self.assertIn("even when no file exists", implementation)
        self.assertIn("Open Verify only after", implementation)

    def test_touched_scanner_examples_use_a_runnable_src_argument(self):
        for relative_path in [
            "SKILL.md",
            "README.md",
            "README.zh-CN.md",
            "references/verification.md",
        ]:
            with self.subTest(path=relative_path):
                text = self.read(relative_path)
                self.assertIn("node scripts/ui-pattern-scan.mjs ./src", text)
                self.assertNotRegex(text, r"ui-pattern-scan\.mjs\s+<[^>]+>")


if __name__ == "__main__":
    unittest.main()
