# Frontier Interactions

## Principle

Design the relationship between human intent and system agency before choosing controls. This optional Modifier consumes the active `DirectionContract` and does not create a secondary route hierarchy; the selected product or brand route still owns task priority, content, and composition.

Load this module only when the experience includes durable intent, delegated action, changing autonomy, simulation, consequential commitment, or an inspectable history. A novel gesture, chat box, or futuristic visual treatment alone is not frontier interaction.

## Contents

- [User intent](#user-intent)
- [System agency](#system-agency)
- [Control transfer](#control-transfer)
- [Time model](#time-model)
- [Object model](#object-model)
- [Commitment model](#commitment-model)
- [Simulation before commit](#simulation-before-commit)
- [Trace and audit](#trace-and-audit)
- [Uncertainty](#uncertainty)
- [Acceptance checks](#acceptance-checks)

## User intent

Represent the user's mission, constraints, preferences, and unacceptable outcomes as durable, editable state. Reflect the interpreted intent back before the system acts. Let the user pin, relax, replace, or reject an assumption without restarting the whole task.

Use an intent surface rather than treating a chat transcript as the only source of truth:

```text
Intent
- mission:
- success evidence:
- constraints:
- unacceptable outcomes:
- delegated decisions:
- decisions reserved for the user:
```

Keep the current interpretation visible beside the object it governs. If intent changes, show which plan, preview, approval, or running action becomes stale.

## System agency

Name the human-system relationship and assign responsibility explicitly:

- who initiates the work
- what the system may infer or suggest
- who decides among alternatives
- who executes each action
- who explains evidence, uncertainty, and failure
- who may pause, reverse, or escalate

For each delegated capability, keep one reviewable agency record:

```text
Agency record
- actor:
- may decide:
- may execute:
- approval trigger:
- explanation duty:
- escalation path:
```

The record binds a capability to its responsible actor and prevents a broad autonomy label from hiding different decision, execution, and approval rights.

Agency must attach to a real capability and policy. Do not use an `AI mode` toggle that changes visual mood without changing decision rights, execution rights, approval boundaries, or trace detail.

## Control transfer

Treat Control transfer as a legible contract, not a binary switch. Use only the levels the product genuinely supports and describe their consequences in the interface.

| Control level | Who decides | Who executes | Approval | Reversibility | Audit |
| --- | --- | --- | --- | --- | --- |
| manual | user | user | each action is explicit | user-controlled undo where supported | record committed changes |
| assisted | user after suggestions | user or system on command | approve selected suggestion | preview and undo supported actions | record suggestion and choice |
| supervised | system within a plan | system | pause at named boundaries | checkpoints and rollback by policy | record decisions, tools, and approvals |
| autonomous | system within explicit guardrails | system | escalate exceptions and high-impact actions | policy states what can be reverted | continuous trace with accountable owner |

Changing level must reveal what changes in decision authority, execution, approval, reversibility, and logging before the transfer takes effect. A user must be able to lower autonomy without losing the current object or its history.

## Time model

Expose time when it changes meaning. Distinguish:

- past: evidence gathered, decisions made, approvals, retries, and committed effects
- present: current state, active step, owner, elapsed work, and safe pause point
- future: planned steps, dependencies, predicted effects, deadlines, and approval gates

Record every state change with temporal and causal identity:

```text
Transition record
- prior state:
- transition trigger:
- actor:
- observed at:
- next state:
- refresh or expiry:
```

Represent queued, running, waiting, paused, failed, completed, and stale as different states. Never present an estimate as elapsed fact or a planned action as completed work. When external state can change, show when evidence was observed and when it should be refreshed.

## Object model

Choose one living object that carries the interaction: a plan, agent run, investigation, workflow, scene, deployment, policy, or transformation. Define its identity, owner, state, provenance, allowed transitions, and terminal conditions before laying out controls.

Map every operation to an allowed transition. Treat the object's state source of truth as the basis for enabling controls and emitting a trace event; a visual state that cannot be reconciled with that source is stale, not authoritative.

```text
Object operation record
- operation:
- state source:
- allowed transition:
- trace event:
```

Expose only valid operations for the current state, such as pause, branch, compare, annotate, replay, resume, merge, or revert. Preserve identity and history across those transitions. Use a table only as an overview when row treatment would hide the object's state, causality, or controllability.

## Commitment model

Classify a proposed effect by consequence and irreversibility. The higher the consequence or the weaker the reversibility, the stronger the preview, approval, authorization, and audit evidence must be.

Define for each committing action:

- effect scope and affected owner
- reversible, compensatable, or irreversible status
- approval and authorization requirement
- checkpoint, undo window, or recovery path
- evidence required before commit
- audit event emitted after commit

Do not use one generic confirmation dialog for materially different commitment classes. Low-risk reversible edits may commit directly; financial, public, destructive, permission-changing, or externally messaged actions need an explicit boundary.

## Simulation before commit

For high-impact or uncertain actions, show a simulation before commit. The preview must state:

- expected changes and affected objects
- confidence, assumptions, and unresolved uncertainty
- reversible and irreversible parts
- required approvals and missing authorization
- side effects, dependencies, and timing
- rollback plan or an explicit statement that rollback is unavailable

Simulation is evidence, not theater. Mark predicted output as predicted, show what input and version produced it, and invalidate it when governing intent, data, permissions, or external state changes.

## Trace and audit

Keep a human-readable trace of intent interpretation, evidence, tool use, system proposals, user decisions, approvals, failures, retries, and final effects. Link each event to its actor, time, governed object, and resulting state.

For every consequential step, preserve one causal chain from input evidence to decision to action to observed effect. Keep predicted effects marked separately until observation confirms or contradicts them.

```text
Trace link
- input evidence:
- decision:
- action:
- observed effect:
```

Use the trace for active control as well as after-the-fact audit: users should be able to inspect why the system is waiting, which evidence supported a decision, and where it can safely resume or branch. Raw logs may support diagnosis but must not replace an understandable causal record.

## Uncertainty

Treat uncertainty as first-class state. Separate:

- confidence: how strongly current evidence supports an inference
- assumption: a provisional choice the user can inspect or change
- unknown: missing evidence that prevents a reliable claim
- resolution: the next check, user decision, permission, or observation that would reduce uncertainty

Uncertainty must change behavior. It may narrow system agency, require simulation, add an approval gate, defer commitment, or block the action. Do not convert missing evidence into confident copy or hide it in a generic warning.

## Acceptance checks

- User intent is editable, reflected back, and linked to governed objects.
- System agency names who decides, executes, explains, approves, and reverses.
- Every Control transfer explains its effect before it takes effect.
- Past, present, planned, predicted, and committed states are visibly distinct.
- The living object has valid transitions and retains history across them.
- High-impact action is simulated before commit and shows recovery limits.
- The trace supports both active inspection and later audit.
- Uncertainty changes agency or commitment instead of becoming decorative copy.
