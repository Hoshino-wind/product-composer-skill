# Visual Quality Rubric

Use this when a UI looks generic, ugly, overdecorated, flat, too AI-flavored, poorly composed, or almost good but not polished enough.

## Principle

High-quality UI is not a style. It is a visible set of decisions: one clear hierarchy, deliberate proportion, controlled density, specific material, disciplined type, and a memorable product object.

## Score The Surface

Rate each dimension as `0`, `1`, or `2`.

- `0`: missing, accidental, or template-like
- `1`: functional but ordinary
- `2`: deliberate, specific, and visually resolved

The screen is not ready if any primary dimension is `0`.

### Primary Dimensions

1. Hierarchy: the eye knows what to read first, second, and third.
2. Proportion: regions have convincing scale relationships, not equal-weight boxes.
3. Typography: type size, weight, line length, and spacing feel intentional.
4. Palette: colors have roles, tension, and restraint; they are not trend filler.
5. Material: surfaces, borders, shadows, blur, imagery, and texture feel physically coherent.
6. Density: information amount matches the job and still leaves breathing room.
7. Specificity: the screen could not belong to any random product after swapping labels.
8. Interaction promise: visible controls imply a believable product behavior.
9. Motion discipline: motion focuses, reveals, connects, or brands; it is not decoration.
10. Finish: edge cases, empty states, long text, mobile layout, and focus states do not break the composition.

## Advanced Versus Generic

| Dimension | Advanced | Generic |
| --- | --- | --- |
| Form | One strong product object or spatial idea | Many cards with equal weight |
| Type | Distinct scale, rhythm, and restraint | Default sizes with random bold text |
| Color | Small set of roles with one memorable accent | Purple-blue gradient or one-hue palette |
| Layout | Built around task or story logic | Nav, hero, cards, stats by habit |
| Detail | Few precise details that carry identity | Many icons, chips, glows, and labels |
| Motion | Clarifies continuity or focus | Loops because animation looks modern |
| Product feel | Looks usable and inspectable | Looks like a poster about software |

## Generic-Default Self-Test

Before implementation, ask whether the design plan depends on any automatic taste reflex:

- warm cream editorial background without subject reason
- near-black surface with one loud neon accent
- broadsheet rules and dense columns without editorial content
- centered hero plus abstract object plus three cards
- neutral typography everywhere with no role contrast
- numbered section markers that do not encode a real sequence
- decorative badges, pills, or pseudo-system labels
- default dashboard collage instead of a real work object

If the answer is yes, revise the design thesis. Do not merely change the palette.

## Concrete Craft Checks

- Body text contrast should feel readable before it feels subtle.
- Muted text on tinted surfaces often needs to move toward the main ink color.
- Body line length should stay controlled; wide paragraphs make polish feel accidental.
- Display type needs a ceiling; bigger is not automatically more designed.
- Tight display tracking must stop before letterforms feel cramped.
- Use one font family well or pair along a real contrast axis.
- Cards are an affordance, not decoration.
- Nested cards are a failure unless the product object truly requires containment.
- Motion should have a cause-effect relationship and a reduced-motion fallback.
- Repeated reveal animation across every section is a tell, not a system.

## Repair Moves

Use the lowest-scoring dimension to choose the repair:

- Weak hierarchy -> remove secondary zones, enlarge the primary object, and reduce competing accents.
- Weak proportion -> make one region dominant, one supporting, and one quiet.
- Weak type -> reduce the number of sizes, fix line length, and create a stronger display/body contrast.
- Weak palette -> assign base, surface, text, semantic, emotional accent, and action roles.
- Weak material -> choose one surface logic: paper, glass, metal, canvas, spatial scene, instrument, or flat product.
- Weak density -> delete or defer weak content; do not shrink everything.
- Weak specificity -> replace decorative elements with product-native objects, states, or materials.
- Weak interaction promise -> show state, affordance, feedback, or before/after relationship.
- Weak motion -> remove motion that does not focus, reveal, connect, or brand.
- Weak finish -> test mobile, long labels, empty data, disabled actions, and reduced motion.

## AI-Flavored Failure Signs

Reject or repair when the design depends on:

- purple-blue gradients as the main identity
- glass panels without a material reason
- nested cards inside cards
- huge rounded icon tiles
- vague SaaS copy
- fake dashboard fragments that do not show a workflow
- decorative particle fields, orbs, or glows
- equal-width feature cards immediately under a hero
- motion labels instead of actual interaction design
- empty premium minimalism with no product object

## Final Pass

Before final output, name:

- the dominant visual form
- the quality risk that was removed
- the one detail that makes the surface specific
- the visual check performed
