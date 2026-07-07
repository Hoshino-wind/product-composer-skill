# Task Router

Use this before loading many references when the request is ambiguous, broad, or easy to over-process.

The goal is to choose the smallest route that can produce a high-quality result. Do not run the full UI generation workflow for a narrow fix, and do not treat a full redesign as a small patch.

## Route Table

| Work mode | Typical trigger | Read | Skip |
|---|---|---|---|
| quick patch | Small visual fix, spacing issue, one component, one state, bug in an existing screen | `design-memory-consistency.md`, `anti-patterns.md`, `verification.md` | Style family questions, direction matrix, full signature system |
| design review | "Review", "audit", "critique", "what is wrong", screenshot review, PR UI review | `design-review-output.md`, `visual-quality-rubric.md`, `anti-patterns.md`, `verification.md` | New visual direction unless requested |
| existing system | Add or adjust UI inside a mature app or design system | `design-memory-consistency.md`, `ant-design-product-values.md` when relevant, `verification.md` | New brand language unless redesign is requested |
| Figma | Figma URL, selected frame, design spec, frame-to-code, design-to-code | `reference-dna-extraction.md`, `concept-to-implementation-lock.md`, `asset-context-protocol.md`, `verification.md` | Style invention unless asked |
| screenshot/reference | Screenshot, visual sample, existing site, accepted mockup, reference image | `reference-dna-extraction.md`, `visual-quality-rubric.md`, `concept-to-implementation-lock.md` | Blind copying and generic restyling |
| image mockup | User asks for generated UI image, visual concept, no-code mockup | `image-generation-aesthetic-calibration.md`, `asset-context-protocol.md`, `direction-matrix-builder.md` when taste is unclear | Hand-built SVG mockups unless deterministic vectors are needed |
| accepted concept | User approved a generated image, design board, mockup, or direction | `concept-to-implementation-lock.md`, `asset-context-protocol.md`, `verification.md` | Silent redesign during implementation |
| layer document | Editable layer output, HTML preview, layer decomposition, chart/table layers | `design-layer-document.md`, `asset-context-protocol.md`, `verification.md` | Flat PNG-only output |
| full redesign | "Redesign", "make it better", weak visual system, stale homepage, broad app refresh | `direction-matrix-builder.md`, `visual-quality-rubric.md`, `design-memory-consistency.md`, then task-specific references | Immediate coding before direction |
| frontier interaction | AI agent, command canvas, automation, simulation, complex creative workflow | `interaction-grammar.md`, `visual-direction.md`, `visual-quality-rubric.md` | Literal drag/click labels or dashboard shells |
| brand/landing | Public homepage, launch page, portfolio, product marketing | `market-calibration.md`, `desire-minimalism-psychology.md`, `signature-aesthetic-systems.md`, `asset-context-protocol.md` | Abstract decoration with no product proof |
| dashboard/data | Admin panel, analytics, table-heavy flow, CRM, settings | `ant-design-product-values.md`, `content-judgment.md`, `visual-quality-rubric.md` | Marketing hero composition inside the product surface |

## Escalation Rules

- Escalate from quick patch to existing system work when the same change touches repeated components, tokens, or multiple screens.
- Escalate from design review to full redesign only when the user asks for implementation or the current UI has no coherent system to preserve.
- Escalate from screenshot/reference to accepted concept only after the user chooses a direction or explicitly says to implement it.
- Escalate from image mockup to accepted concept after a generated visual is selected.
- Escalate from existing system to full redesign only when preserving the local system would keep the main failure intact.

## Output By Route

For quick patch:

- State the local pattern being preserved.
- Make the smallest change that fixes the visible issue.
- Verify layout, text fitting, and affected states.

For design review:

- Use `design-review-output.md`.
- Findings first, then concise next steps.
- Do not redesign unless requested.

For Figma or screenshot/reference:

- Extract hierarchy, spacing, palette roles, type roles, assets, and state behavior.
- Name what is locked and what may adapt.
- Validate in slices rather than only at the end.

For image mockup:

- Define asset context before prompting.
- Pick one dominant object or interaction relationship.
- Keep visible text short.
- Inspect the generated result before claiming it is usable.

For full redesign:

- Diagnose the current failure.
- Produce 3-5 meaningfully different directions when taste is unclear.
- Choose one direction before coding.
- Preserve any local system elements that still work.

For layer document:

- Store structure in `.layerdoc.json`.
- Keep semantic groups meaningful.
- Export HTML only after validation.

## Anti-Overprocessing Guard

If the requested change can be handled by a narrow route, do not ask broad style questions. If a task requires a broad route, do not hide uncertainty behind a polished first draft.

Use the route to reduce work, not to skip quality.
