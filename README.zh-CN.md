# Product Composer Skill

中文 | [English](README.md)

Product Composer 是一个 Codex skill，用于设计、评审、生成和实现高质量产品 UI 界面。

它适合普通 UI prompt 容易产出模板化 SaaS 页面、拥挤 dashboard、弱视觉层级、好看但不好用的 mockup 的场景。这个 skill 会让 Codex 把 UI 当作一个产品系统来处理：先明确任务、内容取舍、视觉方向、交互语法、资产上下文、设计记忆和渲染验证。

## 能解决什么

- 官网、落地页、产品驱动首页
- SaaS 应用、dashboard、后台、表单、数据视图
- AI 产品、agent 工作流、命令界面、前沿交互模型
- 文化、编辑、博物馆、酒店、作品集、高端品牌页面
- 需要欲望感、清晰度和视觉连续性的产品内容页
- 需要避免模板化 AI 味的 image-generated UI mockup
- Figma/reference-to-code、截图提炼设计系统、DESIGN.md 驱动的 UI 工作
- 用户提供、本地已有、或 imagegen 生成的资产工作流
- 可编辑 UI layer document 和 HTML preview
- 现有 UI 评审与 redesign 方向

## 核心思想

### 产品清晰度

每个界面都从用户任务开始：用户需要理解什么、选择什么、完成什么、或产生什么欲望。这个 skill 优先关注任务结构、状态清晰度、渐进披露和可复用产品模式。

### 签名视觉系统

好的 UI 不只是布局。强页面通常成立于一个完整视觉世界：所有可见选择都属于同一套逻辑。

`signature-aesthetic-systems` reference 会把这件事变成可复用方法：

- 识别主题原生的 motif 和 material
- 选择一个主导空间隐喻
- 从主题、产品或材料世界提取 palette
- 定义跨屏连续性装置
- 让 UI 控件看起来属于这个视觉系统
- 删除削弱这个世界的东西

### 风格路由

在全新 UI 生成前，skill 可以让用户选择风格家族、密度和颜色胃口。这样可以避免两个常见问题：视觉方向随机漂移，或者所有结果都变成同一种高端极简首页。

示例回答：

```text
B + 稀疏 + 温暖有欲望
```

路由里也包含实用产品风格的质量底线。工具界面不能退化成普通后台壳，技术界面不能变成黑色驾驶舱、科幻 dashboard、假终端或 `运行舱` 幻想。如果发生这种情况，skill 会把它当作失败方向并重新路由或修复。

### UI 生成方向

这个 skill 把 UI 生成模式吸收到一个本地方向模型中：reference anchor、choice mode、style dials、concept fidelity、artifact mode、visual check。

更深一层是判断力：视觉质量评分、reference DNA 提取、真正不同的方向矩阵、以及保护已接受概念的实现锁。

最深一层是操作行为：选择 surface register、编码前写 design thesis inventory、运行 generic-default self-test、把 copy 当作界面材料、按 section 做还原验证。

最新一层是上下文耐久性：按 input/output mode 路由、在视觉发明前收集 asset context、保留 design memory，避免多轮编辑漂移。

这些已经是主 skill 默认规则，而不仅是深层 reference：

- 先定模式，再定风格
- 先处理资产，再发明视觉：用户提供、本地已有、或 imagegen 生成
- 先保留记忆，再追求新意
- 先定方向，再写代码
- 已接受概念就是契约
- 分段还原验证
- copy 是界面的一部分
- 反默认模板自检

### 欲望驱动的极简

极简不是空。这个 skill 会先判断页面要制造什么心理动机：好奇、信任、解脱、掌控、向往、参与或归属。颜色、布局、证明和交互都会围绕这个目标选择。

### 市场校准

对于官网、落地页和商业内容页，skill 可以使用市场参考，如 WordPress 主题、Webflow 风格模板市场、SaaS landing library 和成熟产品网站。目标是商业成熟度：清晰类别、成品感证明、模块节奏、信任信号、直接的 preview/booking/purchase 路径，同时不复制具体模板。

### 交互语法

对于 AI、agentic、自动化、创作工具或复杂工作流产品，skill 会先定义用户和系统之间的交互关系，再选择组件。它会区分真正的认知交互设计和字面上的拖拽、滑动、点击标签。

### Design Layer Document

这个 skill 也可以把 UI 概念转成结构化 `.layerdoc.json`：

```text
brief / image / data
-> semantic layers
-> .layerdoc.json
-> HTML preview
```

当生成的 UI 需要成为可编辑 HTML preview 或未来视觉编辑器表面，而不只是一个扁平 PNG 时，这个流程很有用。

## 安装

把这个 skill 目录放到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
# 期望路径: ~/.codex/skills/product-composer
```

如果环境需要，重启 Codex 或重新加载 skills。

## 使用方式

显式调用：

```text
Use $product-composer to design a homepage UI for my product.
First create a signature system. Avoid SaaS templates.
Generate a polished image mockup, no code.
```

产品界面：

```text
Use $product-composer to redesign this dashboard.
Prioritize workflow clarity, hierarchy, state visibility, and reusable UI patterns.
```

文化或编辑页面：

```text
Use $product-composer to design a museum homepage.
Build a complete visual world with source motifs, palette origin, and multi-screen continuity.
```

AI 产品：

```text
Use $product-composer to design a frontier AI workflow surface.
Define the interaction grammar before layout. Do not use fake drag or node-graph aesthetics.
```

可编辑 UI layer pipeline：

```text
Use $product-composer to convert this homepage concept into a design layer document.
Export an HTML preview with editable text, shapes, and chart layers.
```

## Reference Map

主 skill 会按任务只读取需要的 focused references：

- `references/ant-design-product-values.md` - 企业产品秩序和 Ant Design 启发的产品价值
- `references/execution-discipline.md` - 避免模板化 UI 的执行纪律
- `references/style-family-router.md` - 用户风格选择和视觉家族路由
- `references/interaction-grammar.md` - AI 和复杂工作流的新交互模型
- `references/taste-calibration.md` - 审美 gate 和反模板化评审
- `references/market-calibration.md` - 产品首页对真实市场预期的校准
- `references/content-judgment.md` - 决定保留、推迟和删除什么
- `references/desire-minimalism-psychology.md` - 能制造产品欲望的极简
- `references/image-generation-aesthetic-calibration.md` - UI image generation 的 prompt 和修复流程
- `references/ui-generation-skill-distillation.md` - UI 生成 workflow 的蒸馏模式
- `references/ui-generation-operating-model.md` - register、thesis、反模板评审和还原循环
- `references/input-output-mode-router.md` - prompt、截图、Figma、概念图、app、prototype 和 layer document 的模式路由
- `references/asset-context-protocol.md` - 设计前收集用户提供、本地已有、imagegen 生成的资产
- `references/design-memory-consistency.md` - 在多轮工作中保留 token、组件决策、spacing、depth 和表面一致性
- `references/visual-quality-rubric.md` - 层级、字体、色彩、材质和 AI 味失败模式的视觉质量评分
- `references/reference-dna-extraction.md` - 从截图、Figma、reference、已接受 mockup 中提取设计 DNA
- `references/direction-matrix-builder.md` - 生成真正不同的视觉方向
- `references/concept-to-implementation-lock.md` - 代码实现时保护已接受的 image concept
- `references/visual-direction.md` - composition、palette、material、silhouette 指导
- `references/react-bits-motion-layer.md` - expressive React motion 和 kinetic accent layer
- `references/signature-aesthetic-systems.md` - 完整视觉世界和多屏连续性
- `references/design-layer-document.md` - 用于 HTML export 的 semantic layer document
- `references/anti-patterns.md` - 常见 AI UI 和产品设计失败
- `references/verification.md` - 最终验证指导

## 内置工具

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

scanner 会标记前端项目里的常见视觉反模式。把输出当作 warning，然后用视觉检查确认。

验证并导出 design layer document：

```bash
python3 scripts/design_layer_tool.py validate examples/opc-homepage.layerdoc.json
python3 scripts/design_layer_tool.py html examples/opc-homepage.layerdoc.json outputs/opc-homepage.html
```

当前 MVP 可以把可编辑文本、shape、image placeholder 和简单 bar chart 导出到 HTML。原生编辑器绑定、表格、mask、复杂 gradient 和更精确的 typography line wrapping 是后续扩展点。

## 验证

使用 Codex skill validator 验证结构：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/product-composer
```

期望结果：

```text
Skill is valid!
```

## License

MIT License. See [LICENSE](LICENSE).
