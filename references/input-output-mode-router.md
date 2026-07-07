# Input Output Mode Router

Use this when the user gives a rough prompt, screenshot, Figma frame, video, existing app, accepted concept, 3D/WebGL request, quick patch, full redesign, or ambiguous deliverable.

## Principle

The input mode determines the workflow. Do not use the same process for a vague homepage prompt, a screenshot replication, a product dashboard patch, and an accepted image concept.

## Input Modes

### Rough Prompt

Use when the user asks for a UI with little detail.

- define audience, job, surface register, and design thesis inventory
- use `direction-matrix-builder.md` if taste is unclear
- use `asset-context-protocol.md` for named brands or products
- do not code until the visual direction is narrow enough to build

### Screenshot Or Figma

Use when the user provides a concrete visual reference.

- use `reference-dna-extraction.md`
- decide strict parity or product-system extension
- extract layout, type, color roles, density, component rhythm, copy voice, and interaction promise
- implement with visual comparison, not reinterpretation

### Video Or Motion Reference

Use when the input includes animation, scroll behavior, transitions, or a recorded UI.

- capture the key states
- name the transition moments
- decide what motion must survive and what can become static
- define reduced-motion fallback
- verify state order and timing after implementation

### Accepted Concept

Use when an image concept or visual comp has been approved.

- use `concept-to-implementation-lock.md`
- inventory locked elements before coding
- implement in parity slices
- do not use the concept as loose mood

### Existing App Patch

Use when changing a live project or one screen in a system.

- use `design-memory-consistency.md`
- inspect tokens, component patterns, nearby screens, and states
- preserve local density and interaction rules
- make the smallest visual change that solves the task unless redesign is requested

### Full Redesign

Use when the user asks for a new direction.

- audit current failure first
- choose surface register and style family
- generate or present direction matrix if taste is open
- create a design thesis inventory
- only then implement

### 3D Or Immersive Request

Use when the main object is spatial, simulated, physical, or inspectable.

- define the object model
- decide camera, scale, material, lighting, and interaction
- keep controls anchored to the object or state
- verify the canvas is nonblank, framed, responsive, and performant

## Output Modes

Choose one deliverable:

- coded app: real interactions, local state, browser verification
- HTML preview: portable inspection and fast visual feedback
- image mockup: visual direction only
- design canvas: side-by-side variants or style comparison
- prototype: clickable flow or state machine
- layer document: structured editable UI representation
- critique: diagnosis and next direction without implementation

## Mode Mismatch Warnings

- Vague prompt + immediate code usually creates generic UI.
- Screenshot request + redesign behavior breaks user intent.
- Accepted concept + engineering convenience causes drift.
- Existing app + new visual language creates inconsistency.
- Full redesign + tiny patch thinking produces timid output.
- Prototype request + static mockup misses the product behavior.

When the mode is unclear, state the inferred mode before proceeding.
