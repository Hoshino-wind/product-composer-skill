# Design Memory Consistency

Use this for existing projects, multi-screen work, repeated edits, design systems, long-running threads, or any task where spacing, color, depth, component behavior, or visual language could drift.

## Principle

Make decisions once, then reuse them. UI generated across turns should feel like one system, not a fresh invention each time.

## Read Existing Memory

Before designing, inspect available local memory:

- `DESIGN.md`
- token files
- component docs
- Storybook or examples
- screenshots in the repo
- nearby screens and routes
- `.product-composer/design-system.md`
- previous accepted concepts in the working folder

If no memory exists, infer a compact design system from the current screen before changing it.

## Memory Snapshot

When a task creates or changes a visual system, keep a compact snapshot in notes or a local project file when useful:

```text
Design memory:
- Surface register:
- Palette roles:
- Type roles:
- Spacing scale:
- Radius scale:
- Depth model:
- Component families:
- State behavior:
- Motion rules:
- Media treatment:
- Refusals:
```

Do not create a new project file unless it helps future work or the user asked for durable design memory.

## Drift Checks

Before finalizing a change, compare against memory:

- Did button height drift?
- Did card padding drift?
- Did radius and shadow drift?
- Did muted text become too faint?
- Did table density change without reason?
- Did empty/error/loading states use a different tone?
- Did a new accent color appear without a role?
- Did a one-off component replace an existing family?
- Did a marketing section enter an operational app surface?

Fix drift unless the task is explicitly a redesign.

## Consistency Rules

- Extend existing tokens before inventing new ones.
- Name new tokens or component variants only when they will be reused.
- Keep depth models consistent: flat, raised, inset, glass, paper, spatial, or instrument.
- Keep spacing on a small scale; avoid arbitrary one-off values.
- Keep state behavior consistent across similar controls.
- For multi-screen flows, repeat navigation, action placement, and feedback patterns.

## Redesign Exception

If redesign is requested, separate old system from new system:

- what remains
- what changes
- what gets deprecated
- what migration path is needed

Do not mix old and new styles accidentally.
