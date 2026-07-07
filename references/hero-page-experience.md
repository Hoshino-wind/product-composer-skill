# Hero Page Experience

Use this when a homepage, launch page, portfolio, or brand/product page needs a signature page experience instead of a standard stacked layout.

## Core Principle

Build the page as a sequence of designed screens, not as a pile of interchangeable sections. The first viewport creates the world; later screens prove, deepen, and convert without breaking that world.

## Screen Model

Define the screen model before layout:

1. Screen 1: emotional anchor, product/category signal, one dominant scene, one primary action.
2. Screen 2: proof or mechanism that continues the same spatial world.
3. Screen 3: capability, collection, or deeper product state with a clear rhythm change.
4. Screen 4: trust, commitment, or conversion using the same visual DNA.

Each screen needs one job. If every screen contains a heading, paragraph, cards, and a button with equal weight, the page has no page rhythm.

## Asset System

A single image is not an asset system. Define roles before building:

- Hero asset: the dominant object, scene, product state, generated visual, or user-provided media that carries the first viewport.
- Support asset: a secondary object, detail, crop, icon set, or interface fragment that proves the world is specific.
- Material asset: texture, lighting, surface, depth, or environmental cue that gives the page a physical or digital material.
- Transition motif: object trail, edge treatment, progress rail, section marker, horizon, path, mask, or motion bridge.
- Proof asset: product shot, credible interface slice, real metric source, workflow state, or generated concept clearly labeled by role.

User-provided assets are strongest. Local assets and imagegen-generated assets are acceptable when their role is explicit. If missing visual assets would leave the hero generic, generate with imagegen before implementation or image mockup work, then choose the best result as a role-specific asset. Do not present generated assets as official logos, real product photos, real metrics, or production screenshots.

## Pagination And Page Rhythm

High-impact pages need visible rhythm. Choose one:

- Section pagination: numbered or labeled screens that indicate progression.
- Scroll snap: each viewport has a clean compositional state.
- Progress rail: a thin navigation or marker system tied to screen jobs.
- Scene transition: objects, masks, light, geometry, or material move across screens.
- Next-screen hint: the first viewport leaves a visible clue that the story continues.

Pagination should encode structure, not decorate the page. If the markers can be deleted without changing comprehension, they are ornamental.

## Layout Rules

- Make one dominant viewport object large enough to be remembered.
- Use asymmetry, cropping, scale contrast, and negative space as composition tools.
- Keep proof, cards, and secondary UI away from the hero until the dominant scene is established.
- Use typography as part of the composition, not only as labels above boxes.
- Let each lower screen change rhythm while preserving palette, material, type character, and motif logic.
- Avoid default two-column SaaS heroes unless the product proof genuinely needs that split.
- Avoid full dashboard screenshots as the default hero proof; prefer a selected interface slice, workflow state, product object, or generated scene with a clear role.

## Output Contract

Before implementation or image generation, state:

- Hero/page experience thesis: what the page should feel like and why.
- Screen model: 3-4 screens, each with one job.
- Asset system: hero, support, material, transition, and proof assets.
- Text-to-image plan: what to generate when the user has not provided enough strong assets.
- Pagination/page rhythm: the chosen rhythm device and how it behaves.
- Continuity device: what keeps sections from feeling unrelated.
- Deletion rule: what disappears first if the page feels crowded.

## Failure Signs

Redesign when:

- The first viewport has no dominant scene.
- The page depends on one small image in a corner.
- The page is only headline, subcopy, screenshot, cards, and logos.
- Sections feel like separate templates rather than a continuous page.
- The layout is cramped because every proof point is forced into the hero.
- The asset system is only a background texture or generic abstraction.
- Pagination exists but does not explain sequence, depth, or progress.
