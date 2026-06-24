---
name: product-composer
description: "Use when designing, redesigning, generating, critiquing, or implementing high-quality UI surfaces: websites, apps, dashboards, admin panels, SaaS workflows, AI products, command canvases, forms, data views, landing pages, product content pages, cultural/editorial pages, multi-screen flows, prototypes, or design systems that need product clarity, distinctive art direction, non-generic aesthetics, interaction grammar, desire-led minimalism, and responsive verification. If Ant Design APIs/components are explicit, also use antd."
---

# Product Composer

## Overview

Compose UI as a product system, not a decorative page. Use Ant Design's product-order mindset for complex work surfaces, Impeccable-inspired execution discipline to avoid generic AI UI, signature art direction for memorable pages, and interaction grammar to invent new control relationships when traditional pages are insufficient.

Prefer the user's existing design system, component library, routing, and styling conventions. Introduce a new visual language only when the project lacks one or the user explicitly asks for a redesign.

## Reference Routing

Read only the references needed for the task:

- `references/ant-design-product-values.md`: read for enterprise products, dashboards, admin tools, forms, tables, Ant Design projects, or complex workflows.
- `references/impeccable-execution-model.md`: read for new UI, redesigns, visual polish, critique, or avoiding generic AI output.
- `references/interaction-grammar.md`: read for AI products, agent workflows, command surfaces, creative tools, simulations, complex operations, or any request for new interaction design.
- `references/taste-calibration.md`: read before net-new visual concepts, after user feedback like "ugly", "generic", "no taste", "too traditional", or when the design needs a sharper aesthetic stance.
- `references/market-calibration.md`: read after user asks to look at excellent market examples, when a homepage feels fake, self-indulgent, too conceptual, or disconnected from real product evidence.
- `references/content-judgment.md`: read when a surface feels dense, over-explained, crowded, or when the user says the design should make stronger decisions.
- `references/desire-minimalism-psychology.md`: read when the user asks for minimalism plus psychology, viewing desire, product desire, conversion pull, appetite, emotional attraction, comfortable but not boring color, or a layout that makes people want to keep watching or use the product.
- `references/image-generation-aesthetic-calibration.md`: read when the user asks to directly generate, draw, or preview UI as an image without code, when image-generated UI looks better than hand-built/vector attempts, when generated UI is rejected as ugly or lacking taste, or when the agent needs reusable prompt templates for elegant UI images.
- `references/visual-direction.md`: read for any net-new UI, homepage, concept, visual redesign, product identity, or when the output risks becoming diagrammatic, generic, cluttered, or ugly.
- `references/signature-aesthetic-systems.md`: read for cultural, editorial, museum, hospitality, fashion, premium brand, emotionally rich homepages, multi-screen visual consistency, or when the user asks for the quality of the stronger Dunhuang-style result without copying that style.
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

## Universal UI Brief Gate

Before designing any substantial surface, define:

- Surface mode: product, brand, hybrid, frontier, editorial, cultural, or utility.
- User mission: what the viewer or operator needs to understand, choose, complete, or desire.
- Evidence source: product screenshot, workflow state, cultural material, venue/object imagery, dataset, brand asset, or existing design system.
- Signature system: the dominant form, material language, palette source, motion/continuity idea, and one ownable detail.
- Density contract: sparse, medium, dense, or dense-with-air; decide what is absent as deliberately as what is present.
- Output path: image mockup, coded implementation, design critique, design prompt, or design-system guidance.

Do not start from a generic layout pattern. Start from the surface's evidence, mission, and signature system, then choose layout.

## Interaction Grammar Gate

Before designing an AI, agentic, automation, creative, or complex workflow surface, define the interaction grammar before the visual layout:

- User intent: what does the user express, command, inspect, or negotiate?
- System agency: what does the system infer, propose, simulate, execute, or refuse?
- Control transfer: where can the user adjust autonomy, pause, approve, override, or rewind?
- Time model: how do past actions, current execution, future plan, and uncertainty appear?
- Object model: what is the living object the user manipulates: goal, run, plan, scene, dataset, policy, workspace, or workflow?
- Commitment model: what can be previewed, simulated, committed, reverted, or audited?
- Interaction level: cognitive model, decision path, system response, feedback loop, or physical gesture? Do not turn interaction design into literal drag/click/slide affordances unless the product truly supports them.

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

If the answer is no, run a `visual direction` pass before adding more UI detail.

## Signature System Gate

For visually memorable pages, especially cultural, editorial, brand, museum, hospitality, portfolio, and premium product surfaces, create a signature visual system before composing sections.

Define:

- Source motifs: 3-5 domain-native forms, textures, artifacts, landscapes, or interface states.
- Spatial metaphor: cave opening, stage, instrument, scroll, atlas, object portrait, workbench, quiet chamber, or another scene that fits the subject.
- Palette origin: colors sampled from the subject's material world, not arbitrary trend palettes.
- Continuity device: a ribbon, horizon, timeline, edge treatment, light path, object trail, or section boundary that connects screens.
- Narrative rhythm: one strong first impression, one slower evidence section, one deeper exploration section.
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

If the design relies on a decorative hero object that does not prove the product, replace it with product evidence or an interaction preview.

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
- Use constraints to prevent known failures: fake drag/slide gestures, photo/quote/widget collages, dashboard templates, and dense feature grids.
- Inspect the result visually before claiming it worked. If the output only appears in chat and does not save to disk, say so instead of copying an old asset.

## Composition Workflow

1. Inspect the local project first: framework, component library, styling system, existing tokens, routes, and nearby screens.
2. State a concise design brief before implementation:
   - surface mode
   - primary user mission
   - information density
   - keep/defer/delete content judgment
   - desire job, desire mechanism, and palette appetite
   - taste stance and anti-reference
   - visual thesis
   - dominant visual form
   - signature system and continuity device when the surface needs memorable visual identity
   - aesthetic risk to avoid
   - one justified design risk
   - interaction grammar for frontier surfaces
   - constraints from the existing codebase
3. Shape the screen around workflow, not decoration:
   - primary task first
   - clear hierarchy between navigation, work area, controls, feedback, and secondary details
   - predictable states for loading, empty, error, success, disabled, selected, and active
4. Build with existing primitives:
   - use local components and tokens where available
   - use familiar controls for familiar jobs
   - keep dimensions stable for boards, grids, tables, toolbars, counters, and icon buttons
5. Tune deliberately:
   - `bolder`: increase identity when the page is correct but forgettable
   - `quieter`: reduce visual noise when the UI competes with the task
   - `distill`: remove decoration, copy, or controls that do not serve the user mission
   - `harden`: cover overflow, i18n, edge cases, accessibility, and responsive states
6. Verify in a real rendered environment when feasible, using screenshots across desktop and mobile before claiming the UI is finished.

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
- For minimal persuasive UI, use color as appetite and attention, not decoration: avoid defaulting to black and white; choose a small expressive palette with a clear base, emotional accent, and action color.
- Do not fake interaction with labels like "drag", "click", or "slide" on static or conceptual UI. Show the product's relationship model instead.
- Avoid generic AI signatures: purple-blue gradients, decorative orbs, nested cards, arbitrary glass panels, huge rounded icon tiles, vague SaaS copy, and ornamental layout flourishes.
- Do not make a one-hue interface. Use neutrals, semantic colors, and one or two purposeful accents.
- Do not scale font size with viewport width. Use stable type scales and responsive layout constraints.
- Use visual assets when a website, game, object, venue, product, or brand page needs inspection or emotional specificity.
- Prefer icons for tool actions and text labels for commands that need interpretation.
- Ensure text never overlaps, clips, or spills out of buttons, tabs, cards, inputs, tables, or mobile containers.

## Optional Scanner

For frontend projects, run the bundled scanner when useful:

```bash
node /Users/gaozengyu/.codex/skills/product-composer/scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

Treat scanner output as warnings, not truth. Confirm visually before changing code.
