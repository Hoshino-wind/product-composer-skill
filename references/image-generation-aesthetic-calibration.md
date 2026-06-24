# Image Generation Aesthetic Calibration

Use this when the user asks to directly generate, draw, or preview UI as an image without code, especially after hand-built or SVG mockups feel stiff.

## Principle

For pure visual UI exploration, let image generation carry aesthetic completion. The agent should provide taste constraints, product intent, interaction relationship, palette, and anti-patterns, not manually assemble a deterministic diagram unless asked.

## What Worked

The stronger image-generated direction worked because it felt like a product website visual, not a method diagram:

- one memorable first viewport
- editorial headline plus one short support line
- one dominant product object
- expressive but controlled color
- interaction framed as relationship: user intent -> system judgment -> desirable preview
- preview/result layer as the most attractive part
- minimal exact text
- no fake drag, slide, cursor, or gesture labels
- no lifestyle photo, quote, metric-card collage, or dashboard proof pile

## Aesthetic Repair Pass

Use this after the user rejects a generated UI as ugly, generic, template-like, or lacking taste. Do not retry by only adding more negative prompts. The failure is usually missing art direction, not missing constraints.

Before regenerating, define these six choices:

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

## Prompt Shape

Use this compact structure:

```text
Create a polished high-end UI mockup for <product>. 16:10 landscape, no browser chrome, no code.

Desired feeling: <3-5 words>.
Psychology: create <curiosity/mastery/relief/desire>.
Interaction model: <relationship>, not a physical gesture.
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

Avoid: drag/slide/click labels, cursor hand, fake gesture affordance, before/after split line, lifestyle photo, famous quote, testimonial, metric-card collage, generic dashboard, feature grid, flowchart, node graph, arrows as main aesthetic, purple-blue gradient, glassmorphism, decorative orbs, stock imagery, mascot, dense panels, tiny unreadable text.
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
Interaction model: user intent -> system judgment -> desirable product result. This is a cognitive relationship, not a drag/slide gesture.
Art direction: [visual genre], [dominant silhouette], [material language], [typography mood], [tension pair]. The image should feel like a carefully art-directed product editorial, not a documentation page.

Composition: editorial product page with one dominant product proof object. First viewport is sparse: one headline, one support line, one action, one beautiful proof object. Show only a small hint of the next section.

Product object: a refined judgment surface with Intent, Judgment, and Preview layers. The Preview layer shows a coherent, beautiful interface result. It must not be a collage.

Palette: [expressive palette], with one rare accent used for desire or commitment.
Exact visible text:
[list no more than 10 short phrases]

Avoid: method diagram, workflow chart, dashboard collage, lifestyle photo, quote card, metric-card proof pile, feature grid, drag/slide/click labels, black-and-white default minimalism, saturated generic gradient, tiny text.
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

Avoid: node graph, exploded requirements diagram, chat-plus-side-panel default, dashboard chrome, drag/slide/click labels, particles, glassmorphism, purple-blue gradient, decorative orbs, tiny labels.
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
- Specify the relationship model, not a gesture control.
- Use `Intent`, `Judgment`, `Preview`, or equivalent conceptual layers only when they support the product story.
- Let the image model choose final proportion, depth, and atmospheric polish.
- Avoid prompt micromanagement that turns the output into a flowchart or static SVG.
- Keep output critique honest: if a generated preview is visible in chat but not saved to disk, report that instead of reusing an old file.

## Failure Signs

Reject or regenerate when the image:

- looks like a method diagram rather than a product page
- uses drag/slide/click labels without a real interactive demo
- relies on before/after split lines as the main idea
- fills the result with photos, quotes, metric cards, or random widgets
- turns into a dashboard, feature grid, node graph, or flowchart
- uses black-and-white minimalism by default when the brief asks for desire
- has tiny unreadable text or too many equally loud zones
