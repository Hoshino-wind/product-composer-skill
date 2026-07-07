# UI Generation Operating Model

Use this when normal workflow guidance still produces shallow UI, same-looking options, weak implementation fidelity, or a design that feels competent but not designed.

## Core Idea

The real job is not to make UI. The real job is to make a sequence of irreversible design decisions before code, then protect those decisions through implementation.

Read the companion references when the problem is not only visual taste:

- `input-output-mode-router.md`: choose the right workflow for the input and deliverable.
- `asset-context-protocol.md`: gather real assets and media constraints before visual invention.
- `design-memory-consistency.md`: preserve decisions across screens, sessions, and edits.

## 1. Choose The Surface Register

Before style, choose the register:

- `brand leads`: public pages, campaign pages, portfolios, editorial pages, cultural pages. Identity, story, and memorability carry the surface.
- `product serves`: dashboards, tools, forms, settings, editors, internal systems. Task flow, state clarity, and repeat use carry the surface.
- `hybrid balances`: product-led homepages, docs, public app pages. Brand expression must be anchored in product proof.
- `artifact packages`: runnable demos, shareable previews, single-file HTML, concept boards. The container and delivery constraints carry the surface.

Register decides what gets expressive. In brand-led work, typography, imagery, composition, and motion can take more risk. In product-serving work, hierarchy, state, density, and control placement take priority.

## 2. Build A Design Thesis Inventory

Before coding or prompting, write this inventory:

```text
Surface register:
One job:
Audience:
Dominant subject material:
Palette roles:
Type roles:
Layout thesis:
Signature element:
Content voice:
Motion role:
One justified risk:
One refusal:
```

Do not proceed if the inventory could fit a different product with only names changed.

## 3. Run The Generic-Default Self-Test

Ask:

- Would I make the same hero for another product in this category?
- Are the colors chosen because of the subject or because they feel modern?
- Is the headline supported by a real product object, state, or scenario?
- Are numbered labels, pills, badges, and dividers encoding structure, or decorating?
- Is the typography carrying personality, or only delivering text?
- Is motion one orchestrated moment, or scattered effects?
- Is the page trying to look premium by removing too much substance?
- Is the product usable, or only visually described?

If two answers point to generic behavior, revise the thesis before code.

## 4. Design The Complete Surface

A full request needs the full surface. A hero is not a product, a dashboard is not three cards, and a long page is not one repeated section.

For websites:

- define first viewport
- define next-section hint
- define section rhythm
- define proof or product moment
- define conversion path
- define mobile continuation

For apps and dashboards:

- define shell
- define primary work object
- define controls near that object
- define selected/loading/empty/error states
- define density behavior
- define responsive collapse

For multi-section work, each section needs a role and a rhythm shift. Do not repeat the same centered block, left text/right panel, or three-card grid.

## 5. Treat Copy As Design Material

Copy is part of the interface, not filler.

Rules:

- Use the user's exact copy when supplied.
- When copy is missing, write from the user's side of the screen.
- Name actions by what happens: save, publish, retry, compare, export, approve.
- Keep one action name consistent across button, toast, and state.
- Empty states invite action.
- Error states state what happened and how to recover.
- Labels label one thing; examples demonstrate one thing; helper text helps one thing.
- Avoid vague SaaS claims, clever abstraction, and invented metrics.

If the copy is generic, the design will feel generic even with good visuals.

## 6. Turn Concepts Into A Local Design System

Before implementation, extract:

- exact visible copy and allowed above-the-fold text
- color roles, including whether a background is true white, off-white, tinted, or dark
- type roles for display, body, labels, controls, captions, and data
- icon style: metaphor, stroke or fill, weight, size, alignment, color, and states
- media treatment: crop, aspect ratio, overlay, edge fade, mask, background blend, and shadow
- container model: open layout, band, rail, list, table, canvas, card, drawer, modal, or full-bleed section
- component families and allowed variants
- state model: selected, hover, focus, disabled, loading, empty, error, success
- motion tokens: duration, easing, stagger, continuity, reduced-motion fallback

This prevents implementation from becoming a new design.

## 7. Implement In Parity Slices

Build and compare in slices:

1. first viewport or primary screen
2. first major section or primary state
3. repeated component family
4. secondary section or state
5. mobile layout

After each slice, compare rendered UI to the chosen concept or reference. Fix visible drift before moving on.

Do not wait until the whole page is built to discover that type, spacing, color temperature, or container model drifted.

## 8. Use Deterministic Anti-Slop Detectors

Flag and repair:

- same font family everywhere with no role contrast
- purple-blue gradient as identity
- cream editorial page used without subject reason
- near-black page with one loud neon accent used by habit
- broadsheet layout used when content is not editorial
- cards nested inside cards
- equal rounded corners on every object
- gray body text on tinted backgrounds
- giant display type that shouts instead of composing
- display tracking so tight letters touch
- decorative image hover zoom
- every section using the same reveal animation
- hidden content that depends on animation firing
- fake dashboard fragments with no workflow
- badges, pills, and markers that encode nothing

Repair the detector that fires. Do not add more decoration to hide it.

## 9. Finish With A Short Parity Note

For implementation work, final review should name:

- locked decisions preserved
- visible deviations and why
- screenshot or browser checks performed
- remaining visual risk, if any

This note should be short and concrete.
