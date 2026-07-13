#!/usr/bin/env python3
"""Compile a Product Composer image contract into portable adapter inputs."""

from __future__ import annotations

import argparse
from copy import deepcopy
import json
import sys
from pathlib import Path
from typing import Any


CANDIDATE_MODES = {
    "direction-exploration",
    "asset-exploration",
    "production-candidate",
    "edit-repair",
}

PROMPT_CONTRACT_VERSION = "2.0"

CONCEPT_TYPES = {
    "visual-asset",
    "ui-mockup-reference",
}

DELIVERY_INTENTS = {
    "preview-only",
    "project-bound",
}

MOUNT_MODES = {
    "background",
    "img",
    "masked",
    "layer",
}

TARGET_FIDELITIES = {
    "low-fi-wireframe",
    "mid-fi-reference",
    "high-fi-reference",
}

VISUAL_EXPLORATION_BINDINGS = {
    "abstraction-level": {"direction.visualGenre"},
    "action-phase": {"asset.action"},
    "atmospheric-density": {"direction.world", "asset.scene"},
    "camera-height": {"target.compositionPlan.viewpoint"},
    "color-temperature": {"direction.light", "direction.color"},
    "crop": {"target.cropBehavior"},
    "environment-density": {"direction.world", "asset.scene"},
    "exposure": {"direction.light"},
    "focal-scale": {"target.compositionPlan.frameOccupancy"},
    "lens-behavior": {"direction.camera"},
    "light-direction": {"direction.light"},
    "light-softness": {"direction.light"},
    "material-response": {"direction.material"},
    "palette-balance": {"direction.color"},
    "prop-density": {"asset.scene"},
    "shot-distance": {"target.compositionPlan.shotDistance"},
    "silhouette-variation": {"direction.dominantSilhouette"},
    "subject-pose": {"asset.action"},
    "texture-scale": {"direction.material"},
    "viewpoint": {"target.compositionPlan.viewpoint"},
}

UI_EXPLORATION_BINDINGS = {
    "content-density": {"target.interfaceFramePlan.contentDensity"},
    "control-emphasis": {
        "target.interfaceFramePlan.activeState",
        "target.interfaceFramePlan.controlsAndAffordances",
    },
    "hierarchy-emphasis": {"direction.hierarchyStrategy"},
    "layout-geometry": {"target.interfaceFramePlan.regionGeometry"},
    "navigation-density": {"target.interfaceFramePlan.navigationAndShell"},
    "proof-proximity": {"target.interfaceFramePlan.proofPlacement"},
    "reading-order": {"target.interfaceFramePlan.readingOrder"},
    "responsive-strategy": {"target.interfaceFramePlan.responsiveBehavior"},
    "whitespace-rhythm": {"direction.densityRhythm"},
}

VISUAL_EXPLORATION_VARIABLES = set(VISUAL_EXPLORATION_BINDINGS)
UI_EXPLORATION_VARIABLES = set(UI_EXPLORATION_BINDINGS)

BINDING_VALUE_KINDS = {
    "asset.action": "string",
    "asset.scene": "string",
    "direction.camera": "text",
    "direction.color": "text",
    "direction.densityRhythm": "text",
    "direction.dominantSilhouette": "string",
    "direction.hierarchyStrategy": "text",
    "direction.light": "text",
    "direction.material": "text",
    "direction.visualGenre": "string",
    "direction.world": "text",
    "target.compositionPlan.frameOccupancy": "text",
    "target.compositionPlan.shotDistance": "text",
    "target.compositionPlan.viewpoint": "text",
    "target.cropBehavior": "text",
    "target.interfaceFramePlan.activeState": "text",
    "target.interfaceFramePlan.contentDensity": "text",
    "target.interfaceFramePlan.controlsAndAffordances": "list",
    "target.interfaceFramePlan.navigationAndShell": "text",
    "target.interfaceFramePlan.proofPlacement": "text",
    "target.interfaceFramePlan.readingOrder": "list",
    "target.interfaceFramePlan.regionGeometry": "list",
    "target.interfaceFramePlan.responsiveBehavior": "list",
}

QUALITY_FLUFF_TERMS = (
    "award-winning",
    "award winning",
    "best quality",
    "masterpiece",
    "高级感",
    "杰作",
    "最高质量",
    "获奖级",
)

COMMON_ASSET_KEYS = {
    "familyId",
    "id",
    "promptContractVersion",
    "conceptType",
    "deliveryIntent",
    "rasterTextPolicy",
    "visibleText",
    "role",
    "maturity",
    "truthBoundary",
    "medium",
    "intendedUse",
    "targetRegion",
    "aspectRatio",
    "fixedAnchors",
    "explorationAxis",
    "referenceRoles",
    "constraints",
    "avoid",
}

VISUAL_ASSET_KEYS = COMMON_ASSET_KEYS | {
    "parentId",
    "stateId",
    "transition",
    "cropBehavior",
    "compositionPlan",
    "variants",
    "mountContract",
    "subject",
    "scene",
    "action",
}

UI_REFERENCE_KEYS = COMMON_ASSET_KEYS | {
    "targetFidelity",
    "interfaceFramePlan",
}


class ContractError(ValueError):
    """A validation error that can be corrected in the input contract."""


def require_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(f"{path} must be an object")
    return value


def reject_unknown_keys(
    container: dict[str, Any], allowed: set[str], path: str
) -> None:
    unknown = sorted(set(container) - allowed)
    if unknown:
        raise ContractError(
            f"{path} contains unsupported fields: {', '.join(unknown)}"
        )


def require_string(container: dict[str, Any], key: str, path: str) -> str:
    field_path = f"{path}.{key}"
    if key not in container:
        raise ContractError(f"missing required field: {field_path}")
    value = container[key]
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{field_path} must be a non-empty string")
    return value


def require_choice(
    container: dict[str, Any], key: str, path: str, choices: set[str]
) -> str:
    value = require_string(container, key, path)
    if value not in choices:
        raise ContractError(
            f"{path}.{key} must be one of: {', '.join(sorted(choices))}; "
            f"received {value!r}"
        )
    return value


def require_text_logic(container: dict[str, Any], key: str, path: str) -> Any:
    """Accept a concise statement or an ordered list of statements."""
    field_path = f"{path}.{key}"
    if key not in container:
        raise ContractError(f"missing required field: {field_path}")
    value = container[key]
    if isinstance(value, str):
        if value.strip():
            return value
        raise ContractError(f"{field_path} must not be empty")
    if isinstance(value, list):
        if not value:
            raise ContractError(
                f"{field_path} must be a non-empty string or list of strings"
            )
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ContractError(
                    f"{field_path}[{index}] must be a non-empty string"
                )
        return value
    raise ContractError(
        f"{field_path} must be a non-empty string or list of strings"
    )


def require_string_list(
    container: dict[str, Any], key: str, path: str, *, allow_empty: bool = False
) -> list[str]:
    field_path = f"{path}.{key}"
    if key not in container:
        raise ContractError(f"missing required field: {field_path}")
    value = container[key]
    if not isinstance(value, list):
        raise ContractError(f"{field_path} must be a list of strings")
    if not value and not allow_empty:
        raise ContractError(f"{field_path} must contain at least one item")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ContractError(f"{field_path}[{index}] must be a non-empty string")
    return value


def require_aesthetic_stance(direction: dict[str, Any]) -> list[str]:
    stance = require_string_list(direction, "aestheticStance", "direction")
    if len(stance) != 3:
        raise ContractError(
            "direction.aestheticStance must contain exactly three concrete "
            f"qualities; received {len(stance)}"
        )
    return stance


def reject_quality_fluff(value: Any, path: str) -> None:
    if isinstance(value, str):
        lowered = value.casefold()
        for term in QUALITY_FLUFF_TERMS:
            if term.casefold() in lowered:
                raise ContractError(
                    f"{path} contains unsupported quality praise {term!r}; "
                    "describe a visible mechanism instead"
                )
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_quality_fluff(item, f"{path}[{index}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            reject_quality_fluff(item, f"{path}.{key}")


def validate_direction(value: Any, concept_type: str) -> dict[str, Any]:
    direction = require_object(value, "direction")
    shared = {
        "thesis",
        "aestheticStance",
        "tensionPair",
        "attentionStrategy",
        "typographyMood",
        "deletionRule",
        "material",
        "color",
    }
    visual_only = {
        "visualGenre",
        "dominantSilhouette",
        "compositionFamily",
        "world",
        "camera",
        "light",
    }
    ui_only = {
        "interfaceArchetype",
        "layoutThesis",
        "hierarchyStrategy",
        "densityRhythm",
    }
    allowed = shared | (visual_only if concept_type == "visual-asset" else ui_only)
    reject_unknown_keys(direction, allowed, "direction")
    validated: dict[str, Any] = {
        "thesis": require_string(direction, "thesis", "direction"),
        "aestheticStance": require_aesthetic_stance(direction),
        "tensionPair": require_string(direction, "tensionPair", "direction"),
        "attentionStrategy": require_text_logic(
            direction, "attentionStrategy", "direction"
        ),
        "typographyMood": require_text_logic(
            direction, "typographyMood", "direction"
        ),
        "deletionRule": require_text_logic(
            direction, "deletionRule", "direction"
        ),
        "material": require_text_logic(direction, "material", "direction"),
        "color": require_text_logic(direction, "color", "direction"),
    }
    if concept_type == "visual-asset":
        validated.update(
            {
                "visualGenre": require_string(
                    direction, "visualGenre", "direction"
                ),
                "dominantSilhouette": require_string(
                    direction, "dominantSilhouette", "direction"
                ),
                "compositionFamily": require_string(
                    direction, "compositionFamily", "direction"
                ),
                "world": require_text_logic(direction, "world", "direction"),
                "camera": require_text_logic(direction, "camera", "direction"),
                "light": require_text_logic(direction, "light", "direction"),
            }
        )
    else:
        validated.update(
            {
                "interfaceArchetype": require_string(
                    direction, "interfaceArchetype", "direction"
                ),
                "layoutThesis": require_text_logic(
                    direction, "layoutThesis", "direction"
                ),
                "hierarchyStrategy": require_text_logic(
                    direction, "hierarchyStrategy", "direction"
                ),
                "densityRhythm": require_text_logic(
                    direction, "densityRhythm", "direction"
                ),
            }
        )
    return validated


def validate_delta_value(value: Any, path: str) -> Any:
    if isinstance(value, str):
        if value.strip():
            return value
        raise ContractError(f"{path} must not be empty")
    if isinstance(value, list):
        if not value:
            raise ContractError(f"{path} must not be an empty list")
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ContractError(f"{path}[{index}] must be a non-empty string")
        return value
    raise ContractError(f"{path} must be a non-empty string or list of strings")


def validate_bound_delta_value(value: Any, binding: str, path: str) -> Any:
    validated = validate_delta_value(value, path)
    kind = BINDING_VALUE_KINDS[binding]
    if kind == "string" and not isinstance(validated, str):
        raise ContractError(f"{path} must be a string for binding {binding!r}")
    if kind == "list" and not isinstance(validated, list):
        raise ContractError(
            f"{path} must be a list of strings for binding {binding!r}"
        )
    return validated


def validate_exploration_axis(value: Any, concept_type: str) -> dict[str, Any]:
    path = "asset.explorationAxis"
    if isinstance(value, list):
        raise ContractError(
            f"{path} must declare exactly one axis object; received {len(value)} items"
        )
    axis = require_object(value, path)
    reject_unknown_keys(
        axis, {"variable", "name", "binding", "allowedValues"}, path
    )
    variable = require_string(axis, "variable", path)
    bindings = (
        VISUAL_EXPLORATION_BINDINGS
        if concept_type == "visual-asset"
        else UI_EXPLORATION_BINDINGS
    )
    variables = (
        VISUAL_EXPLORATION_VARIABLES
        if concept_type == "visual-asset"
        else UI_EXPLORATION_VARIABLES
    )
    if variable not in variables:
        raise ContractError(
            f"{path}.variable must name one supported {concept_type} causal "
            f"variable: {', '.join(sorted(variables))}; received {variable!r}"
        )
    binding = require_string(axis, "binding", path)
    if binding not in bindings[variable]:
        raise ContractError(
            f"{path}.binding must be one of: "
            f"{', '.join(sorted(bindings[variable]))} for {variable!r}; "
            f"received {binding!r}"
        )
    if "allowedValues" not in axis or not isinstance(axis["allowedValues"], list):
        raise ContractError(f"{path}.allowedValues must be a non-empty list")
    if not axis["allowedValues"]:
        raise ContractError(f"{path}.allowedValues must contain at least one item")
    allowed_values = []
    for index, item in enumerate(axis["allowedValues"]):
        item_path = f"{path}.allowedValues[{index}]"
        if isinstance(item, dict):
            if not binding.startswith("target.") or not item:
                raise ContractError(
                    f"{item_path} may be an object only for a target binding"
                )
            mapped = {}
            for target_id, target_value in item.items():
                if not isinstance(target_id, str) or not target_id.strip():
                    raise ContractError(
                        f"{item_path} target ids must be non-empty strings"
                    )
                mapped[target_id] = validate_bound_delta_value(
                    target_value, binding, f"{item_path}.{target_id}"
                )
            allowed_values.append(mapped)
        else:
            allowed_values.append(
                validate_bound_delta_value(item, binding, item_path)
            )
    canonical = [
        json.dumps(item, ensure_ascii=False, sort_keys=True)
        for item in allowed_values
    ]
    if len(set(canonical)) != len(canonical):
        raise ContractError(f"{path}.allowedValues must contain unique values")
    return {
        "variable": variable,
        "name": require_string(axis, "name", path),
        "binding": binding,
        "allowedValues": allowed_values,
    }


def validate_axis_target_values(
    axis: dict[str, Any], target_ids: set[str]
) -> None:
    if not axis["binding"].startswith("target."):
        return
    for index, value in enumerate(axis["allowedValues"]):
        path = f"asset.explorationAxis.allowedValues[{index}]"
        if len(target_ids) > 1 and not isinstance(value, dict):
            raise ContractError(
                f"{path} must map every target id because the binding is "
                "target-specific"
            )
        if isinstance(value, dict) and set(value) != target_ids:
            raise ContractError(
                f"{path} keys must exactly match target ids: "
                f"{', '.join(sorted(target_ids))}"
            )


def validate_transition(asset: dict[str, Any]) -> dict[str, Any] | None:
    if "transition" not in asset:
        return None
    path = "asset.transition"
    transition = require_object(asset["transition"], path)
    reject_unknown_keys(
        transition, {"fromState", "event", "toState", "handoffFrame"}, path
    )
    validated = {
        "fromState": require_string(transition, "fromState", path),
        "event": require_string(transition, "event", path),
        "toState": require_string(transition, "toState", path),
        "handoffFrame": require_text_logic(transition, "handoffFrame", path),
    }
    state_id = require_string(asset, "stateId", "asset")
    if validated["toState"] != state_id:
        raise ContractError(
            "asset.transition.toState must match asset.stateId so continuity is inspectable"
        )
    return validated


def validate_composition_plan(
    value: Any, path: str = "asset.compositionPlan"
) -> dict[str, Any]:
    plan = require_object(value, path)
    if "notApplicable" in plan:
        if set(plan) != {"notApplicable"}:
            raise ContractError(
                f"{path}.notApplicable cannot be combined with framed composition fields"
            )
        reason = require_string(plan, "notApplicable", path)
        if len(reason.strip()) < 16 or reason.strip().casefold() in {
            "not applicable",
            "not applicable.",
            "不适用",
            "不适用。",
        }:
            raise ContractError(
                f"{path}.notApplicable must explain why the asset has no stable frame"
            )
        return {"notApplicable": reason}

    required = {
        "thumbnailRead",
        "focalHierarchy",
        "subjectPlacement",
        "frameOccupancy",
        "shotDistance",
        "viewpoint",
        "depthLayers",
        "backgroundPressure",
        "leadingLine",
        "negativeSpace",
    }
    reject_unknown_keys(plan, required, path)
    missing = sorted(required - set(plan))
    if missing:
        raise ContractError(
            f"missing required fields in {path}: {', '.join(missing)}"
        )

    focal_hierarchy = require_string_list(plan, "focalHierarchy", path)
    if not 2 <= len(focal_hierarchy) <= 4:
        raise ContractError(
            f"{path}.focalHierarchy must contain 2 to 4 ordered reads; "
            f"received {len(focal_hierarchy)}"
        )

    depth_path = f"{path}.depthLayers"
    depth = require_object(plan["depthLayers"], depth_path)
    depth_keys = {"foreground", "middleGround", "background"}
    reject_unknown_keys(depth, depth_keys, depth_path)
    missing_depth = sorted(depth_keys - set(depth))
    if missing_depth:
        raise ContractError(
            f"missing required fields in {depth_path}: {', '.join(missing_depth)}"
        )

    return {
        "thumbnailRead": require_text_logic(plan, "thumbnailRead", path),
        "focalHierarchy": focal_hierarchy,
        "subjectPlacement": require_text_logic(plan, "subjectPlacement", path),
        "frameOccupancy": require_text_logic(plan, "frameOccupancy", path),
        "shotDistance": require_text_logic(plan, "shotDistance", path),
        "viewpoint": require_text_logic(plan, "viewpoint", path),
        "depthLayers": {
            key: require_text_logic(depth, key, depth_path)
            for key in ("foreground", "middleGround", "background")
        },
        "backgroundPressure": require_text_logic(
            plan, "backgroundPressure", path
        ),
        "leadingLine": require_text_logic(plan, "leadingLine", path),
        "negativeSpace": require_text_logic(plan, "negativeSpace", path),
    }


def validate_variants(asset: dict[str, Any]) -> list[dict[str, Any]]:
    value = asset.get("variants", [])
    if not isinstance(value, list):
        raise ContractError("asset.variants must be a list")
    variants: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(value):
        path = f"asset.variants[{index}]"
        variant = require_object(item, path)
        allowed = {
            "id",
            "targetRegion",
            "aspectRatio",
            "cropBehavior",
            "compositionPlan",
        }
        reject_unknown_keys(variant, allowed, path)
        variant_id = require_string(variant, "id", path)
        if variant_id in seen_ids:
            raise ContractError(f"duplicate asset variant id: {variant_id}")
        seen_ids.add(variant_id)
        if "compositionPlan" not in variant:
            raise ContractError(f"missing required field: {path}.compositionPlan")
        variants.append(
            {
                "id": variant_id,
                "targetRegion": require_string(variant, "targetRegion", path),
                "aspectRatio": require_string(variant, "aspectRatio", path),
                "cropBehavior": require_text_logic(
                    variant, "cropBehavior", path
                ),
                "compositionPlan": validate_composition_plan(
                    variant["compositionPlan"], f"{path}.compositionPlan"
                ),
            }
        )
    return variants


def validate_reference_roles(asset: dict[str, Any]) -> list[dict[str, str]]:
    value = asset.get("referenceRoles", [])
    if not isinstance(value, list):
        raise ContractError("asset.referenceRoles must be a list")
    roles: list[dict[str, str]] = []
    for index, item in enumerate(value):
        path = f"asset.referenceRoles[{index}]"
        role = require_object(item, path)
        reject_unknown_keys(role, {"reference", "role"}, path)
        roles.append(
            {
                "reference": require_string(role, "reference", path),
                "role": require_string(role, "role", path),
            }
        )
    return roles


def validate_mount_contract(
    value: Any, asset: dict[str, Any], variants: list[dict[str, Any]]
) -> dict[str, Any]:
    path = "asset.mountContract"
    mount = require_object(value, path)
    required = {
        "consumingRoute",
        "consumingRegion",
        "mountMode",
        "layoutSource",
        "breakpointFrames",
    }
    reject_unknown_keys(mount, required, path)
    missing = sorted(required - set(mount))
    if missing:
        raise ContractError(
            f"missing required fields in {path}: {', '.join(missing)}"
        )

    consuming_region = require_string(mount, "consumingRegion", path)
    if consuming_region != asset["targetRegion"]:
        raise ContractError(
            "asset.mountContract.consumingRegion must match asset.targetRegion"
        )

    frames_value = mount["breakpointFrames"]
    if not isinstance(frames_value, list) or not frames_value:
        raise ContractError(
            "asset.mountContract.breakpointFrames must contain at least one frame"
        )
    frame_keys = {
        "id",
        "viewport",
        "renderBox",
        "exclusionZones",
        "focalAnchor",
        "focalDrift",
        "cropAndBleed",
        "edgeBehavior",
        "contrastRequirement",
    }
    frames: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(frames_value):
        frame_path = f"{path}.breakpointFrames[{index}]"
        frame = require_object(item, frame_path)
        reject_unknown_keys(frame, frame_keys, frame_path)
        missing_frame = sorted(frame_keys - set(frame))
        if missing_frame:
            raise ContractError(
                f"missing required fields in {frame_path}: {', '.join(missing_frame)}"
            )
        frame_id = require_string(frame, "id", frame_path)
        if frame_id in seen_ids:
            raise ContractError(f"duplicate mount breakpoint frame id: {frame_id}")
        seen_ids.add(frame_id)
        frames.append(
            {
                "id": frame_id,
                "viewport": require_string(frame, "viewport", frame_path),
                "renderBox": require_text_logic(frame, "renderBox", frame_path),
                "exclusionZones": require_string_list(
                    frame, "exclusionZones", frame_path, allow_empty=True
                ),
                "focalAnchor": require_text_logic(
                    frame, "focalAnchor", frame_path
                ),
                "focalDrift": require_text_logic(frame, "focalDrift", frame_path),
                "cropAndBleed": require_text_logic(
                    frame, "cropAndBleed", frame_path
                ),
                "edgeBehavior": require_text_logic(
                    frame, "edgeBehavior", frame_path
                ),
                "contrastRequirement": require_text_logic(
                    frame, "contrastRequirement", frame_path
                ),
            }
        )

    target_ids = {variant["id"] for variant in variants} or {"primary"}
    if seen_ids != target_ids:
        raise ContractError(
            "asset.mountContract.breakpointFrames ids must exactly match "
            f"visual target ids: {', '.join(sorted(target_ids))}"
        )

    return {
        "consumingRoute": require_string(mount, "consumingRoute", path),
        "consumingRegion": consuming_region,
        "mountMode": require_choice(mount, "mountMode", path, MOUNT_MODES),
        "layoutSource": require_string(mount, "layoutSource", path),
        "breakpointFrames": frames,
    }


def validate_interface_frame_plan(
    value: Any, path: str = "asset.interfaceFramePlan"
) -> dict[str, Any]:
    plan = require_object(value, path)
    required = {
        "viewport",
        "navigationAndShell",
        "regionGeometry",
        "readingOrder",
        "primaryTask",
        "activeState",
        "controlsAndAffordances",
        "proofPlacement",
        "contentDensity",
        "responsiveBehavior",
        "reconstructionBoundary",
    }
    reject_unknown_keys(plan, required, path)
    missing = sorted(required - set(plan))
    if missing:
        raise ContractError(
            f"missing required fields in {path}: {', '.join(missing)}"
        )
    return {
        "viewport": require_string(plan, "viewport", path),
        "navigationAndShell": require_text_logic(
            plan, "navigationAndShell", path
        ),
        "regionGeometry": require_string_list(plan, "regionGeometry", path),
        "readingOrder": require_string_list(plan, "readingOrder", path),
        "primaryTask": require_text_logic(plan, "primaryTask", path),
        "activeState": require_text_logic(plan, "activeState", path),
        "controlsAndAffordances": require_string_list(
            plan, "controlsAndAffordances", path
        ),
        "proofPlacement": require_text_logic(plan, "proofPlacement", path),
        "contentDensity": require_text_logic(plan, "contentDensity", path),
        "responsiveBehavior": require_string_list(
            plan, "responsiveBehavior", path
        ),
        "reconstructionBoundary": require_string_list(
            plan, "reconstructionBoundary", path
        ),
    }


def validate_candidate_settings(
    value: Any, axis: dict[str, Any]
) -> dict[str, Any]:
    path = "candidateSettings"
    settings = require_object(value, path)
    allowed = {"mode", "count", "selectionCriteria", "variationPolicy"}
    reject_unknown_keys(settings, allowed, path)
    mode = require_choice(settings, "mode", path, CANDIDATE_MODES)
    count = settings.get("count")
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ContractError("candidateSettings.count must be a positive integer")
    criteria = require_string_list(settings, "selectionCriteria", path)
    variation_policy = require_string(settings, "variationPolicy", path)
    if variation_policy != "single-axis":
        raise ContractError(
            "candidateSettings.variationPolicy must be 'single-axis'"
        )
    values = axis["allowedValues"]
    if len(values) != count:
        raise ContractError(
            "asset.explorationAxis.allowedValues count must equal "
            f"candidateSettings.count; received {len(values)} and {count}"
        )
    if mode == "direction-exploration" and count != 1:
        raise ContractError(
            "direction-exploration uses one candidate per contract; create "
            "separate contracts for orthogonal directions"
        )
    return {
        "mode": mode,
        "count": count,
        "selectionCriteria": criteria,
        "variationPolicy": variation_policy,
    }


def validate_common_asset(
    asset: dict[str, Any], concept_type: str
) -> dict[str, Any]:
    return {
        "familyId": require_string(asset, "familyId", "asset"),
        "id": require_string(asset, "id", "asset"),
        "promptContractVersion": require_string(
            asset, "promptContractVersion", "asset"
        ),
        "conceptType": require_string(asset, "conceptType", "asset"),
        "deliveryIntent": require_choice(
            asset, "deliveryIntent", "asset", DELIVERY_INTENTS
        ),
        "rasterTextPolicy": require_string(
            asset, "rasterTextPolicy", "asset"
        ),
        "visibleText": require_string_list(
            asset, "visibleText", "asset", allow_empty=True
        ),
        "role": require_string(asset, "role", "asset"),
        "maturity": require_string(asset, "maturity", "asset"),
        "truthBoundary": require_string(asset, "truthBoundary", "asset"),
        "medium": require_string(asset, "medium", "asset"),
        "intendedUse": require_string(asset, "intendedUse", "asset"),
        "targetRegion": require_string(asset, "targetRegion", "asset"),
        "aspectRatio": require_string(asset, "aspectRatio", "asset"),
        "fixedAnchors": require_string_list(asset, "fixedAnchors", "asset"),
        "explorationAxis": validate_exploration_axis(
            asset.get("explorationAxis"), concept_type
        ),
        "referenceRoles": validate_reference_roles(asset),
        "constraints": require_string_list(asset, "constraints", "asset"),
        "avoid": require_string_list(asset, "avoid", "asset"),
    }


def validate_visual_asset(
    asset: dict[str, Any], common: dict[str, Any]
) -> dict[str, Any]:
    reject_unknown_keys(asset, VISUAL_ASSET_KEYS, "asset")
    if common["rasterTextPolicy"] != "none":
        raise ContractError(
            "visual-asset requires asset.rasterTextPolicy 'none'; publish-bound "
            "text belongs to DOM, SVG, or component code"
        )
    if common["visibleText"]:
        raise ContractError(
            "visual-asset with rasterTextPolicy 'none' requires asset.visibleText []"
        )
    if "compositionPlan" not in asset:
        raise ContractError("missing required field: asset.compositionPlan")
    variants = validate_variants(asset)
    validate_axis_target_values(
        common["explorationAxis"],
        {variant["id"] for variant in variants} or {"primary"},
    )
    validated = {
        **common,
        "cropBehavior": require_text_logic(asset, "cropBehavior", "asset"),
        "compositionPlan": validate_composition_plan(asset["compositionPlan"]),
        "variants": variants,
    }
    if common["deliveryIntent"] == "project-bound":
        if "mountContract" not in asset:
            raise ContractError(
                "missing required field: asset.mountContract for project-bound visual-asset"
            )
        validated["mountContract"] = validate_mount_contract(
            asset["mountContract"], common, variants
        )
    elif "mountContract" in asset:
        raise ContractError(
            "asset.mountContract is forbidden for preview-only visual-asset"
        )

    for key in ("parentId", "stateId", "subject", "scene", "action"):
        if key in asset:
            validated[key] = require_string(asset, key, "asset")
    transition = validate_transition(asset)
    if transition is not None:
        validated["transition"] = transition
    return validated


def validate_ui_reference(
    asset: dict[str, Any], common: dict[str, Any]
) -> dict[str, Any]:
    reject_unknown_keys(asset, UI_REFERENCE_KEYS, "asset")
    if common["deliveryIntent"] != "preview-only":
        raise ContractError(
            "ui-mockup-reference requires asset.deliveryIntent 'preview-only'"
        )
    if common["rasterTextPolicy"] != "reference-only":
        raise ContractError(
            "ui-mockup-reference requires asset.rasterTextPolicy 'reference-only'"
        )
    validate_axis_target_values(common["explorationAxis"], {"primary"})
    return {
        **common,
        "targetFidelity": require_choice(
            asset, "targetFidelity", "asset", TARGET_FIDELITIES
        ),
        "interfaceFramePlan": validate_interface_frame_plan(
            asset.get("interfaceFramePlan")
        ),
    }


def validate_contract(contract: Any) -> dict[str, Any]:
    root = require_object(contract, "contract")
    reject_unknown_keys(root, {"direction", "asset", "candidateSettings"}, "contract")
    if "direction" not in root:
        raise ContractError("missing required field: direction")
    if "asset" not in root:
        raise ContractError("missing required field: asset")
    if "candidateSettings" not in root:
        raise ContractError("missing required field: candidateSettings")

    asset = require_object(root["asset"], "asset")
    if "interactionPlan" in asset:
        raise ContractError(
            "asset.interactionPlan is not an image contract field; move interaction "
            "causality to a code prototype, state machine, or multi-state storyboard"
        )
    if asset.get("conceptType") == "ui-architecture":
        raise ContractError(
            "asset.conceptType 'ui-architecture' was removed; use "
            "'ui-mockup-reference' for one reference frame, or model experience "
            "architecture in code/state artifacts"
        )
    legacy = sorted({"focalPoint", "composition", "depthOrder", "safeArea"} & set(asset))
    if legacy:
        raise ContractError(
            "prompt contract 2.0 uses asset.compositionPlan for visual frame "
            "composition and mountContract for layout exclusion; remove legacy "
            "asset fields: " + ", ".join(legacy)
        )

    concept_type = require_string(asset, "conceptType", "asset")
    if concept_type not in CONCEPT_TYPES:
        raise ContractError(
            "asset.conceptType must be one of: " + ", ".join(sorted(CONCEPT_TYPES))
        )
    common = validate_common_asset(asset, concept_type)
    if common["promptContractVersion"] != PROMPT_CONTRACT_VERSION:
        raise ContractError(
            "asset.promptContractVersion must be '2.0'; migrate image composition "
            "to compositionPlan or interface structure to interfaceFramePlan"
        )

    if concept_type == "visual-asset":
        validated_asset = validate_visual_asset(asset, common)
    else:
        validated_asset = validate_ui_reference(asset, common)

    direction = validate_direction(root["direction"], concept_type)
    settings = validate_candidate_settings(
        root["candidateSettings"], validated_asset["explorationAxis"]
    )
    reject_quality_fluff(direction, "direction")
    reject_quality_fluff(
        {
            key: value
            for key, value in validated_asset.items()
            if key not in {"constraints", "avoid", "truthBoundary"}
        },
        "asset",
    )
    return {
        "direction": direction,
        "asset": validated_asset,
        "candidateSettings": settings,
    }


def field(key: str, value: Any) -> dict[str, Any]:
    return {"key": key, "value": value}


def composition_fields(plan: dict[str, Any]) -> list[dict[str, Any]]:
    if "notApplicable" in plan:
        return [field("notApplicable", plan["notApplicable"])]
    depth = plan["depthLayers"]
    return [
        field("thumbnailRead", plan["thumbnailRead"]),
        field("focalHierarchy", plan["focalHierarchy"]),
        field("subjectPlacement", plan["subjectPlacement"]),
        field("frameOccupancy", plan["frameOccupancy"]),
        field("shotDistance", plan["shotDistance"]),
        field("viewpoint", plan["viewpoint"]),
        field("depth.foreground", depth["foreground"]),
        field("depth.middleGround", depth["middleGround"]),
        field("depth.background", depth["background"]),
        field("backgroundPressure", plan["backgroundPressure"]),
        field("leadingLine", plan["leadingLine"]),
        field("negativeSpace", plan["negativeSpace"]),
    ]


def common_sections(contract: dict[str, Any]) -> list[dict[str, Any]]:
    asset = contract["asset"]
    direction = contract["direction"]
    direction_fields = [
        field("directionThesis", direction["thesis"]),
        field("aestheticStance", direction["aestheticStance"]),
        field("tensionPair", direction["tensionPair"]),
        field("attentionStrategy", direction["attentionStrategy"]),
        field("typographyMood", direction["typographyMood"]),
        field("deletionRule", direction["deletionRule"]),
    ]
    if asset["conceptType"] == "visual-asset":
        direction_fields[3:3] = [
            field("visualGenre", direction["visualGenre"]),
        ]
        direction_fields[5:5] = [
            field("dominantSilhouette", direction["dominantSilhouette"]),
            field("compositionFamily", direction["compositionFamily"]),
        ]
    else:
        direction_fields[3:3] = [
            field("interfaceArchetype", direction["interfaceArchetype"]),
            field("layoutThesis", direction["layoutThesis"]),
            field("hierarchyStrategy", direction["hierarchyStrategy"]),
            field("densityRhythm", direction["densityRhythm"]),
        ]
    return [
        {
            "key": "intent",
            "fields": [
                field("familyId", asset["familyId"]),
                field("assetId", asset["id"]),
                field("promptContractVersion", asset["promptContractVersion"]),
                field("conceptType", asset["conceptType"]),
                field("deliveryIntent", asset["deliveryIntent"]),
                field("assetRole", asset["role"]),
                field("maturity", asset["maturity"]),
                field("truthBoundary", asset["truthBoundary"]),
                field("medium", asset["medium"]),
                field("intendedUse", asset["intendedUse"]),
            ],
        },
        {
            "key": "direction",
            "fields": direction_fields,
        },
    ]


def append_tail_sections(
    sections: list[dict[str, Any]], contract: dict[str, Any]
) -> None:
    asset = contract["asset"]
    if asset["referenceRoles"]:
        sections.append(
            {
                "key": "referenceRoles",
                "fields": [field("referenceRoles", asset["referenceRoles"])],
            }
        )
    sections.extend(
        [
            {
                "key": "fixedAnchors",
                "fields": [field("fixedAnchors", asset["fixedAnchors"])],
            },
            {
                "key": "explorationAxis",
                "fields": [field("explorationAxis", asset["explorationAxis"])],
            },
            {
                "key": "constraints",
                "fields": [field("constraints", asset["constraints"])],
            },
            {"key": "avoid", "fields": [field("avoid", asset["avoid"])]},
            {
                "key": "candidateSettings",
                "fields": [field("candidateSettings", contract["candidateSettings"])],
            },
        ]
    )


def build_visual_sections(contract: dict[str, Any]) -> list[dict[str, Any]]:
    asset = contract["asset"]
    direction = contract["direction"]
    sections = common_sections(contract)
    if "parentId" in asset:
        sections[0]["fields"].append(field("parentId", asset["parentId"]))
    if "stateId" in asset or "transition" in asset:
        continuity = []
        if "stateId" in asset:
            continuity.append(field("stateId", asset["stateId"]))
        if "transition" in asset:
            continuity.append(field("transition", asset["transition"]))
        sections.insert(1, {"key": "lineageAndContinuity", "fields": continuity})

    world_fields = [field("world", direction["world"])]
    for key in ("subject", "scene", "action"):
        if key in asset:
            world_fields.append(field(key, asset[key]))
    sections.extend(
        [
            {"key": "world", "fields": world_fields},
            {
                "key": "targetContext",
                "fields": [
                    field("targetRegion", asset["targetRegion"]),
                    field("aspectRatio", asset["aspectRatio"]),
                    field("cropBehavior", asset["cropBehavior"]),
                ],
            },
        ]
    )
    if "mountContract" in asset:
        sections.append(
            {
                "key": "mountContract",
                "fields": [field("mountContract", asset["mountContract"])],
            }
        )
    sections.append(
        {
            "key": "compositionPlan",
            "fields": composition_fields(asset["compositionPlan"]),
        }
    )
    if asset["variants"]:
        sections.append(
            {"key": "variants", "fields": [field("variants", asset["variants"])]}
        )
    sections.extend(
        [
            {
                "key": "cameraLogic",
                "fields": [field("camera", direction["camera"])],
            },
            {
                "key": "surfaceLogic",
                "fields": [
                    field("light", direction["light"]),
                    field("material", direction["material"]),
                    field("color", direction["color"]),
                ],
            },
            {
                "key": "textBoundary",
                "fields": [
                    field("rasterTextPolicy", asset["rasterTextPolicy"]),
                    field("visibleText", asset["visibleText"]),
                ],
            },
        ]
    )
    append_tail_sections(sections, contract)
    return sections


def build_ui_sections(contract: dict[str, Any]) -> list[dict[str, Any]]:
    asset = contract["asset"]
    direction = contract["direction"]
    sections = common_sections(contract)
    sections.extend(
        [
            {
                "key": "targetContext",
                "fields": [
                    field("targetRegion", asset["targetRegion"]),
                    field("aspectRatio", asset["aspectRatio"]),
                    field("targetFidelity", asset["targetFidelity"]),
                ],
            },
            {
                "key": "interfaceFramePlan",
                "fields": [
                    field(key, asset["interfaceFramePlan"][key])
                    for key in (
                        "viewport",
                        "navigationAndShell",
                        "regionGeometry",
                        "readingOrder",
                        "primaryTask",
                        "activeState",
                        "controlsAndAffordances",
                        "proofPlacement",
                        "contentDensity",
                        "responsiveBehavior",
                        "reconstructionBoundary",
                    )
                ],
            },
            {
                "key": "interfaceBoundary",
                "fields": [
                    field("usage", "reference-only; rebuild deterministically"),
                    field("requiredPresentation", "functional web interface"),
                    field(
                        "forbiddenPresentation",
                        [
                            "poster",
                            "advertising key visual",
                            "editorial cover",
                            "floating device mockup",
                            "cinematic object stage",
                            "concept-art presentation",
                        ],
                    ),
                    field("runtimeEvidence", False),
                ],
            },
            {
                "key": "surfaceLogic",
                "fields": [
                    field("material", direction["material"]),
                    field("color", direction["color"]),
                ],
            },
            {
                "key": "textBoundary",
                "fields": [
                    field("rasterTextPolicy", asset["rasterTextPolicy"]),
                    field("visibleText", asset["visibleText"]),
                ],
            },
        ]
    )
    append_tail_sections(sections, contract)
    return sections


def set_nested_value(container: dict[str, Any], path: list[str], value: Any) -> None:
    current = container
    for key in path[:-1]:
        child = current.get(key)
        if not isinstance(child, dict):
            raise ContractError(
                f"exploration binding cannot resolve {'.'.join(path)}"
            )
        current = child
    current[path[-1]] = deepcopy(value)


def value_for_target(value: Any, target_id: str) -> Any:
    if isinstance(value, dict):
        return value[target_id]
    return value


def build_candidate_targets(
    asset: dict[str, Any], binding: str, value: Any
) -> list[dict[str, Any]]:
    if asset["conceptType"] == "visual-asset":
        targets = deepcopy(
            asset["variants"]
            or [
                {
                    "id": "primary",
                    "targetRegion": asset["targetRegion"],
                    "aspectRatio": asset["aspectRatio"],
                    "cropBehavior": asset["cropBehavior"],
                    "compositionPlan": asset["compositionPlan"],
                }
            ]
        )
        if "mountContract" in asset:
            frames = {
                frame["id"]: frame
                for frame in asset["mountContract"]["breakpointFrames"]
            }
            for target in targets:
                target["mountFrame"] = deepcopy(frames[target["id"]])
    else:
        targets = [
            {
                "id": "primary",
                "targetRegion": asset["targetRegion"],
                "aspectRatio": asset["aspectRatio"],
                "targetFidelity": asset["targetFidelity"],
                "interfaceFramePlan": deepcopy(asset["interfaceFramePlan"]),
            }
        ]

    if binding.startswith("target."):
        path = binding.split(".")[1:]
        for target in targets:
            set_nested_value(
                target, path, value_for_target(value, target["id"])
            )
    for target in targets:
        target_path = f"candidate.targets[{target['id']}]"
        if asset["conceptType"] == "visual-asset":
            target["cropBehavior"] = require_text_logic(
                target, "cropBehavior", target_path
            )
            target["compositionPlan"] = validate_composition_plan(
                target["compositionPlan"], f"{target_path}.compositionPlan"
            )
        else:
            target["interfaceFramePlan"] = validate_interface_frame_plan(
                target["interfaceFramePlan"],
                f"{target_path}.interfaceFramePlan",
            )
    return targets


def build_candidates(contract: dict[str, Any]) -> list[dict[str, Any]]:
    asset = contract["asset"]
    direction = contract["direction"]
    axis = asset["explorationAxis"]
    candidates: list[dict[str, Any]] = []
    for index, value in enumerate(axis["allowedValues"], start=1):
        resolved_inputs: dict[str, Any] = {
            "direction": deepcopy(direction),
            "fixedAnchors": deepcopy(asset["fixedAnchors"]),
            "constraints": deepcopy(asset["constraints"]),
            "avoid": deepcopy(asset["avoid"]),
            "visibleText": deepcopy(asset["visibleText"]),
        }
        for key in ("subject", "scene", "action"):
            if key in asset:
                resolved_inputs[key] = asset[key]

        binding = axis["binding"]
        if binding.startswith("direction."):
            set_nested_value(
                resolved_inputs["direction"], binding.split(".")[1:], value
            )
        elif binding.startswith("asset."):
            resolved_inputs[binding.split(".", 1)[1]] = deepcopy(value)
        resolved_inputs["direction"] = validate_direction(
            resolved_inputs["direction"], asset["conceptType"]
        )
        for key in ("subject", "scene", "action"):
            if key in resolved_inputs:
                resolved_inputs[key] = require_string(
                    resolved_inputs, key, "candidate.resolvedInputs"
                )

        candidates.append(
            {
                "id": f"{asset['id']}-c{index:02d}",
                "index": index,
                "explorationDelta": {
                    "variable": axis["variable"],
                    "name": axis["name"],
                    "binding": binding,
                    "value": value,
                },
                "resolvedInputs": resolved_inputs,
                "targets": build_candidate_targets(asset, binding, value),
            }
        )
    return candidates


def build_adapter_request(contract: dict[str, Any]) -> dict[str, Any]:
    asset = contract["asset"]
    if asset["conceptType"] == "visual-asset":
        return {
            "profile": "prompt-engine-shot",
            "skill": "prompt-engine",
            "operation": "build_six_layer_prompt",
            "language": "zh-CN",
            "styleKey": "no_style",
            "spatialSource": "candidate.targets[].compositionPlan",
            "catalogOwnership": "external-prompt-engine",
            "assemblyOrder": [
                "subject",
                "action",
                "camera",
                "compositionDepth",
                "scene",
                "lightMaterialColor",
            ],
            "sourceMap": {
                "style": "adapterRequest.styleKey",
                "subject": "candidate.resolvedInputs.subject",
                "action": "candidate.resolvedInputs.action",
                "shot_size": "candidate.targets[].compositionPlan.shotDistance",
                "camera_angle": "candidate.targets[].compositionPlan.viewpoint",
                "composition": (
                    "candidate.targets[].compositionPlan in authorial field order"
                ),
                "depth_layer": (
                    "candidate.targets[].compositionPlan.depthLayers + "
                    "backgroundPressure"
                ),
                "scene": (
                    "candidate.resolvedInputs.direction.world + "
                    "candidate.resolvedInputs.scene"
                ),
                "objects": "candidate.resolvedInputs.direction.material",
                "lighting": "candidate.resolvedInputs.direction.light",
                "color_grading": "candidate.resolvedInputs.direction.color",
                "extra": (
                    "candidate.resolvedInputs.direction.camera + fixedAnchors + "
                    "constraints + direction.deletionRule + candidate target mountFrame"
                ),
            },
            "unboundInputs": [
                "camera_move",
                "technique",
                "atmosphere",
                "surface_detail",
                "dynamic_light",
                "emotion",
                "film_look",
                "render_quality",
                "particles",
                "bridge_type",
            ],
            "unboundPolicy": "leave empty; never auto-fill from a style catalog",
        }
    return {
        "profile": "imagegen-ui-mockup",
        "language": "zh-CN",
        "targetFidelity": asset["targetFidelity"],
        "publishable": False,
        "cinematicShotBuilder": False,
        "sourceMap": {
            "viewport": "candidate.targets[].interfaceFramePlan.viewport",
            "interfaceStructure": "candidate.targets[].interfaceFramePlan",
            "direction": "candidate.resolvedInputs.direction",
            "text": "candidate.resolvedInputs.visibleText as reference-only",
            "boundary": "compiled interfaceBoundary",
        },
    }


def compile_contract(contract: Any) -> dict[str, Any]:
    validated = validate_contract(contract)
    asset = validated["asset"]
    sections = (
        build_visual_sections(validated)
        if asset["conceptType"] == "visual-asset"
        else build_ui_sections(validated)
    )
    return {
        "schemaVersion": 2,
        "familyId": asset["familyId"],
        "assetId": asset["id"],
        "promptContractVersion": asset["promptContractVersion"],
        "adapterRequest": build_adapter_request(validated),
        "sections": sections,
        "candidates": build_candidates(validated),
    }


def render_value(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def render_text(compiled: dict[str, Any]) -> str:
    blocks: list[str] = []
    for section in compiled["sections"]:
        lines = ["[" + section["key"] + "]"]
        lines.extend(
            f"{item['key']}: {render_value(item['value'])}"
            for item in section["fields"]
        )
        blocks.append("\n".join(lines))
    blocks.append(
        "[adapterRequest]\n" + render_value(compiled["adapterRequest"])
    )
    blocks.append("[candidates]\n" + render_value(compiled["candidates"]))
    return "\n\n".join(blocks) + "\n"


def read_contract(path: Path) -> Any:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ContractError(f"contract file does not exist: {path}") from exc
    except OSError as exc:
        raise ContractError(f"cannot read contract file {path}: {exc}") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContractError(
            f"invalid JSON in {path} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compile an image direction into portable prompt-engine or UI-mockup "
            "adapter inputs."
        )
    )
    parser.add_argument("contract", type=Path, help="path to a UTF-8 JSON contract")
    parser.add_argument(
        "--format", choices=("text", "json"), default="text", dest="output_format"
    )
    args = parser.parse_args(argv)

    try:
        compiled = compile_contract(read_contract(args.contract))
    except ContractError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.output_format == "json":
        print(json.dumps(compiled, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render_text(compiled))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
