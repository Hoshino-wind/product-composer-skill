import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


HEADINGS = {
    "frontier-interactions.md": [
        "Principle", "Contents", "User intent", "System agency",
        "Control transfer", "Time model", "Object model",
        "Commitment model", "Simulation before commit", "Trace and audit",
        "Uncertainty", "Acceptance checks",
    ],
    "asset-context.md": [
        "Principle", "Contents", "Context questions", "Asset inventory",
        "Role ledger", "Asset-before-IA gate", "Asset system coverage", "Proof rules",
        "Atmosphere/support rules", "Placeholder rules", "Media treatment",
        "Cultural and factual provenance", "Acceptance checks",
    ],
    "image-concepts.md": [
        "Principle", "Contents", "Image eligibility", "Image World Bible",
        "Medium Router", "Asset Family Contract", "Prompt contract", "Candidate Protocol",
        "Interface and interaction boundary", "Composition families", "Visible text",
        "Aesthetic repair", "Anti-convergence", "Result inspection", "Retake Loop",
        "Direction-to-asset-pack", "Asset handoff", "Failure signs",
    ],
    "chinese-aesthetic.md": [
        "Principle", "Contents", "Source contract", "Design grammar",
        "Direction contract", "Modern product translation",
        "Brand translation", "Palette and type", "Image prompt delta",
        "Anti-stereotype rules", "Repair", "Acceptance checks",
    ],
    "react-motion.md": [
        "Principle", "Contents", "Eligibility", "Motion role map",
        "Asset-derived choreography", "Region And Scroll Choreography", "Component selection", "Static-first integration", "Performance",
        "Reduced motion", "Acceptance checks",
    ],
    "reference-translation.md": [
        "Principle", "Contents", "First read", "System read",
        "Temporal read", "Media ecology", "Page trace", "Translation read",
        "Provenance record", "DNA contract",
        "Locked/adaptable decisions", "Conflict priority",
        "Copying boundary", "Acceptance checks",
    ],
}


class ModifierReferenceTests(unittest.TestCase):
    def parse_h2_sections(self, text):
        sections = []
        current_title = None
        current_lines = []
        fence_marker = None

        for line in text.splitlines():
            fence = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
            if fence:
                marker = fence.group(1)[0]
                if fence_marker is None:
                    fence_marker = marker
                elif fence_marker == marker:
                    fence_marker = None
                if current_title is not None:
                    current_lines.append(line)
                continue

            heading = None
            if fence_marker is None:
                heading = re.match(r"^ {0,3}##[ \t]+(.+?)\s*$", line)

            if heading:
                if current_title is not None:
                    sections.append((current_title, "\n".join(current_lines)))
                current_title = heading.group(1)
                current_lines = []
            elif current_title is not None:
                current_lines.append(line)

        if current_title is not None:
            sections.append((current_title, "\n".join(current_lines)))
        return sections

    def read_reference(self, name):
        text = (ROOT / "references" / name).read_text(encoding="utf-8")
        sections = self.parse_h2_sections(text)
        self.assertEqual(HEADINGS[name], [title for title, _ in sections])
        section_map = dict(sections)
        principle = section_map["Principle"]
        if name == "asset-context.md":
            self.assertNotIn("optional Modifier", principle)
            self.assertIn("conditional truth/provenance hard-gate owner", principle)
            self.assertIn("Design Contract", principle)
            self.assertIn("does not create a route axis or Modifier", principle)
        else:
            self.assertIn("optional Modifier", principle)
            self.assertIn("DirectionContract", principle)
            self.assertIn("does not create a secondary route hierarchy", principle)
        return text, section_map

    def assert_terms(self, text, terms):
        for term in terms:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def parse_markdown_table(self, section):
        rows = []
        for line in section.splitlines():
            stripped = line.strip()
            if not (stripped.startswith("|") and stripped.endswith("|")):
                continue
            cells = []
            current = []
            escaped = False
            for character in stripped[1:-1]:
                if escaped:
                    if character == "|":
                        current.append("|")
                    else:
                        current.extend(["\\", character])
                    escaped = False
                elif character == "\\":
                    escaped = True
                elif character == "|":
                    cells.append("".join(current).strip())
                    current = []
                else:
                    current.append(character)
            if escaped:
                current.append("\\")
            cells.append("".join(current).strip())
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            rows.append(cells)

        self.assertGreaterEqual(len(rows), 2, "expected a header and data rows")
        width = len(rows[0])
        self.assertTrue(all(len(row) == width for row in rows))
        return rows[0], rows[1:]

    def get_labeled_field(self, section, field):
        matches = re.findall(
            rf"^\s*-\s*{re.escape(field)}\s*:\s*(.*?)\s*$",
            section,
            re.IGNORECASE | re.MULTILINE,
        )
        self.assertEqual(1, len(matches), f"expected one {field!r} field")
        return matches[0]

    def assert_labeled_fields(self, section, fields):
        for field in fields:
            with self.subTest(field=field):
                self.get_labeled_field(section, field)

    def test_frontier_interaction_contract(self):
        text, sections = self.read_reference("frontier-interactions.md")
        self.assert_terms(text, [
            "User intent", "System agency", "Control transfer", "Time model",
            "Commitment model", "reversible", "audit", "uncertainty",
        ])

        agency = sections["System agency"]
        self.assert_labeled_fields(agency, [
            "actor", "may decide", "may execute", "approval trigger",
            "explanation duty", "escalation path",
        ])

        control = sections["Control transfer"]
        header, rows = self.parse_markdown_table(control)
        self.assertEqual([
            "Control level", "Who decides", "Who executes", "Approval",
            "Reversibility", "Audit",
        ], header)
        levels = {row[0] for row in rows}
        self.assertEqual({"manual", "assisted", "supervised", "autonomous"}, levels)

        time_model = sections["Time model"]
        self.assert_labeled_fields(time_model, [
            "prior state", "transition trigger", "actor", "observed at",
            "next state", "refresh or expiry",
        ])

        object_model = sections["Object model"]
        self.assert_labeled_fields(object_model, [
            "operation", "state source", "allowed transition", "trace event",
        ])

        simulation = sections["Simulation before commit"]
        self.assert_terms(simulation, [
            "affected objects", "reversible and irreversible",
            "required approvals", "rollback plan",
        ])
        commitment = sections["Commitment model"]
        self.assertIn("consequence", commitment)
        self.assertIn("approval", commitment)
        self.assertIn("reversibility", commitment)
        self.assertIn("audit", commitment)

        uncertainty = sections["Uncertainty"]
        self.assert_terms(uncertainty, [
            "confidence", "assumption", "unknown", "resolution",
        ])

        trace = sections["Trace and audit"]
        self.assert_labeled_fields(trace, [
            "input evidence", "decision", "action", "observed effect",
        ])

    def test_asset_truth_roles(self):
        text, sections = self.read_reference("asset-context.md")
        self.assert_terms(text, [
            "proof", "atmosphere", "support", "placeholder",
            "must not impersonate", "provenance", "authorization",
            "dimensions", "placement", "fallback",
            "before information architecture",
        ])

        context = sections["Context questions"]
        self.assert_terms(context, [
            "informative or decorative", "text alternative",
            "caption or transcript", "equivalent textual fallback",
        ])

        inventory = sections["Asset inventory"]
        self.assert_terms(inventory, [
            "semantic role", "text alternative or equivalent",
            "caption or transcript",
        ])

        ledger = sections["Role ledger"]
        header, rows = self.parse_markdown_table(ledger)
        self.assertEqual([
            "Role", "May establish", "Must not establish", "Fallback",
        ], header)
        roles = {row[0] for row in rows}
        self.assertEqual({"proof", "atmosphere", "support", "placeholder"}, roles)
        self.assert_terms(ledger, [
            "informative", "alt text or equivalent text", "caption or transcript",
            "decorative", "empty text alternative",
        ])

        gate = sections["Asset-before-IA gate"]
        self.assertIn(
            "when available media materially shapes composition",
            gate,
        )
        self.assertIn("before information architecture is locked", gate)
        self.assert_terms(gate, [
            "exact source", "authorization", "dimensions or quality",
            "narrative role", "placement", "fallback",
        ])
        self.assertIn(
            "Generated atmosphere never substitutes for missing proof.",
            sections["Proof rules"],
        )

        coverage = sections["Asset system coverage"]
        self.assert_terms(coverage, [
            "A single source repeated through crops, filters, masks",
            "derivations of the same source", "Asset system manifest",
            "content beats and regions served",
            "many-to-many ecology", "One asset may persist through several beats",
            "rest | invitation | response | transition | interrupted | reduced-motion",
            "poster or first frame", "caption, transcript, or equivalent text",
        ])

        placeholder = sections["Placeholder rules"]
        self.assert_terms(placeholder, [
            "informative placeholder", "equivalent textual fallback",
            "decorative placeholder", "empty text alternative",
        ])

        cultural = sections["Cultural and factual provenance"]
        self.assert_terms(cultural, [
            "Visual description is not factual proof",
            "Generated media provenance proves only",
            "not the depicted object",
        ])

        acceptance = sections["Acceptance checks"]
        self.assert_terms(acceptance, [
            "informative", "alt text", "caption or transcript",
            "decorative", "empty text alternative",
            "equivalent textual fallback",
        ])

    def test_image_contract_rejects_fixed_composition(self):
        text, sections = self.read_reference("image-concepts.md")
        self.assert_terms(text, [
            "Prompt contract", "Asset Family Contract", "Image World Bible",
            "composition family", "reference-only text",
            "Art-direction repair", "Do not default to left-copy/right-object",
            "Image generation is an eligibility decision, not a default",
        ])
        self.assert_terms(sections["Image eligibility"], [
            "keep the selected Surface and Image Modifier",
            "close the current window",
            "hand off to Asset truth even when no file exists",
            "resume from the updated Design Contract",
        ])

        world = sections["Image World Bible"]
        self.assert_terms(world, [
            "visual genre and world premise", "realism or abstraction level",
            "camera and depth language", "lighting logic", "color logic",
            "material logic", "continuity anchors", "forbidden drift",
            "do not silently apply a stored style", "artist, director, studio, or work name",
            "Keep UI and image causally related",
            "Composition plan", "dominant asset read", "focal hierarchy",
            "foreground, middle ground, and background", "background pressure",
            "leading line", "negative space", "mountContract",
            "Do not guess a left/right safe zone",
        ])

        medium = sections["Medium Router"]
        medium_header, medium_rows = self.parse_markdown_table(medium)
        self.assertEqual(["Medium", "Direct explicitly", "Do not delegate or fake"], medium_header)
        self.assertEqual({
            "photography", "illustration", "3D or rendered object",
            "texture or material field", "transparent cutout",
            "UI mockup reference", "sequence or storyboard",
        }, {row[0] for row in medium_rows})
        self.assert_terms(medium, [
            "deterministic HTML, CSS, SVG, canvas, or component code",
            "composite exact text, data, logos, and controls deterministically",
        ])

        family = sections["Asset Family Contract"]
        self.assert_terms(family, [
            '"direction"', '"thesis"', '"aestheticStance"', '"tensionPair"',
            '"visualGenre"', '"attentionStrategy"', '"dominantSilhouette"',
            '"compositionFamily"', '"typographyMood"', '"deletionRule"',
            '"world"', '"camera"', '"light"',
            '"material"', '"color"', '"asset"', '"familyId"', '"id"',
            '"promptContractVersion"', '"conceptType"', '"parentId"', '"stateId"',
            '"transition"', '"fromState"', '"event"', '"toState"',
            '"handoffFrame"', '"role"',
            '"maturity"', '"truthBoundary"', '"medium"', '"intendedUse"',
            '"targetRegion"', '"aspectRatio"', '"cropBehavior"',
            '"deliveryIntent"', '"rasterTextPolicy"', '"visibleText"',
            '"compositionPlan"', '"thumbnailRead"', '"focalHierarchy"',
            '"subjectPlacement"', '"frameOccupancy"', '"shotDistance"',
            '"viewpoint"', '"depthLayers"', '"foreground"',
            '"middleGround"', '"background"', '"backgroundPressure"',
            '"leadingLine"', '"negativeSpace"', '"mountContract"',
            '"consumingRoute"', '"consumingRegion"', '"mountMode"',
            '"layoutSource"', '"breakpointFrames"', '"exclusionZones"',
            '"focalAnchor"', '"focalDrift"', '"variants"',
            '"ui-mockup-reference"', '"targetFidelity"',
            '"interfaceArchetype"', '"layoutThesis"',
            '"hierarchyStrategy"', '"densityRhythm"',
            '"interfaceFramePlan"', '"navigationAndShell"',
            '"regionGeometry"', '"primaryTask"', '"activeState"',
            '"controlsAndAffordances"', '"reconstructionBoundary"',
            '"subject"', '"scene"', '"action"', '"fixedAnchors"',
            '"explorationAxis"', '"referenceRoles"', '"constraints"', '"avoid"',
            '"candidateSettings"', '"mode"', '"count"', '"selectionCriteria"',
            '"variable"', '"binding"', '"allowedValues"',
            "exactly one structured `explorationAxis` per batch",
            "Use `variants` when target device", "simplest useful master first",
            "deterministic compiler requires `typographyMood` and `deletionRule`",
            "two to four ordered reads", "only asset-frame spatial source of truth",
            "Interaction and experience architecture are not image concept types",
        ])

        prompt = sections["Prompt contract"]
        self.assert_terms(prompt, [
            "family and asset identity, prompt-contract version",
            "role, intended use, maturity, and truth boundary",
            "visual thesis, attention strategy, tension pair, visual genre, typography mood, and deletion rule",
            "primary target region and the art-directed composition plan",
            "foreground/middle-ground/background", "background pressure",
            "leading line", "negative space", "mount contract",
            "device or target-region variants", "complete composition plan",
            "`ui-mockup-reference`", "cinematic shot/depth pipeline", "fixed anchors",
            "exactly one exploration axis", "scripts/compile-image-prompt.py",
            "--format json", "Preserve the user's language",
            "bounded set of recognizable quality-praise shortcuts",
            "prompt-engine-shot", "styleKey: no_style", "imagegen-ui-mockup",
            "operation `build_six_layer_prompt`", "candidate-resolved inputs",
            "framework", "material", "polish",
            "Modifier delta", "chinese-aesthetic.md",
        ])
        self.assertIn("`chinese-aesthetic.md` supplies the Modifier delta", prompt)

        candidates = sections["Candidate Protocol"]
        self.assert_terms(candidates, [
            "direction exploration", "asset exploration", "production candidate",
            "edit repair", "3–4", "vary only the named exploration axis",
            "universal `16–30` image board", "prompt-contract version",
            "full view, thumbnail scale, and the target crop",
            "Automated ranking or VLM critique", "user or responsible design judgment",
        ])

        scope_output = sections["Interface and interaction boundary"]
        self.assert_terms(scope_output, [
            "route map", "primary interaction state machine", "wireframe",
            "Do not use one attractive image to stand in for a complete website experience",
            "input -> immediate response -> meaningful consequence + horizon -> handoff -> fallback",
            "must not invent the information architecture",
        ])

        escaped_header, escaped_rows = self.parse_markdown_table(
            "| Name | Relationship |\n"
            "| --- | --- |\n"
            r"| sample | proof \| action |"
        )
        self.assertEqual(["Name", "Relationship"], escaped_header)
        self.assertEqual([["sample", "proof | action"]], escaped_rows)

        families = sections["Composition families"]
        header, rows = self.parse_markdown_table(families)
        self.assertEqual([
            "Composition family", "Use when", "Spatial axes changed",
            "Prompt delta", "Avoid",
        ], header)
        self.assertEqual(6, len(rows))
        names = [row[0].casefold() for row in rows]
        deltas = [row[3].casefold() for row in rows]
        self.assertEqual(6, len(set(names)))
        self.assertEqual(6, len(set(deltas)))
        self.assertTrue(all(names))
        self.assertTrue(all(deltas))

        declared_axes = [
            axis.strip().casefold()
            for axis in self.get_labeled_field(
                families,
                "spatial axis enum",
            ).split(",")
        ]
        expected_axes = {
            "focal-position", "scale", "overlap-depth", "crop-frame",
            "reading-axis", "negative-space",
        }
        self.assertEqual(expected_axes, set(declared_axes))
        self.assertEqual(len(declared_axes), len(set(declared_axes)))

        for row in rows:
            axes = [axis.strip().casefold() for axis in row[2].split(",")]
            with self.subTest(family=row[0]):
                self.assertTrue(row[0])
                self.assertTrue(row[3])
                self.assertTrue(all(axes))
                self.assertEqual(len(axes), len(set(axes)))
                self.assertTrue(set(axes).issubset(expected_axes))

        folded_text = text.casefold()
        for chinese_owned_term in [
            "留白", "气韵", "虚实", "藏露", "借景", "层次", "器物感",
            "移步换景", "Modernization ratio", "source-inferred",
            "Chinese-aesthetic Modifier delta", "Cultural source:",
            "motif hierarchy:", "silence budget:", "red-gold", "dragons",
            "lanterns", "pagodas",
        ]:
            with self.subTest(chinese_owned_term=chinese_owned_term):
                self.assertNotIn(chinese_owned_term.casefold(), folded_text)

        repair = sections["Aesthetic repair"]
        self.assert_terms(repair, [
            "style family", "visual genre", "dominant silhouette",
            "material language", "attention strategy", "image-world thesis",
            "typography mood", "tension pair", "fixed anchors and exploration axis",
            "deletion rule", "Art-direction repair", "labels blurred",
            "visual composition plan", "UI hierarchy strategy", "region geometry",
            "control/proof placement", "density rhythm",
            "mounted crop", "deterministic rebuild",
        ])

        retake = sections["Retake Loop"]
        self.assert_terms(retake, [
            "Image review record", "blocking defect", "role fit | attention",
            "lowest weak relationship", "one prompt delta or localized edit",
            "wrong identity", "broken target crop", "forbidden drift",
            "modify only its causal prompt section", "two iterations fail to improve",
            "never approves, mounts, or promotes an asset by itself",
        ])
        for retired_template in [
            "Elegant Product Homepage", "Aesthetic Repair Homepage",
            "Product Content Page", "Frontier AI Product Surface",
        ]:
            self.assertNotIn(retired_template, text)
        self.assertNotIn("Left has headline", text)
        self.assertNotIn("Right/center", text)

        handoff = sections["Asset handoff"]
        self.assert_terms(handoff, [
            "semantic role", "informative", "decorative", "alt text",
            "caption or transcript", "empty text alternative",
            "equivalent textual fallback",
        ])

        pack = sections["Direction-to-asset-pack"]
        self.assert_terms(pack, [
            "not an implementation asset pack", "Selected-direction asset plan",
            "independent asset role", "website scope, content beats, regions, and continuity handoff",
            "rest | invitation | response | transition | interrupted | reduced-motion",
            "A single attractive image cropped five ways is still one source",
            "missing-proof gap",
        ])

    def test_chinese_aesthetic_mechanisms_survive(self):
        text, sections = self.read_reference("chinese-aesthetic.md")
        self.assert_terms(text, [
            "留白", "气韵", "虚实", "藏露", "借景", "层次",
            "器物感", "移步换景", "Modernization ratio", "source-inferred",
        ])

        source = sections["Source contract"]
        self.assert_terms(source, [
            "Cultural source", "source-inferred", "verify",
            "named dynasty", "artifact", "region", "collection",
            "User-provided material may establish the requested direction or content",
            "does not by itself verify a named cultural claim",
            "trustworthy source", "enough context", "unresolved",
        ])
        direction = sections["Direction contract"]
        self.assertIn("Modifier delta", direction)
        self.assertIn("must not replace the DirectionContract", direction)
        self.assert_terms(direction, [
            "Modernization ratio", "dominant scene", "motif hierarchy",
            "material language", "silence budget", "product proof",
        ])
        prompt_delta = sections["Image prompt delta"]
        self.assertIn("`image-concepts.md` owns the base Prompt contract", prompt_delta)
        self.assertIn("only this Modifier delta", prompt_delta)
        self.assertIn("Chinese-aesthetic Modifier delta", prompt_delta)
        self.assertNotIn("Create a polished", prompt_delta)
        self.assert_terms(prompt_delta, [
            "Generated cultural asset provenance proves only",
            "It never proves that the depicted content is a real artifact",
            "historical fact", "certification", "authoritative cultural asset",
            "remain atmosphere or support",
        ])
        self.assertNotIn("unless independent provenance makes it valid proof", prompt_delta)

    def test_source_inferred_route_preserves_surface_and_hands_missing_media_to_asset_truth(self):
        _, sections = self.read_reference("chinese-aesthetic.md")
        self.assert_terms(sections["Source contract"], [
            "retain the selected Surface and Cultural Modifier",
            "follow the SKILL.md sequential-window rule",
            "hand off to Asset truth even when no file exists",
            "Verify remains a subsequent stage",
        ])
        self.assertNotIn("Explore / Brand / Cultural", sections["Source contract"])

    def test_motion_is_optional_and_accessible(self):
        text, sections = self.read_reference("react-motion.md")
        self.assert_terms(text, [
            "static hierarchy", "focus", "reveal", "continuity",
            "feedback", "signature moment", "prefers-reduced-motion",
        ])

        eligibility = sections["Eligibility"]
        self.assertIn("Motion is optional", eligibility)
        self.assertIn("Motion energy", eligibility)
        self.assertIn("none", eligibility)
        self.assert_labeled_fields(eligibility, [
            "static baseline", "observable benefit", "evidence", "removal trigger",
        ])
        decisions = {
            choice.strip().casefold()
            for choice in self.get_labeled_field(
                eligibility,
                "decision",
            ).split("|")
        }
        self.assertEqual({"retain", "reduce", "none"}, decisions)
        roles = sections["Motion role map"]
        header, rows = self.parse_markdown_table(roles)
        self.assertEqual([
            "Role", "Product purpose", "Typical use", "Static equivalent",
        ], header)
        role_names = {row[0] for row in rows}
        self.assertEqual({
            "focus", "reveal", "continuity", "feedback", "signature moment",
        }, role_names)

        choreography = sections["Asset-derived choreography"]
        self.assert_terms(choreography, [
            "derive motion from content beats, region geometry, selected media, and state progression",
            "Interaction-to-media map", "static and reduced-motion equivalent",
            "Tilt, glow, magnetism, particles, pointer-follow, marquee, and scroll-scrub",
            "rest", "invitation", "response", "transition", "interrupted", "reduced-motion",
            "poster, loading state", "static fallback",
        ])

        region_scroll = sections["Region And Scroll Choreography"]
        self.assert_terms(region_scroll, [
            "native document flow", "sticky or pinned chapters", "horizontal translation",
            "spatial camera travel", "Region choreography record",
            "Motion storyboard record", "keyframe role", "per-layer position",
            "entry, one meaningful transformation, and handoff",
            "Ambient pointer motion", "not runtime evidence",
            "A distinct effect may be designed for every region",
            "not the raw count of effects", "Do not hijack scrolling", "MotionSites",
        ])

        self.assert_terms(choreography, [
            "living page object and source state",
            "equivalent explicit, keyboard, touch, or reduced-input path",
            "meaningful consequence, consequence horizon, and downstream handoff",
            "reversibility, interruption, and escape",
            "cannot count as the primary expressive interaction",
        ])

        static_first = sections["Static-first integration"]
        self.assert_terms(static_first, [
            "static hierarchy", "available immediately", "layout shift",
        ])
        reduced = sections["Reduced motion"]
        self.assertIn("prefers-reduced-motion", reduced)
        self.assertIn("equivalent state and meaning", reduced)

    def test_reference_translation_uses_three_reads(self):
        text, sections = self.read_reference("reference-translation.md")
        self.assert_terms(text, [
            "First read", "System read", "Translation read",
            "Do not copy", "locked", "adaptable", "exact source",
            "version or access date", "license boundary", "material reused",
        ])

        self.assert_terms(sections["First read"], [
            "first focal point", "page rhythm", "density", "emotional tone",
        ])
        self.assert_terms(sections["System read"], [
            "layout grid", "type system", "color roles", "spacing rhythm",
            "interaction promise",
        ])
        self.assert_terms(sections["Temporal read"], [
            "first-viewport screenshot cannot prove a temporal mechanism",
            "pinned ranges", "state progression", "handoff",
        ])
        self.assert_terms(sections["Media ecology"], [
            "screen recording", "canvas/WebGL/3D", "source count",
            "persist or transform",
        ])
        self.assert_terms(sections["Page trace"], [
            "complete public experience from opener to footer or interaction endpoint",
            "Page trace", "evidence level", "rare mechanism",
        ])
        self.assert_terms(sections["Translation read"], [
            "must survive", "locked", "adaptable", "replaceable",
        ])

        provenance = sections["Provenance record"]
        for field in [
            "exact source", "version or access date", "license boundary",
            "traits extracted", "locked/adaptable decisions",
            "material reused", "conflict resolution",
        ]:
            self.assertEqual(
                1,
                len(re.findall(rf"(?m)^- {re.escape(field)}:", provenance)),
            )
        boundary = sections["Copying boundary"]
        self.assertIn("Do not copy", boundary)
        self.assertIn("source facts", boundary)
        self.assertIn("interpretation", boundary)

        dna = sections["DNA contract"]
        self.assert_labeled_fields(dna, [
            "source observation", "target translation rule",
            "DirectionContract field", "validation evidence",
        ])

        decisions = sections["Locked/adaptable decisions"]
        self.assert_labeled_fields(decisions, [
            "trait", "preserved role", "adaptation reason", "validation evidence",
        ])
        classifications = {
            choice.strip().casefold()
            for choice in self.get_labeled_field(
                decisions,
                "classification",
            ).split("|")
        }
        self.assertEqual({"locked", "adaptable", "replaceable"}, classifications)

        conflict = sections["Conflict priority"]
        priorities = re.findall(r"(?m)^\d+\.\s+(.+)$", conflict)
        self.assertEqual(6, len(priorities))
        self.assertIn("truth", priorities[0])
        self.assertIn("user mission", priorities[1])
        self.assertIn("accessibility", priorities[2])
        self.assertIn("locked reference", priorities[4])
        self.assertIn("adaptable reference", priorities[5])
        self.assert_labeled_fields(conflict, [
            "higher-priority rule", "lower-priority trait", "evidence",
            "winner", "affected contract fields", "decision owner",
        ])


if __name__ == "__main__":
    unittest.main()
