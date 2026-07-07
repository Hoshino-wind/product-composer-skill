# Execution Discipline

Use this as local execution discipline. The goal is to give the agent a design vocabulary and staged workflow without copying an external style system.

## Capture Context

Before changing UI, inspect or infer:

- product audience
- surface lane: brand, product, or hybrid
- current visual language
- anti-references: what the UI must not feel like
- reusable tokens and components
- content voice
- implementation constraints

If the repo contains `DESIGN.md`, `PRODUCT.md`, `AGENTS.md`, design tokens, Storybook, Figma exports, or nearby screens, read them before inventing style.

## Use Design Verbs

Apply these verbs during work:

- `shape`: plan the information architecture, hierarchy, and task flow before coding.
- `typeset`: choose or preserve type scale, weight, line length, and text density.
- `colorize`: define neutrals, semantic colors, and accents; avoid one-note palettes.
- `arrange`: improve spatial rhythm, alignment, grouping, and scanning.
- `clarify`: rewrite copy, labels, and empty/error states so the UI explains itself.
- `animate`: add restrained motion only when it communicates continuity, status, or causality.
- `critique`: review hierarchy, clarity, brand fit, and emotional tone.
- `audit`: check accessibility, responsive behavior, performance, and edge cases.
- `polish`: final visual pass after behavior is correct.
- `harden`: protect against long text, missing data, permissions, loading, errors, and mobile constraints.

## Brand Mode

Use for marketing, portfolio, launch, editorial, or public-facing pages.

- Lead with identity and narrative.
- Make the first viewport memorable and specific.
- Use real or generated visual assets when they clarify the offer or object.
- Let typography, imagery, composition, and copy carry more expressive weight.
- Avoid generic centered SaaS hero layouts unless the brand truly calls for them.

## Product Mode

Use for applications, dashboards, internal tools, workflows, and repeated-use surfaces.

- Lead with task structure and state clarity.
- Keep density high enough for real work.
- Use restrained visual expression that helps scanning.
- Favor reusable components and predictable interactions.
- Avoid turning operational pages into brand campaigns.

## Tuning Passes

Use these when a UI is functionally correct but visually wrong:

- `bolder`: add contrast, asymmetry, specificity, sharper hierarchy, or a stronger visual thesis.
- `quieter`: reduce accents, shadows, borders, copy, motion, or decorative surfaces.
- `distill`: remove anything that does not support the user mission.
- `align`: bring spacing, tokens, controls, and component choices back to the local system.

## Live Iteration Habit

Prefer changing the real source and reviewing diffs over producing throwaway mockups. When possible, run the app, capture screenshots, patch source, and re-check the rendered result.
