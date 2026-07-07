# Task Router

Use this before loading many references when the UI design request is broad, taste is unclear, or the implementation path could drift.

The goal is to choose the smallest route that can produce a specific, controllable UI design or implementation.

## Route Table

| Work mode | Typical trigger | Read | Skip |
|---|---|---|---|
| new UI design | Create a new app screen, homepage, product surface, or visual concept from a brief | `style-family-router.md`, `visual-direction.md`, `asset-context-protocol.md`, `visual-quality-rubric.md` | Coding before the visual thesis is clear |
| substantial redesign | Current UI feels generic, stale, ugly, weak, or visually uncontrolled | `direction-matrix-builder.md`, `taste-calibration.md`, `visual-quality-rubric.md`, `design-memory-consistency.md` | Tiny cosmetic changes that leave the core failure intact |
| product app implementation | A chosen UI direction must become local components, states, layout, and responsive behavior | `design-memory-consistency.md`, `concept-to-implementation-lock.md`, `verification.md` | Replacing the local system without a redesign reason |
| image mockup | User asks for generated UI image, visual concept, or no-code mockup | `image-generation-aesthetic-calibration.md`, `asset-context-protocol.md`, `direction-matrix-builder.md` when taste is unclear | Hand-built SVG mockups unless deterministic vectors are needed |
| accepted concept | User approved a generated image, design board, mockup, or direction | `concept-to-implementation-lock.md`, `asset-context-protocol.md`, `verification.md` | Silent redesign during implementation |
| hero/page experience | Homepage, launch page, portfolio, or brand/product page needs high visual ambition, stronger first viewport, more assets, section pagination, or screen-based page rhythm | `hero-page-experience.md`, `signature-aesthetic-systems.md`, `asset-context-protocol.md`, `visual-direction.md`, `visual-quality-rubric.md` | Treating the page as a standard hero plus feature-card stack |
| brand/landing | Public homepage, launch page, portfolio, product marketing | `market-calibration.md`, `desire-minimalism-psychology.md`, `signature-aesthetic-systems.md`, `asset-context-protocol.md` | Abstract decoration with no product proof |
| dashboard/data | Admin panel, analytics, table-heavy flow, CRM, settings | `ant-design-product-values.md`, `content-judgment.md`, `visual-quality-rubric.md` | Marketing hero composition inside the product surface |
| frontier interaction | AI agent, command canvas, automation, simulation, complex creative workflow | `interaction-grammar.md`, `visual-direction.md`, `visual-quality-rubric.md` | Literal drag/click labels or dashboard shells |

## Escalation Rules

- Escalate from new UI design to substantial redesign when the request includes an existing weak surface and asks to make it meaningfully better.
- Escalate from image mockup to accepted concept after a generated visual is selected.
- Escalate from accepted concept to product app implementation when the selected direction must be coded.
- Escalate from product app implementation to substantial redesign only when preserving the local system would keep the main visual failure intact.
- Escalate from brand/landing to hero/page experience when the request emphasizes first-viewport impact, spacing, visual ambition, assets, section pagination, or scroll rhythm.

## Output By Route

For new UI design:

- State the visual thesis, style family, asset assumptions, and dominant visual form.
- Choose the layout after the mission and signature system are clear.
- Verify the result against generic-default failures.

For substantial redesign:

- Diagnose the visual failure.
- Produce 3-5 meaningfully different directions when taste is unclear.
- Choose one direction before coding.
- Preserve any local system elements that still work.

For product app implementation:

- Name the chosen direction being implemented.
- Map it to local tokens, components, states, and responsive constraints.
- Verify layout, text fitting, and affected states in the rendered UI.

For image mockup:

- Define asset context before prompting.
- Pick one dominant object or interaction relationship.
- Keep visible text short.
- Inspect the generated result before claiming it is usable.

For accepted concept:

- Freeze visible hierarchy, palette roles, dominant object, copy intent, and spatial relationship.
- Adapt only for accessibility, responsiveness, and local code conventions.
- Compare first viewport, major sections, key states, and mobile layout in slices.

For hero/page experience:

- State the hero/page experience thesis before layout.
- Define a 3-4 screen model with one job per screen.
- Define the asset system: hero, support, material, transition, and proof asset roles.
- Choose pagination/page rhythm: section pagination, scroll snap, progress rail, scene transition, or next-screen hint.
- Keep the hero spacious enough for one dominant scene before adding proof and secondary UI.

## Anti-Dilution Guard

If the request does not need visual direction, aesthetic control, or UI composition, leave this skill out. If the task does need those things, do not hide uncertainty behind a polished first draft.
