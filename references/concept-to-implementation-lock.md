# Concept To Implementation Lock

Use this when implementing from an accepted image concept, generated UI mockup, screenshot, design board, or visual comp.

## Principle

An accepted concept is a design decision, not a mood board. Implementation should preserve the visible intent while making it responsive, accessible, and maintainable.

## Lock The Concept

Before coding, list the locked elements:

- first focal point
- second focal point
- dominant visual object
- visible hierarchy
- key copy intent
- palette roles
- type character
- component density
- spatial relationship between navigation, content, proof object, and action
- image or material treatment
- motion promise, if visible or implied

These should survive implementation.

## Implementation Inventory

Before coding, inventory:

- exact visible copy and which new text is allowed
- nav labels, CTA labels, section headings, proof strings, and data labels
- section order and next-section visibility
- color roles and color temperature
- type roles for display, body, label, control, caption, and data
- icon inventory: metaphor, outline or fill, stroke weight, size, color, padding, and state
- media treatment: crop, overlay, mask, edge fade, shadow, background blend, and aspect ratio
- container model: open, band, rail, list, table, canvas, card, drawer, modal, full-bleed
- responsive intent: what stacks, what stays side-by-side, what becomes condensed, what is removed

## Adapt For Engineering

The implementation may adjust:

- exact token values
- component names and internal structure
- breakpoints and stacking behavior
- accessible contrast and focus states
- real data shape and loading/empty/error states
- long text and localization behavior
- reduced-motion fallback
- performance constraints

These adjustments should protect the concept, not redesign it.

## Change Ledger

When implementation deviates from the concept, record:

```text
Locked:
Adjusted:
Reason:
Visual check:
```

Use this for real deviations, not every small CSS value.

## Redesign Triggers

Stop and ask or state the tradeoff when:

- the concept cannot fit real content without changing hierarchy
- the palette fails accessibility
- the hero or primary object cannot be implemented with available assets
- responsive layout destroys the first read
- the accepted design conflicts with the existing product system
- performance would suffer from the visible motion or 3D layer

## Implementation Checks

After coding, compare rendered output to the concept:

- Is the same thing noticed first?
- Does the second read still support the first?
- Did the dominant object remain dominant?
- Did type scale and density drift?
- Did palette roles survive even if exact colors changed?
- Did the layout become a generic template?
- Did engineering convenience remove the memorable detail?
- Does mobile preserve the concept's intent rather than only stacking blocks?

## Section-By-Section Parity

For long pages or multi-state apps, compare in slices:

1. first viewport
2. each major section
3. repeated component family
4. key state or modal
5. mobile version

Fix visible drift in the current slice before building the next one. This prevents accumulated mismatch.

## Common Failure Modes

- Replacing a distinctive composition with a standard hero/card grid.
- Flattening depth, material, or object treatment into plain panels.
- Changing type scale until the concept loses voice.
- Keeping colors while losing hierarchy.
- Preserving desktop but ignoring mobile.
- Adding components the concept did not need.
- Treating "responsive" as permission to redesign.
