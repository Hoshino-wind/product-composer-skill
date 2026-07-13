# Product Surfaces

## Principle

Design operational surfaces around real work. Make the user's object, current state, next correct action, and recovery path clearer before adding visual expression; let beauty emerge from product order, useful density, and specific interaction structure.

## Contents

- [Priority Order](#priority-order)
- [Product Object And Task Order](#product-object-and-task-order)
- [Navigation And Contextual Actions](#navigation-and-contextual-actions)
- [Forms Tables Filters And Drawers](#forms-tables-filters-and-drawers)
- [State And Permission Clarity](#state-and-permission-clarity)
- [Data Grammar](#data-grammar)
- [Density And Content Judgment](#density-and-content-judgment)
- [3D Eligibility Gate](#3d-eligibility-gate)
- [Technical Surface Rules](#technical-surface-rules)
- [Acceptance Checks](#acceptance-checks)

## Priority Order
task correctness -> interaction clarity -> information architecture -> visual expression

Resolve each layer before optimizing the next. A visually memorable surface still fails when the task sequence, control meaning, object hierarchy, state, or permission model is ambiguous.

## Product Object And Task Order

Name the primary work object in user language: record, task, ticket, order, account, asset, policy, document, experiment, device, or another domain object. Define its identity, lifecycle, owners, permissions, important states, and the decisions users make about it.

Lay out the natural task order rather than the implementation architecture:

1. Establish where the user is and which object or scope is active.
2. Show the state and evidence needed for the current decision.
3. Place the primary action beside the object it changes.
4. Confirm the result and expose recovery or the next useful step.

Preserve capability progressively: give first-time users a clear start, then expose saved views, shortcuts, bulk actions, configuration, and automation when the work demands them. Every visible region must support acting, comparing, deciding, monitoring, or recovering.

## Navigation And Contextual Actions

Use a stable frame for repeated work: location, page identity, scope, navigation, filters, and the primary action should not move unpredictably between states. Make the current place and return path obvious.

Keep contextual actions beside the record, selection, region, or state they affect. Prefer direct manipulation, inline expansion, drawers, split panes, or side sheets when they preserve list or canvas context. Separate object actions from global actions, and keep destructive or high-cost actions visually distinct without repeating the primary action in competing locations.

## Forms Tables Filters And Drawers

- Forms: use persistent labels, explicit required fields, useful defaults, inline validation, clear save behavior, and recovery that preserves entered data.
- Tables: make each column serve identification, comparison, status, or action; keep row actions attached to the row and support sorting, selection, pagination or virtualization, and empty states as the task requires.
- Filters: keep frequent or decision-critical filters visible, show the active scope, make reset behavior obvious, and preserve filters when users inspect details and return.
- Drawers and split panes: use them to inspect or edit without losing context; avoid stacks of modals or hidden state changes behind overlays.
- Controls: prefer familiar platform or design-system semantics unless a custom control measurably reduces work or translation.

Allow long labels, localized content, keyboard operation, focus states, and small viewports to reflow without hiding task-critical controls.

## State And Permission Clarity

Create certainty by making selected, loading, empty, success, error, partial-failure, stale, offline, disabled, and destructive states distinguishable. Explain whether data is absent, delayed, filtered out, unavailable, or forbidden; never collapse these into one blank state.

For permission-limited actions, show what the user can see, why the action is unavailable, and the legitimate next step. Confirm irreversible or high-cost changes, preserve an audit trail when the domain requires it, and provide undo, retry, rollback, or escalation where possible.

## Data Grammar

Data grammar gives every value a consistent meaning and visual role.

- Identify the entity, measure, unit, dimension, time window, comparison basis, source, and freshness that make a value interpretable.
- Use tables for exact lookup and multi-attribute comparison; use charts for trend, distribution, relationship, or composition; use maps only when geography or spatial position changes the decision.
- Keep number formats, units, scales, legends, thresholds, and semantic colors consistent across views.
- Distinguish zero, unknown, not applicable, pending, stale, and access-restricted values.
- Attach annotations, alerts, and actions to the datum or region that caused them.
- Prefer a small set of chart and status grammars that users can learn over decorative variety.

## Density And Content Judgment

Use dense-with-air composition for serious repeated work: retain the information needed to decide, but create air through grouping, alignment, hierarchy, stable row rhythm, and quiet zones rather than oversized whitespace.

Keep task-critical status, filters, comparison data, and actions in the working field. Defer secondary explanation to help, details, progressive disclosure, or later states; delete redundant labels and decoration. Do not hide real data to appear minimal, shrink everything to fit, or turn an operational screen into a marketing hero.

## 3D Eligibility Gate

Apply the 3D eligibility gate only when all three conditions are true:

1. The user task depends on spatial geometry.
2. Readings or controls anchor to real regions of the object.
3. Available assets and performance permit a usable 3D experience.

If any condition fails, select tables, comparison, charts, maps, or calm native product UI. A technical category, a request for visual impact, or the availability of a decorative model does not pass the gate.

## Technical Surface Rules

When the gate passes, make the spatial object an inspectable work surface: show a useful cutaway, exploded layer, sensor region, diagnostic overlay, calibration state, live reading path, or controllable region. Anchor sparse labels, warnings, and controls to the geometry they describe, and provide a readable non-spatial fallback for accessibility or degraded performance.

Technical does not mean black cockpit, blue glow, terminal skin, militarized naming, or equal panels. Build around one specific control, measurement, simulation, audit, or inspection relationship. Keep state explicit, motion causal, reduced-motion behavior available, and layout stable while data loads or updates.

## Acceptance Checks

- Can the user name the active work object, current scope, and next correct action without reading decorative copy?
- Does the screen follow natural task order and keep contextual actions beside affected objects?
- Are navigation, filters, forms, tables, drawers, state, permissions, and recovery behavior explicit?
- Does every chart or value obey the same Data grammar and support a real decision?
- Is the density appropriate for task frequency, with air created by hierarchy rather than missing information?
- If 3D is present, do all three eligibility conditions hold and do controls attach to real regions?
- Does visual expression make the work more specific and legible without displacing task correctness?
