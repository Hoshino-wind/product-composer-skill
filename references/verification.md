# UI Verification

Verify rendered UI before finalizing whenever the project can run locally.

## Local Checks

1. Find the repo's existing commands in `package.json`, lockfiles, README, or prior scripts.
2. Run install only when dependencies are missing and the project expects it.
3. Run typecheck, lint, build, or targeted tests when available and relevant.
4. Start the dev server for frontend changes unless the user explicitly asks not to.
5. Use browser or Playwright screenshots for at least:
   - desktop viewport
   - mobile viewport
   - any critical modal, drawer, menu, empty state, or error state touched by the change

## Visual Checks

- Page is nonblank and assets load.
- Primary workflow is visible without reading explanatory text.
- Text does not overflow, overlap, or clip.
- Buttons, tabs, chips, inputs, and table cells survive long labels.
- Spacing and alignment look intentional at both desktop and mobile sizes.
- Color contrast is sufficient for text and icon controls.
- Interactive states are visible: hover, focus, selected, disabled, loading, error.
- Product surfaces remain scan-friendly and not over-decorated.
- Brand surfaces reveal the actual product, place, offer, or object in the first viewport when relevant.

## Scanner

Run the bundled scanner when useful:

```bash
node /Users/gaozengyu/.codex/skills/product-composer/scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

Review each warning manually. Do not remove intentional design choices only because the scanner warned.

## Reporting

In the final response, say what was changed and what was verified. If a check could not run, state that plainly.
