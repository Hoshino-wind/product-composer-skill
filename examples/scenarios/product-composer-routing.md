# Product Composer Routing Scenarios

These scenarios define expected routing behavior for common UI requests. They are not templates for user-visible responses; they are regression examples for how the skill should choose references and output shape.

## Scenario 1: Quick Patch

User prompt:

```text
This settings drawer looks cramped on mobile. Fix the spacing and button row.
```

Expected routing:

- Work mode: quick patch
- Read: `task-router.md`, `design-memory-consistency.md`, `anti-patterns.md`, `verification.md`
- Skip: style family prompt, direction matrix, signature system

Output contract:

- Preserve the existing component system.
- Make the smallest useful spacing/layout change.
- Mention affected states only if touched.

Acceptance checks:

- Mobile text does not clip or overlap.
- Button row has stable dimensions.
- Existing tokens/components are preserved.

## Scenario 2: Design Review

User prompt:

```text
Review this dashboard screenshot and tell me what feels weak.
```

Expected routing:

- Work mode: design review
- Read: `task-router.md`, `design-review-output.md`, `visual-quality-rubric.md`, `anti-patterns.md`
- Skip: implementation workflow unless requested

Output contract:

- Start with findings.
- Use severity levels.
- Do not redesign the UI unless asked.

Acceptance checks:

- Findings are prioritized.
- Every issue has a clear change.
- Review covers hierarchy, task flow, visual craft, and responsive/state risk when visible.

## Scenario 3: Figma To Code

User prompt:

```text
Implement this Figma frame in our app.
```

Expected routing:

- Work mode: Figma
- Read: `task-router.md`, `reference-dna-extraction.md`, `concept-to-implementation-lock.md`, `asset-context-protocol.md`, `verification.md`
- Also use Figma-specific skills/tools when available

Output contract:

- Extract hierarchy, tokens, assets, spacing, and component structure.
- Reuse local components where possible.
- Validate against screenshot or rendered view in slices.

Acceptance checks:

- Major layout regions match.
- Assets are not replaced by unrelated placeholders when real assets exist.
- Deviations are named.

## Scenario 4: Image Mockup

User prompt:

```text
Generate a polished UI image concept for this AI research product. No code yet.
```

Expected routing:

- Work mode: image mockup
- Read: `task-router.md`, `image-generation-aesthetic-calibration.md`, `asset-context-protocol.md`, `direction-matrix-builder.md` when taste is unclear
- Use image generation when available

Output contract:

- Define asset context, palette appetite, dominant product object, and interaction relationship.
- Keep visible text minimal.
- Inspect generated result before treating it as usable.

Acceptance checks:

- Result is a UI surface, not a method diagram.
- It avoids dashboard-template and dense-widget failure.
- Missing real assets are identified honestly.

## Scenario 5: Accepted Concept Implementation

User prompt:

```text
Use the mockup we approved and build it in React.
```

Expected routing:

- Work mode: accepted concept
- Read: `task-router.md`, `concept-to-implementation-lock.md`, `asset-context-protocol.md`, `design-memory-consistency.md`, `verification.md`

Output contract:

- Freeze visible hierarchy, palette roles, dominant object, copy intent, and spatial relationship.
- Adapt only for accessibility, responsiveness, and local code conventions.
- Do not silently redesign.

Acceptance checks:

- First viewport parity is checked.
- Major sections preserve the concept.
- Mobile layout adapts without changing the visual thesis.

## Scenario 6: Brand Homepage With Missing Assets

User prompt:

```text
Design a homepage for our new physical product. We do not have product photos yet.
```

Expected routing:

- Work mode: brand/landing
- Read: `task-router.md`, `asset-context-protocol.md`, `market-calibration.md`, `desire-minimalism-psychology.md`, `signature-aesthetic-systems.md`

Output contract:

- Identify missing real assets.
- Offer user-provided, local, or imagegen-generated asset paths.
- Avoid pretending generated assets are official product photos.

Acceptance checks:

- First viewport has product/category signal.
- Hero is not pure abstract decoration.
- Asset assumptions are explicit.

## Scenario 7: Frontier Interaction Surface

User prompt:

```text
Design an agent workflow surface for monitoring autonomous research runs.
```

Expected routing:

- Work mode: frontier interaction
- Read: `task-router.md`, `interaction-grammar.md`, `visual-direction.md`, `visual-quality-rubric.md`, `design-memory-consistency.md`

Output contract:

- Define intent, agency, control transfer, time model, object model, and commitment model before layout.
- Use traditional components only where they serve the interaction grammar.

Acceptance checks:

- UI does not collapse into a fake terminal or generic command dashboard.
- User can pause, inspect, approve, override, or rewind where appropriate.
- State and uncertainty are visible.

## Scenario 8: Layer Document

User prompt:

```text
Convert this landing page idea into an editable layer document and HTML preview.
```

Expected routing:

- Work mode: layer document
- Read: `task-router.md`, `design-layer-document.md`, `asset-context-protocol.md`, `verification.md`
- Use `scripts/design_layer_tool.py`

Output contract:

- Produce `.layerdoc.json` first.
- Keep semantic groups for headline, CTA, proof object, sections, charts, tables, and media.
- Export HTML after validation.

Acceptance checks:

- Layer document validates.
- HTML preview opens and preserves semantic layer groups.
- Charts/tables carry data when present.

## Scenario 9: Full Redesign

User prompt:

```text
This SaaS app looks generic. Redesign it so it feels premium but still useful.
```

Expected routing:

- Work mode: full redesign
- Read: `task-router.md`, `direction-matrix-builder.md`, `visual-quality-rubric.md`, `design-memory-consistency.md`, `ant-design-product-values.md`, `content-judgment.md`

Output contract:

- Diagnose current failure.
- Preserve useful local components and tokens.
- Produce meaningfully different directions if taste is unclear.
- Choose one direction before implementation.

Acceptance checks:

- Result is not a generic admin shell.
- Product task clarity improves.
- Repeated components have a stable system.
