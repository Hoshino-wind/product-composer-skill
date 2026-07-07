# Product Composer Skill

English | [Chinese](README.zh-CN.md)

Product Composer is a Codex skill for creating and implementing UI with stronger taste, clearer visual direction, and better control over AI-generated aesthetics.

It is built for cases where a normal UI prompt tends to produce generic SaaS pages, crowded dashboards, weak visual hierarchy, or attractive but unusable mockups. The skill pushes Codex to treat UI as a product system: clear mission, deliberate content judgment, distinctive visual direction, interaction grammar, asset context, design memory, and rendered verification.

## What It Helps With

- Official websites, landing pages, and product-led homepages
- SaaS apps, dashboards, admin panels, forms, and data views
- AI products, agent workflows, command surfaces, and frontier interaction models
- Cultural, editorial, museum, hospitality, portfolio, and premium brand pages
- Product content pages that need desire, clarity, and visual continuity
- Image-generated UI mockups that should avoid template-like AI aesthetics
- User-provided, local, or imagegen-generated asset workflows
- Coded UI implementation after a visual direction or concept is selected

## Core Ideas

### Aesthetic Control Loop

The skill keeps UI work centered on a short control loop:

1. Identify the generic-default risk.
2. Write one visual thesis.
3. Lock taste constraints and anti-defaults.
4. Compose or implement under that contract.
5. Verify the rendered result and repair the weakest visual decision.

### Product Clarity

Every surface starts from the user mission: what the viewer or operator needs to understand, choose, complete, or desire. The skill favors task structure, state clarity, progressive disclosure, and reusable product patterns.

### Signature Visual System

Good UI is not just layout. Strong pages often work because every visible choice belongs to one coherent world.

The skill includes a `signature-aesthetic-systems` reference that turns this into a repeatable method:

- identify subject-native motifs and material
- choose one dominant spatial metaphor
- derive a palette from the subject, product, or material world
- define a continuity device across screens
- make UI controls feel native to the visual system
- remove anything that weakens the world

### Style Family Routing

Before net-new UI generation, the skill can ask the user to choose a style family, density, and color appetite. This prevents two common failures: random visual direction and every result collapsing into the same premium-minimal homepage.

Example answer:

```text
B + sparse + warm and desirable
```

The routing also includes quality floors for practical product styles. Utility screens should not collapse into a generic admin shell, and technical surfaces should not become black cockpits, sci-fi dashboards, fake terminals, or command-center industrial fantasy. When that happens, the skill treats it as a failed direction and reroutes or repairs before regenerating.

### UI Generation Direction

The skill absorbs UI generation patterns into one local direction model: route, visual thesis, asset context, style dials, concept fidelity, implementation lock, and visual check.

The deeper layer is judgment: visual-quality scoring, direction matrices that vary the design thesis, and implementation locks that preserve accepted concepts.

The deepest layer is operating behavior: choose the surface register, write a design thesis before code, run a generic-default self-test, treat copy as design material, and verify implementation section by section.

### Desire-Led Minimalism

Minimalism is treated as focus, not emptiness. The skill asks what desire the page should create: curiosity, confidence, relief, mastery, aspiration, participation, or belonging. Color, layout, proof, and interaction are then chosen to support that job.

### Interaction Grammar

For AI, agentic, automation, creative, or complex workflow products, the skill defines the interaction relationship before choosing components. It distinguishes cognitive interaction design from literal drag, swipe, and click labels.

## Installation

Place this skill directory in your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
# expected location: ~/.codex/skills/product-composer
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

For selected concept implementation:

```text
Use $product-composer to implement the selected UI direction in React.
Preserve the visual thesis, hierarchy, palette roles, and responsive behavior.
```

## Reference Map

The main skill file routes Codex to focused references only when needed:

- `references/task-router.md` - choose the smallest route for UI design and implementation work
- `references/ant-design-product-values.md` - enterprise product order and Ant Design-inspired values
- `references/execution-discipline.md` - execution discipline for non-generic UI
- `references/style-family-router.md` - user style choices and visual family routing
- `references/interaction-grammar.md` - new interaction models for AI and complex workflows
- `references/taste-calibration.md` - taste gates and anti-generic judgment
- `references/market-calibration.md` - product homepage calibration against real market expectations
- `references/content-judgment.md` - deciding what to keep, defer, and delete
- `references/desire-minimalism-psychology.md` - minimalism that creates product desire
- `references/image-generation-aesthetic-calibration.md` - prompts and repair passes for UI image generation
- `references/ui-generation-operating-model.md` - deeper UI generation operating model for register, thesis, anti-template checks, and parity loops
- `references/asset-context-protocol.md` - gather user-provided, local, and imagegen-generated assets before design
- `references/design-memory-consistency.md` - preserve tokens, component decisions, spacing, depth, and surface consistency across work
- `references/visual-quality-rubric.md` - visual quality scoring for hierarchy, type, palette, material, and AI-flavored failure modes
- `references/reference-dna-extraction.md` - extracting design DNA from screenshots, references, and accepted mockups
- `references/direction-matrix-builder.md` - creating genuinely different visual directions before committing
- `references/concept-to-implementation-lock.md` - preserving accepted image concepts during coded implementation
- `references/visual-direction.md` - composition, palette, material, and silhouette guidance
- `references/react-bits-motion-layer.md` - expressive React motion and kinetic accent layers
- `references/signature-aesthetic-systems.md` - complete visual worlds and multi-screen continuity
- `references/anti-patterns.md` - common AI UI and product design failures
- `references/verification.md` - final verification guidance

Scenario examples live in `examples/scenarios/` and define expected routing behavior for UI design and implementation requests.

## Included Tooling

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

The scanner flags common visual anti-patterns in frontend projects. Treat the output as warnings, then confirm visually.

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

Apache License 2.0. See [LICENSE](LICENSE).
