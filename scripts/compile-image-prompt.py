#!/usr/bin/env python3
"""Compile a Product Composer image contract into ordered prompt sections."""

from __future__ import annotations

import argparse
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

EXPLORATION_VARIABLES = {
    "abstraction-level",
    "action-phase",
    "atmospheric-density",
    "camera-height",
    "color-temperature",
    "crop",
    "environment-density",
    "exposure",
    "focal-scale",
    "lens-behavior",
    "light-direction",
    "light-softness",
    "material-response",
    "palette-balance",
    "prop-density",
    "shot-distance",
    "silhouette-variation",
    "subject-pose",
    "texture-scale",
    "viewpoint",
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


class ContractError(ValueError):
    """A validation error that can be corrected in the input contract."""


def require_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(f"{path} must be an object")
    return value


def require_string(container: dict[str, Any], key: str, path: str) -> str:
    field_path = f"{path}.{key}"
    if key not in container:
        raise ContractError(f"missing required field: {field_path}")
    value = container[key]
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{field_path} must be a non-empty string")
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
                f"{field_path} must be a non-empty string or a non-empty list of strings"
            )
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ContractError(
                    f"{field_path}[{index}] must be a non-empty string"
                )
        return value
    raise ContractError(
        f"{field_path} must be a non-empty string or a non-empty list of strings"
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


def require_aesthetic_stance(container: dict[str, Any]) -> list[str]:
    path = "direction.aestheticStance"
    stance = require_string_list(container, "aestheticStance", "direction")
    if len(stance) != 3:
        raise ContractError(
            f"{path} must contain exactly three concrete qualities; received {len(stance)}"
        )
    return stance


def validate_exploration_axis(value: Any) -> dict[str, Any]:
    path = "asset.explorationAxis"
    if isinstance(value, list):
        raise ContractError(
            f"{path} must declare exactly one axis object; received {len(value)} items"
        )
    axis = require_object(value, path)
    allowed_keys = {"variable", "name", "allowedValues"}
    unknown_keys = sorted(set(axis) - allowed_keys)
    if unknown_keys:
        raise ContractError(
            f"{path} contains unsupported fields: {', '.join(unknown_keys)}"
        )
    variable = require_string(axis, "variable", path)
    if variable not in EXPLORATION_VARIABLES:
        choices = ", ".join(sorted(EXPLORATION_VARIABLES))
        raise ContractError(
            f"{path}.variable must name one supported causal variable: {choices}; "
            f"received {variable!r}"
        )
    validated = {
        "variable": variable,
        "name": require_string(axis, "name", path),
    }
    if "allowedValues" in axis:
        validated["allowedValues"] = require_string_list(
            axis, "allowedValues", path
        )
    return validated


def validate_transition(asset: dict[str, Any]) -> dict[str, Any] | None:
    if "transition" not in asset:
        return None
    path = "asset.transition"
    transition = require_object(asset["transition"], path)
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


def validate_variants(asset: dict[str, Any]) -> list[dict[str, Any]]:
    value = asset.get("variants", [])
    if not isinstance(value, list):
        raise ContractError("asset.variants must be a list")
    variants = []
    seen_ids = set()
    for index, item in enumerate(value):
        path = f"asset.variants[{index}]"
        variant = require_object(item, path)
        variant_id = require_string(variant, "id", path)
        if variant_id in seen_ids:
            raise ContractError(f"duplicate asset variant id: {variant_id}")
        seen_ids.add(variant_id)
        variants.append(
            {
                "id": variant_id,
                "targetRegion": require_string(variant, "targetRegion", path),
                "aspectRatio": require_string(variant, "aspectRatio", path),
                "focalPoint": require_text_logic(variant, "focalPoint", path),
                "composition": require_text_logic(variant, "composition", path),
                "depthOrder": require_text_logic(variant, "depthOrder", path),
                "cropBehavior": require_text_logic(
                    variant, "cropBehavior", path
                ),
                "safeArea": require_text_logic(variant, "safeArea", path),
            }
        )
    return variants


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


def validate_reference_roles(asset: dict[str, Any]) -> list[dict[str, str]]:
    value = asset.get("referenceRoles", [])
    if not isinstance(value, list):
        raise ContractError("asset.referenceRoles must be a list")
    result: list[dict[str, str]] = []
    for index, item in enumerate(value):
        path = f"asset.referenceRoles[{index}]"
        reference = require_string(require_object(item, path), "reference", path)
        role = require_string(item, "role", path)
        result.append({"reference": reference, "role": role})
    return result


def validate_candidate_settings(contract: dict[str, Any]) -> dict[str, Any]:
    if "candidateSettings" not in contract:
        raise ContractError("missing required field: candidateSettings")
    settings = require_object(contract["candidateSettings"], "candidateSettings")
    allowed_keys = {
        "mode",
        "count",
        "selectionCriteria",
        "variationPolicy",
        "model",
        "version",
        "settings",
    }
    unknown_keys = sorted(set(settings) - allowed_keys)
    if unknown_keys:
        raise ContractError(
            "candidateSettings contains unsupported fields: "
            + ", ".join(unknown_keys)
        )
    mode = require_string(settings, "mode", "candidateSettings")
    if mode not in CANDIDATE_MODES:
        choices = ", ".join(sorted(CANDIDATE_MODES))
        raise ContractError(
            f"candidateSettings.mode must be one of: {choices}; received {mode!r}"
        )
    count = settings.get("count")
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ContractError("candidateSettings.count must be a positive integer")
    criteria = settings.get("selectionCriteria")
    if not isinstance(criteria, list) or not criteria:
        raise ContractError(
            "candidateSettings.selectionCriteria must contain at least one criterion"
        )
    for index, item in enumerate(criteria):
        if not isinstance(item, str) or not item.strip():
            raise ContractError(
                f"candidateSettings.selectionCriteria[{index}] must be a non-empty string"
            )
    validated = {
        "mode": mode,
        "count": count,
        "selectionCriteria": criteria,
    }
    for optional_key in ("variationPolicy", "model", "version"):
        if optional_key in settings:
            validated[optional_key] = require_string(
                settings, optional_key, "candidateSettings"
            )
    if "settings" in settings:
        validated["settings"] = require_object(
            settings["settings"], "candidateSettings.settings"
        )
    return validated


def validate_contract(contract: Any) -> dict[str, Any]:
    root = require_object(contract, "contract")
    if "direction" not in root:
        raise ContractError("missing required field: direction")
    if "asset" not in root:
        raise ContractError("missing required field: asset")
    direction = require_object(root["direction"], "direction")
    asset = require_object(root["asset"], "asset")

    validated_direction = {
        "thesis": require_string(direction, "thesis", "direction"),
        "aestheticStance": require_aesthetic_stance(direction),
        "tensionPair": require_string(direction, "tensionPair", "direction"),
        "visualGenre": require_string(direction, "visualGenre", "direction"),
        "attentionStrategy": require_text_logic(
            direction, "attentionStrategy", "direction"
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
        "material": require_text_logic(direction, "material", "direction"),
        "color": require_text_logic(direction, "color", "direction"),
    }

    if "explorationAxis" not in asset:
        raise ContractError("missing required field: asset.explorationAxis")
    validated_asset: dict[str, Any] = {
        "familyId": require_string(asset, "familyId", "asset"),
        "id": require_string(asset, "id", "asset"),
        "promptContractVersion": require_string(
            asset, "promptContractVersion", "asset"
        ),
        "role": require_string(asset, "role", "asset"),
        "maturity": require_string(asset, "maturity", "asset"),
        "truthBoundary": require_string(asset, "truthBoundary", "asset"),
        "medium": require_string(asset, "medium", "asset"),
        "intendedUse": require_string(asset, "intendedUse", "asset"),
        "targetRegion": require_string(asset, "targetRegion", "asset"),
        "aspectRatio": require_string(asset, "aspectRatio", "asset"),
        "focalPoint": require_text_logic(asset, "focalPoint", "asset"),
        "composition": require_text_logic(asset, "composition", "asset"),
        "depthOrder": require_text_logic(asset, "depthOrder", "asset"),
        "cropBehavior": require_text_logic(asset, "cropBehavior", "asset"),
        "safeArea": require_text_logic(asset, "safeArea", "asset"),
        "variants": validate_variants(asset),
        "fixedAnchors": require_string_list(asset, "fixedAnchors", "asset"),
        "explorationAxis": validate_exploration_axis(asset["explorationAxis"]),
        "referenceRoles": validate_reference_roles(asset),
        "constraints": require_string_list(asset, "constraints", "asset"),
        "avoid": require_string_list(asset, "avoid", "asset"),
    }
    for optional_key in ("parentId", "stateId", "subject", "scene", "action"):
        if optional_key in asset:
            validated_asset[optional_key] = require_string(
                asset, optional_key, "asset"
            )
    transition = validate_transition(asset)
    if transition is not None:
        validated_asset["transition"] = transition

    reject_quality_fluff(validated_direction, "direction")
    positive_asset_fields = {
        key: value
        for key, value in validated_asset.items()
        if key not in {"constraints", "avoid", "truthBoundary"}
    }
    reject_quality_fluff(positive_asset_fields, "asset")

    return {
        "direction": validated_direction,
        "asset": validated_asset,
        "candidateSettings": validate_candidate_settings(root),
    }


def field(key: str, value: Any) -> dict[str, Any]:
    return {"key": key, "value": value}


def build_sections(contract: dict[str, Any]) -> list[dict[str, Any]]:
    direction = contract["direction"]
    asset = contract["asset"]

    intent_fields = [
        field("familyId", asset["familyId"]),
        field("assetId", asset["id"]),
        field("promptContractVersion", asset["promptContractVersion"]),
        field("assetRole", asset["role"]),
        field("maturity", asset["maturity"]),
        field("truthBoundary", asset["truthBoundary"]),
        field("medium", asset["medium"]),
        field("intendedUse", asset["intendedUse"]),
    ]
    if "parentId" in asset:
        intent_fields.append(field("parentId", asset["parentId"]))

    sections = [
        {"key": "intent", "fields": intent_fields},
        {
            "key": "direction",
            "fields": [
                field("directionThesis", direction["thesis"]),
                field("aestheticStance", direction["aestheticStance"]),
                field("tensionPair", direction["tensionPair"]),
                field("visualGenre", direction["visualGenre"]),
                field("attentionStrategy", direction["attentionStrategy"]),
                field("dominantSilhouette", direction["dominantSilhouette"]),
                field("compositionFamily", direction["compositionFamily"]),
            ],
        },
        {
            "key": "world",
            "fields": [field("world", direction["world"])],
        },
        {
            "key": "targetContext",
            "fields": [
                field("targetRegion", asset["targetRegion"]),
                field("aspectRatio", asset["aspectRatio"]),
                field("focalPoint", asset["focalPoint"]),
                field("composition", asset["composition"]),
                field("depthOrder", asset["depthOrder"]),
                field("cropBehavior", asset["cropBehavior"]),
                field("safeArea", asset["safeArea"]),
            ],
        },
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
            "key": "fixedAnchors",
            "fields": [field("fixedAnchors", asset["fixedAnchors"])],
        },
        {
            "key": "explorationAxis",
            "fields": [field("explorationAxis", asset["explorationAxis"])],
        },
    ]
    for optional_key in ("subject", "scene", "action"):
        if optional_key in asset:
            sections[2]["fields"].append(field(optional_key, asset[optional_key]))
    if "stateId" in asset or "transition" in asset:
        continuity_fields = []
        if "stateId" in asset:
            continuity_fields.append(field("stateId", asset["stateId"]))
        if "transition" in asset:
            continuity_fields.append(field("transition", asset["transition"]))
        sections.insert(
            1,
            {"key": "lineageAndContinuity", "fields": continuity_fields},
        )
    target_index = next(
        index for index, section in enumerate(sections)
        if section["key"] == "targetContext"
    )
    if asset["variants"]:
        sections.insert(
            target_index + 1,
            {
                "key": "variants",
                "fields": [field("variants", asset["variants"])],
            },
        )
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
                "key": "constraints",
                "fields": [field("constraints", asset["constraints"])],
            },
            {"key": "avoid", "fields": [field("avoid", asset["avoid"])]},
            {
                "key": "candidateSettings",
                "fields": [
                    field("candidateSettings", contract["candidateSettings"])
                ],
            },
        ]
    )
    return sections


def compile_contract(contract: Any) -> dict[str, Any]:
    validated = validate_contract(contract)
    return {
        "schemaVersion": 1,
        "familyId": validated["asset"]["familyId"],
        "assetId": validated["asset"]["id"],
        "promptContractVersion": validated["asset"]["promptContractVersion"],
        "sections": build_sections(validated),
    }


def render_text(compiled: dict[str, Any]) -> str:
    blocks = []
    for section in compiled["sections"]:
        lines = ["[" + section["key"] + "]"]
        for item in section["fields"]:
            value = item["value"]
            if isinstance(value, str):
                rendered = value
            else:
                rendered = json.dumps(
                    value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
                )
            lines.append(f"{item['key']}: {rendered}")
        blocks.append("\n".join(lines))
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
        description="Compile an image direction and asset contract into ordered prompt sections."
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
