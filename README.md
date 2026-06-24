# Product Composer Skill

Product Composer is a Codex skill for designing, critiquing, generating, and implementing high-quality product UI surfaces.

It is built for cases where a normal UI prompt tends to produce generic SaaS pages, crowded dashboards, weak visual hierarchy, or attractive but unusable mockups. The skill pushes Codex to treat UI as a product system: clear mission, deliberate content judgment, distinctive visual direction, interaction grammar, and verification.

## What It Helps With

- Official websites, landing pages, and product-led homepages
- SaaS apps, dashboards, admin panels, forms, and data views
- AI products, agent workflows, command surfaces, and frontier interaction models
- Cultural, editorial, museum, hospitality, portfolio, and premium brand pages
- Product content pages that need desire, clarity, and visual continuity
- Image-generated UI mockups that should avoid template-like AI aesthetics
- Editable layer documents, HTML previews, and PPTX exports
- Existing UI critique and redesign direction

## Core Ideas

### Product Clarity

Every surface starts from the user mission: what the viewer or operator needs to understand, choose, complete, or desire. The skill favors task structure, state clarity, progressive disclosure, and reusable product patterns.

### Signature Visual System

Good UI is not just layout. Strong pages often work because every visible choice belongs to one coherent world.

The skill includes a `signature-aesthetic-systems` reference that turns this into a repeatable method:

- identify subject-native motifs and evidence
- choose one dominant spatial metaphor
- derive a palette from the subject, product, or material world
- define a continuity device across screens
- make UI controls feel native to the visual system
- remove anything that weakens the world

This was distilled from a successful Dunhuang Museum page direction, but the method is general. It does not copy Dunhuang motifs unless the subject actually calls for them.

### Desire-Led Minimalism

Minimalism is treated as focus, not emptiness. The skill asks what desire the page should create: curiosity, confidence, relief, mastery, aspiration, participation, or belonging. Color, layout, proof, and interaction are then chosen to support that job.

### Interaction Grammar

For AI, agentic, automation, creative, or complex workflow products, the skill defines the interaction relationship before choosing components. It distinguishes cognitive interaction design from literal drag, slide, and click labels.

### Design Layer Documents

The skill can also turn a UI concept into a structured `.layerdoc.json` file. This gives the design a stable intermediate representation:

```text
brief / image / data
-> semantic layers
-> .layerdoc.json
-> HTML preview
-> PPTX export
```

This is useful when a generated UI should become an editable deck or a future visual editor surface, not just a flat PNG.

## Installation

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Hoshino-wind/product-composer-skill.git ~/.codex/skills/product-composer
```

Restart Codex or reload skills if your environment requires it.

## Usage

Invoke the skill explicitly:

```text
Use $product-composer to design a homepage UI for my product.
First create a signature system. Avoid SaaS templates.
Generate a polished image mockup, no code.
```

For a product surface:

```text
Use $product-composer to redesign this dashboard.
Prioritize workflow clarity, hierarchy, state visibility, and reusable UI patterns.
```

For a cultural or editorial page:

```text
Use $product-composer to design a museum homepage.
Build a complete visual world with source motifs, palette origin, and multi-screen continuity.
```

For an AI product:

```text
Use $product-composer to design a frontier AI workflow surface.
Define the interaction grammar before layout. Do not use fake drag or node-graph aesthetics.
```

For an editable deck pipeline:

```text
Use $product-composer to convert this homepage concept into a design layer document.
Export an HTML preview and a PPTX with editable text, shapes, and chart layers.
```

## Reference Map

The main skill file routes Codex to focused references only when needed:

- `references/ant-design-product-values.md` - enterprise product order and Ant Design-inspired values
- `references/impeccable-execution-model.md` - execution discipline for non-generic UI
- `references/interaction-grammar.md` - new interaction models for AI and complex workflows
- `references/taste-calibration.md` - taste gates and anti-generic critique
- `references/market-calibration.md` - product homepage calibration against real market expectations
- `references/content-judgment.md` - deciding what to keep, defer, and delete
- `references/desire-minimalism-psychology.md` - minimalism that creates product desire
- `references/image-generation-aesthetic-calibration.md` - prompts and repair passes for UI image generation
- `references/visual-direction.md` - composition, palette, material, and silhouette guidance
- `references/signature-aesthetic-systems.md` - complete visual worlds and multi-screen continuity
- `references/design-layer-document.md` - semantic layer documents for HTML/PPTX export
- `references/anti-patterns.md` - common AI UI and product design failures
- `references/verification.md` - final verification guidance

## Included Tooling

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

The scanner flags common visual anti-patterns in frontend projects. Treat the output as warnings, then confirm visually.

Validate and export a design layer document:

```bash
python3 scripts/design_layer_tool.py validate examples/opc-homepage.layerdoc.json
python3 scripts/design_layer_tool.py html examples/opc-homepage.layerdoc.json outputs/opc-homepage.html
python3 scripts/design_layer_tool.py pptx examples/opc-homepage.layerdoc.json outputs/opc-homepage.pptx
```

The current MVP exports editable text, shapes, image placeholders, and simple bar charts. Native PowerPoint charts, tables, masks, complex gradients, and typography-perfect line wrapping are planned extension points.

## Validation

Validate the skill structure with Codex's skill validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/product-composer
```

Expected result:

```text
Skill is valid!
```

## License

MIT License. See [LICENSE](LICENSE).
