---
name: product-composer
description: "Use when designing, redesigning, generating, critiquing, or implementing high-quality UI surfaces: websites, apps, dashboards, SaaS workflows, AI products, command canvases, forms, data views, landing pages, React Bits-style motion pages, product content pages, cultural/editorial pages, multi-screen flows, prototypes, design systems, image mockups, editable UI layer documents, or HTML previews that need product clarity, distinctive art direction, expressive React motion, interaction grammar, desire-led minimalism, and responsive verification. If Ant Design APIs/components are explicit, also use antd."
---

# Product Composer

## Overview

Compose UI as a product system, not a decorative page. Use product-order thinking for complex work surfaces, local execution discipline to avoid generic AI UI, signature art direction for memorable pages, and interaction grammar to invent new control relationships when traditional pages are insufficient.

Prefer the user's existing design system, component library, routing, and styling conventions. Introduce a new visual language only when the project lacks one or the user explicitly asks for a redesign.

## Reference Routing

Read only the references needed for the task:

- `references/ant-design-product-values.md`: read for enterprise products, dashboards, admin tools, forms, tables, Ant Design projects, or complex workflows.
- `references/execution-discipline.md`: read for new UI, redesigns, visual polish, critique, or avoiding generic AI output.
- `references/style-family-router.md`: read before net-new UI generation when the user has not specified a style, when outputs feel random or same-looking, or when the agent needs to ask the user to choose a direction before composing.
- `references/interaction-grammar.md`: read for AI products, agent workflows, command surfaces, creative tools, simulations, complex operations, or any request for new interaction design.
- `references/taste-calibration.md`: read before net-new visual concepts, after user feedback like "ugly", "generic", "no taste", "too traditional", or when the design needs a sharper aesthetic stance.
- `references/market-calibration.md`: read after user asks to look at excellent market examples, ThemeForest/WordPress/Webflow/template-marketplace references, when a homepage feels fake, self-indulgent, too conceptual, or disconnected from real product proof.
- `references/content-judgment.md`: read when a surface feels dense, over-explained, crowded, or when the user says the design should make stronger decisions.
- `references/desire-minimalism-psychology.md`: read when the user asks for minimalism plus psychology, viewing desire, product desire, conversion pull, appetite, emotional attraction, comfortable but not boring color, or a layout that makes people want to keep watching or use the product.
- `references/image-generation-aesthetic-calibration.md`: read when the user asks to directly generate, draw, or preview UI as an image without code, when image-generated UI looks better than hand-built/vector attempts, when generated UI is rejected as ugly or lacking taste, or when the agent needs reusable prompt templates for elegant UI images.
- `references/ui-generation-skill-distillation.md`: read for broad UI generation workflows, image-first concepts, Figma/reference-to-code, screenshot-derived design systems, DESIGN.md-driven work, style-option matrices, fidelity-ledger QA, or when the user asks to absorb UI generation patterns into this skill.
- `references/ui-generation-operating-model.md`: read when the output still feels shallow after normal gates, when the task needs deeper UI generation judgment, or when the agent must avoid default templates through surface register, design thesis inventory, generic-default self-test, and section-by-section parity.
- `references/input-output-mode-router.md`: read when the input type or deliverable is ambiguous: rough prompt, screenshot, Figma, video, existing app, accepted concept, 3D/WebGL request, quick patch, full redesign, coded app, HTML preview, design canvas, prototype, or structured layer document.
- `references/asset-context-protocol.md`: read for named brands, products, venues, public sites, portfolios, marketing pages, image-heavy pages, or any UI where logos, product shots, screenshots, icons, textures, media treatment, or missing assets shape the result.
- `references/design-memory-consistency.md`: read for existing projects, multi-screen work, design systems, repeated edits, long-running threads, or any task where tokens, spacing, component decisions, depth, or surface treatment could drift.
- `references/visual-quality-rubric.md`: read when judging whether a UI is high quality, generic, ugly, too AI-flavored, visually flat, overdecorated, poorly typeset, weakly composed, or ready for final visual polish.
- `references/reference-dna-extraction.md`: read when working from a screenshot, Figma frame, reference site, accepted mockup, existing screen, or visual style sample that must be translated without copying blindly.
- `references/direction-matrix-builder.md`: read when the user wants options, taste is unclear, the first result feels same-looking, or the agent needs 3-5 genuinely different visual directions before implementation.
- `references/concept-to-implementation-lock.md`: read when implementing from an accepted image concept, generated mockup, screenshot, visual comp, or design-board result where hierarchy, palette, dominant object, and spatial relationship must survive coding.
- `references/visual-direction.md`: read for any net-new UI, homepage, concept, visual redesign, product identity, or when the output risks becoming diagrammatic, generic, cluttered, or ugly.
- `references/react-bits-motion-layer.md`: read for React/Next.js surfaces that mention React Bits, reactbits.dev, animated text, kinetic typography, cursor or hover effects, scroll reveals, particles, WebGL, Three.js backgrounds, expressive motion, portfolio polish, or kinetic landing pages.
- `references/signature-aesthetic-systems.md`: read for cultural, editorial, museum, hospitality, fashion, premium brand, emotionally rich homepages, multi-screen visual consistency, or when the user asks for the quality of the stronger Dunhuang-style result without copying that style.
- `references/design-layer-document.md`: read when the user asks for UI layer decomposition, editable UI output, HTML editing, chart/table layers, or any pipeline that should turn a visual design into structured UI elements instead of a flat image.
- `references/anti-patterns.md`: read before visual implementation or design review.
- `references/verification.md`: read before final validation of rendered UI.

If the project explicitly uses `antd`, also use the `antd` skill and query the actual component APIs before writing or changing Ant Design code.

## Surface Decision

Classify the surface before coding:

- `product`: apps, dashboards, admin panels, tools, settings, editors, CRM, data views. Optimize for task completion, scanability, state clarity, and repeat use.
- `brand`: landing pages, marketing sites, portfolios, launch pages, editorial pages. Optimize for identity, story, first-viewport memorability, and emotional clarity.
- `hybrid`: product-led marketing, public docs, app home pages. Keep brand expression but preserve product clarity.
- `frontier`: AI systems, agent operations, simulation tools, command canvases, creative copilots, or products where the main task is not well served by pages, forms, tables, and cards.

Default to `product` when the screen is operational or data-heavy.

## Distilled UI Generation Defaults

These rules are default behavior, not optional references:

- Mode before style: classify the input and output mode before choosing visual direction. A rough prompt, screenshot, Figma frame, accepted concept, existing app patch, full redesign, prototype, and layer document require different workflows.
- Assets before invention: for named brands, products, venues, portfolios, launches, or image-heavy pages, identify user-provided, local, and imagegen-generated assets before inventing visuals.
- Memory before novelty: inspect existing design memory before changing UI. Preserve tokens, spacing, radius, depth, component families, state behavior, and media treatment unless redesign is requested.
- Direction before code: write the design thesis inventory before implementation: surface register, one job, palette roles, type roles, layout thesis, signature element, content voice, motion role, one justified risk, and one refusal.
- Concepts are contracts: accepted mockups, screenshots, Figma frames, and image concepts lock hierarchy, dominant form, copy intent, palette roles, type character, density, media treatment, and spatial relationship.
- Parity in slices: implement and visually compare the first viewport, major sections, repeated components, key states, and mobile layout before moving on.
- Copy is interface: action labels, empty states, error states, helper text, headings, and proof strings must follow the product's voice and interaction promise.
- One orchestrated motion idea beats scattered effects. Motion must focus, reveal, connect, or brand, with reduced-motion fallback for substantial animation.
- Run a generic-default self-test before coding: if the same plan would work after swapping only the product name, revise the plan.
- Final output needs rendered visual verification when feasible. A build or lint pass is not enough.

## Style Selection Gate

Before net-new UI generation, choose or ask for a style family. This gate prevents two failure modes: random style drift and repeated high-end-minimal sameness.

Ask a compact choice question when the brief could support multiple visual directions. Do not ask for narrow fixes, existing design-system work, or requests with a clear reference image.

Ask at most three choices:

- Style family: Utility Product, Editorial Premium, Cultural Immersive, Technical Instrument, Data Dense, Playful Consumer, Soft Craft, or Bold Campaign.
- Density: sparse, balanced, or dense-with-air.
- Color appetite: quiet restrained, warm/desirable, bold contrast, or source-derived.

If the user says to proceed without questions, infer the family from product context and state the choice before designing. Do not silently default to Editorial Premium.

## Universal UI Brief Gate

Before designing any substantial surface, define:

- Surface mode: product, brand, hybrid, frontier, editorial, cultural, or utility.
- Surface register: brand leads, product serves, hybrid balances, or artifact packages.
- Input/output mode: rough prompt, reference implementation, concept-first, existing-system extension, quick patch, full redesign, app, page, prototype, design canvas, or layer document.
- Selected style family: chosen by user or inferred, with one sentence why.
- User mission: what the viewer or operator needs to understand, choose, complete, or desire.
- Design input: product screenshot, workflow state, cultural material, venue/object imagery, dataset, brand asset, or existing design system.
- Generation direction: reference anchor, choice mode, style dials, concept fidelity level, artifact mode, and visual check.
- Design thesis inventory: palette roles, type roles, layout thesis, signature element, content voice, and one justified risk.
- Asset context and design memory: what user-provided assets, local assets, imagegen-generated assets, local tokens, and prior decisions must be preserved.
- Signature system: the dominant form, material language, palette source, motion/continuity idea, and one ownable detail.
- Motion role: none, feedback, focus, reveal, continuity, or signature brand moment; define reduced-motion fallback for substantial animation.
- Density contract: sparse, medium, dense, or dense-with-air; decide what is absent as deliberately as what is present.
- Output path: image mockup, coded implementation, design critique, design prompt, design-system guidance, UI layer document, or HTML preview.

Do not start from a generic layout pattern. Start from the surface's material, mission, and signature system, then choose layout.

## UI Generation Direction Gate

For substantial UI generation, define the direction before writing code, prompting images, or composing screens:

- Reference anchor: brief, existing UI, screenshot, Figma, accepted image concept, DESIGN.md, product data, or brand asset.
- Choice mode: infer, ask, style matrix, strict reference, or product-system extension.
- Style dials: visual variance, motion appetite, density, color appetite, and realism level.
- Concept fidelity: exploratory direction, selected concept, strict reference parity, or existing-system continuation.
- Artifact mode: coded app, HTML artifact, image mockup, Figma/reference implementation, design-layer document, or critique.
- Visual check: rendered screenshot, mobile screenshot, reference comparison, copy/content diff, visual QA notes, or reduced-motion check.

Then bind the direction to implementation:

- Mode route: rough prompt, screenshot/Figma, video/motion, accepted concept, existing app patch, full redesign, 3D/immersive, prototype, or layer document.
- Asset route: user-provided assets, local assets, imagegen-generated assets, missing assets, generated placeholders, media treatment, and do-not-fake items.
- Memory route: local tokens, component families, spacing/radius/depth rules, state behavior, and prior accepted decisions.
- Lock route: what is locked, what may adapt for engineering, and what would require user approval.

If taste is unclear, ask or generate a style matrix with meaningfully different directions. Do not produce tiny variations of the same layout.

If the user supplies a Figma file, screenshot, reference site, accepted image concept, or DESIGN.md, preserve its visible hierarchy, copy intent, palette logic, component density, and interaction promise unless the user explicitly requests reinterpretation.

If an image concept has been accepted, freeze the visible hierarchy, key copy, palette, dominant object, and spatial relationship before implementation. Implementation may harden responsiveness and accessibility, but should not silently redesign the concept.

Rendered verification is part of the output, not an optional polish step. A build or lint pass is not visual proof.

## Context And Memory Gate

Before creating or changing visual direction, inspect durable context:

- local design files: `DESIGN.md`, token files, component docs, Storybook, nearby routes, screenshots, accepted concepts, and `.product-composer/design-system.md`
- asset context: user-provided assets, local assets, imagegen-generated assets, brand mark, product shots, UI screenshots, object/venue images, icon and illustration style, media constraints, and missing assets
- component memory: button heights, table density, card padding, radius scale, shadow/depth model, navigation behavior, empty/error/loading states, and action naming

If context is missing, state the gap and design around an honest placeholder, inferred local system, or generated asset. Imagegen-generated assets can become first-class design assets when their role is explicit, but they must not impersonate official logos, real product screenshots, real venue/object photos, metrics, or brand assets.

For existing projects, extend the local system before inventing a new one. For redesigns, separate what remains, what changes, and what gets deprecated.

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
- For technical instrument surfaces, should the proof object be a 3D instrument/digital twin with anchored state and controls instead of flat cards?
- If this is part of a set, is it structurally different from the other accepted outputs? Reject same-looking variants that reuse warm cards, central rails, right panels, thin borders, status chips, or the same proof-object placement.

If the answer is no, run a `visual direction` pass before adding more UI detail.

## Signature System Gate

For visually memorable pages, especially cultural, editorial, brand, museum, hospitality, portfolio, and premium product surfaces, create a signature visual system before composing sections.

Define:

- Source motifs: 3-5 domain-native forms, textures, artifacts, landscapes, or interface states.
- Spatial metaphor: cave opening, stage, instrument, scroll, atlas, object portrait, workbench, quiet chamber, or another scene that fits the subject.
- Palette origin: colors sampled from the subject's material world, not arbitrary trend palettes.
- Continuity device: a ribbon, horizon, timeline, edge treatment, light path, object trail, or section boundary that connects screens.
- Narrative rhythm: one strong first impression, one slower proof section, one deeper exploration section.
- Modernization ratio: what remains authentic and what becomes contemporary UI.
- Deletion rule: remove any motif, card, label, or decoration that does not strengthen the world.

This gate is not a request to copy a historical or cultural style. It extracts the reason a page works: one coherent world, content paced through that world, and UI elements that feel native to it.

## Taste Calibration Gate

Taste is selection under pressure. It is not adding premium adjectives.

Before generating or implementing an important new visual direction, define:

- Taste stance: three words that describe the desired feeling.
- Anti-reference: three things the design must not resemble.
- Signature restraint: what the design deliberately refuses to show.
- Memorability hook: what the viewer should remember.
- Deletion rule: what gets removed first if the page feels busy.

If a design looks correct but lifeless, run `bolder`. If it looks novel but ugly, run `quieter`, `distill`, and then rebuild around one stronger form.

## Market Calibration Gate

Do not invent a homepage in isolation. Strong product websites usually earn beauty through clarity, proof, and momentum.

Before regenerating a weak homepage, identify:

- One sharp positioning sentence.
- One visible product proof, not an abstract metaphor.
- One narrative movement from problem to capability.
- One brand behavior that feels ownable.
- One conversion path with low friction.

If the design relies on a decorative hero object that does not prove the product, replace it with product proof or an interaction preview.

## Content Judgment Gate

Do not show everything that is true. Decide what the page needs the user to understand now, what can wait, and what should disappear.

For important first screens, define:

- Keep: one primary message, one primary proof, one primary action.
- Defer: supporting details that belong below the fold, in hover states, tabs, or later sections.
- Delete: anything included only to prove thoroughness.

If a first viewport has more than three content zones competing for attention, simplify before styling.

## Desire Minimalism Gate

Minimalism is not emptiness, and psychology is not only comfort. For brand, homepage, and product content pages, the psychological job is often to create viewing desire, product desire, curiosity, and willingness to act while keeping the surface simple.

Before choosing color or layout for a minimal persuasive surface, define:

- Desire job: curiosity, aspiration, confidence, urgency, relief, mastery, belonging, or play.
- Desire mechanism: reveal gap, contrast, transformation, participation, social proof, progress promise, or unfinished story.
- Palette appetite: base mood, emotional accent, action accent, layer tone, and semantic colors.
- Attention path: the first thing noticed, the question it opens, the proof that resolves it, and the action it makes desirable.
- Layout rhythm: margins, grouping, reading width, and where the eye rests.
- Safety signals: visible state, reversibility, preview, confirmation, or progress where the user needs control.

If a design is calm but not magnetic, add a stronger hook through color, contrast, transformation, copy, or interaction preview. If it is exciting but noisy, distill to one desire mechanism.

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

## Layer Document UI Gate

When the user asks for layer decomposition, editable UI output, HTML editing, chart/table layers, or structured UI elements, use a Design Layer Document as the canonical design record.

Rules:

- Store the design as `.layerdoc.json` before exporting. Do not make HTML the canonical record.
- Preserve semantic groups: headline, CTA, proof object, chart, table, background, decoration, navigation, and content sections should stay meaningful.
- Charts and tables must carry data, not only drawn marks.
- Export HTML for inspection and element-level editing.
- Run `scripts/design_layer_tool.py validate` before exporting HTML.
- For image-derived designs, use the image only to infer the layer document; future edits happen in the layer document.

Commands:

```bash
python3 scripts/design_layer_tool.py validate examples/opc-homepage.layerdoc.json
python3 scripts/design_layer_tool.py html examples/opc-homepage.layerdoc.json outputs/opc-homepage.html
```

## Composition Workflow

1. Inspect the local project first: framework, component library, styling system, existing tokens, routes, and nearby screens.
   Also inspect local design memory files when present: `DESIGN.md`, Storybook, token files, component docs, screenshots, or `.product-composer/design-system.md`.
2. Choose the workflow mode before styling:
   - rough prompt -> direction matrix or inferred design thesis
   - screenshot/Figma/reference -> DNA extraction and parity implementation
   - accepted concept -> concept lock and parity slices
   - existing app patch -> design memory and smallest useful change
   - full redesign -> failure audit, direction matrix, then new system
   - prototype/layer document -> choose artifact structure before visual polish
3. State a concise design brief before implementation:
   - surface mode
   - surface register
   - input/output mode
   - selected style family and whether it was user-chosen or inferred
   - primary user mission
   - generation direction: reference anchor, choice mode, style dials, concept fidelity, artifact mode, and visual check
   - design thesis inventory: palette roles, type roles, layout thesis, signature element, content voice, and one justified risk
   - asset context and design memory constraints
   - information density
   - keep/defer/delete content judgment
   - desire job, desire mechanism, and palette appetite
   - taste stance and anti-reference
   - visual thesis
   - dominant visual form
   - quality target: what must make the surface feel specific, composed, and non-generic
   - signature system and continuity device when the surface needs memorable visual identity
   - aesthetic risk to avoid
   - one justified design risk
   - motion role and reduced-motion fallback when animation is substantial
   - interaction grammar for frontier surfaces
   - constraints from the existing codebase
   - generated asset plan when imagegen should create hero media, product scenes, illustrations, textures, thumbnails, empty-state art, or concept support imagery
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
   - map visible concept/reference elements to code, user-provided assets, local assets, imagegen-generated assets, or intentional deviations
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
- Prefer icons for tool actions and text labels for commands that need interpretation.
- Ensure text never overlaps, clips, or spills out of buttons, tabs, cards, inputs, tables, or mobile containers.

## Optional Scanner

For frontend projects, run the bundled scanner when useful:

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

Treat scanner output as warnings, not truth. Confirm visually before changing code.

For editable layer documents, use the bundled exporter:

```bash
python3 scripts/design_layer_tool.py validate <file.layerdoc.json>
python3 scripts/design_layer_tool.py html <file.layerdoc.json> <out.html>
```
