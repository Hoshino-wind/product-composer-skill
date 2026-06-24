# Interaction Grammar

Use this when a traditional page, table, form, or dashboard would merely display a system instead of changing how the user controls it.

## First Principle

Design the relationship between human intent and system agency before arranging components.

Interaction is not the same as gesture. Do not reduce interaction design to dragging, clicking, swiping, sliders, or playful controls. Those are input mechanics. Interaction design is the system of intent, response, agency, feedback, time, trust, and commitment.

Ask:

- What does the user command?
- What does the system infer?
- What can be simulated before commitment?
- What can be reversed?
- What must be explained?
- Where does time, history, uncertainty, and provenance appear?
- How does the user shift autonomy?
- What relationship does the user feel: guided, in control, invited, challenged, reassured, or empowered?
- Is a physical gesture truly needed, or is the real interaction a decision, comparison, preview, negotiation, or commitment?

Use literal gestures only when they are real product capabilities and improve understanding. Avoid fake affordances like "drag to..." in static marketing mockups unless the page contains an actual interactive demo.

## Core Primitives

### Relationship Model

Name the human-system relationship before choosing controls.

Examples:
- critic and craftsperson
- pilot and autopilot
- editor and assistant
- planner and simulator
- buyer and trusted advisor
- creator and instrument

The relationship model should determine the UI's posture:
- who initiates
- who suggests
- who decides
- who explains
- who commits
- who can reverse

Avoid: choosing a novel control before knowing the relationship it serves.

### Intent Surface

The primary surface lets users express goals, constraints, preferences, and unacceptable outcomes.

- Show the interpreted intent back to the user.
- Turn vague goals into editable structure.
- Keep constraints visible while the system works.
- Let users pin, relax, or strengthen constraints.

Avoid: a chat box as the only control surface when the task has durable state.

### Living Object

The main object is alive: it changes over time, carries state, and can be manipulated directly.

Examples:
- workflow
- plan
- agent run
- creative scene
- investigation
- deployment
- policy
- dataset transformation

Capabilities:
- pause
- branch
- replay
- annotate
- compare
- merge
- revert
- resume from checkpoint

Avoid: reducing living objects to table rows unless the table is only an overview.

### Agency Dial

Represent control as a spectrum, not a binary.

Example levels:
- manual
- assisted
- suggested
- supervised auto
- autonomous with guardrails

The dial should explain what changes at each level:
- who decides
- who executes
- what requires approval
- what can be undone
- what is logged

Avoid: a vague "AI mode" toggle.

### Simulation Before Commit

High-impact actions should produce a preview of likely effects before execution.

Show:
- expected changes
- affected objects
- confidence and uncertainty
- reversible and irreversible parts
- required approvals
- rollback plan

Avoid: asking users to approve an opaque action.

### Trace Timeline

Make the system's reasoning and work inspectable over time.

Use a timeline for:
- intent interpretation
- tool calls
- evidence gathered
- decisions made
- uncertainty discovered
- user approvals
- failures and retries
- final commit

Avoid: hiding important agency in raw logs or after-the-fact audit tables.

### Negotiated UI

The interface should ask for the smallest missing decision at the right moment.

Patterns:
- "I can proceed automatically for A and C; B needs your boundary."
- "This action is safe to simulate, but not safe to commit."
- "Two interpretations are possible; choose the operating assumption."
- "The plan is blocked by a missing permission. Grant, skip, or replace the step."

Avoid: interrupting users with generic confirmations.

### Command Canvas

Use a persistent spatial workspace when the task has multiple active objects, plans, traces, or alternatives.

Canvas regions may include:
- intent nucleus
- active living objects
- timeline spine
- simulation shadow
- autonomy controls
- evidence tray
- risk ledger
- commit rail

Avoid: a blank infinite canvas with no grammar or object behavior.

## Design Method

1. Name the relationship model.
2. Name the living object.
3. Define its states and transitions.
4. Define how the user changes autonomy.
5. Define what the system must explain.
6. Define the simulation and commit boundary.
7. Define how history and reversibility are represented.
8. Only then choose visual layout, components, and any physical input mechanics.

## Visual Guidance

- Make new interaction primitives legible through spatial behavior, labels, and consistent state language.
- Use familiar micro-controls inside unfamiliar macro-structures.
- Keep frontier interfaces calm; novelty should come from the control model, not from visual chaos.
- Use motion conceptually: reveal causality, branching, replay, and commitment.
- Treat uncertainty as first-class information, not as an error state.
- Let interaction be felt through cause, consequence, and control. Do not rely on decorative hand, drag, or swipe metaphors to signal novelty.

## Anti-Defaults

Do not start with:

- navigation plus dashboard
- chat plus side panel
- table plus details drawer
- cards plus status chips
- a prompt box on top of a normal app

These can appear later, but only after the interaction grammar demands them.
