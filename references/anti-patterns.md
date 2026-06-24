# UI Anti-Patterns

Use this as a checklist before implementation and during critique. These are warnings, not absolute bans; keep a pattern only when it is clearly justified by the product and executed well.

## Generic AI Visual Signatures

- Purple-to-blue gradients as the main identity.
- Glowing blobs, bokeh dots, or decorative orbs with no product meaning.
- Nested cards inside cards inside cards.
- Rounded-square icon tiles above every heading.
- Huge centered hero plus three generic benefit cards.
- Glass panels and blur effects used as decoration.
- Overuse of soft shadows, translucent borders, and vague depth.
- Stock-like dark abstract imagery that hides the actual product.
- Lifestyle photos, famous quotes, metric cards, and small widgets used together as fake product proof.
- Placeholder copy such as "unlock", "seamless", "powerful", "transform", "all-in-one" without specific proof.
- Fake interaction labels such as "drag to", "click to", or "slide to" when the product is not actually offering that interaction.
- Flowcharts or node graphs used as the main aesthetic when the user asked for a product experience.
- Formulaic SaaS homepage layout: nav, left headline, two CTAs, right screenshot, three proof cards, with no ownable composition.
- Hand-built SVG or diagram mockups used for aesthetic exploration when the user asked to directly generate a beautiful UI image.
- UI image prompts that omit feeling, psychology, interaction relationship, palette, exact text, or an explicit avoid list.

## Product UI Mistakes

- Dashboard designed like a landing page.
- Too much vertical whitespace for repeated-use workflows.
- Primary action unclear or repeated in multiple competing places.
- Filters hidden when filtering is central to the workflow.
- Table rows with actions far away from the record they affect.
- Empty states that explain the feature but do not help the user proceed.
- Error states that blame the user or hide recovery actions.
- Modal stacks that trap the user and destroy context.
- Custom controls where familiar controls would be faster and clearer.

## Typography Mistakes

- Using default fonts without checking the repo or brand.
- Fluid viewport-scaled type inside app UI.
- Hero-sized text inside cards, panels, sidebars, tables, or compact controls.
- Too many font sizes with no scale.
- Low-contrast gray body text on tinted or busy backgrounds.
- Long labels that cannot fit localized strings.

## Color Mistakes

- One-hue palettes where every surface is the same color family.
- Black-and-white minimalism used as the default answer when the product needs desire, warmth, or appetite.
- Pure decorative accent colors with no semantic role.
- Pure white emptiness or pure black drama used as a substitute for composition.
- Saturated accent color used across large areas when the user asked for calm minimalism.
- Color as the only signal for status, risk, category, or selection.
- Low contrast text, icons, chips, and disabled states.
- Competing accents that make every region look equally important.

## Layout Mistakes

- No stable dimensions for toolbars, icon buttons, boards, counters, tiles, and tables.
- Breakpoints that hide important workflow controls.
- Text overlapping images, charts, buttons, or adjacent panels.
- Cards used as page sections instead of repeated items or actual framed tools.
- Many equal boxes in the first viewport, forcing the user to choose where to look.
- Before/after layouts where the "after" side is less coherent, less beautiful, or less product-specific than the "before" side.
- Fixed heights that clip real content.
- Mobile layouts that keep desktop density without reflowing controls.
- Flowcharts that explain system logic but fail as a beautiful or usable interaction surface.

## Motion Mistakes

- Motion that delays task completion.
- Bounce effects in serious product contexts.
- Decorative animation that fights data scanning.
- No reduced-motion consideration for large or repeated motion.

## Keep Only If

Keep a risky pattern only when all are true:

- It supports the user mission or brand thesis.
- It remains accessible and responsive.
- It fits the existing design system or intentionally evolves it.
- It does not make real product data harder to inspect.
