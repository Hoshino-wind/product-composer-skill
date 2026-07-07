# React Bits Motion Layer

Use this when a React or Next.js UI can benefit from React Bits-style motion: animated text, kinetic typography, cursor/hover effects, scroll reveals, particle fields, WebGL backgrounds, Three.js scenes, or expressive portfolio polish.

## Principle

Motion is an interface layer, not a substitute for product hierarchy. The screen must work as a static composition first; animation may then focus attention, reveal state, connect sections, or create one memorable brand moment.

## When To Use

Use for:

- brand surfaces, launch pages, portfolios, campaigns, product showcases, cultural/editorial pages, and polished empty states
- hero headlines, section reveals, product proof moments, feature tiles, galleries, and memorable first-viewport backgrounds
- playful consumer, bold campaign, editorial premium, and visually rich hybrid surfaces where motion supports desire or identity
- frontier or technical surfaces only when motion explains state, time, simulation, execution, or controllable system behavior

Avoid by default for:

- admin panels, CRM, ERP, settings, forms, tables, filters, and repeated high-frequency workflows
- dense dashboards where animation slows scanning or competes with data comparison
- mobile screens where heavy effects reduce responsiveness or battery life
- any screen where the user must wait for animation before reading, choosing, or acting

## Motion Role Map

| Role | Use | Examples |
|---|---|---|
| Focus | Direct the first look | headline reveal, cursor spotlight, one active card |
| Reveal | Pace narrative information | scroll reveal, staggered proof points, metric count-up |
| Feedback | Confirm state change | selection pulse, success transition, loading skeleton motion |
| Continuity | Connect sections or states | shared background field, line trail, object transformation |
| Signature | Make the page memorable | WebGL hero, kinetic wordmark, inspectable 3D product moment |

If the role is only "looks cool", remove the effect.

## Component Selection

- Animated text: use for one hero line, one short metric cluster, or one section intro. Do not animate long paragraphs or delay comprehension.
- Background effects: use only behind sparse content with proven contrast. Keep calls to action readable without waiting for motion.
- Hover and cursor effects: use for galleries, feature cards, creative tools, or playful brand surfaces. Do not hide essential actions behind hover.
- Scroll reveals: use for narrative pages. Avoid scroll-jacking and avoid revealing every block with the same effect.
- WebGL, Three.js, and particles: use for one signature scene or product proof. Lazy-load when practical and provide a static fallback.

## Integration Workflow

1. Classify the surface: product, brand, hybrid, frontier, editorial, cultural, or utility.
2. Define the motion role: focus, reveal, feedback, continuity, signature, or none.
3. Confirm the static layout already has clear hierarchy, readable text, and an immediate primary action.
4. Choose the smallest React Bits-style component that serves the role.
5. Adapt typography, color, spacing, easing, duration, and density to the existing design system.
6. Add reduced-motion behavior before accepting the implementation.
7. Verify desktop, mobile, interaction states, and performance in a rendered browser.

## Implementation Rules

- Prefer local project patterns for components, styling, animation libraries, and client/server boundaries.
- Treat React Bits code as source to adapt, not as a visual style to copy wholesale.
- Keep animated containers dimensionally stable to prevent layout shift.
- Mark purely decorative motion as `aria-hidden` and never rely on motion alone to communicate status.
- For SSR frameworks, isolate browser-only animation, canvas, or WebGL code behind client boundaries.
- Lazy-load heavy scenes and avoid placing expensive effects behind every route or repeated component.
- Respect upstream licensing if copying component code; do not repackage the copied components as a competing component library.

## Quality Gates

- One or two major animated moments per screen is usually enough.
- Primary navigation, primary action, and core content must be available immediately.
- Text must not overlap, clip, flash unreadably, or wrap badly during animation.
- Background motion must not reduce contrast or make text shimmer.
- Product data, tables, forms, and controls must remain scan-friendly.
- The reduced-motion experience must still look intentional, not broken.

## Common Mistakes

- Applying a different effect to every section.
- Using animated text for long copy or critical instructions.
- Placing particles or WebGL behind dense UI.
- Making a dashboard feel like a marketing hero.
- Keeping React Bits default colors, timing, or spacing when they clash with the product system.
- Forgetting mobile screenshots and reduced-motion checks.
