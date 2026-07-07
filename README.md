# Product Composer Skill

English | [Chinese](README.zh-CN.md)

Product Composer is a Codex skill for aesthetic control in AI-assisted UI design and implementation.

It is not a general UI toolkit. Use it when the UI itself needs stronger taste, a clearer visual thesis, and tighter control over AI defaults. The target failure is specific: AI output that looks generic, overdecorated, poorly composed, visually unfocused, or hard to preserve during implementation.

## When To Use

Use Product Composer for:

- net-new UI surfaces that need a distinctive direction before code
- substantial redesigns where the current UI feels generic, weak, or uncontrolled
- product apps, dashboards, landing pages, AI surfaces, and editorial/brand pages when visual quality is central
- generated UI image concepts that need stronger composition and fewer template artifacts
- implementation of an accepted visual direction where hierarchy, palette roles, density, motion, and asset treatment must survive coding

Leave it out when the task is only mechanical, local, or unrelated to visual direction.

## Core Contract

Every substantial use should produce or preserve a compact design contract:

1. Generic-default risk: what AI is likely to make badly.
2. Visual thesis: the one sentence that explains the surface's aesthetic direction.
3. Taste constraints: 3-5 choices that make the UI specific.
4. Anti-defaults: 2-3 patterns the UI must avoid.
5. Asset plan: user-provided, local, or imagegen-generated assets, with missing assets named honestly.
6. Implementation lock: what must survive coding, and what may adapt for engineering.
7. Visual verification: rendered checks across key sections and responsive states when feasible.

If the same plan would still work after swapping only the product name, the direction is not specific enough.

## Operating Model

### Direction Before Layout

Start from mission, material, audience, and product proof. Choose layout only after the visual thesis is clear.

### Taste Before Decoration

Taste is selection under pressure: proportion, deletion, restraint, contrast, and specificity before effects.

### Assets Before Invention

Real assets, local assets, and generated assets shape the surface. Generated assets are allowed, but their role must be explicit and they must not impersonate real product proof.

### Implementation As Preservation

Coding is not a second redesign. Preserve the accepted hierarchy, dominant form, palette roles, type character, density, motion role, and asset treatment unless there is a clear engineering reason to adapt.

### Verification Is Visual

A build or lint pass is not enough. When feasible, inspect the rendered UI, mobile layout, text fitting, key states, and visible deviations.

## Usage Examples

```text
Use $product-composer to design a homepage UI for my product.
Avoid generic SaaS templates. Create a strong visual thesis first.
```

```text
Use $product-composer to redesign this dashboard.
Keep it useful, but make the visual system less generic and more controlled.
```

```text
Use $product-composer to generate an image concept for this AI workflow UI.
Use real product structure, not a method diagram.
```

```text
Use $product-composer to implement the selected UI direction in React.
Preserve the hierarchy, palette roles, density, and responsive behavior.
```

## Reference Map

The main skill routes Codex to focused references only when needed:

- `references/task-router.md` - choose the smallest UI design and implementation route
- `references/style-family-router.md` - choose a style family, density, and color appetite
- `references/visual-direction.md` - composition, palette, material, silhouette, and specificity
- `references/taste-calibration.md` - taste stance, anti-defaults, restraint, and memorability
- `references/direction-matrix-builder.md` - create meaningfully different visual directions
- `references/concept-to-implementation-lock.md` - preserve accepted concepts during coded implementation
- `references/asset-context-protocol.md` - plan user-provided, local, and imagegen-generated assets
- `references/design-memory-consistency.md` - preserve tokens, component decisions, spacing, depth, and surface consistency
- `references/visual-quality-rubric.md` - judge hierarchy, type, palette, material, depth, and AI-flavored failures
- `references/image-generation-aesthetic-calibration.md` - prompt and repair generated UI concepts
- `references/interaction-grammar.md` - define control relationships for AI and complex workflows
- `references/ant-design-product-values.md` - keep enterprise product surfaces ordered and usable
- `references/content-judgment.md` - decide what to keep, defer, and delete
- `references/desire-minimalism-psychology.md` - build minimal UI with product desire
- `references/market-calibration.md` - calibrate commercial pages against real market expectations
- `references/signature-aesthetic-systems.md` - create coherent visual worlds and continuity
- `references/react-bits-motion-layer.md` - use expressive React motion as a controlled accent
- `references/execution-discipline.md` - keep implementation grounded in local context
- `references/anti-patterns.md` - avoid common AI UI failures
- `references/verification.md` - final rendered verification guidance

## Tooling

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

The scanner flags common visual anti-patterns in frontend projects. Treat the output as warnings, then confirm visually.

## Validation

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/product-composer
python3 tests/test_skill_guidance_structure.py
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
