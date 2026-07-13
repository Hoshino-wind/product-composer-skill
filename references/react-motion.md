# React Motion

## Principle

Use time and input to clarify hierarchy, state, continuity, spatial meaning, feedback, atmosphere, or a memorable content-native behavior. This optional Modifier consumes the active `DirectionContract` and does not create a secondary route hierarchy; static product behavior and the selected route remain authoritative.

Motion is not a fixed layer of fade-ups, nor must a complete website share one effect. Each region may use a distinct mechanism when its content earns that mechanism and the whole route shares intentional timing, transformation, input, and handoff rules.

## Contents

- [Eligibility](#eligibility)
- [Motion role map](#motion-role-map)
- [Asset-derived choreography](#asset-derived-choreography)
- [Region And Scroll Choreography](#region-and-scroll-choreography)
- [Component selection](#component-selection)
- [Static-first integration](#static-first-integration)
- [Performance](#performance)
- [Reduced motion](#reduced-motion)
- [Acceptance checks](#acceptance-checks)

## Eligibility

Motion is optional. Read `Motion energy` from the active `DirectionContract`, then validate it against website archetype, content, target devices, input model, performance budget, and access needs. The correct role may be `none` even when expressive motion is technically possible.

Use motion when it provides at least one observable benefit:

- directs attention or establishes anticipation without delaying access
- reveals a causal sequence, product state, collection relationship, or spatial rule
- maintains identity and orientation across a transition
- confirms an action, system response, or commitment
- turns content-native material, time, or movement into a signature experience
- makes an atmosphere or emotional change legible as part of the real subject

Compare the animated behavior with a static baseline and name the benefit to comprehension, orientation, state clarity, confidence, memory, or emotional fit. Experiential benefit may be qualitative, but it must still be tied to the content rather than novelty alone.

```text
Motion eligibility decision
- static baseline:
- observable benefit:
- evidence:
- decision: retain | reduce | none
- removal trigger:
```

Avoid or reduce sustained motion for repeated high-frequency work, dense comparison, forms and tables, urgent decisions, low-power contexts, unstable layouts, or any flow where it increases time-to-action. A Brand, Portfolio, or Cultural experience can legitimately carry more motion than an operational work surface when its content and target environment support it.

## Motion role map

Assign a primary role to each effect; add a secondary role only when the relationship remains clear.

| Role | Product purpose | Typical use | Static equivalent |
| --- | --- | --- | --- |
| focus | direct the first look or current locus | headline, selected object, active region, or product detail | scale, contrast, position, and explicit selected state |
| reveal | expose information or material at the right moment | progressive detail, mask, crop, disclosure, or completed result | visible hierarchy and disclosure control |
| continuity | preserve identity, location, or causality | persistent object, route path, shared camera, or progress field | stable object, connector, order label, or before/after relationship |
| feedback | confirm input, state change, success, warning, or wait | button response, selection, save, loading, error, or mode change | immediate icon, text, color-plus-shape, and status message |
| signature moment | make a content-native behavior memorable | product transformation, spatial scene, authored type, or cinematic passage | resolved key visual, sequence, or product portrait |

Signature behavior may appear in several regions when each occurrence develops the same content system rather than replaying the same trick. Do not conceal critical content behind reveal motion or let feedback replace an accessible status announcement.

## Asset-derived choreography

For a media-led opener, route, or complete website, derive motion from content beats, region geometry, selected media, and state progression rather than from an effect catalog.

```text
Interaction-to-media map
- content beat and region job:
- trigger and user intent:
- source state:
- affected media or type role:
- state progression:
- response and destination state:
- meaning made clearer:
- static and reduced-motion equivalent:
- removal trigger:
```

Valid relationships include a video timeline revealing real time, layered cutouts creating bounded depth, a mask uncovering a material or proof transition, product UI changing through a real workflow, an object persisting while its context changes, or type exchanging roles with media at a chapter boundary. These are possibilities, not defaults.

Tilt, glow, magnetism, particles, pointer-follow, marquee, and scroll-scrub are rejected only when they have no content/media cause, user-readable purpose, or experiential benefit. They are not globally banned and they are not accepted merely because an award site uses them.

Use states appropriate to the mechanism, such as `rest`, `invitation`, `response`, `transition`, `interrupted`, and `reduced-motion`. Hover may enrich invitation but cannot be the only path to essential content. Time-based media needs a poster, loading state, pause behavior when sustained, and a static fallback; autoplay must not carry essential information.

## Region And Scroll Choreography

Treat scroll and other inputs as architecture, not a universal reveal trigger. Choose the mechanism that matches the relationship:

- native document flow for reading, FAQ, pricing, specifications, testimony, and ordinary explanation
- sticky or pinned chapters when one object changes through ordered states
- scroll-scrubbed state changes when progress maps meaningfully to time, distance, assembly, or transformation
- bounded snap segments when discrete states require clear arrival and exit
- horizontal translation for same-level collections, cases, or timelines with visible progress
- mask, crop, split, or replacement when comparison or chapter exchange is the content
- video-timeline mapping for real footage, product recording, or authored animation
- spatial camera travel, drag, or map navigation when space itself carries the content
- type/media role exchange when editorial hierarchy changes between chapters
- click, hover, pointer, keyboard, or time triggers when they fit the public interaction model better than scroll

Record one mechanism per interactive region; ordinary regions may record `native flow`.

```text
Region choreography record
- region job and content beats:
- geometry and scroll length:
- trigger and input model:
- mechanism:
- affected media:
- state progression and thresholds:
- entry, handoff, and exit:
- simultaneous energy and competing motion:
- interruption, escape, and progress:
- runtime cost and loading behavior:
- target-device treatment:
- reduced-motion and static fallback:
```

A distinct effect may be designed for every region when each effect is earned by that region's content and the sequence shares an intentional motion grammar. Judge simultaneous competition, redundancy, transition quality, runtime cost, and input control—not the raw count of effects. Repeating one preset everywhere and forcing one global effect are both failures.

Do not hijack scrolling or trap the viewer inside a pinned, horizontal, or spatial region. Preserve native input expectations, a visible sense of progress, a bounded exit, interruption behavior, focus stability, and access to essential content before animation initializes. A region may change the meaning of the wheel or pointer only when the mode transition is explicit and reversible.

MotionSites and award-site references should contribute an observed relationship—persistent-object transformation, scene replacement, mask handoff, spatial camera move, collection navigation, video-state mapping, or type/media exchange—not their easing values or visual skin. A first-viewport still cannot prove any of these mechanisms.

## Component selection

Choose the smallest local mechanism that serves the region:

- CSS transition for simple hover, focus, disclosure, and state feedback
- existing project motion primitive for coordinated component states
- framework animation library when sequencing, layout, scroll progress, or gesture state genuinely needs it
- native video or image sequence when authored media already contains the needed transformation
- canvas, WebGL, 3D, or shaders when spatial, material, simulation, or visual-computation relationships are the content and the target devices can support them

Do not restrict canvas or WebGL to an arbitrary count, and do not add them because a demo looks attractive. Several spatial regions may be valid; one decorative scene may still be invalid. Inspect license, accessibility, bundle cost, loading, thermal impact, fallback behavior, and repository conventions.

Essential actions must not depend on hover, cursor tracking, high-precision drag, scroll-jacking, or a canvas-only control. Decorative motion stays silent to assistive technology; meaningful state remains semantic.

## Static-first integration

Prove static hierarchy and content access before animating:

1. Render final content, navigation, actions, and current state without motion.
2. Confirm first, second, and third reads through type, proportion, spacing, and contrast.
3. Reserve stable geometry for pinned regions, media, and state transitions.
4. Add one region mechanism at a time and verify reading order, state truth, and interaction rights.
5. Keep primary navigation, action, orientation, and core content available immediately.
6. Test loading, failure, interruption, focus, reduced-motion, and declared target-device states.

Static-first does not require the final experience to look static. It ensures that motion enriches a complete composition rather than compensating for a weak one. Avoid layout shift by reserving geometry and preferring transform, opacity, clip, or media-time changes when appropriate.

## Performance

Set a budget proportional to the surface and declared target devices. Measure rather than assuming:

- lazy-load heavy regions below the first useful boundary
- preload only media required for a stable entry and first transition
- pause off-screen, hidden-tab, background, or inactive-mode animation
- avoid a separate observer, event loop, or canvas for every repeated item
- keep pointer, wheel, and scroll handlers bounded and non-blocking
- prevent motion from delaying hydration, input, navigation, or useful content
- test long routes, rapid direction reversal, resize, interruption, and concurrent media
- profile representative target hardware instead of automatically testing devices outside the declared scope

Degrade from heavy scene to lightweight transition to static equivalent without changing product meaning. A PC-only contract may retain a desktop-only mechanism when explicitly intended and verified; it still needs a stable fallback for load failure and reduced motion.

## Reduced motion

Honor `prefers-reduced-motion` at the system boundary and allow product-level control when sustained motion is central to the experience.

- Remove parallax, auto-panning, continuous rotation, particles, large zooms, and nonessential looping when they create vestibular or attention burden.
- Replace spatial travel with an immediate state change, static sequence, or short low-distance transition.
- Preserve equivalent state and meaning, including content order, through text, position, connectors, and semantic announcements.
- Keep focus visible and prevent motion from stealing focus or moving a target during interaction.
- Ensure the reduced experience looks intentional and complete rather than frozen mid-transition.

Reduced motion is not merely shorter duration. When an effect communicates causality or location, provide a static relationship that carries the same information.

## Acceptance checks

- Every effect has a content/media cause, a role, and a stated user or experiential benefit.
- Motion is mapped from content beat and region geometry rather than screen count or an effect catalog.
- Every interactive region records trigger, mechanism, state progression, handoff, input control, runtime cost, and fallback.
- Distinct per-region effects remain coherent through named motion-grammar rules; neither one repeated preset nor one forced global effect dominates the route.
- Sticky, pinned, horizontal, snap, scrubbed, video, and spatial mechanisms have explicit entry, progress, interruption, escape, and exit behavior.
- Static hierarchy, actions, orientation, content, and state work before animation loads.
- Motion energy follows the contract but can be reduced when task or runtime evidence requires it.
- Animated containers remain dimensionally stable and avoid accidental layout shift.
- Keyboard, focus, pointer, wheel/trackpad, loading, failure, and declared target-device behavior remain usable.
- `prefers-reduced-motion` preserves equivalent state and meaning.
- Heavy or decorative motion has a deliberate fallback and does not block action.
