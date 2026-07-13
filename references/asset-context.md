# Asset Context

## Principle

Use this conditional truth/provenance hard-gate owner when assets affect behavior, evidence, factual claims, or composition. It consumes and updates the active Design Contract, including its `DirectionContract` projection, and does not create a route axis or Modifier.

An attractive image is not automatically proof. Every asset needs a declared role, provenance boundary, placement, and fallback before it influences a factual claim.

## Contents

- [Context questions](#context-questions)
- [Asset inventory](#asset-inventory)
- [Role ledger](#role-ledger)
- [Asset-before-IA gate](#asset-before-ia-gate)
- [Asset system coverage](#asset-system-coverage)
- [Proof rules](#proof-rules)
- [Atmosphere/support rules](#atmospheresupport-rules)
- [Placeholder rules](#placeholder-rules)
- [Media treatment](#media-treatment)
- [Cultural and factual provenance](#cultural-and-factual-provenance)
- [Acceptance checks](#acceptance-checks)

## Context questions

Ask only what can change truth, direction, or composition:

- Which assets were supplied by the user, already exist locally, or may be generated?
- Which logo, product, interface, venue, person, artifact, or result must be authentic?
- Which asset is the primary proof object, and what claim may it support?
- What may serve only as atmosphere or visual support?
- Is each asset's semantic role informative or decorative?
- What text alternative communicates an informative asset's purpose, and does its time-based or complex content need a caption or transcript?
- If the medium or asset cannot be provided, what equivalent textual fallback preserves the same information or action?
- What rights, consent, confidentiality, attribution, or cultural-source limits apply?
- Which crops, aspect ratios, transparency, resolution, color profiles, or target-device variants exist?
- What is missing, and is honest generation, a labeled placeholder, or omission the correct fallback?

Do not delay a text-led or operational structure for irrelevant media questions. Escalate only gaps that affect a claim, a required visual object, or the selected composition.

Missing relevant media is itself an Asset truth input when its absence constrains proof, factual claims, accessibility, or composition. Open this owner even when no file exists; record an explicit missing-proof or missing-asset gap instead of waiting for a saved asset.

Do not open Asset truth merely because a screenshot, render, or media object could be useful evidence. The task or selected direction must make that object material to proof, factual claims, accessibility, or composition; otherwise record the missing project or verification input in the owning contract without inventing an Asset dependency.

## Asset inventory

Create one record per relevant asset:

```text
Asset record
- id:
- exact source:
- source class: user-provided | local | generated | verified external
- authorization:
- dimensions or quality:
- factual subject:
- narrative role:
- semantic role: informative | decorative
- text alternative or equivalent:
- caption or transcript:
- placement:
- allowed transformations:
- prohibited claims:
- fallback:
```

Inventory real files, not hoped-for media. A filename, URL, or generated preview that cannot be accessed is an availability gap, not an asset; keep that gap in the same ledger with its required role, owner, replacement trigger, and fallback.

## Role ledger

Assign exactly one primary truth role; add a secondary visual role only when it cannot confuse the claim.

| Role | May establish | Must not establish | Fallback |
| --- | --- | --- | --- |
| proof | an inspectable fact, product state, object, place, person, or result within provenance | claims outside the captured subject, time, or authorization | verified replacement, explicit missing-proof state, or omission |
| atmosphere | mood, material feeling, light, depth, or a declared fictional world | product existence, official appearance, real venue, customer, metric, certification, or outcome | simpler material treatment or quiet space |
| support | explanation, navigation, analogy, transition, empty state, or non-factual illustration | the primary evidence for a factual or commercial claim | text, diagram, icon, or omitted embellishment |
| placeholder | intended crop, ratio, slot, or content dependency | completion, authenticity, approval, or final visual quality | labeled neutral frame with replacement requirement |

Generated or stock-like media must not impersonate official assets, screenshots, artifacts, venues, customers, team members, certifications, metrics, or documented results.

Classify accessibility semantics separately from the truth role. An informative asset requires alt text or equivalent text that communicates its purpose and, when time, sequence, or detail exceeds concise alt text, a caption or transcript. A decorative asset uses an empty text alternative and stays out of the accessible reading order; a decorative label is not a substitute for correct markup.

## Asset-before-IA gate

Apply this gate only when available media materially shapes composition; before information architecture is locked, record for each relevant asset its exact source, authorization, dimensions or quality, narrative role, placement, and fallback.

Then choose one outcome:

- `shape IA`: a real proof object determines hierarchy, crop, sequence, or responsive behavior
- `constrain IA`: rights, quality, aspect ratio, or inspectability limits where the object can appear
- `support later`: the asset decorates or explains an already-correct structure
- `exclude`: truth, authorization, quality, or relevance is insufficient

When available media does not materially shape composition, do not create a blocking asset ceremony. Continue with the owning route and keep any later media inside the same role ledger.

## Asset system coverage

When a Brand or Hybrid experience is media-led, inventory media as a many-to-many ecology rather than a folder of interchangeable files or an allocation of one asset per screen. A content beat may use no external media or several synchronized media. One asset may persist through several beats and regions. One region may combine stills, image sequences, video, screen recordings, live DOM UI, SVG, canvas/WebGL/3D, shaders, typographic fields, textures, or audio.

A single source repeated through crops, filters, masks, color shifts, blur, compositing, or perspective is still one source for provenance. Record those treatments as derivations of the same source, but do not equate independent-source count with design quality. Reuse can be the correct visual and narrative mechanism when the same object, interface, place, or world changes state over time.

Create only the composition and communication roles the selected content/region model requires, such as a persistent scene, supporting view, transparent cutout, material or texture field, art-typography asset, transition plate, product recording, live interface, spatial model, ambient audio, or proof object. Keep composition role separate from the primary truth role in the Role ledger. An art-typography raster or video cannot be the sole accessible instance of essential wording.

```text
Asset system manifest
- source id and derivation parent:
- content beats and regions served:
- composition role:
- communication role:
- truth role:
- semantic role:
- states served: rest | invitation | response | transition | interrupted | reduced-motion
- relationship to other media and reuse rule:
- target devices and focal crops:
- poster or first frame:
- loading, failure, and static fallback:
- caption, transcript, or equivalent text when required:
```

Coverage is sufficient when content, proof, transition, interaction state, and failure behavior remain credible and understandable, not when a fixed file or region count is reached. A beat may be text- or DOM-led and need no external media. Another region may legitimately need several synchronized sources. A new state may reuse the same anchor when the transformation itself carries meaning; another crop does not create new proof when the factual subject has not changed.

A video or animated asset requires a poster or first frame; sustained motion requires pause behavior; informative time-based media requires the appropriate caption, transcript, or equivalent text. Transparent cutouts, layered plates, alternate viewpoints, or device-specific art direction are separate sources only when they contain materially different visual information rather than exported variations of the same source.

## Proof rules

Generated atmosphere never substitutes for missing proof.

- Use real or verifiably authorized media when the claim concerns a real product, interface state, place, person, artifact, credential, or result.
- Keep proof inspectable: avoid blur, darkness, tiny crops, overlays, or perspective effects that conceal the claimed evidence.
- State capture time, version, or environment when it changes what the proof means.
- Preserve material differences between source evidence and annotation; an annotation may explain but cannot alter the underlying fact.
- If required proof is absent, label the gap and adjust the claim, composition, or maturity statement.

## Atmosphere/support rules

Atmosphere may establish feeling, material, or a fictional scene. Support may clarify a concept or connect sections. Both must remain subordinate to truthful product proof and to the active Design Contract, including its `DirectionContract` projection.

- Give generated media an explicit atmosphere or support role before generation.
- Label generated or composited nature in working records when authenticity could be inferred.
- Do not let atmosphere redefine the approved palette, silhouette, product object, or cultural source without revising the contract.
- Keep support imagery replaceable; factual copy and interaction must not depend on an invented detail.
- Prefer omission when a support image would be mistaken for official evidence.

## Placeholder rules

A placeholder represents a dependency, not a solved asset. Mark its required subject, aspect ratio, minimum quality, owner, replacement trigger, and fallback.

An informative placeholder must already provide an equivalent textual fallback for the information or action the missing asset would carry. A decorative placeholder must use an empty text alternative and must not add noise to the accessible name or reading order.

Use a visibly neutral frame or honest text state. Do not hide a missing asset behind blur, shadow, gradient, generic stock imagery, or a fabricated screenshot. A placeholder must not impersonate approved, official, generated-final, or user-provided media.

## Media treatment

Record treatment as an implementation contract:

- crop: full object, macro, portrait, landscape, cutaway, device frame, or full bleed
- integration: standalone, masked, embedded, background, texture, or driving the layout
- edge: hard, framed, faded, reflected, shadowed, or bleeding
- contrast and color: natural, muted, monochrome, warm, cool, or high contrast
- relationship: behind, beside, inside, anchored to, or governing nearby UI
- target-device behavior: focal point, art direction per declared viewport, safe crop, and text overlap rule

Transformations must not change the factual meaning of proof. Keep source media recoverable when edits, crops, or annotations are applied.

## Cultural and factual provenance

For culturally specific or factual media, provenance records source, creator or custodian when known, authorization, access date or version, subject identification, allowed use, required attribution, transformations, and uncertainty.

Visual description is not factual proof; alt text, a caption, a transcript, or a model-generated description communicates content but cannot authenticate it. Generated media provenance proves only the output's source, creation, rights, and authorization, not the depicted object, event, identity, history, certification, or claim.

Do not infer a dynasty, region, craft, collection, author, location, species, person, brand, or historical claim from visual resemblance alone. Verify named facts or mark them unresolved. Generated cultural atmosphere must not impersonate a documented artifact or institutional collection.

## Acceptance checks

- Every visible asset has a role from the ledger and a recoverable source record.
- Required proof is authentic, authorized, inspectable, and scoped to the claim.
- Atmosphere and support never masquerade as proof.
- The Asset-before-IA gate runs only when media materially affects composition.
- A media-led experience has a many-to-many asset-system manifest that separates provenance from quality and covers every selected content, proof, transition, state, and failure role without allocating one asset per screen.
- Missing media uses an honest placeholder, a declared generation plan, or omission.
- Crop, integration, edge, target-device behavior, and fallback are implementable.
- Cultural and factual claims have provenance or an explicit uncertainty state.
- Every informative asset has alt text and, when needed, a caption or transcript; every decorative asset uses an empty text alternative; when media is unavailable, an equivalent textual fallback preserves its information or action.
