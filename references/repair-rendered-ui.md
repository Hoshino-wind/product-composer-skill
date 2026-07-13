# Repair Rendered UI

## Principle

Repair the rendered surface from observed evidence. Preserve the owning route, accepted `DirectionContract`, functional behavior, and approved Modifier deltas unless the evidence proves that the contract itself must change.

This module operates only on a target UI surface. It does not revise Product Composer guidance, route definitions, reference modules, tests, or metadata. Choose the weakest visible failure, patch the smallest useful slice, and decide again from new evidence.

## Contents

- [Baseline evidence](#baseline-evidence)
- [Loop budget](#loop-budget)
- [Diagnosis](#diagnosis)
- [Repair axes](#repair-axes)
- [Patch one vertical slice](#patch-one-vertical-slice)
- [Verification](#verification)
- [Decision protocol](#decision-protocol)
- [Stop conditions](#stop-conditions)
- [Output shape](#output-shape)

## Baseline evidence

Before opening any Stage or Gate owner or searching the workspace, determine whether the request supplies both task-scoped rendered evidence and a behavioral baseline. If either input is absent, stop owner selection immediately: do not search the checkout or temporary directories for substitute evidence, and Block from the Repair / Surface owners alone.

Capture this record before patching:

```text
- target project: exact local project and changed surface
- scenario: named task, state, content, and actor
- viewport: dimensions, device class, and input mode
- rendered evidence: screenshot, recording, or inspected runtime locator
- behavioral baseline: observed workflow result and its locator
- known gap: missing state, asset, command, environment, or acceptance evidence
- active contract: route owner, DirectionContract revision, and Modifier deltas
```

Use the actual rendered result as the visual baseline. Source inspection may explain a symptom, but it does not show what the user saw.

Until both task-scoped rendered evidence and a behavioral baseline exist, select no repair axis, not even provisionally or tentatively; make no diagnosis and authorize no patch boundary. Block and name the missing evidence, the claims it prevents, and the safest next action.

This missing-baseline Block stays inside Repair plus the selected Surface owner set: two active owners for Product or Brand and three for Hybrid. Do not open Verify when the baseline is missing and no patch or new evidence exists; record verification as a later gap that opens only after the required baseline permits Repair work.

## Loop budget

Choose one repair axis per loop and set the budget before editing:

- normal polish: at most two evidence-producing repairs
- substantial visual correction: at most three evidence-producing repairs
- risky production surface: one repair before re-evaluating risk

The user may set a different budget. End early when the contract is satisfied, when the contract must change, or when verification cannot run. Do not spend a loop on speculative preference without new evidence.

## Diagnosis

Compare the named scenario against its acceptance checks and active direction. Diagnose only what the evidence exposes:

- first, second, and third read
- task and state clarity
- product specificity and proof truth
- dominant proportion and density
- text fit, localization, and responsive continuity
- asset role and provenance honesty
- implementation fidelity to hierarchy, palette, type, material, and motion roles
- keyboard, focus, semantics, touch, contrast, and reduced-motion behavior

Name the weakest applicable dimension and point to its evidence locator. A scanner warning or code pattern may prompt inspection; neither is a diagnosis by itself.

## Repair axes

Select exactly one keyed row for the current loop.

| Repair axis | Diagnose | Patch boundary | Verify with |
| --- | --- | --- | --- |
| shape | The dominant hierarchy, work object, or section order hides the user mission. | Change one dominant form or relationship without inventing a new route. | Before/after rendered evidence plus primary-task visibility. |
| arrange | Grouping, alignment, spacing, or reading order obscures the intended scan path. | Regroup or reposition one vertical slice using the existing component and token system. | Declared viewport comparison and keyboard focus-order check when order changes. |
| typeset | Type roles, scale, measure, weight, density, or overflow weaken hierarchy or comprehension. | Adjust the affected type role and its real-content containers. | Desktop, mobile, and long-text rendered evidence. |
| colorize | Palette roles, contrast, semantic color, or one-hue drift weakens meaning. | Correct named color roles without adding an unrelated palette. | Rendered comparison plus applicable contrast evidence. |
| distill | Redundant copy, panels, chips, badges, or controls compete with the task. | Remove or combine only elements unsupported by the user mission. | Before/after task visibility and preserved workflow behavior. |
| harden | Loading, empty, error, permission, disabled, sparse, dense, or localized states break the surface. | Repair one state family through its real data and interaction path. | Behavioral state evidence and rendered edge-state evidence. |
| asset | Missing, fake, decorative, low-quality, or mis-role media weakens proof or composition. | Replace or re-role one asset with provenance, authorization, fallback, and text alternative intact. | Asset locator, provenance record, and rendered placement. |
| motion | Motion obscures causality, delays access, breaks continuity, or decorates without purpose. | Repair one transition or remove it while preserving static comprehension. | Runtime motion evidence, performance observation, and reduced motion result. |

## Patch one vertical slice

Patch the smallest end-to-end slice that can prove the selected repair: one primary work object, first viewport, repeated component family, state group, or responsive breakpoint.

Preserve local routes, components, tokens, data shapes, workflow transitions, and accepted decisions outside that slice. When the evidence requires a locked decision to change, stop patching and use the Escalate decision. Do not hide a functional defect with visual polish.

Complete this causal record in order. The entry functional gate runs before any visual patch; a failed gate leaves Repair ownership immediately.

```text
- entry functional gate: pass with behavioral evidence before visual repair; otherwise Handoff to Implementation with that evidence
- selected repair axis: exactly one keyed Repair axis supported by the rendered baseline
- bounded vertical slice: one named end-to-end slice inside the selected axis
- baseline scenario: named task, actor, content, and state from the rendered baseline
- baseline viewport: exact dimensions, device class, input mode, theme, and platform settings
- rerun scenario: same as baseline scenario after the bounded patch
- rerun viewport: same as baseline viewport after the bounded patch
- evidence: new behavioral and rendered evidence locators plus any remaining defect
- decision: exactly one of Continue, Stop, Escalate, Block, or Handoff
```

## Verification

After the patch, rerun the named scenario and compare new evidence with the baseline on the selected axis:

1. Run the smallest relevant behavioral command and observe the changed workflow or state.
2. Capture the same viewport, content, and state used by the rendered baseline.
3. Check the affected desktop, mobile, long-text, keyboard, focus, touch, and reduced-motion conditions.
4. Confirm that unrelated locked decisions and functional behavior did not drift.
5. Record the new evidence locator and any remaining gap.

Re-run a scanner only when the changed visual code could affect its warnings. Inspect warnings manually.

| Rerun relationship | Baseline | Required match | New evidence |
| --- | --- | --- | --- |
| scenario | Named task, actor, content, state, and acceptance check. | Rerun the same named scenario after the bounded patch. | Observed outcome and remaining defect for that scenario. |
| viewport | Dimensions, device class, input mode, theme, and platform settings. | Rerun the same viewport and settings used by the baseline. | Capture locator with the unchanged viewport metadata. |
| behavior | Entry functional result and affected workflow or state. | Preserve the passing baseline behavior and rerun the affected transition. | New behavioral evidence for the observed post-patch result. |
| rendered surface | Baseline capture for the selected repair axis. | Compare the same slice, state, and visual conditions. | New rendered evidence for the selected axis and remaining defect. |

Any functional, data, permission, or accessibility regression introduced by the current bounded slice triggers rollback before decision selection. Stop further Repair work, revert that slice, and rerun the entry functional baseline. Complete the Rollback record before selecting a decision.

```text
- regression observed: post-patch functional, data, permission, or accessibility regression introduced by the current bounded slice
- affected behavior: failed acceptance check and locator from the same functional baseline that passed at entry
- patch reverted: stop Repair immediately and revert the current bounded slice before any further patch
- baseline rerun: run the same functional baseline, scenario, actor, data, environment, and command after rollback
- baseline restored: record yes or no from the rerun; inference is not restoration evidence
- failure evidence: regression command, output, trace, state, scenario, and affected behavior locator
- rollback evidence: revert diff or commit plus the baseline rerun command, output, and evidence locator
- next owner or decision: restored and repair budget remains -> Continue; restored and repair budget is exhausted -> Handoff; cannot revert or restore -> Handoff to Implementation or responsible owner
```

## Decision protocol

End every entry gate or verified repair with exactly one line:

```text
Continue: [next weakest axis] because [new evidence]
Stop: contract satisfied because [evidence]
Escalate: design contract must change because [reason]
Block: verification cannot run because [missing input or environment]
Handoff: [Implementation or responsible owner] because [functional baseline failed, post-patch baseline was not restored, or repair budget exhausted with verified defect remaining]
```

Select exactly one decision; the five states are mutually exclusive and exhaustive for Repair.

| Decision | Select when | Required record | Forbidden claim |
| --- | --- | --- | --- |
| Continue | The entry gate passed, verification ran, a verified surface defect remains, the design contract stands, repair budget remains, and no post-patch regression is active; if a regression occurred, the current slice was reverted and the same functional baseline was restored. | New evidence plus the next weakest axis inside the remaining budget; after rollback, include restoration evidence. | Continue when the budget is exhausted, without new evidence, with an unreverted regression, or before the baseline is restored. |
| Stop | The contract is satisfied and no verified defect or post-patch regression remains in the applicable acceptance checks. | Evidence locators for the satisfied contract. | Success while any remaining defect or regression is known. |
| Escalate | Evidence shows the design contract must change before the surface can satisfy it. | The locked decision, reason, evidence, and decision owner. | Missing verification, functional implementation failure, or budget exhaustion. |
| Block | Required verification cannot run because of a missing input or environment. | The missing input or environment, attempts, prevented claims, and safest next action. | A failed check that ran, a remaining verified defect, or an exhausted budget. |
| Handoff | The entry functional baseline fails; a post-patch regression cannot be reverted or the same functional baseline cannot be restored; or verification ran, the repair budget is exhausted, a verified surface defect remains, and neither contract change nor missing environment applies. | Handoff to Implementation with behavioral evidence for an entry failure; for a regression preserve failure evidence, rollback evidence, baseline rerun, affected behavior, and the responsible owner; otherwise preserve the remaining defect for the responsible owner for budget or authority. | Contract satisfaction, speculative success, or additional unapproved Repair. |

Evaluate the predicates in order. Use Block when required verification cannot run. If the entry baseline runs and fails, use Handoff. A post-patch regression suspends normal decision selection: revert the current slice and rerun the same baseline first. When rollback restores the baseline, the original surface defect remains; use Continue when budget remains or Handoff when the budget is exhausted. When the patch cannot be reverted or the rerun does not restore the baseline, use Handoff to Implementation or the responsible owner. Otherwise, after a verified repair, use Escalate for a required contract change, Stop for a satisfied contract, Continue for a remaining defect within budget, and Handoff for a remaining verified defect after budget exhaustion. Do not combine decisions.

## Stop conditions

Apply Continue, Stop, Escalate, and Block only under their Decision protocol predicates. Use Handoff for these three non-Repair ownership cases:

| Handoff case | Required owner | Evidence to preserve | Must not claim |
| --- | --- | --- | --- |
| entry functional baseline fails | Implementation owns the failed workflow, data, permission, recovery, or irreversible-action behavior. | Behavioral evidence, failed acceptance check, scenario, environment, and observed outcome. | That visual repair started, the contract is satisfied, or verification was blocked. |
| post-patch regression not restored | Implementation or responsible owner owns a patch that cannot be reverted or a functional, data, permission, or accessibility baseline that the rerun did not restore. | Preserve failure evidence, rollback evidence, affected behavior, patch state, and baseline rerun result. | Continue Repair, contract satisfaction, or a restored baseline. |
| budget exhausted with verified surface defect | The responsible owner for budget or authority decides whether another repair is authorized. | Baseline and post-patch evidence, selected axis, patches attempted, consumed budget, and remaining defect. | Continue, success, contract satisfaction, contract change, or missing verification. |

Handoff is terminal for the current Repair run. Stop editing, preserve the evidence and remaining defect, and do not silently expand scope.

## Output shape

Use this compact record:

```text
Repair baseline:
- target project, scenario, viewport:
- rendered evidence and behavioral baseline:
- active contract and known gap:
Diagnosis:
- weakest axis and evidence:
Patch:
- vertical slice and preserved boundaries:
Verification:
- commands, observations, and evidence locators:
- rollback record and baseline restoration evidence, when a regression occurred:
Decision:
- Continue | Stop | Escalate | Block | Handoff line:
- handoff owner and remaining defect, when applicable:
```

Keep the report shorter than the repair work. Evidence locators carry the claim; commentary does not.
