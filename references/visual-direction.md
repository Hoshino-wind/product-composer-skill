# Visual Direction

Use this before generating or implementing new UI. The goal is taste, not decoration.

## Principle

Interaction design does not excuse ugly composition. A good product surface needs a memorable form, controlled rhythm, strong proportion, and enough restraint for the interaction model to feel inevitable.

## Aesthetic Brief

Before making the UI, define:

- Style family: the selected visual family and why it fits the product.
- Dominant visual form: the one shape or spatial structure the user remembers.
- Composition type: centered instrument, diagonal flow, editorial split, radial control, layered stage, map, timeline, canvas, or object portrait.
- Density strategy: sparse, medium, dense, or dense-with-air.
- Material language: paper, instrument panel, editorial print, precision hardware, calm software, luminous ink, spatial layer, or tactile control.
- Color tension: the contrast between neutral base and accent system.
- Signature detail: one detail that feels ownable, not borrowed.
- What to remove first if the layout becomes busy.

## Composition Rules

- One hero form should dominate the first viewport.
- Secondary UI must orbit, support, or reveal that form; it should not compete with it.
- In a transformation layout, the result side must be more beautiful and more coherent than the source side; it cannot become a collage of proof fragments.
- Use asymmetry deliberately; avoid perfectly distributed widgets that feel like a diagram.
- Use negative space as structure, not leftover emptiness.
- Create a clear visual path for the eye: anchor, secondary read, action, evidence.
- Let important objects have room to breathe.
- Use fewer labels when shape, grouping, and state can communicate.
- Design the silhouette first; details come second.
- When producing a set of alternatives, each direction must be visually orthogonal. Changing copy while keeping the same warm background, central object, right panel, rounded cards, and status chips is not a new direction.

## Taste Checks

Ask:

- Would this look composed as a black-and-white thumbnail?
- Does the image have a clear foreground, middle ground, and background?
- Is there a memorable contour or spatial gesture?
- Are there too many boxes of similar size?
- Are accents rare enough to matter?
- Is the typography doing hierarchy work, or merely labeling clutter?
- Does the interface feel designed by a product brand, not assembled from UI kits?

## Frontier UI Beauty

For new interaction paradigms, do not make the interface look like an exploded requirements diagram.

Prefer:

- one iconic interactive object
- large quiet areas
- sparse labels
- direct manipulation handles
- visible state through form, position, tension, and color
- compact panels that feel attached to the object
- cinematic but functional staging

Avoid:

- node graphs with dozens of equal nodes
- flowcharts as the main aesthetic
- every primitive visible at once
- busy annotation layers
- generic enterprise dashboard chrome
- sterile whiteboard diagrams
- cockpit, command-center, terminal, or sci-fi dashboard styling unless the product is literally in that domain
- militarized or industrial-fantasy names such as `运行舱`, `指挥舱`, `智控舱`, `超脑`, or `中枢` for normal software products
- lifestyle photo, quote, metric-card, and widget collages pretending to be product proof

## Utility And Technical Beauty Floor

Utility and technical surfaces need taste as much as brand pages. Do not accept a screen just because it is clear, aligned, and functional.

For utility product screens:

- The screen needs one memorable workflow object, not only a left rail plus cards and a table.
- For SaaS and enterprise tools, reference Ant Design values: natural task order, certainty, meaningful work objects, and progressive capability.
- Beauty should come from product order: stable frame, object hierarchy, contextual actions, explicit state, disciplined tables/forms/filters/drawers, and reusable rhythm.
- Use state, grouping, and proportion to create beauty; avoid pale generic software chrome.
- Keep real operational density, but make the main work area feel composed and product-specific.

For technical instrument screens:

- Precision is not the same as darkness, glow, or complexity.
- Start with a specific control object: audit lens, simulation strip, execution timeline, approval surface, risk dial, or evidence ledger.
- When the product can plausibly be physical or inspectable, start with a 3D instrument/digital-twin viewport instead of flat panels.
- Anchor overlays, labels, readings, warnings, and controls to parts of the 3D object.
- Use warm precision when in doubt: graphite, ivory, muted cyan, brass, paper, and technical ink.
- If the result feels like a control room, rebuild around a smaller, quieter, more desirable object.

## 3D Instrument Composition

Use for technical instrument, device, robotics, IoT, industrial, scientific, medical, monitoring, or simulation products.

Composition requirements:

- Make the 3D object the main proof, not a decorative hero image.
- Show a useful inspection state: cutaway, exploded layer, sensor hotspots, diagnostic overlay, calibration ring, heat/state field, or live reading path.
- Attach controls to the relevant object region instead of placing generic action cards around it.
- Use depth deliberately: object, overlays, and background must read as a product viewport.
- Keep labels sparse and operational; the object shape should carry most of the meaning.

Avoid:

- flat dashboard cards pretending to be an instrument
- generic dark cockpit styling
- glowing terminal panels
- decorative 3D models with no inspectable state
- many unrelated floating labels around a 3D object

## Direction Orthogonality

When a user is comparing multiple UI images, visual difference must be structural, not cosmetic.

Different enough:

- different dominant silhouette
- different spatial grammar
- different material system
- different action placement
- different density rhythm
- different proof object

Not different enough:

- same centered artifact with renamed labels
- same right-hand action panel
- same warm card background with fine borders
- same timeline/rail metaphor reused across product categories
- same status chips and rounded card hierarchy
- same "tasteful enterprise" look with different accent colors

If a repair fixes one failure by returning to a familiar safe pattern, treat it as failed. Regenerate from an opposing composition family.

## Palette Guidance

Start with a tasteful base, then add tension and appetite. Minimal does not mean default black-and-white.

Good bases:
- warm white, ink, graphite, mineral gray
- chalk, charcoal, muted green-black
- paper white, oxblood, desaturated blue-gray
- soft black, silver, muted cyan, warm warning amber
- pistachio, ink green, warm cream, muted coral
- powder blue, deep navy, porcelain, warm amber
- clay, plum ink, linen, pale peach
- mist lavender, graphite, off-white, acid lime used rarely

Use bright color sparingly for agency, risk, selection, commitment, or desire. A beautiful interface often uses fewer colors, but not necessarily less emotional color.

## Image Generation Guidance

When prompting an image model for UI:

- Ask for a refined design-board quality mockup, not a screenshot full of tiny labels.
- Let the image model carry aesthetic composition; do not over-specify the prompt into a box-by-box SVG or flowchart.
- Specify one dominant visual object.
- Limit visible text to a few exact phrases.
- Ask for large negative space and restrained secondary UI.
- Avoid asking for every interaction primitive to be visible at equal prominence.
- Require that the image still reads well when viewed as a thumbnail.
- If the user asks for UI without code, prefer an image-generation aesthetic pass before hand-built vector mockups.
- For elegant UI image prompts, use a reusable prompt template before improvising; the template should define feeling, psychology, interaction relationship, dominant object, palette, exact text, and avoid list.
- Do not reuse the same composition family by habit; make the selected style family change density, material, palette, and proof object.
- If the user says the output looks like prior images, perform an orthogonality pass before generating again.
