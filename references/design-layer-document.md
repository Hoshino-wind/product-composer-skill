# Design Layer Document

Use this when a design needs to become editable UI output: HTML, chart/table layers, or a future visual editor. The goal is to turn design intent and visual composition into structured elements instead of a flat image.

## Principle

Use `.layerdoc.json` as the source of truth.

Do not treat generated UI images or HTML as the only canonical representation. Images are good for taste exploration; HTML is good for editing and preview. The layer document is the stable bridge between them.

## Pipeline

```text
brief / image / data
-> semantic layer decomposition
-> .layerdoc.json
-> HTML preview and element editing
```

## Document Shape

Minimum shape:

```json
{
  "version": "0.1",
  "canvas": {
    "width": 1600,
    "height": 1000,
    "background": "#eef4ff"
  },
  "theme": {
    "fontFamily": "Inter, Arial, sans-serif",
    "colors": {
      "ink": "#10223f",
      "surface": "#ffffff",
      "accent": "#2f6df6"
    }
  },
  "pages": [
    {
      "id": "home",
      "name": "Homepage",
      "layers": []
    }
  ]
}
```

## Layer Types

### `text`

Editable text block.

Required: `id`, `type`, `text`, `x`, `y`, `width`, `height`.

Useful style keys: `fontSize`, `fontWeight`, `color`, `lineHeight`.

### `shape`

Editable rectangle or rounded rectangle.

Required: `id`, `type`, `x`, `y`, `width`, `height`.

Useful style keys: `fill`, `stroke`, `strokeWidth`, `radius`, `opacity`.

### `image`

Image or image placeholder. Use for generated illustrations, photos, complex textures, or bitmap islands.

Required: `id`, `type`, `x`, `y`, `width`, `height`.

Optional: `src`.

### `chart`

Chart layer with data. The exporter renders simple bar charts as div-based bars in HTML.

Required: `id`, `type`, `chart`, `data`, `x`, `y`, `width`, `height`.

Data shape:

```json
[
  { "label": "Draft", "value": 32 },
  { "label": "Reviewed", "value": 68 },
  { "label": "Approved", "value": 92 }
]
```

### `group`

Semantic grouping for repeated sections or product objects. Group child layers under `layers`.

## Authoring Rules

- Keep meaningful layers, not pixel fragments.
- Use `role` to preserve intent: `headline`, `cta`, `proof`, `navigation`, `background`, `decoration`, `chart`, `table`, `artifact`.
- Keep repeated content as data plus a template layer when possible.
- Do not flatten charts into decorative rectangles unless the chart is purely illustrative.
- Use image layers only for content that cannot reasonably stay editable.
- Use stable layer ids so edits can be traced back.

## Export Commands

```bash
python3 scripts/design_layer_tool.py validate examples/opc-homepage.layerdoc.json
python3 scripts/design_layer_tool.py html examples/opc-homepage.layerdoc.json outputs/opc-homepage.html
```

## Current MVP Limits

- HTML export supports editable text, shapes, image placeholders, and simple bar charts rendered as structured DOM.
- Native editor bindings, tables, masks, complex gradients, blend modes, and typography-perfect line wrapping are future extensions.
- Image-derived layer extraction is still an authoring step: infer the layer document first, then export.

## Quality Checks

Before claiming an export works:

- Run `validate`.
- Open or inspect the HTML for obvious layer positions.
- Keep the `.layerdoc.json` alongside exported HTML for future edits.
