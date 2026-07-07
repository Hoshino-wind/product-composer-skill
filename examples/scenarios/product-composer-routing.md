# Product Composer Routing Scenarios

These scenarios define expected routing behavior for UI design and implementation requests. They are not templates for user-visible responses; they are regression examples for how the skill should choose references and output shape.

## Scenario 1: New UI Design

User prompt:

```text
Design a polished homepage UI for our AI research product. It should avoid generic SaaS templates.
```

Expected routing:

- Work mode: new UI design
- Read: `task-router.md`, `style-family-router.md`, `visual-direction.md`, `asset-context-protocol.md`, `visual-quality-rubric.md`
- Choose a visual thesis before layout.

Output contract:

- Define mission, style family, asset assumptions, dominant visual form, and taste constraints.
- Produce a specific visual direction, not a reusable template.

Acceptance checks:

- The first viewport has a memorable product signal.
- The design would not still fit after swapping only the product name.
- Asset assumptions are explicit.

## Scenario 2: Image Mockup

User prompt:

```text
Generate a polished UI image concept for this AI research product. No code yet.
```

Expected routing:

- Work mode: image mockup
- Read: `task-router.md`, `image-generation-aesthetic-calibration.md`, `asset-context-protocol.md`, `direction-matrix-builder.md` when taste is unclear
- Use image generation when available.

Output contract:

- Define asset context, palette appetite, dominant product object, and interaction relationship.
- Keep visible text minimal.
- Inspect generated result before treating it as usable.

Acceptance checks:

- Result is a UI surface, not a method diagram.
- It avoids dashboard-template and dense-widget failure.
- Missing real assets are identified honestly.

## Scenario 3: Accepted Concept Implementation

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

## Scenario 4: Brand Homepage With Missing Assets

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

## Scenario 5: Frontier Interaction Surface

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

## Scenario 6: Substantial SaaS Redesign

User prompt:

```text
This SaaS app looks generic. Redesign it so it feels premium but still useful.
```

Expected routing:

- Work mode: substantial redesign
- Read: `task-router.md`, `direction-matrix-builder.md`, `taste-calibration.md`, `visual-quality-rubric.md`, `design-memory-consistency.md`, `ant-design-product-values.md`, `content-judgment.md`

Output contract:

- Diagnose current visual failure.
- Preserve useful local components and tokens.
- Produce meaningfully different directions if taste is unclear.
- Choose one direction before implementation.

Acceptance checks:

- Result is not a generic admin shell.
- Product task clarity improves.
- Repeated components have a stable system.

## Scenario 7: Product App Implementation

User prompt:

```text
Implement the selected UI direction inside our dashboard app.
```

Expected routing:

- Work mode: product app implementation
- Read: `task-router.md`, `design-memory-consistency.md`, `concept-to-implementation-lock.md`, `verification.md`

Output contract:

- Map the chosen visual direction to local components, tokens, states, and responsive constraints.
- Preserve the accepted hierarchy and visual thesis while hardening the UI for real use.

Acceptance checks:

- Layout, text fitting, and key states are checked in a rendered environment.
- Local components are reused where they support the direction.
- Any visible deviation from the selected direction is named.
