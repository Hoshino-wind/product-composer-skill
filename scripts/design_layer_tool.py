#!/usr/bin/env python3
import argparse
import html
import json
import sys
from pathlib import Path


KNOWN_LAYER_TYPES = {"text", "shape", "image", "chart", "group"}


class LayerDocumentError(Exception):
    pass


def load_document(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise LayerDocumentError(f"invalid JSON: {exc}") from exc


def require_number(obj, key, context):
    value = obj.get(key)
    if not isinstance(value, (int, float)) or value < 0:
        raise LayerDocumentError(f"{context}.{key} must be a non-negative number")
    return value


def validate_layer(layer, context):
    if not isinstance(layer, dict):
        raise LayerDocumentError(f"{context} must be an object")
    layer_id = layer.get("id")
    if not isinstance(layer_id, str) or not layer_id:
        raise LayerDocumentError(f"{context}.id is required")
    layer_type = layer.get("type")
    if layer_type not in KNOWN_LAYER_TYPES:
        raise LayerDocumentError(f"unknown layer type: {layer_type!r} at {context}")
    for key in ("x", "y", "width", "height"):
        require_number(layer, key, context)
    if layer["width"] == 0 or layer["height"] == 0:
        raise LayerDocumentError(f"{context} width and height must be greater than 0")
    if layer_type == "text" and not isinstance(layer.get("text"), str):
        raise LayerDocumentError(f"{context}.text is required for text layers")
    if layer_type == "chart":
        data = layer.get("data")
        if not isinstance(data, list) or not data:
            raise LayerDocumentError(f"{context}.data must be a non-empty list for chart layers")
        for index, item in enumerate(data):
            item_ctx = f"{context}.data[{index}]"
            if not isinstance(item, dict):
                raise LayerDocumentError(f"{item_ctx} must be an object")
            if not isinstance(item.get("label"), str):
                raise LayerDocumentError(f"{item_ctx}.label is required")
            value = item.get("value")
            if not isinstance(value, (int, float)) or value < 0:
                raise LayerDocumentError(f"{item_ctx}.value must be a non-negative number")
    if layer_type == "group":
        children = layer.get("layers")
        if not isinstance(children, list):
            raise LayerDocumentError(f"{context}.layers must be a list for group layers")
        for index, child in enumerate(children):
            validate_layer(child, f"{context}.layers[{index}]")


def validate_document(doc):
    if not isinstance(doc, dict):
        raise LayerDocumentError("document must be an object")
    canvas = doc.get("canvas")
    if not isinstance(canvas, dict):
        raise LayerDocumentError("canvas is required")
    width = canvas.get("width")
    height = canvas.get("height")
    if not isinstance(width, (int, float)) or width <= 0:
        raise LayerDocumentError("canvas.width must be greater than 0")
    if not isinstance(height, (int, float)) or height <= 0:
        raise LayerDocumentError("canvas.height must be greater than 0")
    pages = doc.get("pages")
    if not isinstance(pages, list) or not pages:
        raise LayerDocumentError("pages must be a non-empty list")
    page_ids = set()
    for page_index, page in enumerate(pages):
        context = f"pages[{page_index}]"
        if not isinstance(page, dict):
            raise LayerDocumentError(f"{context} must be an object")
        page_id = page.get("id")
        if not isinstance(page_id, str) or not page_id:
            raise LayerDocumentError(f"{context}.id is required")
        if page_id in page_ids:
            raise LayerDocumentError(f"duplicate page id: {page_id}")
        page_ids.add(page_id)
        layers = page.get("layers")
        if not isinstance(layers, list):
            raise LayerDocumentError(f"{context}.layers must be a list")
        layer_ids = set()
        for layer_index, layer in enumerate(layers):
            validate_layer(layer, f"{context}.layers[{layer_index}]")
            layer_id = layer["id"]
            if layer_id in layer_ids:
                raise LayerDocumentError(f"duplicate layer id on page {page_id}: {layer_id}")
            layer_ids.add(layer_id)
    return doc


def style_value(style, key, fallback=None):
    if isinstance(style, dict) and key in style:
        return style[key]
    return fallback


def layer_css(layer, canvas):
    style = layer.get("style") or {}
    declarations = {
        "position": "absolute",
        "left": f"{layer['x']}px",
        "top": f"{layer['y']}px",
        "width": f"{layer['width']}px",
        "height": f"{layer['height']}px",
        "box-sizing": "border-box",
    }
    if "opacity" in style:
        declarations["opacity"] = str(style["opacity"])
    if layer["type"] == "text":
        declarations["font-size"] = f"{style_value(style, 'fontSize', 18)}px"
        declarations["font-weight"] = str(style_value(style, "fontWeight", 400))
        declarations["color"] = style_value(style, "color", "#111827")
        declarations["line-height"] = str(style_value(style, "lineHeight", 1.15))
    elif layer["type"] == "shape":
        declarations["background"] = style_value(style, "fill", "transparent")
        declarations["border-radius"] = f"{style_value(style, 'radius', 0)}px"
        if "stroke" in style:
            declarations["border"] = f"{style_value(style, 'strokeWidth', 1)}px solid {style['stroke']}"
    elif layer["type"] == "image":
        declarations["overflow"] = "hidden"
        declarations["background"] = style_value(style, "fill", "#dbe5f4")
    elif layer["type"] == "chart":
        declarations["display"] = "flex"
        declarations["align-items"] = "end"
        declarations["gap"] = "12px"
        declarations["padding"] = "20px"
        declarations["background"] = style_value(style, "background", "rgba(255,255,255,0.75)")
        declarations["border-radius"] = f"{style_value(style, 'radius', 18)}px"
    return "; ".join(f"{key}: {value}" for key, value in declarations.items())


def render_chart_html(layer):
    data = layer.get("data", [])
    max_value = max((item["value"] for item in data), default=1) or 1
    fill = html.escape(style_value(layer.get("style") or {}, "fill", "#2f6df6"))
    parts = []
    for item in data:
        height = max(6, round((item["value"] / max_value) * 100))
        label = html.escape(item["label"])
        parts.append(
            "<div class=\"dl-chart-item\">"
            f"<div class=\"dl-chart-bar\" style=\"height:{height}%;background:{fill}\"></div>"
            f"<div class=\"dl-chart-label\">{label}</div>"
            "</div>"
        )
    return "".join(parts)


def render_layer_html(layer, canvas):
    layer_id = html.escape(layer["id"])
    layer_type = layer["type"]
    css = html.escape(layer_css(layer, canvas), quote=True)
    if layer_type == "text":
        text = html.escape(layer.get("text", ""))
        return f'<div class="dl-layer dl-text" data-layer-id="{layer_id}" style="{css}">{text}</div>'
    if layer_type == "shape":
        return f'<div class="dl-layer dl-shape" data-layer-id="{layer_id}" style="{css}"></div>'
    if layer_type == "image":
        src = layer.get("src")
        if src:
            src_attr = html.escape(src, quote=True)
            return f'<img class="dl-layer dl-image" data-layer-id="{layer_id}" src="{src_attr}" style="{css}" />'
        return f'<div class="dl-layer dl-image" data-layer-id="{layer_id}" style="{css}"></div>'
    if layer_type == "chart":
        return f'<div class="dl-layer dl-chart" data-layer-id="{layer_id}" style="{css}">{render_chart_html(layer)}</div>'
    if layer_type == "group":
        children = "".join(render_layer_html(child, canvas) for child in layer.get("layers", []))
        return f'<div class="dl-layer dl-group" data-layer-id="{layer_id}" style="{css}">{children}</div>'
    raise AssertionError(layer_type)


def export_html(doc, out_path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas = doc["canvas"]
    body = []
    for page in doc["pages"]:
        layers = "".join(render_layer_html(layer, canvas) for layer in page.get("layers", []))
        page_name = html.escape(page.get("name") or page["id"])
        body.append(
            f'<section class="dl-page" data-page-id="{html.escape(page["id"])}" aria-label="{page_name}">'
            f"{layers}</section>"
        )
    background = html.escape(canvas.get("background", "#ffffff"), quote=True)
    font = html.escape((doc.get("theme") or {}).get("fontFamily", "Inter, Arial, sans-serif"), quote=True)
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Design Layer Document</title>
  <style>
    body {{ margin: 0; background: #f3f6fb; font-family: {font}; }}
    .dl-page {{
      position: relative;
      width: {canvas['width']}px;
      height: {canvas['height']}px;
      margin: 32px auto;
      overflow: hidden;
      background: {background};
      box-shadow: 0 24px 80px rgba(20, 36, 66, 0.16);
    }}
    .dl-chart-item {{ flex: 1; height: 100%; display: flex; flex-direction: column; justify-content: end; min-width: 0; }}
    .dl-chart-bar {{ width: 100%; min-height: 6px; border-radius: 8px 8px 0 0; }}
    .dl-chart-label {{ margin-top: 8px; font-size: 12px; color: #334155; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  </style>
</head>
<body>
{''.join(body)}
</body>
</html>
"""
    out_path.write_text(content, encoding="utf-8")


def command_validate(args):
    validate_document(load_document(args.input))
    print(f"valid: {args.input}")


def command_html(args):
    doc = validate_document(load_document(args.input))
    export_html(doc, args.output)
    print(f"wrote: {args.output}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Validate and export Product Composer design layer documents."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate a .layerdoc.json file")
    validate.add_argument("input")
    validate.set_defaults(func=command_validate)

    html_parser = subparsers.add_parser("html", help="Export a .layerdoc.json file to editable HTML")
    html_parser.add_argument("input")
    html_parser.add_argument("output")
    html_parser.set_defaults(func=command_html)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except LayerDocumentError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
