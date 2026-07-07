import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillGuidanceStructureTests(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_main_skill_routes_to_optimization_references(self):
        skill = self.read("SKILL.md")

        self.assertIn("references/task-router.md", skill)
        self.assertIn("references/design-review-output.md", skill)

    def test_design_review_output_contract_exists(self):
        review = self.read("references/design-review-output.md")

        for severity in ["Blocking", "Major", "Minor", "Polish", "Verification"]:
            self.assertIn(severity, review)

        self.assertIn("Findings", review)
        self.assertIn("What to change", review)

    def test_task_router_covers_common_work_modes(self):
        router = self.read("references/task-router.md")

        for work_mode in [
            "quick patch",
            "design review",
            "Figma",
            "image mockup",
            "accepted concept",
            "layer document",
            "full redesign",
            "existing system",
        ]:
            self.assertRegex(router, re.compile(re.escape(work_mode), re.IGNORECASE))

    def test_scenario_examples_cover_routing_contracts(self):
        scenarios_dir = ROOT / "examples" / "scenarios"
        scenario_files = sorted(scenarios_dir.glob("*.md"))
        self.assertGreaterEqual(len(scenario_files), 1)

        scenario_text = "\n".join(path.read_text(encoding="utf-8") for path in scenario_files)
        self.assertGreaterEqual(scenario_text.count("## Scenario"), 8)

        for section in ["User prompt", "Expected routing", "Output contract", "Acceptance checks"]:
            self.assertIn(section, scenario_text)


if __name__ == "__main__":
    unittest.main()
