import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPILER = ROOT / "scripts" / "compile-image-prompt.py"


def valid_contract():
    return {
        "direction": {
            "thesis": "以克制的空间张力承载可信的产品证据",
            "aestheticStance": ["克制", "精密", "有呼吸感"],
            "tensionPair": "工程秩序与材料诗意并置，工程秩序占主导",
            "visualGenre": "一座真实可制造的清晨材料实验室",
            "attentionStrategy": ["先看到产品轮廓", "随后进入右侧操作区"],
            "dominantSilhouette": "低矮横向设备被一条垂直隔断切出可识别缺口",
            "compositionFamily": "object portrait",
            "world": "清晨的半透明材料实验室，真实可制造",
            "camera": ["与产品齐平的视点", "保留右侧负空间"],
            "light": "左后方大面积柔光，操作区保持清晰对比",
            "material": "磨砂再生铝与轻微使用痕迹",
            "color": "石墨灰为结构色，低饱和青色只标示可操作状态",
        },
        "asset": {
            "familyId": "hero-product-world",
            "id": "hero-product-01",
            "promptContractVersion": "1.0",
            "parentId": "hero-product-master",
            "stateId": "capturing",
            "transition": {
                "fromState": "rest",
                "event": "用户开始录制",
                "toState": "capturing",
                "handoffFrame": "设备接口灯刚亮起，环境仍保持安静",
            },
            "role": "首屏产品世界观与真实主体之间的过渡资产",
            "maturity": "production candidate",
            "truthBoundary": "只可建立氛围与产品轮廓，不得建立性能、客户或认证事实",
            "medium": "写实产品摄影",
            "intendedUse": "桌面端首屏背景，承载左侧主体与右侧标题",
            "subject": "一台没有虚构标识的模块化桌面设备",
            "scene": "半透明隔断围合的材料实验台",
            "action": "接口灯由暗转亮，设备和环境保持静止",
            "targetRegion": "homepage.hero",
            "aspectRatio": "16:9",
            "focalPoint": "左侧 38% 处的设备接口缺口",
            "composition": "低机位横向物像肖像，主体与右侧标题形成不对称平衡",
            "depthOrder": "前景留空，中景设备清晰，背景隔断柔化",
            "cropBehavior": "窄裁切时保留接口缺口和右侧标题安全区",
            "safeArea": ["右侧 36% 不放置高对比物体", "顶部导航区保持安静"],
            "variants": [
                {
                    "id": "desktop-wide",
                    "targetRegion": "homepage.hero.desktop",
                    "aspectRatio": "16:9",
                    "focalPoint": "左侧 38% 处的设备接口缺口",
                    "composition": "完整横向产品肖像",
                    "depthOrder": "前景留空，中景设备，背景隔断",
                    "cropBehavior": "保留完整设备轮廓和右侧标题区",
                    "safeArea": "右侧 36% 保持安静",
                },
                {
                    "id": "mobile-portrait",
                    "targetRegion": "homepage.hero.mobile",
                    "aspectRatio": "4:5",
                    "focalPoint": "设备接口缺口",
                    "composition": "接口缺口主导的纵向局部肖像",
                    "depthOrder": "中景设备，背景隔断弱化",
                    "cropBehavior": "纵向裁切保留缺口，背景隔断可移出画面",
                    "safeArea": "顶部 24% 保持低对比",
                },
            ],
            "fixedAnchors": [
                "设备轮廓和接口位置不变",
                "石墨灰主体材料不变",
                "主光始终来自左后方",
            ],
            "explorationAxis": {
                "variable": "focal-scale",
                "name": "主体尺度",
                "allowedValues": ["占画面宽度 38%", "占画面宽度 46%"],
            },
            "referenceRoles": [
                {"reference": "product-front.png", "role": "主体身份与轮廓"},
                {"reference": "material-swatch.png", "role": "材料粗糙度"},
            ],
            "constraints": ["不得生成文字", "不得改变接口数量"],
            "avoid": ["霓虹泛光", "无来源的品牌标识", "塑料般高光"],
        },
        "candidateSettings": {
            "mode": "asset-exploration",
            "count": 4,
            "selectionCriteria": ["首屏裁切稳定", "主体身份准确", "材料可信"],
            "variationPolicy": "每个候选只改变主体尺度",
            "model": "adapter-selected",
            "version": "record-at-runtime",
            "settings": {"seedPolicy": "record-each-candidate"},
        },
    }


class ImagePromptCompilerCliTests(unittest.TestCase):
    def run_compiler(self, contract, *args):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "contract.json"
            path.write_text(json.dumps(contract, ensure_ascii=False), encoding="utf-8")
            return subprocess.run(
                ["python3", "-B", str(COMPILER), str(path), *args],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_text_output_is_ordered_and_preserves_contract_language(self):
        completed = self.run_compiler(valid_contract(), "--format", "text")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        headings = [
            "[intent]",
            "[lineageAndContinuity]",
            "[direction]",
            "[world]",
            "[targetContext]",
            "[variants]",
            "[cameraLogic]",
            "[surfaceLogic]",
            "[fixedAnchors]",
            "[explorationAxis]",
            "[referenceRoles]",
            "[constraints]",
            "[avoid]",
            "[candidateSettings]",
        ]
        positions = [completed.stdout.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("以克制的空间张力承载可信的产品证据", completed.stdout)
        self.assertIn("右侧 36% 不放置高对比物体", completed.stdout)
        self.assertIn("主体身份与轮廓", completed.stdout)

    def test_compiler_does_not_inject_style_names_or_quality_fluff(self):
        completed = self.run_compiler(valid_contract())
        self.assertEqual(completed.returncode, 0, completed.stderr)
        lower = completed.stdout.lower()
        for injected_term in (
            "artist",
            "studio",
            "masterpiece",
            "best quality",
            "award-winning",
            "cinematic",
            "高级感",
        ):
            self.assertNotIn(injected_term, lower)

    def test_json_output_exposes_raw_sections_and_candidate_settings(self):
        completed = self.run_compiler(valid_contract(), "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["schemaVersion"], 1)
        self.assertEqual(payload["familyId"], "hero-product-world")
        self.assertEqual(payload["assetId"], "hero-product-01")
        self.assertEqual(payload["promptContractVersion"], "1.0")
        self.assertEqual(
            [section["key"] for section in payload["sections"]],
            [
                "intent",
                "lineageAndContinuity",
                "direction",
                "world",
                "targetContext",
                "variants",
                "cameraLogic",
                "surfaceLogic",
                "fixedAnchors",
                "explorationAxis",
                "referenceRoles",
                "constraints",
                "avoid",
                "candidateSettings",
            ],
        )
        sections = {section["key"]: section for section in payload["sections"]}
        intent = {
            item["key"]: item["value"] for item in sections["intent"]["fields"]
        }
        self.assertEqual(intent["parentId"], "hero-product-master")
        direction = sections["direction"]
        self.assertEqual(
            [item["key"] for item in direction["fields"]],
            [
                "directionThesis",
                "aestheticStance",
                "tensionPair",
                "visualGenre",
                "attentionStrategy",
                "dominantSilhouette",
                "compositionFamily",
            ],
        )
        target = sections["targetContext"]
        self.assertEqual(
            [item["key"] for item in target["fields"]],
            [
                "targetRegion",
                "aspectRatio",
                "focalPoint",
                "composition",
                "depthOrder",
                "cropBehavior",
                "safeArea",
            ],
        )
        continuity = sections["lineageAndContinuity"]["fields"]
        self.assertEqual(continuity[0]["value"], "capturing")
        self.assertEqual(continuity[1]["value"]["fromState"], "rest")
        self.assertEqual(len(sections["variants"]["fields"][0]["value"]), 2)
        exploration = sections["explorationAxis"]["fields"][0]["value"]
        self.assertEqual(exploration["variable"], "focal-scale")
        self.assertEqual(exploration["name"], "主体尺度")
        settings = payload["sections"][-1]["fields"][0]["value"]
        self.assertEqual(settings["mode"], "asset-exploration")
        self.assertEqual(settings["count"], 4)
        self.assertEqual(settings["model"], "adapter-selected")
        self.assertEqual(settings["settings"]["seedPolicy"], "record-each-candidate")

    def test_subject_scene_and_references_are_optional_for_abstract_assets(self):
        contract = valid_contract()
        del contract["asset"]["subject"]
        del contract["asset"]["scene"]
        del contract["asset"]["action"]
        contract["asset"]["referenceRoles"] = []
        contract["asset"]["medium"] = "抽象程序纹理"
        completed = self.run_compiler(contract, "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        section_keys = [section["key"] for section in payload["sections"]]
        self.assertNotIn("referenceRoles", section_keys)
        world = next(section for section in payload["sections"] if section["key"] == "world")
        world_keys = [item["key"] for item in world["fields"]]
        self.assertNotIn("subject", world_keys)
        self.assertNotIn("scene", world_keys)
        self.assertNotIn("action", world_keys)

    def test_state_lineage_and_variants_are_optional_for_a_static_asset(self):
        contract = valid_contract()
        for key in ("parentId", "stateId", "transition"):
            del contract["asset"][key]
        contract["asset"]["variants"] = []
        completed = self.run_compiler(contract, "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        section_keys = [section["key"] for section in payload["sections"]]
        self.assertNotIn("lineageAndContinuity", section_keys)
        self.assertNotIn("variants", section_keys)
        self.assertEqual(payload["familyId"], "hero-product-world")

    def test_same_contract_compiles_deterministically(self):
        first = self.run_compiler(valid_contract(), "--format", "json")
        second = self.run_compiler(valid_contract(), "--format", "json")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)

    def test_missing_required_field_reports_actionable_json_path(self):
        contract = valid_contract()
        del contract["asset"]["medium"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("missing required field: asset.medium", completed.stderr)
        self.assertEqual(completed.stdout, "")

    def test_missing_creative_direction_field_is_rejected(self):
        contract = valid_contract()
        del contract["direction"]["visualGenre"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("missing required field: direction.visualGenre", completed.stderr)

    def test_aesthetic_stance_requires_exactly_three_concrete_qualities(self):
        contract = valid_contract()
        contract["direction"]["aestheticStance"] = ["克制", "精密"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must contain exactly three concrete qualities; received 2", completed.stderr)

    def test_more_than_one_exploration_axis_is_rejected(self):
        contract = valid_contract()
        contract["asset"]["explorationAxis"] = ["主体尺度", "机位高度"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must declare exactly one axis object; received 2 items", completed.stderr)

    def test_composite_or_unknown_exploration_variable_is_rejected(self):
        contract = valid_contract()
        contract["asset"]["explorationAxis"]["variable"] = (
            "shot-distance-and-light-direction"
        )
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must name one supported causal variable", completed.stderr)

    def test_transition_must_end_at_the_declared_asset_state(self):
        contract = valid_contract()
        contract["asset"]["transition"]["toState"] = "published"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must match asset.stateId", completed.stderr)

    def test_variant_ids_must_be_unique(self):
        contract = valid_contract()
        contract["asset"]["variants"][1]["id"] = "desktop-wide"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("duplicate asset variant id: desktop-wide", completed.stderr)

    def test_quality_praise_is_rejected_from_positive_prompt_fields(self):
        contract = valid_contract()
        contract["direction"]["visualGenre"] = "masterpiece best quality 科技棚拍"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("describe a visible mechanism instead", completed.stderr)

    def test_invalid_candidate_settings_are_rejected(self):
        contract = valid_contract()
        contract["candidateSettings"]["count"] = 0
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("candidateSettings.count must be a positive integer", completed.stderr)

    def test_model_settings_must_be_structured_metadata(self):
        contract = valid_contract()
        contract["candidateSettings"]["settings"] = "quality=high"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("candidateSettings.settings must be an object", completed.stderr)

    def test_unknown_candidate_mode_is_rejected(self):
        contract = valid_contract()
        contract["candidateSettings"]["mode"] = "make-it-pretty"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("candidateSettings.mode must be one of", completed.stderr)

    def test_malformed_json_and_missing_file_are_actionable(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            malformed = Path(temp_dir) / "bad.json"
            malformed.write_text('{"direction":', encoding="utf-8")
            bad_json = subprocess.run(
                ["python3", "-B", str(COMPILER), str(malformed)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            missing = subprocess.run(
                ["python3", "-B", str(COMPILER), str(Path(temp_dir) / "missing.json")],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertNotEqual(bad_json.returncode, 0)
        self.assertIn("invalid JSON", bad_json.stderr)
        self.assertIn("line 1, column", bad_json.stderr)
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("contract file does not exist", missing.stderr)


if __name__ == "__main__":
    unittest.main()
