# Reference Translation

## Principle

Translate the design logic of a supplied reference without blindly copying pixels or drifting into an unrelated style. This optional Modifier consumes the active `DirectionContract` and does not create a secondary route hierarchy; source evidence may constrain contract fields, while the owning route still governs the user job, content truth, and implementation behavior.

Separate observation, interpretation, and adaptation so another person can trace why a trait survived, changed, or was excluded.

## Contents

- [First read](#first-read)
- [System read](#system-read)
- [Temporal read](#temporal-read)
- [Media ecology](#media-ecology)
- [Page trace](#page-trace)
- [Translation read](#translation-read)
- [Provenance record](#provenance-record)
- [DNA contract](#dna-contract)
- [Locked/adaptable decisions](#lockedadaptable-decisions)
- [Conflict priority](#conflict-priority)
- [Copying boundary](#copying-boundary)
- [Acceptance checks](#acceptance-checks)

## First read

Capture the perceptual outcome before measuring details:

- first focal point and second focal point
- page rhythm and direction of travel
- dominant form or product object
- density and quiet-space pattern
- emotional tone and strongest color relationship
- content voice and label behavior
- whether the artifact reads as product, brand, hybrid, editorial, cultural, or utility

Write observations as visible facts: `a large pale object occupies the center`, not `the designer wanted calm`. If the first read is unclear, record the ambiguity instead of inventing intent.

## System read

Extract repeatable relationships:

- layout grid: margins, columns, gutters, alignments, section height, and breakpoint behavior
- type system: display, body, data, control, metadata, line length, weight, case, and leading
- color roles: base, surface, text, quiet text, border, accent, action, and semantic state
- surface and material behavior: flat, layered, paper, glass, metal, canvas, or native software
- component density and grouping: rows, cards, controls, tables, navigation, overlays, and repeated offsets
- imagery: crop, scale, light, realism, angle, texture, and integration
- spacing rhythm: tight semantic groups, section gaps, and repeated alignment rules
- content hierarchy: primary, deferred, grouped, compared, or hidden information
- structural devices: which rules, numbers, chips, badges, or dividers carry meaning
- interaction promise: what appears clickable, adjustable, inspectable, animated, reversible, or committed

Distinguish a true system from an incidental screenshot condition. One unusual spacing value is not a rule unless it supports a repeated relationship.

## Temporal read

Inspect time and input directly rather than inferring them from a still:

- entry, loading, and first useful state
- native document flow, pinned ranges, snap segments, horizontal tracks, route transitions, and spatial modes
- trigger: scroll, wheel, pointer, drag, click, keyboard, time, video progress, or system state
- state progression and thresholds inside each region
- persistent, replaced, masked, transformed, or newly introduced objects
- interruption, reverse direction, resize, focus, escape, and completion behavior
- handoff from one region or interaction mode into the next
- reduced-motion, loading-failure, and static equivalence when observable

A first-viewport screenshot cannot prove a temporal mechanism. A full-page still may prove section order and approximate geometry, but cannot prove sticky behavior, scroll-scrub, snap, horizontal mapping, drag, spatial travel, interruption, or timing. Record `not observed` rather than inferring motion from visual style.

## Media ecology

Inventory the media relationships across the complete route:

- still photography, illustration, image sequence, video, screen recording, product UI, SVG, canvas/WebGL/3D, shader, typographic field, texture, and audio
- which content beats and regions each item serves
- which items persist or transform across states
- where several media synchronize inside one region
- where layout, type, data, or live DOM carries the content without a new asset
- proof, atmosphere, support, and placeholder boundaries
- loading, poster, failure, transcript, and static behavior

Do not estimate design quality from source count. A single persistent model may carry a complete spatial process; a media-dense route may legitimately combine hundreds of items. Judge whether the media graph communicates the content, supports state changes, and remains truthful.

## Page trace

For a live site, gallery case, or recorded page reference, inspect the complete public experience from opener to footer or interaction endpoint. Scroll through ordinary flow, enter bounded modes, open representative details, and use the native interaction verbs needed to understand the structure. Do not treat the gallery platform shell as the case design.

```text
Page trace
- source and evidence level: live runtime | recording | full-page still | first viewport
- website archetype and user job:
- route/page map:
- ordered content beats:
- region geometry: intrinsic | subviewport | viewport | overviewport/pinned | horizontal track | spatial canvas
- media set and reuse:
- trigger and state change:
- handoff and orientation:
- proof, trust, conversion, or terminal state:
- transferable relationship:
- conditional boundary and non-transferable treatment:
```

Separate cross-case invariants from conditional mechanisms. A rare mechanism may enter the conditional library when its content, enabling constraints, and runtime evidence are explicit; it need not recur across unrelated cases to be useful.

## Translation read

Decide what must survive in the target context:

- `locked`: relationships essential to the reference's first read or explicitly required by the user
- `adaptable`: rules whose role should survive while values, components, copy length, breakpoint arrangement, or accessible states change
- `replaceable`: ornament or incidental detail that does not support the product, content, or selected direction

Test every trait against the target user mission, real content, platform, declared target devices, accessibility, brand system, and existing product behavior. The Translation read must name why a changed trait improves fit instead of treating implementation convenience as design evidence.

## Provenance record

Create one record for each reference that materially influences the direction:

- exact source:
- version or access date:
- license boundary:
- traits extracted:
- locked/adaptable decisions:
- material reused:
- conflict resolution:

Record access gaps and uncertain rights. A URL without a stable version, a screenshot without origin, or an image visible only in conversation must be described honestly. `material reused` is `none` when only independently expressed traits are translated.

## DNA contract

Write a compact, reviewable contract before prompting or implementation:

```text
Reference DNA
- source record id:
- First read:
- source observation:
- target translation rule:
- DirectionContract field:
- validation evidence:
- dominant form:
- layout and spacing rules:
- type roles:
- color roles:
- surface/material rules:
- imagery treatment:
- component density:
- interaction promise:
- temporal and scroll relationships:
- media ecology and reuse:
- region geometry and handoffs:
- content voice:
- structural devices:
- locked:
- adaptable:
- replaceable:
- target-context additions:
- prohibited copying or licensed material:
```

For each material trait, link source observation to target translation rule, `DirectionContract` field, and validation evidence. A trait without that chain remains an ungrounded preference and cannot be locked.

Map locked and adaptable traits to named `DirectionContract` fields when they affect visual thesis, composition family, experience architecture, page rhythm, dominant silhouette, material language, palette roles, type roles, signature detail, restraint, or anti-default overrides. Leave unrelated fields unchanged.

## Locked/adaptable decisions

Lock the role and relationship, not arbitrary pixels:

Classify each material trait as exactly one of locked, adaptable, or replaceable; the classifications are mutually exclusive. A locked trait must survive in role and relationship, and its survival requires validation evidence. An adaptable trait must preserve its source role while changing implementation details for a recorded reason.

```text
Classification decision
- trait:
- classification: locked | adaptable | replaceable
- preserved role:
- adaptation reason:
- validation evidence:
```

- Lock hierarchy when changing it would alter the first read; adapt exact sizes for content and viewport.
- Lock palette roles when their tension defines the world; adapt values for contrast, tokens, and brand constraints.
- Lock density and grouping when they support comparison or task speed; adapt component mechanics to local patterns.
- Lock a dominant form when it carries recognition; adapt crop and geometry to declared target-device bounds.
- Lock interaction meaning; adapt gestures and controls for accessibility and platform conventions.

For every deviation from a locked trait, record `adjusted`, `reason`, and `evidence check`. Do not silently relabel a broken constraint as adaptable after implementation.

## Conflict priority

Resolve conflicts in this order:

1. truth, authorization, license, privacy, and safety
2. user mission, task correctness, and real product behavior
3. accessibility and platform constraints
4. explicit user requirements and established local brand/product systems
5. locked reference relationships
6. adaptable reference traits and aesthetic preference

Record every resolved conflict:

```text
Conflict record
- higher-priority rule:
- lower-priority trait:
- evidence:
- winner:
- affected contract fields:
- decision owner:
```

When higher-priority evidence changes the central visual thesis, revise the `DirectionContract` explicitly. When it changes only one trait, record the local adaptation and preserve the rest of the DNA.

## Copying boundary

Do not copy a reference's protected expression, assets, code, text, distinctive naming, or exact composition unless authorization and license allow that reuse. Never disguise reuse as inspiration.

Keep source facts separate from interpretation:

- source facts describe directly observable content and documented provenance
- interpretation explains the inferred system or effect and must be labeled as analysis
- translation states a fresh target rule tied to the new user mission

Use local components, tokens, content, states, and accessible behavior. Do not reproduce visual defects, hidden actions, fake data, inaccessible contrast, or device assumptions outside the declared target scope merely because they appear in the source.

## Acceptance checks

- First read, System read, Temporal read, Media ecology, Page trace, and Translation read are distinct and complete when the source is a live or recorded website.
- The complete route was inspected to its footer or interaction endpoint, or the evidence limit is explicit.
- Static evidence is never used to claim an unobserved scroll, drag, snap, sticky, spatial, or timing mechanism.
- Observed source facts are separated from interpretation and target decisions.
- Every material reference has the required provenance record and access gaps.
- The DNA contract names locked, adaptable, replaceable, and prohibited material.
- Reference constraints map to specific contract fields instead of creating another route.
- Deviations from locked relationships have reason and evidence.
- Conflict priority protects truth, task behavior, accessibility, and licensing.
- Reused material is authorized and declared; otherwise the translation is independently expressed.
