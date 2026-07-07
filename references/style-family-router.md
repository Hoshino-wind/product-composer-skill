# Style Family Router

Use this before net-new UI generation when the user's style direction is not explicit. The goal is to reduce both randomness and sameness by making the user choose a visual family before composition begins.

## Principle

Ask for style choice when the output could plausibly go in multiple directions. Do not silently default to `Editorial Premium` or `high-end minimal` for every brief.

Skip the question only when:

- the user provided a clear reference image, brand system, or existing UI to follow
- the task is a narrow fix to an existing screen
- the user explicitly says to proceed without questions
- the product category makes the family obvious

## User Choice Menu

Use the user's language. Keep the question compact and ask at most three choices.

Example:

```text
开始前先选一下方向，避免风格随机或同质化：

1. 风格族：A 实用产品 / B 高级编辑 / C 文化沉浸 / D 技术仪器 / E 数据密集 / F 轻快消费 / G 温暖手作 / H 强转化活动
2. 信息密度：稀疏 / 平衡 / 密集但有空气
3. 色彩倾向：安静克制 / 温暖有欲望 / 鲜明高对比 / 从产品或文化素材提取

你可以直接回复：B + 稀疏 + 温暖有欲望。
```

If asking only one question, ask for `style family` and infer density/color from product context.

## Style Families

| Code | Family | Use When | Visual DNA | Avoid |
|---|---|---|---|---|
| A | Utility Product | SaaS, admin, CRM, settings, forms, internal tools | Ant Design-inspired product order, stable navigation, clear object hierarchy, contextual actions, dense-with-air, explicit state, restrained accents | marketing hero, oversized decorative objects, generic white-blue admin shell, bland left-nav/table/card template, purely decorative dashboard |
| B | Editorial Premium | brand sites, launch pages, portfolios, premium product homepages | art-directed spread, refined type, negative space, one composed proof object | generic left-copy/right-screenshot SaaS |
| C | Cultural Immersive | museums, cities, exhibitions, hospitality, heritage, editorial culture | subject-native motifs, texture, atmosphere, continuity device across screens | tourist collage, random historical decoration |
| D | Technical Instrument | AI tools, developer tools, command surfaces, automation, ops, device monitoring, industrial/medical/scientific products | 3D instrument or digital-twin object, sensor/status overlays, calibration controls, visible state, inspectable geometry, muted technical palette, one beautiful physical-control object | sci-fi dashboard, node graph as decoration, black cockpit, military command center, terminal cosplay, generic "control room" aesthetic, flat card-only technical UI |
| E | Data Dense | analytics, BI, trading, risk, finance, ops review | compact data hierarchy, chart grammar, comparison, filters, semantic color | hiding data to look minimal |
| F | Playful Consumer | education, lifestyle, social, wellness, mobile-first products | bright but controlled color, friendly illustration, motion cues, approachable shapes | childish visuals when the audience is serious |
| G | Soft Craft | creator tools, writing, design, content, boutique products | tactile materials, warm neutrals, hand-finished details, gentle contrast | generic beige, decorative craft with no product proof |
| H | Bold Campaign | launches, campaigns, conversion pages, events, short-term offers | high contrast, strong type, kinetic composition, direct action path | noise, unreadable type, fake urgency |

## Selection Logic

- Operational or repeated-use SaaS screen -> start with A and apply Ant Design product values: natural task order, certainty, meaningful work objects, and progressive capability.
- Public homepage with strong brand emotion -> ask between B, C, F, G, or H.
- AI or automation workflow -> start with D only when the primary value is control, audit, simulation, or execution safety. If D produces a cockpit, command-room, terminal, or sci-fi surface, reroute to A for calm product, E for proof-heavy analytics, or B for product-led editorial proof.
- Physical, industrial, medical, scientific, IoT, robotics, or monitoring products -> start with D and make a 3D instrument/digital-twin object the central proof. Do not flatten it into a card dashboard.
- Cultural or place-based subject -> start with C, then define source motifs before layout.
- If the user says "像敦煌那版一样好看", choose the method, not the motifs: coherent world, source-derived palette, continuity device, paced density.

## Naming And Copy Taste Gate

Names and labels can make a visually correct screen feel cheap. Before generating Chinese UI, reject names that sound like industrial fantasy, military command, or generic AI product slang unless the real product domain requires it.

Avoid for normal software products:

- `运行舱`, `指挥舱`, `智控舱`, `超脑`, `中枢`, `驾驶舱`, `作战室`
- vague suffixes like `智服台`, `数观台`, `运行台` when they do not describe a real user job
- hard technical copy that makes the product feel like equipment rather than a useful interface

Prefer names tied to the user job or product promise:

- `任务审阅`, `执行预演`, `风险复核`, `内容整理`, `线索分析`, `页面生成`
- `审阅台`, `复核台`, `预演台`, `工作台`, `分析室` only when the surrounding visual system is tasteful and specific

If the first generated result feels ugly because of naming or hard technical mood, rename and regenerate before changing layout details.

## Family Quality Floors

Each family needs an aesthetic floor. Do not accept outputs that merely match the category label.

- A Utility Product must still feel designed. It needs a product-specific workflow object, tasteful empty space, and a palette with tension. Reject if it looks like a default admin template with a pale background, left rail, table, and equal cards.
- A Utility Product should reference Ant Design's product philosophy, not imitate a default theme. Keep stable navigation, contextual actions, state clarity, filter/table/form discipline, and progressive disclosure.
- D Technical Instrument must feel like a precision product surface, not a "cool control room". Prefer 3D instrument display, digital twin, cutaway model, sensor overlay, calibration ring, viewport controls, and state layers. Reject black panels, blue glows, fake terminal grids, cockpit framing, dense equal modules, and any wording that makes the product feel militarized or cheap.
- For A and D, if the output is usable but ugly, run a `quieter + warmer + more specific` repair: reduce chrome, introduce one tactile or editorial material, make the central object beautiful, and remove generic technical naming.

## Anti-Sameness Rules

For every selected family, change at least four of these variables:

- composition type
- density
- palette source
- material language
- typography mood
- proof object
- interaction object
- section rhythm

Do not reuse the same `one dominant product object + left headline + right preview` structure by default. A dominant form can be a map, table field, instrument panel, editorial sheet, timeline, object portrait, quiet chamber, or data wall.

## Orthogonality Gate

Use this when reviewing multiple generated UI directions or repairing rejected outputs. A direction can pass local quality checks and still fail if it converges with the rest of the set.

Before accepting a generated image, compare it with the previous accepted images across these variables:

- background material
- dominant silhouette
- primary layout grammar
- navigation/control placement
- proof object
- accent palette
- density rhythm
- icon/decoration language

If it shares five or more variables with another accepted direction, reject it as same-looking and regenerate with a different composition family. Do not describe it as a successful style-family variant.

Hard repeated-pattern warnings:

- `warm ivory background + central horizontal rail/timeline + right action panel + rounded cards`
- `large centered object + supporting cards orbiting it`
- `left list + center document/work surface + right recommendation panel`
- `magnifier/lens/inspection object` reused across unrelated families
- `paper-like UI + fine border cards + green/red status chips` reused as the default "tasteful" repair

When a repair starts to converge, do not make it merely warmer or quieter. Change the spatial metaphor.

Examples:

- A Utility Product can become a dense command ledger, radial triage map, split-screen compare tool, calendar/resource matrix, or compact queue lane system.
- D Technical Instrument can become a 3D device viewport, digital twin, exploded instrument, cutaway machine, calibration dial, simulation oscilloscope, reversible commit switch, audit prism, or constraint field.
- G Soft Craft can remain paper/editorial; A and D should not both use the same paper-and-panel language unless the user's product actually requires it.

## Brief Fields

After selection, record:

- selected family and why
- density and color appetite
- what this family must show
- what this family must avoid
- what nearby style or prior output it must not resemble
- one deliberate risk
- one deletion rule
