# Reference DNA Extraction

Use this when working from a screenshot, reference site, accepted mockup, existing product screen, or visual style sample.

## Principle

Do not copy pixels blindly and do not reinterpret the reference into a different style. Extract the design DNA: the choices that make the reference work.

## Three Passes

### 1. First Read

Capture what is immediately visible:

- first focal point
- second focal point
- page rhythm
- dominant shape or product object
- density level
- emotional tone
- strongest color relationship
- content voice and label behavior
- whether it feels product, brand, hybrid, editorial, cultural, or utility

If the first read is unclear, the implementation will drift.

### 2. System Read

Extract repeatable rules:

- layout grid: columns, margins, gutters, section height, breakpoint behavior
- type system: display size, body size, weights, case, line height, reading width
- color roles: base, surface, text, quiet text, border, accent, action, semantic states
- surface logic: flat, layered, glass, paper, metal, canvas, spatial, instrument, editorial
- component density: cards, rows, controls, inputs, chips, tables, navigation, modals
- imagery: crop, scale, lighting, realism, object angle, texture, integration with UI
- spacing rhythm: tight groups, loose section gaps, alignment rules, repeated offsets
- content hierarchy: what is primary, deferred, grouped, or hidden
- structural meaning: whether numbering, dividers, chips, badges, and labels encode real information
- copy system: action names, empty state tone, error tone, label length, and whether copy sells or guides
- interaction promise: what appears clickable, adjustable, inspectable, animated, or reversible

### 3. Translation Read

Decide what must survive:

- locked: hierarchy, dominant form, palette roles, density, type character, key copy intent, and spatial relationship
- adaptable: exact copy length, component names, token values, breakpoint layout, accessible states, loading/empty/error behavior
- replaceable: ornamental details that do not support the product or the user's requested direction

## DNA Output Shape

Before coding or prompting, write a compact extraction:

```text
Reference DNA:
- First read:
- Dominant form:
- Layout rule:
- Type rule:
- Color rule:
- Surface/material rule:
- Component density:
- Interaction promise:
- Copy voice:
- Structural devices:
- Locked elements:
- Adaptable elements:
```

## Common Mistakes

- Copying only colors and missing density.
- Copying component shapes while changing the hierarchy.
- Preserving decorative details but losing the product object.
- Treating a brand page reference as if it were an app UI reference.
- Treating a dense utility screenshot as if it needed a marketing hero.
- Matching desktop while ignoring mobile composition.
- Using a reference as permission to ignore the local design system.

## Translation Check

After implementation, compare:

- Does the first read still match?
- Is the dominant form still dominant?
- Did type rhythm survive?
- Did the palette keep the same role structure?
- Did density drift lighter or heavier without reason?
- Did the copy still sound like the same product?
- Did structural devices keep their meaning?
- Are deviations intentional and useful?
