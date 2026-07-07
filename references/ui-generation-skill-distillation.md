# UI Generation Skill Distillation

Use this reference when a UI task is broad, vague, image-first, Figma/reference-driven, screenshot-derived, design-system-driven, or when the user asks to absorb UI generation patterns into this skill.

## Core Model

Strong UI generation is a pipeline:

```text
context -> direction -> concept -> system -> implementation -> rendered check
```

Do not treat the prompt as the whole brief. Define the reference anchor first, then choose how much creative freedom is allowed.

## Distilled Patterns

### Judgment Layers

Use the focused references when the task needs more than workflow:

- `ui-generation-operating-model.md`: choose register, thesis, self-critique, and parity loop.
- `visual-quality-rubric.md`: decide whether a screen is composed, specific, and polished enough.
- `reference-dna-extraction.md`: extract the design logic from a reference before translating it.
- `direction-matrix-builder.md`: create directions with different theses, not cosmetic variants.
- `concept-to-implementation-lock.md`: preserve an accepted concept during implementation.

### Subject-Grounded Originality

The best design skills avoid generic SaaS output by grounding the surface in the subject's real material: product states, domain objects, culture, venue, workflow, data, or brand behavior.

Use when a design feels fashionable but unowned:

- identify the subject-native forms, assets, states, and proof objects
- make one of them the dominant visual object or interaction object
- derive palette and motion from the subject instead of trend colors
- remove decorative motifs that could belong to any product

### Image-First Specification

When generating a visual concept before code, the image is not only inspiration. Once accepted, it becomes a fidelity contract.

Use this sequence:

1. Generate or select the concept with visible hierarchy, palette, density, and dominant object.
2. Name the stable elements that must survive implementation.
3. Build the UI around those elements.
4. Compare rendered output against the concept before claiming completion.

Do not reinterpret an accepted image into a safer template.

### Artifact Scaffold

For demos, interactive tools, data surfaces, and pages that need to run, choose an artifact mode early:

- `coded app`: production-style implementation in the local framework
- `HTML artifact`: quick inspection or portable preview
- `image mockup`: visual direction only
- `design-layer document`: editable structured layers
- `Figma/reference implementation`: strict visual translation
- `critique`: diagnosis and direction without implementation

The artifact mode controls how much polish, interactivity, data modeling, and verification are required.

### Taste Dials

Expose taste as controllable dials instead of vague adjectives:

- visual variance: safe, elevated, expressive, experimental
- motion appetite: static, feedback, reveal, kinetic, signature
- density: sparse, balanced, dense-with-air, operational dense
- color appetite: restrained, warm/desirable, bold contrast, material-derived
- realism: production product, editorial concept, cinematic mockup, technical instrument

If the user cannot describe taste, present a style matrix with meaningfully different directions. Avoid minor variants that only change color, border radius, or hero placement.

### Command Vocabulary

Use short design commands to repair work quickly:

- `bolder`: increase identity, contrast, or memorability
- `quieter`: reduce noise and competing elements
- `distill`: remove decoration, excess copy, and weak sections
- `harden`: cover edge cases, responsiveness, accessibility, and states
- `lock`: preserve a chosen reference or accepted concept
- `extract`: turn a screenshot, Figma file, or site into tokens, components, and layout rules
- `compare`: visually check implementation against the reference

### Reference Parity Workflow

For screenshots, Figma files, reference sites, and accepted concepts:

1. Inspect the reference.
2. Extract layout grid, typography scale, color roles, component density, asset treatment, copy hierarchy, and interaction promise.
3. Decide whether the job is strict parity or product-system extension.
4. Implement only after the fidelity level is clear.
5. Run rendered visual comparison and list intentional deviations.

Do not invent a new style when the user asked for translation, matching, or implementation.

### Design-System Anchor

When a repo has `DESIGN.md`, design tokens, component docs, Storybook, Figma exports, or existing nearby screens, treat them as the first constraint.

Extract:

- tokens: colors, type, spacing, radius, shadow, motion
- components: navigation, cards, forms, tables, dialogs, toolbars, empty states
- layout rules: grids, breakpoints, page rhythm, density
- behavior rules: loading, error, disabled, selected, active, hover, focus
- copy rules: label tone, action naming, information hierarchy

New visual direction should extend the system unless the task is explicitly a redesign.

### Screenshot-Derived Design System

If only screenshots exist, infer a compact design system before changing the UI:

- name the main components and their roles
- identify spacing and density patterns
- identify repeated color roles and semantic colors
- identify the page structure and content hierarchy
- identify which details are intentional versus accidental

Then use that system to redesign or implement, rather than copying pixels blindly.

### Style-Option Matrix

When the brief is open, offer a small matrix of distinct directions before implementation.

Good matrices vary the underlying design thesis:

- operational utility versus editorial product story
- technical instrument versus warm consumer confidence
- material-derived cultural world versus neutral product clarity
- kinetic brand moment versus calm workflow surface

Weak matrices only vary color palettes or decorative backgrounds.

### Fidelity Ledger QA

For reference-driven work, keep a short ledger:

- locked elements: what must match
- intentional deviations: what changed and why
- unresolved risks: what needs user judgment or browser/device proof
- checked views: which screenshots or comparisons were reviewed

Use this instead of vague claims like "matches the design".

## Generation Direction

Before substantial UI generation, define:

- reference anchor: brief, existing UI, screenshot, Figma, accepted image concept, DESIGN.md, product data, or brand asset
- choice mode: infer, ask, style matrix, strict reference, or product-system extension
- style dials: variance, motion, density, color, realism
- concept fidelity: exploratory, selected concept, strict reference parity, or existing-system continuation
- artifact mode: coded app, HTML artifact, image mockup, Figma/reference implementation, design-layer document, or critique
- visual check: rendered screenshot, mobile screenshot, reference comparison, copy diff, visual QA, or reduced-motion check

State this direction before implementation when the task has enough ambiguity to drift.

## When To Ask, Infer, Or Generate

Ask when multiple style families are plausible and the user's preference matters.

Infer when the product category, existing system, or reference gives a clear answer.

Generate a style matrix when the user wants exploration but cannot name a direction.

Use strict reference mode when the user provides Figma, a screenshot, a reference site, or an accepted image concept and asks for implementation or matching.

Use product-system extension mode when adding a new screen to an existing app.

## Failure Modes

- Building from a prompt before defining context and direction.
- Producing small variants instead of genuinely different directions.
- Turning a full product into a hero-only marketing composition.
- Reinterpreting an accepted image concept during implementation.
- Guessing Figma/reference intent without inspecting hierarchy, copy, density, and tokens.
- Treating build success as visual proof.
- Reusing the same AI UI formula: purple gradients, glass panels, nested cards, vague SaaS claims, and decorative motion.
- Extracting visual style but losing product workflow, states, and content priority.
