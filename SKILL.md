---
name: product-composer
description: "Use when creating or substantially redesigning UI where visual taste, non-generic aesthetics, or controllable visual direction matters: product apps, dashboards, SaaS workflows, AI/agent surfaces, landing pages, brand/editorial pages, React motion pages, or image UI concepts. If Ant Design APIs/components are explicit, also use antd."
---

# Product Composer

## Overview

Product Composer is for UI design and implementation when the output needs stronger taste, clearer visual direction, and tighter control than a generic UI prompt usually produces.

Use it to compose a product surface as a coherent system: one mission, one visual thesis, deliberate content hierarchy, domain-specific assets, durable design memory, and rendered verification.

Prefer the user's existing design system, component library, routing, and styling conventions. Introduce a new visual language only when the project lacks one or the user explicitly asks for a redesign.

## Reference Routing

Read only the references needed for the design task:

- `references/task-router.md`: read when the UI design route is ambiguous or broad.
- `references/ant-design-product-values.md`: read for enterprise products, dashboards, admin tools, forms, tables, Ant Design projects, or complex workflows.
- `references/execution-discipline.md`: read for new UI, redesigns, visual polish, or avoiding generic AI output.
- `references/style-family-router.md`: read before net-new UI generation when the user has not specified a style, when outputs feel random or same-looking, or when the agent needs to ask the user to choose a direction before composing.
- `references/interaction-grammar.md`: read for AI products, agent workflows, command surfaces, creative tools, simulations, complex operations, or any request for new interaction design.
- `references/taste-calibration.md`: read before net-new visual concepts, after user feedback like "ugly", "generic", "no taste", "too traditional", or when the design needs a sharper aesthetic stance.
- `references/market-calibration.md`: read after user asks to look at excellent market examples, ThemeForest/WordPress/Webflow/template-marketplace references, when a homepage feels fake, self-indulgent, too conceptual, or disconnected from real product proof.
- `references/content-judgment.md`: read when a surface feels dense, over-explained, crowded, or when the user says the design should make stronger decisions.
- `references/desire-minimalism-psychology.md`: read when the user asks for minimalism plus psychology, viewing desire, product desire, conversion pull, appetite, emotional attraction, comfortable but not boring color, or a layout that makes people want to keep watching or use the product.
- `references/image-generation-aesthetic-calibration.md`: read when the user asks to directly generate, draw, or preview UI as an image without code, when generated UI is rejected as ugly or lacking taste, or when the agent needs reusable prompt templates for elegant UI images.
- `references/ui-generation-operating-model.md`: read when the output still feels shallow after normal gates, when the task needs deeper UI generation judgment, or when the agent must avoid default templates through surface register, design thesis inventory, generic-default self-test, and section-by-section parity.
- `references/hero-page-experience.md`: read for high-impact homepages, launch pages, portfolios, product/brand pages, or any hero/page experience that needs a screen model, asset system, pagination, page rhythm, stronger first viewport, richer assets, or more spacious composition.
- `references/asset-context-protocol.md`: read for named brands, products, venues, public sites, portfolios, marketing pages, image-heavy pages, or any UI where logos, product shots, screenshots, icons, textures, media treatment, or missing assets shape the result.
- `references/design-memory-consistency.md`: read for multi-screen work, design systems, repeated edits, long-running threads, or any task where tokens, spacing, component decisions, depth, or surface treatment could drift.
- `references/visual-quality-rubric.md`: read when judging whether a UI is high quality, generic, ugly, too AI-flavored, visually flat, overdecorated, poorly typeset, weakly composed, or ready for final visual polish.
- `references/reference-dna-extraction.md`: read when working from a screenshot, reference site, accepted mockup, existing screen, or visual style sample that must be translated without copying blindly.
- `references/direction-matrix-builder.md`: read when the user wants options, taste is unclear, the first result feels same-looking, or the agent needs 3-5 genuinely different visual directions before implementation.
- `references/concept-to-implementation-lock.md`: read when implementing from an accepted image concept, generated mockup, screenshot, visual comp, or design-board result where hierarchy, palette, dominant object, and spatial relationship must survive coding.
- `references/visual-direction.md`: read for any net-new UI, homepage, concept, visual redesign, product identity, or when the output risks becoming diagrammatic, generic, cluttered, or ugly.
- `references/react-bits-motion-layer.md`: read for React/Next.js surfaces that mention React Bits, reactbits.dev, animated text, kinetic typography, cursor or hover effects, scroll reveals, particles, WebGL, Three.js backgrounds, expressive motion, portfolio polish, or kinetic landing pages.
- `references/signature-aesthetic-systems.md`: read for cultural, editorial, museum, hospitality, fashion, premium brand, emotionally rich homepages, multi-screen visual consistency, or when the user asks for the quality of the stronger Dunhuang-style result without copying that style.
- `references/anti-patterns.md`: read before visual implementation.
- `references/verification.md`: read before final validation of rendered UI.

If the project explicitly uses `antd`, also use the `antd` skill and query the actual component APIs before writing or changing Ant Design code.

## Task Route Gate

Before loading multiple references or running a full design workflow, choose one route:

- new UI design: define the product mission, visual thesis, asset context, style family, and implementation target.
- substantial redesign: diagnose the current visual failure, preserve useful product structure, create direction options when taste is unclear, then implement one direction.
- product app implementation: turn a chosen visual direction into local components, tokens, states, and responsive behavior.
- image mockup: gather asset context, define the dominant object or interaction relationship, then use image generation when appropriate.
- accepted concept: freeze the accepted hierarchy, palette roles, dominant object, and spatial relationship before coding.
- hero/page experience: compose a signature page experience with a screen model, asset system, pagination/page rhythm, dominant first viewport scene, and continuity device.
- brand/landing: build around product proof, first-viewport memorability, desire mechanism, and a clear conversion path.
- dashboard/data: prioritize task order, scanability, state clarity, table/chart grammar, and calm density.
- frontier interaction: define intent, system agency, control transfer, time model, object model, and commitment model before layout.

Use `references/task-router.md` whenever the route is not obvious. The route exists to sharpen the design path, not to expand the skill into unrelated work.

## Core Control Loop

For substantial UI work, keep the loop short:

1. Identify the generic-default risk.
2. Write one visual thesis for the surface.
3. Lock 3-5 taste constraints and 2-3 anti-defaults.
4. Compose or implement under that contract.
5. Verify the rendered result and repair the weakest visual decision.

If the same plan would still work after changing only the product name, revise the visual thesis before coding.

## Surface Decision

Classify the surface before coding:

- `product`: apps, dashboards, admin panels, tools, settings, editors, CRM, data views. Optimize for task completion, scanability, state clarity, and repeat use.
- `brand`: landing pages, marketing sites, portfolios, launch pages, editorial pages. Optimize for identity, story, first-viewport memorability, and emotional clarity.
- `hybrid`: product-led marketing, public docs, app home pages. Keep brand expression but preserve product clarity.
- `frontier`: AI systems, agent operations, simulation tools, command canvases, creative copilots, or products where the main task is not well served by pages, forms, tables, and cards.

Default to `product` when the screen is operational or data-heavy.

## Design Direction Contract

Before generating or implementing any important UI surface, define:

- Surface mode: product, brand, hybrid, frontier, editorial, cultural, or utility.
- Selected style family: chosen by user or inferred, with one sentence why.
- User mission: what the viewer or operator needs to understand, choose, complete, or desire.
- Asset context: user-provided assets, local assets, imagegen-generated assets, missing assets, and do-not-fake items.
- Page experience: for homepages, launches, portfolios, and brand/product pages, define the screen model, pagination/page rhythm, first-viewport scene, next-screen hint, and continuity device.
- Asset system: for image-heavy or ambitious pages, define hero, support, material, transition, and proof asset roles before layout.
- Design memory: tokens, components, spacing, radius, depth, state behavior, and accepted decisions to preserve.
- Visual thesis: palette roles, type roles, layout thesis, signature element, content voice, and one justified risk.
- Taste contract: three desired feeling words, three anti-defaults, one restraint, one memorability hook, and one deletion rule.
- Density contract: sparse, medium, dense, or dense-with-air; decide what is absent as deliberately as what is present.
- Motion role: none, feedback, focus, reveal, continuity, or signature brand moment; define reduced-motion fallback for substantial animation.
- Implementation lock: what is locked, what may adapt for engineering, and what would require user approval.

Do not start from a generic layout pattern. Start from the surface's material, mission, and signature system, then choose layout.

## Style Selection Gate

Before net-new UI generation, choose or ask for a style family. This gate prevents two failure modes: random style drift and repeated high-end-minimal sameness.

Ask a compact choice question when the brief could support multiple visual directions. Ask at most three choices:

- Style family: Utility Product, Editorial Premium, Cultural Immersive, Technical Instrument, Data Dense, Playful Consumer, Soft Craft, or Bold Campaign.
- Density: sparse, balanced, or dense-with-air.
- Color appetite: quiet restrained, warm/desirable, bold contrast, or source-derived.

If the user says to proceed without questions, infer the family from product context and state the choice before designing. Do not silently default to Editorial Premium.

## Context And Memory Gate

Before creating or changing visual direction, inspect durable context:

- local design files: `DESIGN.md`, token files, component docs, Storybook, nearby routes, screenshots, accepted concepts, and `.product-composer/design-system.md`
- asset context: user-provided assets, local assets, imagegen-generated assets, brand mark, product shots, UI screenshots, object/venue images, icon and illustration style, media constraints, and missing assets
- component memory: button heights, table density, card padding, radius scale, shadow/depth model, navigation behavior, empty/error/loading states, and action naming

If context is missing, state the gap and design around an honest placeholder, inferred local system, or generated asset. Imagegen-generated assets can become first-class design assets when their role is explicit, but they must not impersonate official logos, real product screenshots, real venue/object photos, metrics, or brand assets.

For redesigns, separate what remains, what changes, and what gets deprecated.

## Interaction Grammar Gate

Before designing an AI, agentic, automation, creative, or complex workflow surface, define the interaction grammar before the visual layout:

- User intent: what does the user express, command, inspect, or negotiate?
- System agency: what does the system infer, propose, simulate, execute, or refuse?
- Control transfer: where can the user adjust autonomy, pause, approve, override, or rewind?
- Time model: how do past actions, current execution, future plan, and uncertainty appear?
- Object model: what is the living object the user manipulates: goal, run, plan, scene, dataset, policy, workspace, or workflow?
- Commitment model: what can be previewed, simulated, committed, reverted, or audited?
- Interaction level: cognitive model, decision path, system response, feedback loop, or physical gesture? Do not turn interaction design into literal drag/click/swipe affordances unless the product truly supports them.

Do not default to menus, tables, cards, forms, and dashboards until this grammar is clear. If traditional components remain useful, make them subordinate to the new control model.

## Aesthetic Gate

Do not treat interaction novelty as visual quality. A concept can be structurally correct and still be ugly.

Before finalizing any visual surface, pass this gate:

- Is there one dominant visual form the user remembers after 5 seconds?
- Is the page composed through proportion, rhythm, contrast, and negative space rather than many equally loud widgets?
- Is the primary interaction object beautiful enough to be the product's signature?
- Does the palette have taste and tension rather than merely safe enterprise neutrals?
- Is the density intentional, with enough breathing room for the eye to rest?
- Would this still look good if the labels were blurred?
- Would the same visual plan appear for a similar prompt with only the product name changed? If yes, revise the plan before coding.
- Does the design pass visual-quality checks for hierarchy, proportion, type, palette, material, depth, specificity, and motion discipline?
- For utility or technical surfaces, does it avoid generic admin-shell and black cockpit aesthetics? Reject `运行舱`-style industrial fantasy unless the real domain requires it.
- For SaaS, does it apply Ant Design product values: natural task order, certainty, meaningful work objects, and progressive capability?
- If this is part of a set, is it structurally different from the other accepted outputs? Reject same-looking variants that reuse warm cards, central rails, right panels, thin borders, status chips, or the same proof-object placement.

If the answer is no, run a visual direction pass before adding more UI detail.

## Taste Calibration Gate

Taste is selection under pressure. It is not adding premium adjectives.

Before generating or implementing an important new visual direction, define:

- Taste stance: three words that describe the desired feeling.
- Anti-reference: three things the design must not resemble.
- Signature restraint: what the design deliberately refuses to show.
- Memorability hook: what the viewer should remember.
- Deletion rule: what gets removed first if the page feels busy.

If a design looks correct but lifeless, run `bolder`. If it looks novel but ugly, run `quieter`, `distill`, and then rebuild around one stronger form.

## Image Mockup Generation Gate

When the user asks to generate UI directly without code, prefer the `imagegen` skill and let the image model resolve aesthetic composition. Do not hand-build SVG mockups unless the user needs deterministic vector structure, diagrams, or editable primitives.

For image UI mockups:

- Define the product desire, interaction relationship, palette appetite, and one dominant product object.
- For culturally rich or brand-specific pages, define the signature system and continuity device before prompting.
- Select one reusable prompt template from `image-generation-aesthetic-calibration.md` before calling image generation.
- If a generated result is rejected as ugly, do not keep regenerating from the same template. Run the aesthetic repair pass in `image-generation-aesthetic-calibration.md` first, then rebuild the prompt around visual direction rather than product explanation.
- Prompt for `design-board quality` and a real product website/app surface, not a method diagram.
- Keep exact visible text minimal.
- Avoid over-specifying geometry into boxes, arrows, or flowcharts.
- Use constraints to prevent known failures: fake drag/swipe gestures, photo/quote/widget collages, dashboard templates, and dense feature grids.
- Inspect the result visually before claiming it worked. If the output only appears in chat and does not save to disk, say so instead of copying an old asset.

## Implementation Workflow

1. Inspect the local project first: framework, component library, styling system, existing tokens, routes, and nearby screens.
2. Choose the UI route before styling: new design, substantial redesign, product app implementation, hero/page experience, brand/landing, dashboard/data, frontier interaction, image mockup, or accepted concept.
3. State the design direction contract before implementation.
4. Shape the screen around workflow, not decoration:
   - primary task first
   - clear hierarchy between navigation, work area, controls, feedback, and secondary details
   - predictable states for loading, empty, error, success, disabled, selected, and active
5. Build with existing primitives:
   - use local components and tokens where available
   - use familiar controls for familiar jobs
   - use React Bits-style components only as an accent or signature layer after the core hierarchy works statically
   - keep dimensions stable for boards, grids, tables, toolbars, counters, and icon buttons
6. Preserve locked design decisions while coding:
   - map visible concept elements to code, user-provided assets, local assets, imagegen-generated assets, or intentional deviations
   - keep copy voice, type roles, color roles, density, media treatment, and component families consistent
   - compare first viewport, major sections, repeated components, key states, and mobile layout in slices
7. Tune deliberately:
   - `bolder`: increase identity when the page is correct but forgettable
   - `quieter`: reduce visual noise when the UI competes with the task
   - `distill`: remove decoration, copy, or controls that do not serve the user mission
   - `harden`: cover overflow, i18n, edge cases, accessibility, and responsive states
8. Verify in a real rendered environment when feasible, using screenshots across desktop and mobile before claiming the UI is finished. Name visible deviations, fixes, or blockers.

## Product UI Rules

- Make operational tools dense but calm. Avoid marketing-style hero sections inside dashboards and admin pages.
- Preserve user orientation: stable navigation, visible filters, clear selected states, and reversible actions.
- Prefer contextual actions over distant global actions when the action belongs to a specific row, card, record, or field.
- Use progressive disclosure for advanced capability: defaults first, details on demand.
- Make status, validation, permissions, and system feedback explicit.
- Keep copy short and task-facing. Do not use visible instructional filler to explain obvious UI behavior.
- Avoid one-off styling that cannot be reused, named, or explained.

## Visual Rules

- Choose typography, color, spacing, and motion to support the surface mode.
- Make the first impression visually composed before making every secondary function visible.
- Prefer one strong signature form over many small clever widgets.
- Treat taste as deletion, proportion, and specificity before decoration.
- Treat React Bits-style motion as an expressive layer, not a default layout system. Use it to focus, reveal, connect, or create a signature moment.
- For minimal persuasive UI, use color as appetite and attention, not decoration: avoid defaulting to black and white; choose a small expressive palette with a clear base, emotional accent, and action color.
- Do not fake interaction with labels like "drag", "click", or "swipe" on static or conceptual UI. Show the product's relationship model instead.
- Avoid generic AI signatures: purple-blue gradients, decorative orbs, nested cards, arbitrary glass panels, huge rounded icon tiles, vague SaaS copy, and ornamental layout flourishes.
- Do not make a one-hue interface. Use neutrals, semantic colors, and one or two purposeful accents.
- Do not scale font size with viewport width. Use stable type scales and responsive layout constraints.
- Support `prefers-reduced-motion` for large, repeated, background, WebGL, particle, or text animation.
- Use visual assets when a website, game, object, venue, product, or brand page needs inspection or emotional specificity.
- For hero/page experience work, treat the page as designed screens with a screen model, asset system, pagination/page rhythm, and continuity device; do not stack independent sections by habit.
- One small image or one full product screenshot is not enough when the user asks for a visually ambitious page. Use user-provided assets, local assets, or imagegen-generated assets with explicit roles.
- Prefer icons for tool actions and text labels for commands that need interpretation.
- Ensure text never overlaps, clips, or spills out of buttons, tabs, cards, inputs, tables, or mobile containers.

## Optional Scanner

For frontend projects, run the bundled scanner when useful:

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

Treat scanner output as warnings, not truth. Confirm visually before changing code.
