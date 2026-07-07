import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillGuidanceStructureTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_skill_description_is_limited_to_ui_design_and_implementation(self):
        skill = self.read("SKILL.md")
        description = re.search(r'description: "([^"]+)"', skill).group(1)

        self.assertIn("creating or substantially redesigning UI", description)
        self.assertIn("controllable visual direction", description)
        for forbidden_trigger in [
            "critiquing",
            "Figma",
            "reference-to-code",
            "editable layer documents",
            "HTML previews",
        ]:
            self.assertNotIn(forbidden_trigger, description)

    def test_main_skill_keeps_review_and_restoration_out_of_primary_flow(self):
        skill = self.read("SKILL.md")

        self.assertIn("references/task-router.md", skill)
        self.assertNotIn("references/design-review-output.md", skill)
        for removed_scope in [
            "quick patch",
            "design review",
            "Figma",
            "reference-to-code",
            "layer document",
            "code edits",
        ]:
            self.assertNotIn(removed_scope, skill)

    def test_task_router_covers_core_design_and_implementation_modes(self):
        router = self.read("references/task-router.md")

        for work_mode in [
            "new UI design",
            "substantial redesign",
            "product app implementation",
            "brand/landing",
            "dashboard/data",
            "frontier interaction",
            "accepted concept",
            "image mockup",
        ]:
            self.assertRegex(router, re.compile(re.escape(work_mode), re.IGNORECASE))

        for forbidden_mode in ["quick patch", "design review", "Figma", "layer document"]:
            self.assertNotRegex(
                router,
                re.compile(rf"^\| {re.escape(forbidden_mode)} \|", re.IGNORECASE | re.MULTILINE),
            )

    def test_scenario_examples_cover_routing_contracts(self):
        scenarios_dir = ROOT / "examples" / "scenarios"
        scenario_files = sorted(scenarios_dir.glob("*.md"))
        self.assertGreaterEqual(len(scenario_files), 1)

        scenario_text = "\n".join(path.read_text(encoding="utf-8") for path in scenario_files)
        self.assertGreaterEqual(scenario_text.count("## Scenario"), 6)

        for section in ["User prompt", "Expected routing", "Output contract", "Acceptance checks"]:
            self.assertIn(section, scenario_text)

        for forbidden_scenario in ["Quick Patch", "Design Review", "Figma To Code", "Layer Document"]:
            self.assertNotIn(forbidden_scenario, scenario_text)

    def test_readmes_present_narrow_aesthetic_control_positioning(self):
        english = self.read("README.md")
        chinese = self.read("README.zh-CN.md")
        combined = f"{english}\n{chinese}"

        self.assertIn("not a general UI toolkit", english)
        self.assertIn("不是通用 UI 工具包", chinese)
        self.assertIn("aesthetic control", english)
        self.assertIn("审美控制", chinese)

        for removed_scope in [
            "Figma",
            "reference-to-code",
            "design review",
            "quick patch",
            "layer document",
            "HTML preview",
        ]:
            self.assertNotIn(removed_scope, combined)


if __name__ == "__main__":
    unittest.main()
