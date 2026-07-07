# Image Generation Aesthetic Calibration

Use this when the user asks to directly generate, draw, or preview UI as an image without code, especially after hand-built or SVG mockups feel stiff.

## Principle

For pure visual UI exploration, let image generation carry aesthetic completion. The agent should provide style family, taste constraints, product intent, interaction relationship, palette, and anti-patterns, not manually assemble a deterministic diagram unless asked.

## What Worked

The stronger image-generated direction worked because it felt like a product website visual, not a method diagram:

- one memorable first viewport
- editorial headline plus one short support line
- one dominant product object
- expressive but controlled color
- interaction framed as relationship: user intent -> system judgment -> desirable preview
- preview/result layer as the most attractive part
- minimal exact text
- no fake drag, swipe, cursor, or gesture labels
- no lifestyle photo, quote, metric-card collage, or dashboard proof pile

## Aesthetic Repair Pass

Use this after the user rejects a generated UI as ugly, generic, template-like, or lacking taste. Do not retry by only adding more negative prompts. The failure is usually missing art direction, not missing constraints.

Before regenerating, define style family plus these six choices:

- Style family: Utility Product, Editorial Premium, Cultural Immersive, Technical Instrument, Data Dense, Playful Consumer, Soft Craft, or Bold Campaign.
- Visual genre: editorial product page, luxury software instrument, crafted portfolio, spatial OS surface, museum label system, precision hardware interface, or another specific visual world.
- Dominant silhouette: one clear outline the viewer remembers, such as a folded sheet, monolithic console, suspended canvas, quiet stage, product portrait, or asymmetric editorial spread.
- Material language: paper, ink, ceramic, brushed metal, translucent film, textile softness, luminous UI layer, or calm native software.
- Typography mood: literary, technical, institutional, fashion editorial, product-system, or quiet utility.
- Tension pair: two forces that make the image alive, such as warm paper vs cold instrument, craft vs automation, restraint vs charged accent, softness vs precision.
- Deletion rule: what must disappear first if the design becomes busy.

If these choices are vague, do not generate yet. Tighten the art direction first.

## Stronger Prompt Biases

Use these biases when a homepage still looks like a SaaS template:

- Ask for art-directed composition, not a conventional website screenshot.
- Replace "right-side product object" with a more specific visual object: folded editorial sheet, suspended interface plate, premium control surface, product portrait, or quiet stage.
- Reduce conceptual labels. `Intent`, `Judgment`, and `Preview` should appear only if they look like real product language, not diagram labels.
- Prefer one beautiful product artifact over explanatory layers.
- Ask for a screen that would pass as a launch image from a high-taste design studio, while avoiding named-brand imitation.
- Make the product result emotionally desirable before making the mechanism explicit.
- Make the image work as a poster-quality thumbnail before adding UI detail.

## Aesthetic Failure Notes

Treat these as hard warnings:

- "Elegant", "premium", and "minimal" are too weak without a visual genre and material language.
- A product page can still be ugly when it follows all structural rules.
- Concept labels can make a composition feel like a workshop diagram.
- Repeated left-copy/right-mockup layouts often look correct but dead.
- A beautiful UI image needs proportion, typography, material, color tension, and silence. Feature meaning alone is not enough.
- A utility screen can be functionally correct and still look like a disposable admin template.
- A technical screen can be structurally correct and still look cheap if it becomes a black cockpit, command center, fake terminal, or sci-fi dashboard.
- Product names and section labels are part of taste. Generic Chinese names such as `运行舱`, `指挥舱`, `智控舱`, `超脑`, or `中枢` often push normal software into low-grade industrial fantasy.

## Utility And Technical Repair

Use this when A Utility Product or D Technical Instrument produces an ugly image.

Do not fix it by adding more panels, more glow, or more "technical" detail. The failure is usually caused by generic category signals replacing a real product world.

For A Utility Product:

- Replace the default admin shell with one product-specific workflow object: review queue, approval lane, claim desk, proof board, case timeline, or workbench.
- Use a warmer or more editorial base when the screen feels sterile: porcelain, warm gray, ink, muted green, amber, or clay accents.
- Reduce equal cards. Let navigation, list, detail, and action form one composed work surface.
- Keep operational clarity, but make one object memorable enough to survive the thumbnail test.

For D Technical Instrument:

- Replace cockpit/control-room metaphors with a precision review surface: preview rail, audit lens, execution ledger, approval dial, safety timeline, or simulation sheet.
- When the product has a physical, industrial, scientific, medical, robotics, IoT, or monitoring aspect, make a 3D instrument/digital-twin viewport the primary object.
- Use sensor overlays, calibration rings, exploded/cutaway geometry, perspective viewport controls, status layers, and direct controls attached to the object.
- Avoid black drama unless the product truly requires dark mode. Prefer `warm precision`: graphite + ivory, muted cyan + brass, deep green + porcelain, or paper + technical ink.
- Remove terminal cosplay, fake code, blue glow, neon particles, sci-fi panels, and militarized labels.
- Rename before regenerating if copy is causing the mood problem. Prefer job-based language such as `执行预演`, `风险复核`, `审计轨迹`, `确认执行`, `回滚记录`.

Repair prompt fragment:

```text
Aesthetic repair: the previous direction looked like a generic admin/technical template. Rebuild around one specific product object, not a control room. Use warm precision, strong proportion, sparse labels, and a tasteful Chinese product name. Avoid cockpit, command center, terminal, black-blue sci-fi dashboard, generic left navigation, equal cards, and labels such as 运行舱 or 指挥舱.
```

## Anti-Convergence Repair

Use this when the user says the new result is returning to the same style, same elements, or same design mode as previous images.

Do not keep the same safe repair formula. In particular, reject the common fallback of:

```text
warm ivory background + thin rounded cards + central rail/timeline/proof object + right action panel + green/red chips
```

That formula can be tasteful once, but it becomes a template when repeated across families.

Before regenerating, force a different spatial grammar:

- Replace horizontal rails with radial maps, stacked ledgers, split comparison, field grids, compact lane systems, or object portraits.
- Replace right action panels with embedded actions, bottom action strips, inline approvals, corner instruments, or direct state controls.
- Replace paper-and-card material with ceramic, textile, dense native software, matte metal, map layers, monochrome print, or product-specific surfaces.
- Replace magnifier/lens inspection motifs if another output already used them.
- Keep only one continuity trait from the prior output; change at least five major traits.

Prompt fragment:

```text
Anti-convergence repair: do not reuse the prior warm-card/central-rail/right-panel structure. Make this direction visually orthogonal to the previous accepted images. Change the dominant silhouette, spatial grammar, material language, action placement, and proof object. It should not look like a variant of the earlier A, D, or G images.
```

## SaaS Ant Design Anchor

Use this when generating SaaS, admin, CRM, forms, settings, tables, approval, or enterprise workflow UI.

The goal is Ant Design product order, not an Ant Design skin. Do not turn it into a generic blue-white admin demo.

Required qualities:

- Natural: task sequence and layout follow how enterprise users think and act.
- Certain: reusable component-like rules, predictable spacing, explicit states, stable navigation.
- Meaningful: visible objects, statuses, filters, actions, and details support the user's work mission.
- Growing: first view stays clear while expert capability appears through saved views, bulk actions, drawers, column control, and drill-downs.

Prompt fragment:

```text
SaaS product order inspired by Ant Design values: natural task flow, high certainty, meaningful work objects, progressive capability. Use stable navigation, explicit filters/status, contextual actions, real enterprise objects, table/form/drawer discipline, and dense-with-air layout. It should feel like a serious product work surface, not a marketing page, decorative dashboard, or default admin template.
```

## Theme Marketplace Anchor

Use this when generating an official website, WordPress-style homepage, business site, venue page, service page, product content page, agency site, eCommerce page, or commercial landing page that should feel market-ready.

The goal is ThemeForest/WordPress-market maturity, not copying a marketplace template.

Required qualities:

- Clear industry/category fit in the first viewport.
- A finished-site or offer preview that proves what the visitor gets.
- Modular section rhythm with enough below-the-fold signals to feel complete.
- Trust markers such as demos, ratings-style proof, customer logos, results, integrations, locations, inventory, or case snippets.
- Specific visual language from the business category, not generic SaaS polish.
- Direct commercial path: preview, book, buy, contact, compare, or start.

Prompt fragment:

```text
Commercial WordPress-theme maturity inspired by ThemeForest: clear category fit, polished first viewport, realistic offer/site preview, modular section rhythm, early trust proof, and a direct conversion path. Use industry-specific imagery, typography, palette, and section sequencing. Avoid copied marketplace templates, generic multipurpose demo grids, decorative hero visuals, and vague SaaS layout.
```

## 3D Instrument UI Anchor

Use this when D Technical Instrument should feel like a real instrument UI.

The dominant proof object should be a 3D instrument, digital twin, cutaway device, machine module, lab device, sensor rig, robot, medical/scientific apparatus, or other inspectable product object. UI overlays should attach to the object's geometry instead of floating as unrelated cards.

Required qualities:

- A primary 3D viewport or isometric device object.
- Sensor/status overlays anchored to real parts of the object.
- Calibration, threshold, safety, state, or diagnostic controls near the affected region.
- A clear foreground/middle/background depth relationship.
- A restrained technical palette with one or two semantic accents.
- Evidence that the 3D object is useful for inspection, not decorative product art.

Prompt fragment:

```text
Technical instrument UI with a 3D digital-twin object as the main surface. Show an isometric/cutaway instrument in a product viewport, with sensor overlays, calibration rings, diagnostic callouts, state layers, and controls attached to the object's geometry. Avoid flat dashboard cards, generic command centers, terminal screens, sci-fi cockpit styling, and decorative 3D art unrelated to the task.
```

## Prompt Shape

Use this compact structure:

```text
Create a polished high-end UI mockup for <product>. 16:10 landscape, no browser chrome, no code.

Desired feeling: <3-5 words>.
Psychology: create <curiosity/mastery/relief/desire>.
Interaction model: <relationship>, not a physical gesture.
Style family: <selected family and why>.
Art direction: <visual genre>, <dominant silhouette>, <material language>, <typography mood>, <tension pair>.

Layout: one memorable first viewport. Left has headline, support copy, one CTA. Right/center has one dominant product object with <few conceptual layers>. The preview/result layer must be the most desirable part.

Palette: <small expressive palette>. Colorful but controlled, not black-and-white minimalism.

Exact visible text:
<short text list>

Avoid: <known failures>.
```


## Prompt Templates

Use these as starting points. Replace bracketed parts, keep exact visible text short, and keep the avoid list strong.

### Elegant Product Homepage

```text
Create a polished high-end UI mockup for [product name]. 16:10 landscape, no browser chrome, no code.

Desired feeling: elegant, magnetic, intelligent, alive.
Psychology: create curiosity, mastery, relief, and product desire.
Interaction model: [relationship model], not a physical gesture.
Art direction: [visual genre], [dominant silhouette], [material language], [typography mood], [tension pair]. The image should feel art-directed, not assembled from SaaS sections.

Layout: one memorable first viewport. Left side has an editorial headline, one supporting sentence, and one CTA. Right/center has one dominant product object that feels like a real product surface, not a diagram. The product object has three calm conceptual layers: Intent, Judgment, Preview. The Preview/result layer must be the most desirable part.

Palette: [small expressive palette]. Colorful but controlled, not black-and-white minimalism.
Typography: refined modern serif headline, clean sans-serif UI text, strong hierarchy, normal letter spacing.

Exact visible text:
[product name]
[2-3 nav labels]
[headline]
[supporting sentence]
[CTA]
Intent
Judgment
Preview
[one concise judgment/proof line]

Avoid: drag/swipe/click labels, cursor hand, fake gesture affordance, before/after split line, lifestyle photo, famous quote, testimonial, metric-card collage, generic dashboard, feature grid, flowchart, node graph, arrows as main aesthetic, purple-blue gradient, glassmorphism, decorative orbs, stock imagery, mascot, dense panels, tiny unreadable text.
```

### Aesthetic Repair Homepage

Use after an otherwise correct homepage is rejected as ugly.

```text
Create an art-directed high-end homepage UI image for [product name]. 16:10 landscape, no browser chrome, no code. This should look like a polished launch image from a high-taste product design studio, without imitating any named brand.

Desired feeling: [three words].
Psychology: create [one primary desire job] through [one desire mechanism].
Interaction model: [relationship model]. Express the relationship through composition, product result, state, and hierarchy, not through labels or controls.

Art direction:
Visual genre: [specific genre].
Dominant silhouette: [one memorable silhouette].
Material language: [specific material].
Typography mood: [specific typography mood].
Tension pair: [force A] vs [force B].
Deletion rule: remove anything that makes the page feel like SaaS, dashboard, documentation, or a diagram.

Composition: design the silhouette first. Use one large quiet field, one memorable product artifact, and one editorial text block. The product artifact should be beautiful before it is explanatory. Keep secondary UI almost silent. The image must read well as a poster-quality thumbnail.

Palette: [small expressive palette with base, text, emotional accent, action accent]. Use accents rarely.

Exact visible text:
[product name]
[headline]
[one support line]
[one CTA]
[optional one product-state phrase]

Avoid: conventional left-copy/right-screenshot SaaS template, many cards, feature grid, dashboard, flowchart, node graph, gesture labels, sliders, knobs, fake controls, lifestyle photo, stock imagery, decorative orbs, glassmorphism, purple-blue gradient, black-and-white-only minimalism, tiny unreadable text.
```

### Product Content Page

```text
Create a high-end product content page UI mockup for [product name]. 16:10 landscape, no browser chrome, no code.

Purpose: make viewers understand the product mechanism and want to keep exploring.
Desired feeling: precise, desirable, calm, premium.
Psychology: curiosity plus confidence. The page should create a sense that the product knows what to keep, remove, and intensify.
Interaction model: user intent -> system judgment -> desirable product result. This is a cognitive relationship, not a drag/swipe gesture.
Art direction: [visual genre], [dominant silhouette], [material language], [typography mood], [tension pair]. The image should feel like a carefully art-directed product editorial, not a documentation page.

Composition: editorial product page with one dominant product proof object. First viewport is sparse: one headline, one support line, one action, one beautiful proof object. Show only a small hint of the next section.

Product object: a refined judgment surface with Intent, Judgment, and Preview layers. The Preview layer shows a coherent, beautiful interface result. It must not be a collage.

Palette: [expressive palette], with one rare accent used for desire or commitment.
Exact visible text:
[list no more than 10 short phrases]

Avoid: method diagram, workflow chart, dashboard collage, lifestyle photo, quote card, metric-card proof pile, feature grid, drag/swipe/click labels, black-and-white default minimalism, saturated generic gradient, tiny text.
```

### Frontier AI Product Surface

```text
Create a polished UI concept image for [AI product]. 16:10 landscape, no browser chrome, no code.

Desired feeling: frontier, calm, controllable, desirable.
Interaction model: [user role] and [system role]. Show intent, agency, uncertainty, and preview-before-commit as a relationship, not as a flowchart or gesture.
Art direction: [visual genre], [dominant silhouette], [material language], [typography mood], [tension pair]. The image should feel like a new product instrument with taste, not a science-fiction dashboard.

Dominant visual object: one living product object that carries state and agency. It should feel inspectable and useful, not decorative.

Composition: large quiet areas, one iconic product object, sparse labels, visible state through form/color/position, no dense panels. Let the image model resolve final proportion and polish.

Palette: [controlled expressive palette]. Use color for agency, risk, selection, or desire.
Visible text:
[short exact text]

Avoid: node graph, exploded requirements diagram, chat-plus-side-panel default, dashboard chrome, drag/swipe/click labels, particles, glassmorphism, purple-blue gradient, decorative orbs, tiny labels.
```

## Palette Recipes

Use one recipe per generation unless the user provides brand colors:

- Lavender product: mist lavender, porcelain, warm peach, deep plum ink, soft sage, muted coral, one acid-lime spark.
- Editorial warmth: linen, clay, pale peach, plum ink, oxblood accent, muted sage structure.
- Fresh craft: soft pistachio, warm cream, ink green, muted coral, brass/amber detail.
- Quiet premium: powder blue, porcelain, deep navy, warm amber, soft gray-violet.
- Focused frontier: deep forest, ivory, muted cyan, brass, soft charcoal.

## Reusable Avoid List

Use this avoid list for most elegant UI image prompts:

```text
Avoid: drag to compose, drag label, slider, swipe, cursor hand, fake gesture affordance, before/after split line as main idea, lifestyle photo, famous quote, testimonial card, metric-card collage, generic dashboard, feature grid, three benefit cards, flowchart, node graph, arrows as the main aesthetic, purple-blue gradient, glassmorphism, decorative orbs, stock imagery, mascot, dense panels, tiny unreadable text, black-and-white-only minimalism.
```

## Generation Rules

- Ask for `design-board quality`, `high-end product website aesthetic`, and `not a wireframe`.
- Select or ask for style family before choosing a prompt template.
- Specify the relationship model, not a gesture control.
- Use `Intent`, `Judgment`, `Preview`, or equivalent conceptual layers only when they support the product story.
- Let the image model choose final proportion, depth, and atmospheric polish.
- Avoid prompt micromanagement that turns the output into a flowchart or static SVG.
- Keep output critique honest: if a generated preview is visible in chat but not saved to disk, report that instead of reusing an old file.

## Failure Signs

Reject or regenerate when the image:

- looks like a method diagram rather than a product page
- uses drag/swipe/click labels without a real interactive demo
- relies on before/after split lines as the main idea
- fills the result with photos, quotes, metric cards, or random widgets
- turns into a dashboard, feature grid, node graph, or flowchart
- uses black-and-white minimalism by default when the brief asks for desire
- has tiny unreadable text or too many equally loud zones
- looks like a default enterprise admin shell with no memorable product object
- looks like a dark control room, sci-fi cockpit, terminal skin, or militarized operations screen
- relies on cheap product naming or hard technical labels that make the interface feel less desirable
- shares the same warm-card, central-object, right-panel, thin-border language with another accepted style direction
- feels like a variant of a previous output after only changing the product name and labels
