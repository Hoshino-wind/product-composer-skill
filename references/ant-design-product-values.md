# Ant Design Product Values

Use these values as product UI decision checks, especially for enterprise software and complex work surfaces.

Sources for inspiration:
- https://ant.design/docs/spec/values/
- https://ant.design/docs/spec/introduce/

## Natural

Reduce cognitive and operational cost.

- Match the user's mental model and task sequence.
- Put controls near the object they affect.
- Prefer direct manipulation when it saves navigation or mental translation.
- Organize functions by context, not by implementation detail.
- Use familiar patterns for forms, filters, tables, navigation, and confirmation flows.

Design question: does this feel like the obvious next step for the user?

## Certain

Reduce collaboration entropy and maintenance cost.

- Prefer reusable tokens, components, and layout patterns over one-off styling.
- Keep visual rules simple enough for another contributor to extend.
- Use restraint: remove UI that does not clarify, guide, or complete the task.
- Preserve predictable spacing, state behavior, and component semantics.
- Abstract repeated patterns into named components or variants when the repo already supports that.

Design question: could another engineer extend this without guessing the visual logic?

## Meaningful

Serve the user's work mission.

- Start from what the user is trying to accomplish, not what the page can display.
- Make the primary action, current status, and next step unmistakable.
- Use hierarchy to separate decision data from supporting detail.
- Avoid decoration that competes with task-critical information.
- Write copy that helps users act, recover, compare, or decide.

Design question: what user mission does each visible element support?

## Growing

Expose capability progressively.

- Make first-run value clear without hiding advanced power forever.
- Use empty states, examples, defaults, and suggested next actions.
- Let expert users move faster through shortcuts, saved views, bulk actions, and dense modes.
- Introduce complexity in layers: summary, drill-down, configuration, automation.
- Keep upgrade paths discoverable without turning the product into a marketing page.

Design question: does the UI help both first-time and repeat users become more capable?

## Enterprise Surface Checklist

- Navigation: user always knows where they are.
- Data views: filters, sorting, selection, pagination, and empty states are explicit.
- Forms: labels, validation, required fields, errors, and save behavior are clear.
- Tables: columns serve comparison or action; avoid decorative columns.
- Drawers/modals: use when they preserve context; avoid stacking modals.
- Status: loading, success, partial failure, permission limits, and stale data states are visible.
- Internationalization: allow longer labels and values without breaking layout.
- Auditability: destructive, irreversible, or high-cost actions need confirmation and recovery paths.
