---
name: product-composer
description: "Use when creating or substantially redesigning UI where visual direction, aesthetic judgment, asset-family art direction, image-concept generation, accepted-design fidelity, rendered repair, or artifact-maturity or visual-parity judgment materially affects the result."
---

# Product Composer

## Principle

Compose a specific UI system, not a fashionable template. Preserve product correctness, local conventions, and accepted visual decisions while producing the outcome appropriate to the selected phase.

## Creative Core

Act as a creative director as well as a contract governor. Produce a positive visual thesis before applying anti-defaults; constraint compliance alone is not a designed result.

- Let truth constrain claims, not imagination; never let invention impersonate proof.
- Derive order from the user mission and expressive force from the intended feeling.
- Design relationships among content, control, proof, space, and time before components or assets.
- Resolve attention, silhouette, proportion, rhythm, and silence before surface polish.
- Use fixed anchors for coherence and one controlled tension or exploration axis for character.
- Treat layout, type, image, material, and motion as one visual grammar.
- Generate visibly different alternatives when direction is unresolved; make selection and deletion part of taste.
- Judge the direction in an inspectable target context, not from adjectives, prompts, or isolated polish.

## Route

- Phase: Explore | Implement | Repair
- Surface: Product | Brand | Hybrid
- Modifiers: Data | Frontier | Cultural | Image | Motion | Reference-led

Choose exactly one Phase and one Surface. Add only Modifiers that change required behavior or evidence; deduplicate repeated owners. Infer and disclose when safe, or ask one focused question when a wrong choice would materially change the result.

Design read and direction parameters are Design Contract fields, not route axes. Reference-led requires a supplied or accepted visual reference, or an explicit parity or fidelity target. Preserving an existing design system, product workflow, or interaction convention does not add Reference-led.

Add Data only when value or record semantics—such as comparison, monitoring, analysis, source, freshness, provenance, or risk—materially change decisions, states, or evidence. Dashboard work adds Data when its requested purpose is analytics, monitoring, comparison, provenance, or risk, because value and record semantics then define the surface. An analytics label on a generic workspace or onboarding flow alone does not add Data.

## Design Contract

Design Contract is the only runtime record. Every owner reads and updates this same record.

- Route: selected Phase, Surface, and behavior-changing Modifiers
- DirectionContract projection: complete visual-direction record below
- Experience architecture and region model: beats, geometry, states, continuity, scene graph, proof/action
- Workflow and required states: behavior/recovery; media roles, state progression, device variants, loading, fallbacks
- Truth and provenance ledger: source, status, role, uncertainty, rights
- Artifact target and maturity: requested reusable output and evidenced maturity
- Functional delta: behavior, data, permissions, recovery, irreversible actions, accessibility, responsive/performance constraints
- Locked and adaptable decisions: preservation boundary
- Acceptance checks: behavioral, rendered, structural, provenance, judgment evidence; contract-valid/visual-pass/runtime-pass verdicts

Do not implement an image concept until Functional delta is complete. Generated or inferred material is not factual proof.

### DirectionContract Projection

`DirectionContract` is the named visual-direction projection of the Design Contract, not a second record.

| DirectionContract field | Design Contract field |
| --- | --- |
| Design read | Design read |
| Visual thesis | Visual thesis |
| user mission | user mission |
| aesthetic stance | aesthetic stance |
| tension pair | tension pair |
| visual genre | visual genre |
| attention strategy | attention strategy |
| Style family | Style family |
| dominant silhouette | dominant silhouette |
| composition family | composition family |
| experience architecture | experience architecture |
| page rhythm and continuity | page rhythm and continuity |
| Composition variance | Composition variance |
| Motion energy | Motion energy |
| Information density | Information density |
| material language | material language |
| image-world thesis | image-world thesis |
| palette roles | palette roles |
| type roles | type roles |
| signature detail | signature detail |
| justified risk | justified risk |
| restraint | restraint |
| fixed anchors | fixed anchors |
| exploration axis | exploration axis |
| anti-defaults | anti-defaults |
| Override condition | Override condition |
| Deletion rule | Deletion rule |

### Stage Handoff

Every stage summary updates the same Design Contract. Before unloading owner documents, preserve the complete record rather than a partial field list.

| Handoff record | Preservation rule |
| --- | --- |
| Design Contract | all fields, including the complete DirectionContract projection |

## Owner Matrix

| Axis | Value | Owner reference |
| --- | --- | --- |
| Phase | Explore | direction: references/direction-system.md<br>validation-only: references/verification.md + necessary claim owner |
| Phase | Implement | references/implementation-fidelity.md |
| Phase | Repair | references/repair-rendered-ui.md |
| Surface | Product | references/product-surfaces.md |
| Surface | Brand | references/brand-experiences.md |
| Surface | Hybrid | references/product-surfaces.md<br>references/brand-experiences.md |
| Modifier | Data | references/product-surfaces.md |
| Modifier | Frontier | references/frontier-interactions.md |
| Modifier | Cultural | references/chinese-aesthetic.md |
| Modifier | Image | references/image-concepts.md |
| Modifier | Motion | references/react-motion.md |
| Modifier | Reference-led | references/reference-translation.md |
| Gate | Asset truth | references/asset-context.md |
| Stage | Verify | references/verification.md |

Apply the Asset truth gate when assets affect behavior, evidence, factual claims, or composition. A missing target UI, source tree, or rendered baseline is a Frame or verification gap, not an Asset truth input unless the task supplies or explicitly requires it as a media artifact or proof object. Asset truth is not a route axis or Modifier. Verify is a subsequent stage owner, not an initial route owner.

## Reference Windows

- Active references: owner documents open in the current window
- Normal maximum: 3
- Window close: write decisions into the complete Design Contract, then unload all owner documents
- Owner overflow: open sequential windows of at most 3; never omit an owner
- Exception set: R3 only

| Exception | Initial route | Active owner references | Count |
| --- | --- | --- | --- |
| R3 | Implement / Product / Image + Reference-led / accepted image concept | implementation-fidelity.md<br>product-surfaces.md<br>image-concepts.md<br>reference-translation.md | 4 |

R3 is the only exception. No other window may exceed 3. Close R3 before opening a later verification window.

## Phase Outcomes

- Entry intent: direction-only | implementation-authorized | rendered-repair | validation-only

Entry intent interprets the requested outcome; it is not a route axis or Phase. Every request still selects exactly one Phase and one Surface. An implementation-authorized new UI selects Implement and completes a selected or inferred DirectionContract before the first slice. Validation-only uses the artifact's Surface and verification plus only necessary claim owners within the normal reference-window budget; it never opens R3.

Create, design, or redesign alone selects direction-only Explore; Implement requires an explicit request to build, implement, edit target code, or otherwise mutate the target project. Preserve this boundary even when the requested direction concerns an existing interface.

An explicit screenshot, reference-parity, or reference-fidelity implementation uses the accepted-concept path even when the referenced artifact is unavailable; do not open direction-system.md to replace it. Stop inside the selected Implement / Surface / Modifier owners, then apply the normal Asset truth handoff when the missing reference is material.

A rendered-repair request resolves its baseline gate before inferring any Modifier. When task-scoped rendered evidence or the behavioral baseline is missing, stay in Repair plus the selected Surface with no inferred Modifiers; preserve possible Modifier needs as unresolved Design Contract gaps.

| Trigger class | Entry intent | Phase | Owner | Required input or evidence | Output | Mutation or stop |
| --- | --- | --- | --- | --- | --- | --- |
| new UI or substantial-redesign direction | direction-only | Explore | references/direction-system.md | framed inputs | updated Design Contract plus selected direction | stop; enter Implement only with explicit user authorization |
| new UI or substantial-redesign implementation | implementation-authorized | Implement | references/direction-system.md plus references/implementation-fidelity.md | explicit authorization to infer or select direction, framed inputs, and complete Functional delta | selected or inferred DirectionContract, implemented vertical slice, and updated Design Contract | select or infer direction and complete Functional delta before the first slice; then Verify |
| image concept | direction-only | Explore | references/direction-system.md plus references/image-concepts.md | framed inputs plus image eligibility | updated Design Contract plus image concept | stop; enter Implement only with explicit user authorization |
| accepted concept implementation | implementation-authorized | Implement | references/implementation-fidelity.md | complete Functional delta plus locked direction | implemented vertical slice plus updated Design Contract | Verify; enter Repair only from observed failure |
| rendered repair | rendered-repair | Repair | references/repair-rendered-ui.md | rendered evidence plus observed failure | one evidence-backed repair axis plus updated Design Contract | continue, stop, escalate, or block; stop without new evidence |
| artifact maturity or visual parity validation | validation-only | Explore | references/verification.md plus necessary claim owner | inspectable artifact or claim | Evidence report plus verification gaps | no mutation; do not enter Build, Implement, or Repair |

## Frame

Inspect the project, design memory, assets, real content, target, constraints, and nearby surfaces before selecting the route. Inspect a supplied reference before proposing a direction. Reference-first does not automatically add Reference-led.

Resolve website archetype and route scope before `hero`. A hero is the opening experience inside a route; it may contain several beats, regions, media, and states across several viewports. It is not required to be one `100vh` section, one image, or the whole website. Complete brand, landing, SaaS, portfolio, and experimental sites continue beyond it. Gallery references select case research, not target archetype or geometry.

`website archetype and route scope -> content beats -> region geometry and scroll model -> media palette and many-to-many mapping -> motion grammar and per-region choreography -> typography and interaction -> implementation`

A content beat is not a screen. It may be shorter or longer than a viewport; one region may carry several states, and several beats may share a region. Map all media by communication role, not screen count. One asset may persist across several beats, while one region may combine several media. Derivatives remain one provenance source; source count is not a quality score.

For a live reference, trace the complete route from opener to footer or interaction endpoint using its public inputs. Record `content beat -> region geometry -> media set -> trigger -> state change -> handoff -> proof/conversion`. A first-viewport screenshot can establish composition only; it cannot establish sticky, snap, scrubbed, horizontal, spatial, or full-page behavior.

## Verify

Use Verify after changes or for validation-only Explore. Direction-only Explore is not a change-producing output and stops without opening Verify. Acceptance reporting alone does not open Verify; keep future checks and named gaps in the Design Contract. Report contract-valid, visual-pass, and runtime-pass independently. Structural/package evidence proves only contract-valid; missing evidence is a gap. Test workflow, states, accessibility, target devices/inputs, assets, hierarchy, and parity in runtime. PC-only covers named widths, pointer, keyboard, wheel/trackpad, interruption, and reduced motion. Match claims to evidence; recipes/previews are not runnable or reusable.

## Hard Gates

| Priority | Rule |
| --- | --- |
| 1 | product correctness; state clarity; accessibility; reversibility; truth and provenance; license boundaries |
| 2 | explicit user direction and approved references within valid options |
| 3 | existing design system, components, information architecture, routes, and interaction conventions |
| 4 | owner guidance, then Product Composer aesthetic heuristics |

- Direction parameters: infer from evidence; no universal default; never override locked decisions
- Creative-core gate: require source signals, visible consequences, fixed anchors, and one exploration axis; anti-defaults alone are not a direction
- Art-direction repair gate: diagnose the lowest failure. Reset for Form, Proportion, Memory, or repeated structure; otherwise repair one axis. Review full/thumbnail/crop/blurred-label; preserve truth/mission.
- Composition-divergence gate: for every new UI or substantial redesign, establish a comparison fingerprint; when spatial direction is unresolved and no locked reference exists, compare three structurally different candidates before polish. Reject variants that change only copy, palette, assets, or card styling; compare the selected fingerprint with nearby or accepted outputs visible in the task or project and change at least four fingerprint axes, including at least two structural axes and composition family or experience architecture, unless explicit continuity evidence requires the same system
- Aesthetic anti-defaults: require context and an override condition; popularity alone never creates a ban
- Experience architecture gate: do not code a media- or scroll-led website until its archetype, route scope, ordered content beats, region geometry, interaction states, handoffs, proof/conversion path, and target device scope are recorded in the Design Contract
- Interaction-causality gate: record living object and `input -> response -> meaningful consequence + horizon -> handoff -> fallback`; horizon is moment, region, route, or session. Operational work may retain state; cultural/narrative work may use orientation, revelation, or scene progress. Ambient response is neither primary nor essential; use one state machine
- Media-led implementation gate: before coding record media map, truth/state/device coverage, loading/fallback; independent depth/occlusion/mask/motion requires `source/layer -> mount -> overlap/mask -> transform -> loading -> composite fallback`. A flat image proves none
- Motion-storyboard gate: before coding a multi-state/pinned/spatial/scene-led opener, link entry, transformation, and handoff keyframes to region, media, and state ids
- Readiness gate: contract-valid cannot substitute for visual-pass or runtime-pass; an interactive hero requires every applicable lane to pass

Do not synthesize official proof or factual cultural provenance. Do not let novelty hide state or control. Do not silently redesign an accepted concept. Do not force 3D, motion, image generation, or cultural motifs without the matching Modifier and eligibility evidence. Do not expose skill authoring or self-maintenance as runtime work.

## Optional Scanner

Run `node scripts/ui-pattern-scan.mjs ./src` when visual code could contain known generic-default signals. Treat findings as evidence prompts, not automatic failures.
