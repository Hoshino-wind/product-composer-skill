# Image Concepts

## Principle

Use image generation to explore or supply a visual role only after truth, artifact target, and direction are known. This optional Modifier consumes the active `DirectionContract` and does not create a secondary route hierarchy; it owns image-world art direction, asset-family continuity, prompt compilation, candidate selection, and targeted retake without replacing the owning product, brand, or cultural guidance.

Own why the asset should look and behave a certain way; let the image tool own rendering or editing. Prefer one reusable Asset Family Contract plus a compiled prompt and selected composition-family delta. Do not preserve fixed page recipes, named-style presets, or universal cinematic defaults that force unrelated products into the same world.

## Contents

- [Image eligibility](#image-eligibility)
- [Image World Bible](#image-world-bible)
- [Medium Router](#medium-router)
- [Asset Family Contract](#asset-family-contract)
- [Prompt contract](#prompt-contract)
- [Candidate Protocol](#candidate-protocol)
- [Experience-Architecture Output](#experience-architecture-output)
- [Composition families](#composition-families)
- [Visible text](#visible-text)
- [Aesthetic repair](#aesthetic-repair)
- [Anti-convergence](#anti-convergence)
- [Result inspection](#result-inspection)
- [Retake Loop](#retake-loop)
- [Direction-to-asset-pack](#direction-to-asset-pack)
- [Asset handoff](#asset-handoff)
- [Failure signs](#failure-signs)

## Image eligibility

Image generation is an eligibility decision, not a default.

Generate when at least one condition is true:

- the user explicitly asks for an image, visual concept, or image asset
- comparing direction options requires a visual artifact before implementation
- the approved experience needs atmosphere or support media that may be fictional
- a generated product metaphor, illustration, texture, or empty-state asset can be honest about what it is

Do not generate when a supplied reference or local asset already answers the need, when the next useful evidence must be rendered code, or when the image would impersonate missing proof. A real logo, interface state, person, venue, artifact, certification, result, or product photograph remains an asset-truth problem, not a prompting opportunity.

For a physical-product direction with no official media, keep the selected Surface and Image Modifier. When the absence constrains proof or composition, close the current window and hand off to Asset truth even when no file exists; resume from the updated Design Contract before selecting or generating atmosphere.

Name the intended artifact and maturity before generating: exploratory direction, selected concept, support asset, or production candidate. A chat preview alone is not a saved implementation asset.

## Image World Bible

Translate the selected `image-world thesis` into a reusable world before generating a family of assets. Build the full bible when several generated assets must belong together; for one simple texture, cutout, or support image, keep only the applicable fields.

```text
Image World Bible
- visual genre and world premise:
- place, time, era, climate, and atmosphere:
- realism or abstraction level:
- subject, casting, wardrobe, prop, and environment rules:
- camera and depth language:
- lighting logic: source, direction, softness, temperature, contrast, exposure:
- color logic and grading relationship:
- material logic, texture scale, edge behavior, and physical imperfections:
- continuity anchors shared across the family:
- forbidden drift:
```

Start from the active direction, real content, available references, and intended use; do not silently apply a stored style. Describe visible mechanisms rather than an artist, director, studio, or work name. A reference may contribute composition, camera, light, material, or rhythm only through the authorized translation rules in `reference-translation.md`.

Keep UI and image causally related: the same attention strategy, tension pair, palette roles, material behavior, and continuity rule should remain legible in both. Do not force literal sameness. An austere UI may intentionally frame an expressive image when the tension pair names that relationship and the image does not compete with controls or proof.

## Medium Router

Choose a medium because its controllable variables fit the role. Do not send every visual need to one generic prompt:

| Medium | Direct explicitly | Do not delegate or fake |
| --- | --- | --- |
| photography | subject relationship, casting, action, environment, shot distance, viewpoint, lens behavior, depth, practical light, exposure, and believable imperfections | official people, places, products, or results without authentic source material |
| illustration | shape language, abstraction, line or edge behavior, mark, texture, palette, perspective, and detail hierarchy | a living artist's name as a shortcut for the visual system |
| 3D or rendered object | geometry, scale reference, material response, edge wear, camera, light rig, grounding, reflection, and render realism | fake product truth, impossible material behavior, or decorative CG with no role |
| texture or material field | physical scale, repeat or seam policy, directional grain, surface response, tonal range, and crop tolerance | a focal subject or narrative scene when the role is only a reusable field |
| transparent cutout | contour, source identity, viewpoint, edge quality, transparency, contact shadow, and target-background compatibility | complex transparency or reverse views that the available source cannot support |
| UI or architecture concept | hierarchy, region geometry, states, proof placement, exact-text boundary, media relationship, and target-device scope | production UI, correct runtime behavior, or factual screenshots inferred from a concept image |
| sequence or storyboard | stable identity and world anchors, from-state, event, to-state, camera relationship, and handoff frame | multiple incompatible events compressed into one frame or continuity inferred from prose alone |

Prefer deterministic HTML, CSS, SVG, canvas, or component code for exact UI, charts, icons, logos, diagrams, and typography when those are the required deliverables. Use generation for exploration, authored raster media, atmosphere, texture, illustration, or another eligible role; composite exact text, data, logos, and controls deterministically for publish-bound work.

## Asset Family Contract

Create one contract for each independent asset role. Related variants share an asset-family identity and lineage; unrelated roles receive separate contracts rather than one prompt with many jobs.

```json
{
  "direction": {
    "thesis": "...",
    "aestheticStance": ["...", "...", "..."],
    "tensionPair": "... versus ...; ... dominates",
    "visualGenre": "...",
    "attentionStrategy": "...",
    "dominantSilhouette": "...",
    "compositionFamily": "...",
    "world": "...",
    "camera": "...",
    "light": "...",
    "material": "...",
    "color": "..."
  },
  "asset": {
    "familyId": "...",
    "id": "...",
    "promptContractVersion": "1.0",
    "parentId": "...",
    "stateId": "...",
    "transition": {
      "fromState": "...",
      "event": "...",
      "toState": "...",
      "handoffFrame": "..."
    },
    "role": "...",
    "maturity": "...",
    "truthBoundary": "...",
    "medium": "...",
    "intendedUse": "...",
    "targetRegion": "...",
    "aspectRatio": "...",
    "focalPoint": "...",
    "composition": "...",
    "depthOrder": "...",
    "cropBehavior": "...",
    "safeArea": "...",
    "variants": [{
      "id": "desktop-wide",
      "targetRegion": "...",
      "aspectRatio": "...",
      "focalPoint": "...",
      "composition": "...",
      "depthOrder": "...",
      "cropBehavior": "...",
      "safeArea": "..."
    }],
    "subject": "...",
    "scene": "...",
    "action": "...",
    "fixedAnchors": ["..."],
    "explorationAxis": {
      "variable": "shot-distance",
      "name": "镜头距离",
      "allowedValues": ["...", "..."]
    },
    "referenceRoles": [{"reference": "Image 1", "role": "identity anchor"}],
    "constraints": ["..."],
    "avoid": ["..."]
  },
  "candidateSettings": {
    "mode": "asset-exploration",
    "count": 4,
    "selectionCriteria": ["..."],
    "model": "...",
    "version": "...",
    "settings": {}
  }
}
```

Use one stable `familyId` across related assets and a unique `id` for each output. Record `parentId` only for a derivative or edit. Add `stateId` and `transition` only when the asset represents a state change; `transition.toState` must equal `stateId`, and the handoff frame must be usable by the next asset or medium. Keep a versioned prompt lineage instead of overwriting the contract that produced an accepted candidate.

Treat `fixedAnchors` as invariants: truth boundary, subject identity, product contour, world, palette role, material behavior, target geometry, or another selected rule must not drift. Declare exactly one structured `explorationAxis` per batch. Its stable `variable` must be one supported causal variable such as `focal-scale`, `crop`, `viewpoint`, `shot-distance`, `light-direction`, `environment-density`, `abstraction-level`, `texture-scale`, `material-response`, `subject-pose`, or `action-phase`; keep the localized `name` and optional allowed values beside it. Do not combine several repair requests into the same delta.

Use `variants` when target device, region, aspect ratio, focal point, crop behavior, or safe area materially changes; do not hide several target geometries in one prose field. Omit `parentId`, `stateId`, `transition`, `variants`, `subject`, `scene`, or `action` only when they are genuinely inapplicable. The compiler contract otherwise remains complete; write `not applicable` rather than silently dropping a required art-direction field.

For identity-critical families, create and approve the simplest useful master first, then derive angles, states, crops, or scenes from that reference. A character may need a neutral master and views; a product may need an authorized object master; a scene-led website may need a master environment. Do not force character grids, dense asset graphs, or master imagery onto a simple one-off role.

Keep truth role, semantic role, provenance, and rights in the shared Design Contract and `asset-context.md`; the Asset Family Contract controls creative production, not authentication.

## Prompt contract

Compile the Asset Family Contract into this ordered prompt logic:

1. family and asset identity, prompt-contract version, applicable parent/state lineage, role, intended use, maturity, and truth boundary
2. visual thesis, attention strategy, tension pair, and visual genre
3. image world, applicable transition, and the applicable subject, scene, action, or material field
4. primary target region plus any structured device or target-region variants: aspect ratio, focal point, composition, depth order, crop behavior, and safe area
5. medium-specific camera, light, material, texture, palette, and finish logic
6. fixed anchors and the declared role of every input reference
7. exactly one exploration axis for the current batch
8. constraints and a short avoid list tied to real failure risks
9. candidate count, selection criteria, model, version, and settings as generation metadata

For a saved or production-candidate contract, run the deterministic compiler:

```bash
python3 scripts/compile-image-prompt.py /absolute/path/asset-contract.json --format text
```

Use `--format json` when the execution adapter or evidence record needs ordered sections and candidate metadata. Preserve the user's language. The compiler rejects a bounded set of recognizable quality-praise shortcuts and validates structural continuity, variants, and the single exploration variable; named people or studios and unsupported narrative claims still require human or owner review because string matching cannot establish their meaning reliably. Do not add a named artist or studio, an unsupported narrative object, or a silent style fallback. Keep model-specific settings outside the creative thesis so another execution adapter can consume the same contract.

Resolve composition hierarchy, focal scale, safe area, depth intent, camera logic, light logic, material behavior, and color relationship before generation. Let the model vary local texture and rendering detail only inside those decisions; do not outsource the art direction to a vague request for something `cinematic`, `premium`, or `beautiful`. Do not micromanage a UI concept into a box-by-box pixel diagram.

When the execution path supports image editing, use three purposeful passes only when they reduce risk:

- `framework`: establish subject, silhouette, composition, depth, crop, and base color relationship
- `material`: preserve the framework while resolving material, object detail, light source, and surface response
- `polish`: preserve structure and identity while refining atmosphere, texture, grading, and artifact defects

Use one full prompt when the role is simple or the tool cannot preserve a prior pass. Do not repeat a pass merely to chase random novelty.

Domain-specific constraints remain with their owners. For Chinese-aesthetic work, `chinese-aesthetic.md` supplies the Modifier delta; do not restate its domain grammar here. Apply the delta after the base contract and record any field it intentionally changes.

## Candidate Protocol

Treat generation as proposing evidence for selection, not as producing one presumed answer.

- `direction exploration`: compare `2–3` orthogonal directions with the smallest real image set that reveals each spatial and world thesis.
- `asset exploration`: keep one direction and its fixed anchors; normally create `3–4` candidates that vary only the named exploration axis.
- `production candidate`: use the selected master or reference roles, target geometry, and acceptance criteria; create only the alternatives needed to judge craft and integration.
- `edit repair`: use the selected image as the parent, repeat every invariant, and change only the diagnosed prompt delta or localized region.

Infer count from ambiguity, cost, identity risk, and the consequence of a wrong choice. Do not import a universal `16–30` image board, a mandatory character grid, or a dense asset graph into every UI task. Generate a master first only when identity or world continuity makes derivatives unsafe without it.

Name every output with asset id, family or direction id, prompt-contract version, candidate index, parent id when edited, pass, model/version when known, and creation time. Preserve rejected candidates long enough to explain selection, then keep them out of implementation unless the user reopens the choice.

Compare candidates in one review surface at full view, thumbnail scale, and the target crop. Automated ranking or VLM critique may identify defects and recommend an order, but the user or responsible design judgment selects, rejects, promotes maturity, or authorizes another batch.

## Experience-Architecture Output

Match the generated artifact to the selected architecture:

- `opener or hero`: one concept may specify an opening state, but a multi-state opener needs the key states, region geometry, transition relationship, target-device treatment, and fallback.
- `route or page experience`: create an architecture board or storyboard containing the ordered content beats, varied region geometries, ordinary-flow and immersive passages, state changes, handoffs, and proof/action/orientation placement.
- `multi-route website`: add the route map, shared navigation, representative detail/product/collection pages, and cross-route states needed to prove a complete website rather than one landing route.

Do not use one attractive image to stand in for a complete website experience. Do not let the model invent later regions from a generic landing-page recipe or render every beat as an equal full-screen poster. Establish the content/region model first, then generate one coherent architecture board per direction or the independent media required by that architecture.

Keep global signature-system fields stable while allowing each region to change height, composition family, focal scale, proof object, media set, interaction mechanism, and density for its content. Inspect the board at route, region, state-pair, and thumbnail-strip scales. Reject repeated hero posters with changed copy or crops, or a board that cannot distinguish intrinsic content flow from pinned, horizontal, or spatial behavior.

## Composition families

Select one family because it best exposes the user job or proof. The delta changes spatial relationships; it is not a decorative label.

- spatial axis enum: focal-position, scale, overlap-depth, crop-frame, reading-axis, negative-space

`focal-position` moves the primary anchor; `scale` changes relative dominance; `overlap-depth` changes foreground/middle/background relationships; `crop-frame` changes the aperture or boundary; `reading-axis` changes the scan path; `negative-space` changes where silence protects the proof.

| Composition family | Use when | Spatial axes changed | Prompt delta | Avoid |
| --- | --- | --- | --- | --- |
| object portrait | one product, artifact, result, or crafted object carries the claim | focal-position, scale, negative-space | stage one dominant object with quiet supporting evidence and a memorable contour | equal feature cards orbiting a generic object |
| editorial spread | authority, narrative, portfolio proof, or comparison needs art-directed reading order | focal-position, reading-axis, negative-space | use asymmetric type, one evidence field, and deliberate continuation beyond the viewport | a conventional marketing shell disguised by serif type |
| instrument viewport | spatial inspection, simulation, calibration, or direct control is legitimate | overlap-depth, crop-frame, scale | attach sparse state, readings, and controls to the inspected object's geometry | cockpit chrome and unrelated floating panels |
| split comparison | a consequential judgment depends on two states or alternatives | focal-position, reading-axis, scale | give both sides a shared scale and put the decision boundary where differences can be inspected | decorative before/after theater with unequal evidence |
| atlas or matrix | relationships, coverage, location, or many comparable values drive the task | reading-axis, scale, negative-space | establish a stable field, semantic axes, and one inspectable focus path | a dashboard collage of unrelated widgets |
| sequence | causality, time, approval, or transformation is the proof | reading-axis, overlap-depth, negative-space | make state transitions and commitment gates legible while preserving one dominant path | a flowchart in which every node has equal weight |

Do not default to left-copy/right-object. Do not default to any family across unrelated briefs. If two concepts are requested, vary dominant silhouette, control placement, proof object, material behavior, and density rhythm before varying color.

## Visible text

List exact visible text rather than asking the model to invent copy. Keep it short enough to render legibly and include only phrases required to identify the product, establish hierarchy, show one meaningful state, or make the action credible.

Separate:

- must render exactly: product name, headline, primary action, critical state
- may be abstracted: non-factual microcopy whose geometry matters more than wording
- must not invent: metrics, testimonials, customers, certifications, claims, historical labels, URLs, or interface states

Reject an image whose factual or action-critical text is wrong even if the composition is attractive. Treat unreadable incidental glyphs as a concept limitation, not finished product copy.

## Aesthetic repair

When a result is correct but generic, run an aesthetic repair rather than adding more negative adjectives. Re-read the already selected fields; do not invent visual genre or tension for the first time after generation:

- style family: the behavioral visual family supported by evidence
- visual genre: the specific world the artifact should plausibly belong to
- dominant silhouette: the contour that survives at thumbnail size
- material language: how surface, depth, edge, and light behave
- attention strategy: the intended focal order, silence, and relationship to the consuming UI
- image-world thesis: the shared camera, light, material, color, and continuity logic
- typography mood: the role contrast and voice, not a named font imitation
- tension pair: two controlled forces that keep the direction alive
- fixed anchors and exploration axis: what must survive and what this batch may change
- deletion rule: what disappears first when the composition becomes busy

Repair the lowest weak relationship first. If the object is forgettable, change silhouette or family; if hierarchy is flat, change proportion and silence; if the world feels cheap, resolve type, material, palette roles, and edge craft without changing the thesis.

## Anti-convergence

Compare each candidate with accepted concepts across dominant silhouette, spatial grammar, control placement, proof object, material behavior, accent roles, and density rhythm. Reject a supposed alternative that changes only copy, color, corner radius, or background mood.

When convergence appears, preserve at most one continuity trait and change at least four structural variables. Choose an opposing composition family before adding novelty. Do not repeatedly retreat to warm cards, a centered rail, a detached action panel, status chips, a lens motif, or a generic floating object.

## Result inspection

Inspect the actual image at full view, thumbnail size, and inside its target region and crop variants:

- Does the asset perform its declared role and intended use without impersonating proof?
- Is the first focal point the intended subject, relationship, or product proof rather than decoration?
- Does the dominant silhouette match the `DirectionContract`?
- Does the selected composition family reveal the intended relationship?
- Do safe area, focal point, crop tolerance, edge behavior, and target-background integration work?
- Does the result obey the Image World Bible and remain coherent with sibling assets?
- Are camera, light, material, color, depth, and physical relationships plausible for the selected medium?
- Are factual objects and exact text accurate enough for the artifact maturity?
- Did fixed anchors survive, and did only the named exploration axis materially change?
- Are hierarchy, specificity, tension, craft, and silence resolved without quality-word polish?
- Is this structurally distinct from prior accepted directions?

Accept, repair, regenerate, or reject with a concrete reason. Do not call a result production-ready based only on prompt quality.

## Retake Loop

Use a bounded critique-to-retake loop after candidates exist:

```text
Image review record
- asset id, role, maturity, and target context:
- baseline candidate and evidence locator:
- blocking defect:
- scores with evidence: role fit | attention | form/proportion | specificity | world coherence | medium craft | continuity | integration
- lowest weak relationship:
- fixed anchors preserved:
- one prompt delta or localized edit:
- new candidate ids and comparison:
- selected result and reason:
- budget, convergence, and stop decision:
```

Treat wrong identity, invented proof, prohibited text or claim, broken target crop, missing required transparency, forbidden drift, or a contradiction of locked direction as blocking defects; do not average them away with polish scores. Score other dimensions from `1–5` and cite visible evidence. A high average cannot hide role failure, unusable integration, or broken continuity.

Select the lowest credible weak relationship and modify only its causal prompt section: composition, camera, light, material, color, world density, abstraction, or another named axis. Repeat all fixed anchors and reference roles. Generate the smallest useful comparison batch, review against the same baseline and target context, then keep, revert, or continue.

Stop when the selected candidate meets its acceptance criteria, the budget is exhausted, two iterations fail to improve the diagnosed dimension, or the remaining difference requires a new direction, authentic source, different medium, or user decision. Automated critique remains advisory and never approves, mounts, or promotes an asset by itself.

## Direction-to-asset-pack

An exploratory opener preview proves one local direction decision; it is not an implementation asset pack or a complete website specification. After an architecture board is selected, inspect it and extract only the media required to preserve its visual mechanisms, content beats, region handoffs, and state progressions.

Possible outputs include persistent scenes, materially different supporting views, transparent foreground or object cutouts, material/texture fields, art-typography treatments, transition plates, video or recording storyboards, poster frames, product UI captures, image sequences, spatial models, and target-device variants. Generate only roles visible in or logically required by the selected concept. Do not manufacture a checklist of assets for every project or allocate one source per region.

```text
Selected-direction asset plan
- selected concept and locked visual mechanism:
- website scope, content beats, regions, and continuity handoff:
- independent asset role:
- relationship to other media and reuse across regions:
- state served: rest | invitation | response | transition | interrupted | reduced-motion
- exact crop, transparency, or loop need:
- semantic and truth role:
- target-device, poster, and static fallback:
- acceptance evidence:
```

Generate and inspect each independent role as its own candidate. A single attractive image cropped five ways is still one source, not five assets. Do not reuse a rejected or unrelated local image merely because it already exists. If the selected direction depends on authentic proof that cannot be generated, preserve the concept as atmosphere/support, record the missing-proof gap, and adapt the claim or stop.

## Asset handoff

For every selected output, record generation source, model or tool when available, creation date, prompt-contract version, selected composition family, declared truth role, semantic role, file path or access gap, dimensions, placement, allowed edits, provenance label, and fallback.

For an informative output, hand off alt text that communicates purpose and a caption or transcript when complex, sequential, or time-based information needs more than concise alt text. For a decorative output, require an empty text alternative and exclude it from the accessible reading order. If the visual asset cannot be provided or perceived, supply an equivalent textual fallback that preserves the same information or action; a visual description does not turn generated content into factual proof.

Pass saved assets and their role records to `asset-context.md`. If the result exists only in conversation, say so and do not substitute an older local file. A selected concept may guide implementation without becoming factual proof.

## Failure signs

- Generation was automatic although no visual role or decision required it.
- A style label, artist or studio name, or quality praise replaced an Image World Bible and visible art-direction decisions.
- Several assets were generated independently with no family anchors, forbidden drift, or shared camera, light, material, and color logic.
- The first attractive output was accepted without a comparable candidate set or target-context review.
- A retake changed several causal variables at once, so improvement or regression could not be attributed.
- A fixed arrangement overrode the chosen composition family.
- The output looks like a diagram, feature grid, dashboard collage, or generic marketing shell.
- Product proof is decorative, hidden, invented, or less prominent than atmosphere.
- Exact text is wrong, unreadable, or replaced by fabricated factual claims.
- The direction repeats a prior silhouette, action placement, proof object, and material system.
- A domain-specific system was copied into the base prompt instead of loaded as its Modifier delta.
- The saved asset, role, provenance, dimensions, placement, or fallback is missing.
- The isolated asset looks polished but its focal point, crop, safe area, edge, contrast, or world conflicts with the consuming UI.
- Generated text, logo, chart, icon, or UI was treated as deterministic publish-bound output without reconstruction and verification.
- A selected opener preview was treated as a complete asset pack, or one source was disguised as variety through derivative crops and effects.
- A single hero poster was treated as a complete route or website direction.
- Later regions were invented from a generic section template instead of the content/region model and many-to-many media map.
