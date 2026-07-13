# Product Composer Skill

English | [Chinese](README.zh-CN.md)

## Positioning

Product Composer is a Codex skill that gives UI work an explicit aesthetic and creative core. It derives a traceable visual thesis, directs coherent image worlds and asset families, compiles inspectable generation prompts, preserves accepted decisions during implementation, repairs rendered UI from evidence, and validates visual parity or artifact maturity.

Runtime authority: root `SKILL.md` only.

This README explains the package without redefining its route contract.

## When To Use

Use Product Composer when visual direction materially affects the result:

- create a new product, brand, or hybrid surface
- substantially redesign an existing interface
- derive a positive visual direction from real product, audience, content, and reference signals
- direct a coherent image world or asset family, then compare candidates in target context
- translate an accepted UI or image reference without losing its causal design rules
- implement without losing locked behavior or visual decisions
- repair a rendered result from observed evidence
- validate visual parity or an artifact-maturity claim

Do not activate it for routine UI construction that follows an established system without a material art-direction or fidelity decision, a small mechanical edit, a non-visual engineering task, document translation, or a UX audit that does not request redesign.

## Runtime Model

The root skill selects one Phase and one Surface, adds only behavior-changing Modifiers, and opens the smallest owner-reference window that can do the work. Every owner reads and updates one shared Design Contract. Direction-only Explore stops at an accepted direction. An implementation-authorized new UI selects Implement, establishes a selected or inferred DirectionContract and completes the Functional delta before the first slice, and then builds. The validation-only Explore path reports evidence and verification gaps without mutation. Repair changes one evidence-backed axis at a time, and Verify maps each claim to matching evidence.

The creative core turns source signals into visible consequences across layout, type, image, material, and motion. Image work adds an Image World Bible, chooses the appropriate medium, locks family anchors, compiles a deterministic prompt contract, compares bounded candidate sets, and retakes only the diagnosed causal variable. It never forces image generation when imagery is not material to the result.

For brand, landing, SaaS, portfolio, commerce, and experimental websites, Product Composer separates the opener from the complete route and multi-route site. A hero may contain multiple beats, regions, media, and interaction states, but it is not automatically one full-screen section or the whole website. Content beats, region geometry, scroll choreography, and media form independent many-to-many relationships; explicit PC-only work does not inherit a mobile requirement.

The full owner matrix, reference budget, exception, phase outcomes, and hard gates live only in [`SKILL.md`](SKILL.md). Executable discovery and initial-window expectations are linked from the package map below.

## What The Skill Preserves

Product Composer preserves product correctness, local conventions, content and asset truth, the selected aesthetic stance and visual thesis, image-world and asset-family continuity, locked implementation decisions, accessible state behavior, and traceable verification. It separates artifact-maturity labels so evidence cannot be promoted by wording alone:

- **recipe**: complete non-runnable direction metadata and acceptance checks
- **preview**: a rendered view for a named scenario, state, and viewport, with limitations stated
- **runnable starter**: an executable entrypoint with behavioral evidence for its declared basic interaction
- **tested golden**: a named scenario whose applicable behavioral and rendered checks have passed
- **template**: a reusable package with a manifest, entrypoint, replaceable-input contract, provenance, smoke test, and rendered evidence

These are claim levels, not a list of artifacts shipped by this repository. The package does not claim to include a runnable starter, tested golden, or production template.

## Package Map

- [`SKILL.md`](SKILL.md) is the only runtime authority.
- [`references/`](references) contains the focused runtime-owner documents indexed by `SKILL.md`.
- [`scripts/compile-image-prompt.py`](scripts/compile-image-prompt.py) validates an asset-family contract and emits deterministic ordered prompt sections without adding a hidden style preset.
- [`scripts/ui-pattern-scan.mjs`](scripts/ui-pattern-scan.mjs) provides the optional deterministic scanner.
- [`tests/`](tests) contains structural, provenance, integrity, and scanner checks.
- [`evals/discovery-scenarios.md`](evals/discovery-scenarios.md) and [`evals/routing-scenarios.md`](evals/routing-scenarios.md) make activation and reference-window expectations reviewable.
- [`evals/source-ledger.json`](evals/source-ledger.json) is repository provenance evidence; it is not a runtime reference.
- [`examples/scenarios/product-composer-routing.md`](examples/scenarios/product-composer-routing.md) shows two compact routing examples without copying the full route table.

## Scanner

Run the scanner against a project or source directory when visual code may contain known generic-default signals:

```bash
node scripts/ui-pattern-scan.mjs ./src
```

The default JSON findings are evidence prompts, not automatic failures. Use `--strict` only when warnings should make the command fail, then confirm every finding against the active contract and rendered result.

## Validation

From the repository root, run:

```bash
python3 -B "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$PWD"
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/test_scanner.mjs
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
