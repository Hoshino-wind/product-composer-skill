# UI Verification

## Principle

Verify public behavior and rendered quality against named acceptance checks in the target project. Every claim needs claim-specific evidence; a passing package check, a source file, or a screenshot proves only what it directly observes.

The active route owns task and content truth, the `DirectionContract` owns the visual thesis, and optional Modifier deltas own only their declared acceptance checks. Verification reports their results without creating a new design contract.

## Contents

- [Command discovery](#command-discovery)
- [Functional checks](#functional-checks)
- [State checks](#state-checks)
- [Accessibility checks](#accessibility-checks)
- [Target-device and localization checks](#target-device-and-localization-checks)
- [Visual checks](#visual-checks)
- [Concept parity](#concept-parity)
- [Scanner](#scanner)
- [Evidence classes](#evidence-classes)
- [Artifact maturity](#artifact-maturity)
- [Evidence report](#evidence-report)
- [Verification gaps](#verification-gaps)

## Command discovery

Discover the target project's own verification surface before running commands:

1. Read project instructions, package manifests, lockfiles, build files, scripts, and existing test configuration.
2. Select the smallest command that exercises the named acceptance check, then run the relevant full suite before completion.
3. Install dependencies only when they are missing, the project expects installation, and the action is in scope.
4. Start the actual application when a browser or device claim needs runtime evidence.
5. Record the exact command, environment, scenario, result, and evidence locator.

Do not substitute a Product Composer package test for target-project runtime verification.

Keep one repo-local command discovery record:

```text
- repo-local instructions: project instruction files and verification guidance inspected
- repo-local manifests: package, build, lock, workspace, and test configuration files inspected
- repo-local scripts: existing project scripts and command definitions inspected
- selected command: exact command chosen for the named acceptance check
- working directory: exact target-project directory where the command is run
- scenario and environment: named state, actor, data, viewport, platform, and relevant settings
- run status: exactly one of Pass, Fail, or Not run
- evidence locator: command output, trace, report, capture, or gap record
- Not run reason: for a required check, name the missing input or environment and prevented claim; omit non-applicable checks from this record
- decision: report Pass or Fail when the command ran; use Block only when a required check is Not run for missing input or environment
```

| Run status | Meaning | Required record | Allowed decision |
| --- | --- | --- | --- |
| Pass | The selected repo-local command ran and the named acceptance check was observed to pass. | Command, working directory, environment, output, and evidence locator. | Report Pass for that check only. |
| Fail | The selected repo-local command ran and the named acceptance check failed. | Command, failure output, observed result, and owning implementation or contract decision. | Report Fail; do not relabel a completed command as Block. |
| Not run | The required command or observation did not execute. | The missing input or environment, attempts made, and claims this prevents. | Use Block for the affected required check; never report Pass. |

## Functional checks

Verify the Functional delta through the public interface and record behavioral evidence for each applicable claim:

| Functional check | Required observation | Behavioral evidence | Failure owner |
| --- | --- | --- | --- |
| Workflow | Actor, trigger, user-visible transition, outcome, and recovery path. | Public-interface run, trace, or recording of the transition and resulting state. | Implementation owns a failed or missing workflow. |
| Data | The source of truth, representative read and write behavior, freshness, and honest fallback. | Observed request, response, stored result, refresh, and fallback as applicable. | Implementation owns false, stale, lost, or invented data behavior. |
| Permissions | The authorization boundary plus allowed, denied, disabled, and escalation behavior. | Runs for each applicable actor and permission outcome. | Implementation owns a missing or dishonest permission boundary. |
| Error recovery | Failure signal, retained input, retry or alternate path, and recovered state. | Triggered failure followed through the named recovery path. | Implementation owns a missing or failed recovery path. |
| Irreversible actions | Consequence, confirmation or approval, audit event, and rollback or explicit no-rollback rule. | Safe equivalent, controlled run, or an explicit verification gap for an unsafe action. | Implementation owns missing safeguards, audit, or rollback semantics. |

A component that renders is not proof that its workflow works. Observe the transition and resulting state.

## State checks

Exercise applicable loading, empty, error, permission, selected, disabled, success, sparse-data, dense-data, and stale-data states. For each state, verify:

- how the state is entered
- what the user can perceive and do
- whether data and authorization remain honest
- how the user exits or recovers
- whether the state preserves task priority and layout integrity

Do not fabricate fixtures or permissions that the target project cannot actually support without labeling the limitation.

## Accessibility checks

Verify the changed interaction with the methods available in the target project:

- complete the primary path by keyboard and inspect focus order
- confirm visible focus and focus restoration after modal, drawer, menu, or route transitions
- inspect semantic structure, names, roles, states, relationships, and announcements
- check each interactive pointer or touch target for the declared device and input scope
- confirm contrast for text, icons, controls, and state indicators
- exercise zoom, text resizing, and long content where applicable
- verify reduced motion preserves meaning, access, and completion
- confirm informative media has an equivalent and decorative media stays silent

Static markup inspection supports a structural claim; interaction evidence is still required for keyboard and focus behavior.

## Target-device and localization checks

Capture the same named task and critical states across the declared target-device scope. Responsive work normally includes desktop and mobile plus intermediate widths where mechanics change. An explicit PC-only contract requires only the named desktop width range and its pointer, wheel/trackpad, keyboard, resize, and reduced-motion behavior; do not create a mobile acceptance requirement.

Use real or representative long text, localization expansion, narrow labels, missing optional content, dense data, and sparse data. Verify that:

- task priority and first read survive reflow
- controls remain visible, reachable, and correctly grouped
- text does not clip, overlap, or depend on accidental truncation
- tables, charts, media, and proof objects retain their intended relationships
- action names and state language remain consistent
- direction and script constraints are honored for supported locales

Target-device adaptation may change mechanics; it must not silently change behavior or content truth.

For a complete route or website, verify the ordered content beats, region geometry, state progression, media graph, handoffs, and terminal action or endpoint on every declared target device. Record any region combined, removed, reordered, or mechanically changed and identify the Design Contract decision that permits it.

## Visual checks

Inspect rendered evidence for visual parity and baseline quality:

- the rendered scope matches opener, complete route, and multi-route website claims; one polished first viewport cannot pass a complete-experience claim
- every ordered content beat and required route is present, with region geometry, proof/action/orientation role, and media coverage matching the contract
- interactive regions preserve the accepted state progression, thresholds, entry, handoff, interruption, and exit relationships
- the intended first, second, and third reads remain clear
- the dominant silhouette and composition family match the accepted direction
- palette, type, spacing, depth, material, icon, media, and motion roles remain coherent
- text, controls, tables, charts, and assets do not clip, overlap, disappear, or load blank
- interactive states are visually distinguishable
- product surfaces remain useful and scan-friendly; brand surfaces still reveal real proof or offer
- every declared target device preserves the same product promise and content truth

Compare like with like: same scenario, content, state, viewport, theme, and relevant platform settings.

For a complete route or website, capture the full page and at least one rendered or behavioral observation for every interactive region and important handoff. A full-page screenshot may prove overall composition and approximate geometry, but does not prove sticky, snap, scroll-scrub, horizontal mapping, scene replacement, drag, spatial travel, route, interruption, or timing behavior. Record video, trace, or reproducible runtime observations for those claims. Reject repeated regions that differ only by crop, color, or copy when the contract promises meaningful state or content progression.

## Concept parity

Compare each implemented parity slice with the accepted `DirectionContract`, approved concept, and applicable Modifier delta:

- name the locked decision being checked
- name any adaptable mechanic used to satisfy engineering constraints
- identify the visible deviation and its decision owner
- attach rendered evidence for the same scenario and viewport
- attach behavioral evidence when the concept implies an interaction or state change

Color similarity alone is not concept parity. Preserve hierarchy, relationship, task meaning, and signature detail.

Keep this traceable record for every implemented parity slice:

```text
- locked decision: named DirectionContract field or approved Modifier relationship being preserved
- adaptable mechanic: engineering constraint, local mechanic used, and evidence that the locked relationship survives
- change ledger entry: baseline, implemented delta, reason, evidence locator, and owner for any material deviation
- parity slice: exact implemented workflow, state, component family, or viewport under comparison
- parity evidence: behavioral and rendered locators for the same scenario and same viewport
- decision owner: active route, DirectionContract, Modifier, Implementation, or user authority that owns the result
```

## Scanner

Run the bundled scanner only when the changed visual code is in its scope:

```bash
node scripts/ui-pattern-scan.mjs ./src
```

Review every result manually: scanner warnings are evidence prompts, not failures and not proof. Keep an intentional pattern when the active contract and rendered inspection justify it. Repair a warning only after identifying the affected acceptance check.

## Evidence classes

Map every acceptance check to exactly one evidence class.

| Evidence class | Proves | Does not prove | Required locator |
| --- | --- | --- | --- |
| behavioral evidence | An observed workflow, state transition, outcome, recovery, permission result, or runtime interaction. | Visual quality outside the observed behavior. | Test name, runtime trace, recording, or reproducible command and observation. |
| rendered evidence | The rendered result at a declared scenario, state, viewport, theme, and platform setting. | Workflow execution, data truth, or unobserved states. | Screenshot, video, browser or device capture, or inspected preview identifier. |
| structural evidence | Source, configuration, semantic declaration, manifest field, or static artifact structure. | Actual rendering, runtime behavior, or aesthetic quality. | File and line, configuration key, generated manifest, or inspection output. |
| provenance evidence | Asset origin, authorization, license, transformation, and declared semantic role. | Depicted factual truth, correct placement, or visual quality. | Source ledger, asset record, license or permission artifact, and local destination. |
| judgment evidence | A calibrated comparison against the named direction, acceptance criterion, or before/after repair axis. | Unrun behavior, unseen rendering, or unsupported factual claims. | Reviewer, criterion, compared artifacts, conclusion, and stated uncertainty. |
| verification gap | A specific acceptance check that cannot be run or observed with the available input or environment. | Satisfaction of the missing check. | Missing command, state, asset, permission, environment, or user decision plus impact. |

Screenshots do not prove workflow behavior.

Source inspection does not prove rendering.

Static strings do not prove aesthetic quality.

Inference is not evidence.

Runtime browser/device evidence belongs to the target project verification loop; package CI must not pretend it rendered a project it did not run.

## Artifact maturity

Verify the declared artifact target without promoting it beyond matching evidence.

Start validation-only with Verify plus the selected Surface owners: two active owners for Product or Brand and three for Hybrid. After recording surface claims and closing that window, open a sequential window of at most three with Verify, one necessary claim owner, and only the Surface owner needed to interpret that claim. Never create a verification gap merely to avoid a required owner; use sequential windows and carry the complete Design Contract forward.

A supplied static preview is validation evidence input, not Image work. In validation-only entry it does not activate the Image modifier or open image-concepts.md unless the user explicitly asks to generate, direct, or repair imagery. Inspect each material claim in its owning sequential window rather than forcing every owner into the initial Surface window.

Route and owner selection precede all modifier-owner loading. Do not open image-concepts.md merely to decide whether a supplied static preview counts as Image. Static preview plus validation-only intent resolves that decision before reference loading; open the Image owner later only for an explicit image-generation, direction, or repair request.

When a validation-only overclaim prompt includes an existing, missing, or inaccessible preview, choose Asset truth as the claim owner because source, availability, authorization, rights, and limitations affect the evidence claim. The maturity table already covers template and tested-golden packaging/runtime gaps; open implementation-fidelity.md in a later window only when an implementation-owned claim needs evidence beyond this table.

| Artifact target | Minimum verification | Forbidden overclaim |
| --- | --- | --- |
| recipe | Structural inspection of complete non-runnable direction metadata and acceptance checks. | Executable, rendered, or production-ready behavior. |
| preview | Rendered evidence with named scenario, state, viewport, and known limitations. | Workflow behavior claims or reusable production packaging. |
| runnable starter | Successful entrypoint plus behavioral evidence for the declared basic interaction. | Complete acceptance, golden stability, or template reuse. |
| tested golden | A named scenario whose applicable acceptance checks have runtime and rendered evidence. | Coverage of unnamed scenarios, environments, or inputs. |
| template | Manifest, entrypoint, replaceable-input contract, origin/license record, smoke test, and rendered evidence. | Production fitness for consumers and inputs that were not tested. |

Do not promote an artifact without matching evidence. A recipe or preview is not a production template.

## Evidence report

Create one row per applicable acceptance check. Replace the instructional row; do not leave it as evidence.

| Acceptance check | Evidence class | Evidence locator | Result | Notes |
| --- | --- | --- | --- | --- |
| [exact acceptance check] | One allowed evidence class. | Exact command, trace, capture, file, ledger, review, or missing-input locator. | pass, fail, or gap. | Scenario, environment, scope, and material limitation. |

### Readiness ladder

Report these lanes independently; use `pass`, `fail`, or `gap` for every applicable lane and omit only a genuinely non-applicable lane with a reason.

- `C0 contract-valid`: required records exist and structural, compiler, package, and applicable provenance checks pass. It does not approve aesthetics or runtime.
- `V1 visual-pass`: rendered plus judgment evidence in the consuming viewport passes full view, thumbnail, mounted crop, and blurred-label inspection for hierarchy, silhouette, media/type integration, depth, reference relationships, and the first handoff.
- `R2 runtime-pass`: the target app demonstrates entry, meaningful state change, handoff, reversal/interruption, equivalent keyboard or explicit controls, reduced motion, loading/failure fallback, and declared target-device behavior.

Structural or package tests can pass C0 only. Source inspection cannot pass V1; one screenshot cannot pass R2. A direction-only Explore result does not need a runtime lane, but an implemented interactive Hero is verified only when C0, V1, and R2 all pass. If V1 fails after C0 passes, report `structure passed, visual failed`; no lane may promote another.

Use one class per row. When a claim needs behavioral and rendered proof, split it into two acceptance checks so each result remains traceable.

## Verification gaps

Report a verification gap at the acceptance-check level:

```text
Verification gap:
- acceptance check:
- missing input or environment:
- commands or alternatives attempted:
- claims this prevents:
- safest next action:
```

A gap is an honest result, not a pass and not a reason to infer completion. Do not hide a blocked browser, unavailable state, missing permission, absent asset, or unrun command behind package CI or source inspection.
