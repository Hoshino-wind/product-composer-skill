import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPILER = ROOT / "scripts" / "compile-image-prompt.py"


def valid_composition_plan(*, mobile=False):
    return {
        "thumbnailRead": (
            "一个接口缺口切开纵向设备轮廓"
            if mobile
            else "一个低矮设备与垂直缺口形成清晰的不对称轮廓"
        ),
        "focalHierarchy": [
            "先看到设备接口缺口",
            "再读设备主轮廓",
            "最后看到接口状态灯",
        ],
        "subjectPlacement": (
            "设备缺口落在下半部中轴，主体向画面底部延伸"
            if mobile
            else "设备重心落在左下三分之一，缺口靠近画面中轴"
        ),
        "frameOccupancy": (
            "设备占画面宽度约 78%，高度约 52%"
            if mobile
            else "设备占画面宽度约 42%，高度约 34%"
        ),
        "shotDistance": "近景接口肖像" if mobile else "中近景产品肖像",
        "viewpoint": "与接口齐平的正面视点" if mobile else "与设备接口齐平的轻微低机位",
        "depthLayers": {
            "foreground": "底部保留一小段失焦台面作为进入画面的边",
            "middleGround": "设备与接口缺口保持最清晰",
            "background": "半透明隔断低对比退后，不形成第二主体",
        },
        "backgroundPressure": (
            "隔断从两侧轻压主体，顶部保持松弛"
            if mobile
            else "背景结构从左后方向主体靠拢，右侧保持松弛"
        ),
        "leadingLine": "台面边缘把视线引向接口缺口",
        "negativeSpace": "主体外侧保持低对比留白，具体文字区由布局合同决定",
    }


def valid_direction():
    return {
        "thesis": "以克制的空间张力承载可信的产品证据",
        "aestheticStance": ["克制", "精密", "有呼吸感"],
        "tensionPair": "工程秩序与材料诗意并置，工程秩序占主导",
        "visualGenre": "一座真实可制造的清晨材料实验室",
        "attentionStrategy": ["先看到产品轮廓", "随后进入真实操作区"],
        "dominantSilhouette": "低矮横向设备被一条垂直隔断切出可识别缺口",
        "compositionFamily": "object portrait",
        "typographyMood": "安静的产品编辑感，标题宽松，数据克制",
        "deletionRule": "画面拥挤时先删除解释性标签和次要道具",
        "world": "清晨的半透明材料实验室，真实可制造",
        "camera": ["与产品齐平的视点", "镜头关系服从资产构图计划"],
        "light": "左后方大面积柔光，设备接口保持清晰对比",
        "material": "磨砂再生铝与轻微使用痕迹",
        "color": "石墨灰为结构色，低饱和青色只标示可操作状态",
    }


def valid_ui_direction():
    return {
        "thesis": "把一次录制变成可检查、可撤回、可继续的工作过程",
        "aestheticStance": ["克制", "清晰", "有操作感"],
        "tensionPair": "持续记录与明确控制并置，明确控制占主导",
        "interfaceArchetype": "单任务录制工作区",
        "layoutThesis": "录制对象、实时状态与持久证据形成因果相邻关系",
        "hierarchyStrategy": "当前对象最强，状态紧随操作，证据靠近结果",
        "densityRhythm": "主工作区宽松，状态列紧凑，证据表保持真实密度",
        "attentionStrategy": ["先确认录制对象", "再操作状态", "最后检查证据"],
        "typographyMood": "操作标签清晰，状态数字稳定，说明文字克制",
        "deletionRule": "拥挤时先删除装饰说明，不删除状态、证据或恢复路径",
        "material": "扁平网页表面，层级来自边界、留白与状态色而非物体舞台",
        "color": "中性灰建立结构，低饱和青只表示活动状态",
    }


def mount_frame(frame_id, *, mobile=False):
    return {
        "id": frame_id,
        "viewport": "390x844" if mobile else "1440x900",
        "renderBox": (
            "x=0 y=0 w=390 h=520" if mobile else "x=0 y=0 w=1440 h=720"
        ),
        "exclusionZones": (
            ["DOM hero copy: x=24 y=96 w=342 h=188"]
            if mobile
            else [
                "DOM navigation: x=72 y=24 w=1296 h=56",
                "DOM hero copy: x=864 y=168 w=456 h=292",
            ]
        ),
        "focalAnchor": "设备接口缺口",
        "focalDrift": "横纵方向均不超过画面 4%",
        "cropAndBleed": "四边保留 3% 出血，窄屏允许背景隔断移出",
        "edgeBehavior": "右缘低对比融入页面底色",
        "contrastRequirement": "排除区内保持正文对比所需的低纹理底",
    }


def valid_visual_contract():
    return {
        "direction": valid_direction(),
        "asset": {
            "familyId": "hero-product-world",
            "id": "hero-product-01",
            "promptContractVersion": "2.0",
            "conceptType": "visual-asset",
            "deliveryIntent": "project-bound",
            "rasterTextPolicy": "none",
            "visibleText": [],
            "parentId": "hero-product-master",
            "stateId": "capturing",
            "transition": {
                "fromState": "rest",
                "event": "录制开始后的视觉状态",
                "toState": "capturing",
                "handoffFrame": "设备接口灯刚亮起，环境仍保持安静",
            },
            "role": "首屏产品世界观与真实主体之间的过渡资产",
            "maturity": "production candidate",
            "truthBoundary": "只可建立氛围与产品轮廓，不得建立性能、客户或认证事实",
            "medium": "写实产品摄影",
            "intendedUse": "桌面端首屏背景，DOM 承载标题与行动",
            "targetRegion": "homepage.hero",
            "aspectRatio": "16:9",
            "cropBehavior": "窄裁切时保留接口缺口，文字排除区由 mountContract 提供",
            "compositionPlan": valid_composition_plan(),
            "variants": [
                {
                    "id": "desktop-wide",
                    "targetRegion": "homepage.hero.desktop",
                    "aspectRatio": "16:9",
                    "cropBehavior": "保留完整设备轮廓",
                    "compositionPlan": valid_composition_plan(),
                },
                {
                    "id": "mobile-portrait",
                    "targetRegion": "homepage.hero.mobile",
                    "aspectRatio": "4:5",
                    "cropBehavior": "纵向裁切保留缺口，背景隔断可移出画面",
                    "compositionPlan": valid_composition_plan(mobile=True),
                },
            ],
            "mountContract": {
                "consumingRoute": "/",
                "consumingRegion": "homepage.hero",
                "mountMode": "background",
                "layoutSource": "src/routes/home/Hero.tsx rendered DOM skeleton",
                "breakpointFrames": [
                    mount_frame("desktop-wide"),
                    mount_frame("mobile-portrait", mobile=True),
                ],
            },
            "subject": "一台没有虚构标识的模块化桌面设备",
            "scene": "半透明隔断围合的材料实验台",
            "action": "接口灯由暗转亮，设备和环境保持静止",
            "fixedAnchors": [
                "设备轮廓和接口位置不变",
                "石墨灰主体材料不变",
                "主光始终来自左后方",
            ],
            "explorationAxis": {
                "variable": "focal-scale",
                "name": "主体尺度",
                "binding": "target.compositionPlan.frameOccupancy",
                "allowedValues": [
                    {
                        "desktop-wide": "设备占画面宽度约 38%，高度约 32%",
                        "mobile-portrait": "设备占画面宽度约 72%，高度约 48%",
                    },
                    {
                        "desktop-wide": "设备占画面宽度约 46%，高度约 38%",
                        "mobile-portrait": "设备占画面宽度约 82%，高度约 56%",
                    },
                ],
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
            "count": 2,
            "selectionCriteria": ["挂载裁切稳定", "主体身份准确", "材料可信"],
            "variationPolicy": "single-axis",
        },
    }


def valid_ui_reference_contract():
    return {
        "direction": valid_ui_direction(),
        "asset": {
            "familyId": "capture-interface",
            "id": "capture-ui-reference-01",
            "promptContractVersion": "2.0",
            "conceptType": "ui-mockup-reference",
            "deliveryIntent": "preview-only",
            "rasterTextPolicy": "reference-only",
            "visibleText": ["开始录制", "录制中", "查看证据"],
            "role": "判断录制工作区的层级、状态与控制密度",
            "maturity": "direction reference",
            "truthBoundary": "只表达布局与状态意图，不冒充真实产品截图或运行证据",
            "medium": "网页界面参考图",
            "intendedUse": "确定性重建前的单视口方向判断",
            "targetRegion": "capture.workspace",
            "aspectRatio": "16:10",
            "targetFidelity": "mid-fi-reference",
            "interfaceFramePlan": {
                "viewport": "1440x900 desktop browser viewport",
                "navigationAndShell": "64px 顶栏与持久项目导航，主工作区不套设备外框",
                "regionGeometry": [
                    "左侧 68% 为录制对象与时间轴",
                    "右侧 32% 为状态、证据与提交区",
                ],
                "readingOrder": ["当前录制对象", "实时状态", "证据记录", "下一步行动"],
                "primaryTask": "开始或停止一次录制并确认已留下可追溯证据",
                "activeState": "录制进行中，时间轴持续增长，停止操作最突出",
                "controlsAndAffordances": [
                    "明确的开始/停止按钮",
                    "键盘等价输入提示",
                    "可检查的录制状态与时长",
                ],
                "proofPlacement": "证据记录紧邻状态结果，不放在装饰卡片中",
                "contentDensity": "真实工作区密度；一个主对象、一个状态列、短证据表",
                "responsiveBehavior": [
                    "窄桌面把状态列移到对象下方",
                    "不把所有区域折叠成相同卡片",
                ],
                "reconstructionBoundary": [
                    "所有文字、按钮、图标、状态和数据由 HTML/CSS/SVG 重建",
                    "参考图不作为页面背景或发布截图",
                ],
            },
            "fixedAnchors": [
                "录制对象始终是页面主对象",
                "状态变化紧邻触发操作",
                "证据是持久结果而不是装饰标签",
            ],
            "explorationAxis": {
                "variable": "content-density",
                "name": "工作区密度",
                "binding": "target.interfaceFramePlan.contentDensity",
                "allowedValues": ["稀疏单任务", "中等真实密度"],
            },
            "referenceRoles": [],
            "constraints": ["保持真实网页 viewport", "只表现一个明确状态"],
            "avoid": ["海报主视觉", "悬浮设备模型", "概念艺术舞台"],
        },
        "candidateSettings": {
            "mode": "asset-exploration",
            "count": 2,
            "selectionCriteria": ["任务层级清楚", "控件可重建", "密度可信"],
            "variationPolicy": "single-axis",
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

    def test_visual_text_output_is_ordered_and_includes_adapter_candidates(self):
        completed = self.run_compiler(valid_visual_contract(), "--format", "text")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        headings = [
            "[intent]",
            "[lineageAndContinuity]",
            "[direction]",
            "[world]",
            "[targetContext]",
            "[mountContract]",
            "[compositionPlan]",
            "[variants]",
            "[cameraLogic]",
            "[surfaceLogic]",
            "[textBoundary]",
            "[referenceRoles]",
            "[fixedAnchors]",
            "[explorationAxis]",
            "[constraints]",
            "[avoid]",
            "[candidateSettings]",
            "[adapterRequest]",
            "[candidates]",
        ]
        positions = [completed.stdout.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("interactionPlan", completed.stdout)
        self.assertIn("prompt-engine-shot", completed.stdout)

    def test_composition_plan_preserves_authorial_order_without_safe_zone(self):
        completed = self.run_compiler(valid_visual_contract(), "--format", "text")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        block = completed.stdout.split("[compositionPlan]\n", 1)[1].split("\n\n", 1)[0]
        keys = [
            "thumbnailRead:",
            "focalHierarchy:",
            "subjectPlacement:",
            "frameOccupancy:",
            "shotDistance:",
            "viewpoint:",
            "depth.foreground:",
            "depth.middleGround:",
            "depth.background:",
            "backgroundPressure:",
            "leadingLine:",
            "negativeSpace:",
        ]
        positions = [block.index(key) for key in keys]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("typographySafeZone", block)

    def test_visual_json_instantiates_one_candidate_per_axis_value(self):
        completed = self.run_compiler(valid_visual_contract(), "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["schemaVersion"], 2)
        self.assertEqual(payload["adapterRequest"]["profile"], "prompt-engine-shot")
        self.assertEqual(
            payload["adapterRequest"]["operation"], "build_six_layer_prompt"
        )
        self.assertEqual(payload["adapterRequest"]["styleKey"], "no_style")
        self.assertEqual(
            payload["adapterRequest"]["assemblyOrder"],
            [
                "subject",
                "action",
                "camera",
                "compositionDepth",
                "scene",
                "lightMaterialColor",
            ],
        )
        self.assertEqual(
            payload["adapterRequest"]["sourceMap"]["shot_size"],
            "candidate.targets[].compositionPlan.shotDistance",
        )
        self.assertIn(
            "depthLayers",
            payload["adapterRequest"]["sourceMap"]["depth_layer"],
        )
        self.assertEqual(
            [item["id"] for item in payload["candidates"]],
            ["hero-product-01-c01", "hero-product-01-c02"],
        )
        self.assertEqual(
            [item["explorationDelta"]["value"] for item in payload["candidates"]],
            valid_visual_contract()["asset"]["explorationAxis"]["allowedValues"],
        )
        first_targets = payload["candidates"][0]["targets"]
        self.assertEqual(
            [target["id"] for target in first_targets],
            ["desktop-wide", "mobile-portrait"],
        )
        self.assertEqual(
            first_targets[0]["compositionPlan"]["frameOccupancy"],
            "设备占画面宽度约 38%，高度约 32%",
        )
        self.assertEqual(
            first_targets[1]["compositionPlan"]["frameOccupancy"],
            "设备占画面宽度约 72%，高度约 48%",
        )
        self.assertEqual(first_targets[0]["mountFrame"]["id"], "desktop-wide")
        self.assertEqual(first_targets[1]["mountFrame"]["id"], "mobile-portrait")
        self.assertIn(
            "direction.camera",
            payload["adapterRequest"]["sourceMap"]["extra"],
        )
        self.assertIn("camera_move", payload["adapterRequest"]["unboundInputs"])

    def test_ui_reference_bypasses_camera_depth_and_composition(self):
        completed = self.run_compiler(valid_ui_reference_contract(), "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        keys = [section["key"] for section in payload["sections"]]
        self.assertEqual(payload["adapterRequest"]["profile"], "imagegen-ui-mockup")
        self.assertFalse(payload["adapterRequest"]["cinematicShotBuilder"])
        self.assertEqual(
            payload["adapterRequest"]["sourceMap"]["interfaceStructure"],
            "candidate.targets[].interfaceFramePlan",
        )
        for forbidden in (
            "world",
            "cameraLogic",
            "compositionPlan",
            "variants",
            "mountContract",
            "lineageAndContinuity",
        ):
            self.assertNotIn(forbidden, keys)
        self.assertIn("interfaceFramePlan", keys)
        self.assertIn("interfaceBoundary", keys)
        self.assertNotIn("object portrait", completed.stdout)
        direction = next(
            section for section in payload["sections"]
            if section["key"] == "direction"
        )
        direction_keys = {item["key"] for item in direction["fields"]}
        self.assertTrue(
            {
                "interfaceArchetype",
                "layoutThesis",
                "hierarchyStrategy",
                "densityRhythm",
            }.issubset(direction_keys)
        )
        self.assertTrue(
            {
                "visualGenre",
                "dominantSilhouette",
                "compositionFamily",
            }.isdisjoint(direction_keys)
        )
        boundary = next(
            section for section in payload["sections"]
            if section["key"] == "interfaceBoundary"
        )
        forbidden_presentation = next(
            item["value"] for item in boundary["fields"]
            if item["key"] == "forbiddenPresentation"
        )
        self.assertIn("poster", forbidden_presentation)
        self.assertIn("concept-art presentation", forbidden_presentation)

    def test_ui_reference_preserves_real_interface_fields(self):
        completed = self.run_compiler(valid_ui_reference_contract(), "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        frame = next(
            section for section in payload["sections"]
            if section["key"] == "interfaceFramePlan"
        )
        fields = {item["key"]: item["value"] for item in frame["fields"]}
        self.assertEqual(fields["viewport"], "1440x900 desktop browser viewport")
        self.assertIn("开始或停止", fields["primaryTask"])
        self.assertEqual(len(fields["readingOrder"]), 4)
        self.assertEqual(
            payload["candidates"][0]["targets"][0]["interfaceFramePlan"][
                "contentDensity"
            ],
            "稀疏单任务",
        )
        self.assertEqual(
            payload["candidates"][1]["targets"][0]["interfaceFramePlan"][
                "contentDensity"
            ],
            "中等真实密度",
        )

    def test_same_contract_compiles_deterministically(self):
        first = self.run_compiler(valid_visual_contract(), "--format", "json")
        second = self.run_compiler(valid_visual_contract(), "--format", "json")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)

    def test_preview_only_unframed_visual_asset_can_skip_mount(self):
        contract = valid_visual_contract()
        contract["asset"]["deliveryIntent"] = "preview-only"
        del contract["asset"]["mountContract"]
        contract["asset"]["variants"] = []
        contract["asset"]["compositionPlan"] = {
            "notApplicable": "无缝程序纹理会平铺重复，因此没有稳定画框或固定焦点"
        }
        contract["asset"]["explorationAxis"] = {
            "variable": "texture-scale",
            "name": "纹理尺度",
            "binding": "direction.material",
            "allowedValues": ["细密纹理", "宽松纹理"],
        }
        completed = self.run_compiler(contract, "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertNotIn(
            "mountContract", [section["key"] for section in payload["sections"]]
        )
        self.assertEqual(payload["candidates"][0]["targets"][0]["id"], "primary")
        self.assertEqual(
            payload["candidates"][0]["resolvedInputs"]["direction"]["material"],
            "细密纹理",
        )

    def test_project_bound_visual_requires_mount_contract(self):
        contract = valid_visual_contract()
        del contract["asset"]["mountContract"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("asset.mountContract for project-bound visual-asset", completed.stderr)

    def test_preview_only_visual_forbids_mount_contract(self):
        contract = valid_visual_contract()
        contract["asset"]["deliveryIntent"] = "preview-only"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("mountContract is forbidden for preview-only", completed.stderr)

    def test_mount_contract_must_match_consuming_region(self):
        contract = valid_visual_contract()
        contract["asset"]["mountContract"]["consumingRegion"] = "homepage.footer"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("consumingRegion must match asset.targetRegion", completed.stderr)

    def test_mount_frame_ids_must_match_visual_variants(self):
        contract = valid_visual_contract()
        contract["asset"]["mountContract"]["breakpointFrames"][1]["id"] = "tablet"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("ids must exactly match visual target ids", completed.stderr)

    def test_mount_frame_ids_must_be_unique(self):
        contract = valid_visual_contract()
        contract["asset"]["mountContract"]["breakpointFrames"][1]["id"] = "desktop-wide"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("duplicate mount breakpoint frame id", completed.stderr)

    def test_mount_mode_is_bounded(self):
        contract = valid_visual_contract()
        contract["asset"]["mountContract"]["mountMode"] = "poster"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("mountMode must be one of", completed.stderr)

    def test_typography_safe_zone_is_rejected_from_image_composition(self):
        contract = valid_visual_contract()
        contract["asset"]["compositionPlan"]["typographySafeZone"] = "模型猜测的右侧安全区"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("unsupported fields: typographySafeZone", completed.stderr)

    def test_ui_architecture_gets_actionable_migration_error(self):
        contract = valid_ui_reference_contract()
        contract["asset"]["conceptType"] = "ui-architecture"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("'ui-architecture' was removed", completed.stderr)
        self.assertIn("code/state artifacts", completed.stderr)

    def test_interaction_plan_is_rejected_from_all_image_contracts(self):
        contract = valid_visual_contract()
        contract["asset"]["interactionPlan"] = {"userEvent": "click"}
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("not an image contract field", completed.stderr)
        self.assertIn("state machine", completed.stderr)

    def test_visual_and_ui_fields_are_mutually_exclusive(self):
        contract = valid_visual_contract()
        contract["asset"]["interfaceFramePlan"] = {}
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("unsupported fields: interfaceFramePlan", completed.stderr)

        contract = valid_ui_reference_contract()
        contract["asset"]["compositionPlan"] = valid_composition_plan()
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("unsupported fields: compositionPlan", completed.stderr)

        contract = valid_ui_reference_contract()
        contract["direction"]["visualGenre"] = "不应进入 UI 的物体舞台"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("direction contains unsupported fields: visualGenre", completed.stderr)

    def test_ui_reference_cannot_claim_project_delivery(self):
        contract = valid_ui_reference_contract()
        contract["asset"]["deliveryIntent"] = "project-bound"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("requires asset.deliveryIntent 'preview-only'", completed.stderr)

    def test_raster_text_policies_enforce_deterministic_boundaries(self):
        contract = valid_visual_contract()
        contract["asset"]["rasterTextPolicy"] = "reference-only"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("visual-asset requires asset.rasterTextPolicy 'none'", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["visibleText"] = ["Buy now"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("requires asset.visibleText []", completed.stderr)

        contract = valid_ui_reference_contract()
        contract["asset"]["rasterTextPolicy"] = "none"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("requires asset.rasterTextPolicy 'reference-only'", completed.stderr)

    def test_ui_reference_requires_fidelity_and_interface_frame(self):
        contract = valid_ui_reference_contract()
        del contract["asset"]["targetFidelity"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("asset.targetFidelity", completed.stderr)

        contract = valid_ui_reference_contract()
        del contract["asset"]["interfaceFramePlan"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("asset.interfaceFramePlan must be an object", completed.stderr)

    def test_legacy_prompt_contract_and_spatial_fields_get_migration_errors(self):
        contract = valid_visual_contract()
        contract["asset"]["promptContractVersion"] = "1.0"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must be '2.0'", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["safeArea"] = "legacy duplicate"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("mountContract for layout exclusion", completed.stderr)

    def test_allowed_values_are_required_unique_and_match_count(self):
        contract = valid_visual_contract()
        del contract["asset"]["explorationAxis"]["allowedValues"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("asset.explorationAxis.allowedValues", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["explorationAxis"]["allowedValues"] = ["same", "same"]
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must contain unique values", completed.stderr)

        contract = valid_visual_contract()
        contract["candidateSettings"]["count"] = 3
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("allowedValues count must equal", completed.stderr)

    def test_exploration_axis_is_type_specific_bound_and_target_complete(self):
        contract = valid_ui_reference_contract()
        contract["asset"]["explorationAxis"] = {
            "variable": "shot-distance",
            "name": "错误镜头轴",
            "binding": "target.compositionPlan.shotDistance",
            "allowedValues": ["近景", "远景"],
        }
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("supported ui-mockup-reference causal variable", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["explorationAxis"]["binding"] = "direction.light"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("binding must be one of", completed.stderr)

        contract = valid_visual_contract()
        values = contract["asset"]["explorationAxis"]["allowedValues"]
        values[0]["tablet"] = values[0].pop("mobile-portrait")
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("keys must exactly match target ids", completed.stderr)

    def test_candidate_bindings_preserve_the_resolved_schema(self):
        contract = valid_ui_reference_contract()
        contract["asset"]["explorationAxis"] = {
            "variable": "layout-geometry",
            "name": "区域结构",
            "binding": "target.interfaceFramePlan.regionGeometry",
            "allowedValues": ["错误的字符串", "仍然是字符串"],
        }
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must be a list of strings for binding", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["explorationAxis"] = {
            "variable": "action-phase",
            "name": "动作阶段",
            "binding": "asset.action",
            "allowedValues": [["错误列表一"], ["错误列表二"]],
        }
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must be a string for binding 'asset.action'", completed.stderr)

        contract = valid_visual_contract()
        contract["asset"]["deliveryIntent"] = "preview-only"
        del contract["asset"]["mountContract"]
        contract["asset"]["variants"] = []
        contract["asset"]["compositionPlan"] = {
            "notApplicable": "无缝程序纹理会平铺重复，因此没有稳定画框或固定焦点"
        }
        contract["asset"]["explorationAxis"] = {
            "variable": "shot-distance",
            "name": "错误的画框字段",
            "binding": "target.compositionPlan.shotDistance",
            "allowedValues": ["近景", "远景"],
        }
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn(
            "notApplicable cannot be combined with framed composition fields",
            completed.stderr,
        )

    def test_variation_policy_must_be_single_axis(self):
        contract = valid_visual_contract()
        contract["candidateSettings"]["variationPolicy"] = "change-everything"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must be 'single-axis'", completed.stderr)

    def test_direction_alternatives_use_separate_contracts(self):
        contract = valid_visual_contract()
        contract["candidateSettings"]["mode"] = "direction-exploration"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("one candidate per contract", completed.stderr)

    def test_execution_metadata_is_rejected_from_creative_contract(self):
        contract = valid_visual_contract()
        contract["candidateSettings"]["model"] = "some-model"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("unsupported fields: model", completed.stderr)

        contract = valid_visual_contract()
        contract["renderPass"] = "framework"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("contract contains unsupported fields: renderPass", completed.stderr)

    def test_compiler_does_not_inject_a_style_catalog_or_desktop_path(self):
        completed = self.run_compiler(valid_visual_contract())
        self.assertEqual(completed.returncode, 0, completed.stderr)
        lower = completed.stdout.lower()
        self.assertIn('"stylekey":"no_style"', lower)
        self.assertNotIn("/users/", lower)
        for term in ("masterpiece", "best quality", "award-winning", "高级感"):
            self.assertNotIn(term, lower)

    def test_quality_praise_is_rejected_from_positive_fields(self):
        contract = valid_visual_contract()
        contract["direction"]["visualGenre"] = "masterpiece best quality 科技棚拍"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("describe a visible mechanism instead", completed.stderr)

    def test_transition_must_end_at_declared_asset_state(self):
        contract = valid_visual_contract()
        contract["asset"]["transition"]["toState"] = "published"
        completed = self.run_compiler(contract)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must match asset.stateId", completed.stderr)

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
