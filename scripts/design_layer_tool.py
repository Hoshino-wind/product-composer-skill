#!/usr/bin/env python3
import argparse
import html
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


EMU_PER_PX = 9144
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


def hex_color(value, fallback="000000"):
    if not isinstance(value, str):
        return fallback
    value = value.strip()
    if value.startswith("#"):
        value = value[1:]
    if len(value) == 3 and all(ch in "0123456789abcdefABCDEF" for ch in value):
        return "".join(ch * 2 for ch in value).upper()
    if len(value) == 6 and all(ch in "0123456789abcdefABCDEF" for ch in value):
        return value.upper()
    return fallback


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


def emu(value):
    return str(round(float(value) * EMU_PER_PX))


def ppt_color(value, fallback="000000"):
    return hex_color(value, fallback)


def ppt_text_run(text, style=None):
    style = style or {}
    size = int(round(float(style_value(style, "fontSize", 18)) * 100))
    bold = ' b="1"' if int(style_value(style, "fontWeight", 400)) >= 600 else ""
    color = ppt_color(style_value(style, "color", "#111827"))
    return (
        f'<a:r><a:rPr lang="en-US" sz="{size}"{bold}>'
        f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'</a:rPr><a:t>{escape(text)}</a:t></a:r>'
    )


def ppt_shape(layer, shape_id):
    style = layer.get("style") or {}
    layer_type = layer["type"]
    prst = "roundRect" if style_value(style, "radius", 0) else "rect"
    fill = style_value(style, "fill", None)
    if layer_type == "image":
        fill = style_value(style, "fill", "#dbe5f4")
    fill_xml = (
        f'<a:solidFill><a:srgbClr val="{ppt_color(fill)}"/></a:solidFill>'
        if fill
        else "<a:noFill/>"
    )
    stroke = style_value(style, "stroke", None)
    stroke_xml = (
        f'<a:ln w="{emu(style_value(style, "strokeWidth", 1))}"><a:solidFill><a:srgbClr val="{ppt_color(stroke)}"/></a:solidFill></a:ln>'
        if stroke
        else "<a:ln><a:noFill/></a:ln>"
    )
    text_xml = ""
    tx_box = ""
    if layer_type == "text":
        tx_box = ' txBox="1"'
        text_xml = (
            '<p:txBody><a:bodyPr wrap="square" rtlCol="0"/><a:lstStyle/>'
            f'<a:p>{ppt_text_run(layer.get("text", ""), style)}</a:p></p:txBody>'
        )
        fill_xml = "<a:noFill/>"
    return f"""<p:sp>
  <p:nvSpPr><p:cNvPr id="{shape_id}" name="{escape(layer['id'])}"/><p:cNvSpPr{tx_box}/><p:nvPr/></p:nvSpPr>
  <p:spPr><a:xfrm><a:off x="{emu(layer['x'])}" y="{emu(layer['y'])}"/><a:ext cx="{emu(layer['width'])}" cy="{emu(layer['height'])}"/></a:xfrm><a:prstGeom prst="{prst}"><a:avLst/></a:prstGeom>{fill_xml}{stroke_xml}</p:spPr>
  {text_xml}
</p:sp>"""


def ppt_chart(layer, first_shape_id):
    data = layer.get("data", [])
    style = layer.get("style") or {}
    max_value = max((item["value"] for item in data), default=1) or 1
    gap = 12
    label_height = 22
    plot_padding = 18
    bar_count = max(1, len(data))
    usable_width = layer["width"] - plot_padding * 2 - gap * (bar_count - 1)
    bar_width = max(8, usable_width / bar_count)
    plot_height = layer["height"] - plot_padding * 2 - label_height
    parts = [
        ppt_shape(
            {
                **layer,
                "type": "shape",
                "shape": "roundRect",
                "style": {
                    "fill": style_value(style, "background", "#ffffff"),
                    "stroke": style_value(style, "axis", "#d7e1f0"),
                    "strokeWidth": 1,
                    "radius": style_value(style, "radius", 18),
                },
            },
            first_shape_id,
        )
    ]
    shape_id = first_shape_id + 1
    for index, item in enumerate(data):
        bar_h = max(4, (item["value"] / max_value) * plot_height)
        x = layer["x"] + plot_padding + index * (bar_width + gap)
        y = layer["y"] + plot_padding + (plot_height - bar_h)
        parts.append(
            ppt_shape(
                {
                    "id": f"{layer['id']}-{index}-bar",
                    "type": "shape",
                    "shape": "rect",
                    "x": x,
                    "y": y,
                    "width": bar_width,
                    "height": bar_h,
                    "style": {"fill": style_value(style, "fill", "#2f6df6"), "radius": 4},
                },
                shape_id,
            )
        )
        shape_id += 1
        parts.append(
            ppt_shape(
                {
                    "id": f"{layer['id']}-{index}-label",
                    "type": "text",
                    "text": item["label"],
                    "x": x,
                    "y": layer["y"] + layer["height"] - plot_padding - label_height,
                    "width": bar_width,
                    "height": label_height,
                    "style": {"fontSize": 11, "color": style_value(style, "text", "#10223f")},
                },
                shape_id,
            )
        )
        shape_id += 1
    return "".join(parts), shape_id


def ppt_layers(layers, start_shape_id=2):
    parts = []
    shape_id = start_shape_id
    for layer in layers:
        if layer["type"] == "group":
            group_xml, shape_id = ppt_layers(layer.get("layers", []), shape_id)
            parts.append(group_xml)
        elif layer["type"] == "chart":
            chart_xml, shape_id = ppt_chart(layer, shape_id)
            parts.append(chart_xml)
        else:
            parts.append(ppt_shape(layer, shape_id))
            shape_id += 1
    return "".join(parts), shape_id


def slide_xml(page, doc):
    canvas = doc["canvas"]
    bg = ppt_color(canvas.get("background", "#ffffff"), "FFFFFF")
    layers_xml, _ = ppt_layers(page.get("layers", []))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="{bg}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {layers_xml}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def content_types(page_count):
    slides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, page_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  {slides}
</Types>"""


def presentation_xml(doc):
    canvas = doc["canvas"]
    slide_ids = "\n".join(
        f'<p:sldId id="{256 + index}" r:id="rId{index + 2}"/>'
        for index, _ in enumerate(doc["pages"])
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{slide_ids}</p:sldIdLst>
  <p:sldSz cx="{emu(canvas['width'])}" cy="{emu(canvas['height'])}" type="custom"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>"""


def presentation_rels(page_count):
    rels = "\n".join(
        f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        for i in range(1, page_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  {rels}
</Relationships>"""


def slide_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>"""


def slide_master_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>"""


def slide_master_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>"""


def slide_layout_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank">
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>"""


def slide_layout_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>"""


def theme_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Product Composer">
  <a:themeElements>
    <a:clrScheme name="Product Composer">
      <a:dk1><a:srgbClr val="10223F"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1E293B"/></a:dk2>
      <a:lt2><a:srgbClr val="EEF4FF"/></a:lt2>
      <a:accent1><a:srgbClr val="2F6DF6"/></a:accent1>
      <a:accent2><a:srgbClr val="D69A27"/></a:accent2>
      <a:accent3><a:srgbClr val="53657F"/></a:accent3>
      <a:accent4><a:srgbClr val="7890B3"/></a:accent4>
      <a:accent5><a:srgbClr val="D7E1F0"/></a:accent5>
      <a:accent6><a:srgbClr val="F8FBFF"/></a:accent6>
      <a:hlink><a:srgbClr val="2F6DF6"/></a:hlink>
      <a:folHlink><a:srgbClr val="6B5CA5"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Product Composer">
      <a:majorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>
      <a:minorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Product Composer">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>"""


def root_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def app_props():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Product Composer Design Layer Tool</Application>
</Properties>"""


def core_props():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Design Layer Document</dc:title>
  <dc:creator>Product Composer</dc:creator>
  <cp:lastModifiedBy>Product Composer</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:modified>
</cp:coreProperties>"""


def export_pptx(doc, out_path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types(len(doc["pages"])))
        package.writestr("_rels/.rels", root_rels())
        package.writestr("docProps/app.xml", app_props())
        package.writestr("docProps/core.xml", core_props())
        package.writestr("ppt/presentation.xml", presentation_xml(doc))
        package.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(len(doc["pages"])))
        package.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        package.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rels())
        package.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        package.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rels())
        package.writestr("ppt/theme/theme1.xml", theme_xml())
        for index, page in enumerate(doc["pages"], start=1):
            package.writestr(f"ppt/slides/slide{index}.xml", slide_xml(page, doc))
            package.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", slide_rels())


def command_validate(args):
    validate_document(load_document(args.input))
    print(f"valid: {args.input}")


def command_html(args):
    doc = validate_document(load_document(args.input))
    export_html(doc, args.output)
    print(f"wrote: {args.output}")


def command_pptx(args):
    doc = validate_document(load_document(args.input))
    export_pptx(doc, args.output)
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

    pptx_parser = subparsers.add_parser("pptx", help="Export a .layerdoc.json file to editable PPTX")
    pptx_parser.add_argument("input")
    pptx_parser.add_argument("output")
    pptx_parser.set_defaults(func=command_pptx)
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
