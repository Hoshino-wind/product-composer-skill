# Design Review Output

Use this when the user asks to review, audit, critique, compare, or diagnose a UI surface, screenshot, PR, implementation, image mockup, or design direction.

The review should be direct, prioritized, and actionable. Do not bury problems under praise. Do not redesign the whole UI unless the user asks for a redesign.

## Output Shape

Start with:

```text
Findings
```

Then list issues in this order:

1. Blocking
2. Major
3. Minor
4. Polish
5. Verification

Use only the severities that apply. If there are no issues at a severity, omit that severity.

Each finding should follow this structure:

```text
[Severity] Area - short finding
Why it matters: ...
What to change: ...
```

Use line/file references when reviewing code. Use screen region names when reviewing screenshots or generated images.

## Severity Meanings

Blocking:

- User cannot complete the primary task.
- Layout breaks, overlaps, clips, or hides critical content.
- Accessibility failure prevents keyboard, screen reader, or mobile use.
- Implemented UI contradicts an accepted concept, Figma frame, screenshot, or local design system in a high-impact way.

Major:

- Primary hierarchy is unclear.
- Competing actions or content zones dilute the main job.
- Color, type, spacing, or depth breaks the stated design direction.
- The UI reads as a generic template rather than a product-specific surface.
- Missing loading, empty, error, disabled, selected, or active states in an important flow.

Minor:

- Inconsistent radius, spacing, icon style, border, shadow, or copy tone.
- Non-critical responsive issue.
- Small mismatch with a reference that does not change the main task.
- An avoidable one-off style should become a token or component if repeated.

Polish:

- Better optical alignment, text wrapping, tabular numbers, hover feel, focus ring, or reduced-motion behavior.
- More specific asset treatment, copy, or micro-interaction would raise perceived quality.
- The direction works but one detail still feels stock or unfinished.

Verification:

- Call out what still needs rendered checking: desktop, mobile, keyboard, reduced motion, screenshot parity, data states, asset loading, or text overflow.
- If a check was not run, say it was not run.

## Review Dimensions

Check these dimensions before writing findings:

- Task: primary job, action hierarchy, progressive disclosure, state visibility.
- Composition: focal point, proportion, rhythm, density, first viewport, repeated sections.
- Visual craft: typography, palette roles, spacing, radius, depth, material, motion.
- Specificity: domain-native motifs, asset use, signature element, anti-generic behavior.
- System fit: local components, tokens, naming, repeated patterns, dark/light behavior.
- Accessibility: keyboard, focus, labels, contrast, touch targets, reduced motion.
- Responsiveness: mobile layout, text wrapping, stable dimensions, scroll behavior.
- Content: headings, labels, empty/error text, action verbs, trust/proof strings.
- Fidelity: accepted concept, screenshot, Figma frame, reference DNA, or design memory.

## No-Issue Output

If no material problems are found, say:

```text
No blocking or major UI issues found.
```

Then list remaining risks or checks that were not run. Keep the summary short.

## Common Review Mistakes

- Turning every critique into a redesign proposal.
- Listing generic advice without pointing to a visible symptom.
- Praising before naming the issues.
- Treating visual taste as separate from task completion.
- Calling something polished without checking responsive and state behavior.
