# Product Composer Skill

中文 | [English](README.md)

Product Composer 是一个 Codex skill，用于 AI 辅助 UI 设计与实现中的审美控制。

它不是通用 UI 工具包。只有当 UI 本身需要更强审美、更清晰的视觉 thesis、更可控的 AI 输出时，才应该使用它。它要解决的核心失败很具体：AI 做出的 UI 泛化、过度装饰、构图松散、视觉焦点不清，或者在代码实现时无法保住原本的设计方向。

## 什么时候使用

适合使用 Product Composer 的场景：

- 从零设计 UI，并且需要先建立清晰视觉方向
- 大幅重设计现有界面，因为当前 UI 显得泛、弱、丑或不可控
- 产品应用、dashboard、落地页、AI 界面、编辑/品牌页面中，视觉质量是核心问题
- 高冲击力 hero/page experience，需要屏幕节奏、分页、更丰富资产和更舒展的首屏构图
- 生成 UI 图片概念，并且需要更强构图和更少模板感
- 已选视觉方向的代码实现，需要保住层级、色彩角色、密度、动效和资产处理

如果任务只是机械修改、局部处理，或者和视觉方向无关，就不要使用这个 skill。

## 核心契约

每次重要使用都应该产出或保留一个紧凑的设计契约：

1. 默认模板风险：AI 最可能把哪里做坏。
2. 视觉 thesis：一句话说明这个界面的审美方向。
3. 审美约束：3-5 个让 UI 具体起来的选择。
4. 反默认项：2-3 个必须避免的模板化模式。
5. 资产计划：用户提供、本地已有、或 imagegen 生成的资产，并诚实说明缺失资产。
6. 页面体验计划：对于高要求首页或发布页，定义 screen model、asset system、pagination/page rhythm 和连续性装置。
7. 实现锁定：哪些设计必须在代码里保住，哪些可以因工程原因调整。
8. 视觉验证：可行时检查渲染结果、关键 section 和响应式状态。

如果只替换产品名后这套方案仍然成立，说明视觉方向还不够具体。

## 操作模型

### 先定方向，再定布局

从任务、材料、受众和产品证明出发。视觉 thesis 清楚之后，再选择布局。

### 先有审美，再加装饰

审美不是堆效果，而是在压力下做选择：比例、删除、克制、对比、具体性，都先于视觉特效。

### 先处理资产，再发明视觉

真实资产、本地资产和生成资产都会影响界面。可以使用生成资产，但必须明确它的角色，不能伪装成真实产品证明。

### 先定屏幕，再堆 section

对于 signature page experience，先定义 screen model 和 page rhythm，再组织 section。强页面需要首屏场景、可见的延续提示，以及角色清晰的 asset system。

### 实现是保真，不是二次重设计

写代码不是重新设计。除非有明确工程理由，否则要保住已接受方向里的层级、主导形体、色彩角色、字体性格、密度、动效角色和资产处理。

### 验证必须是视觉的

build 或 lint 通过不等于 UI 成立。可行时要检查实际渲染、移动端布局、文字容纳、关键状态和可见偏差。

## 使用示例

```text
Use $product-composer to design a homepage UI for my product.
Avoid generic SaaS templates. Create a strong visual thesis first.
```

```text
Use $product-composer to redesign this dashboard.
Keep it useful, but make the visual system less generic and more controlled.
```

```text
Use $product-composer to generate an image concept for this AI workflow UI.
Use real product structure, not a method diagram.
```

```text
Use $product-composer to implement the selected UI direction in React.
Preserve the hierarchy, palette roles, density, and responsive behavior.
```

## Reference Map

主 skill 只会在需要时路由到 focused references：

- `references/task-router.md` - 选择最小有效的 UI 设计与实现路线
- `references/style-family-router.md` - 选择风格家族、密度和颜色胃口
- `references/visual-direction.md` - 构图、色彩、材质、轮廓和具体性
- `references/hero-page-experience.md` - 用于 signature page experience 的 screen model、asset system、pagination 和 page rhythm
- `references/taste-calibration.md` - 审美立场、反默认项、克制和记忆点
- `references/direction-matrix-builder.md` - 生成真正不同的视觉方向
- `references/concept-to-implementation-lock.md` - 代码实现时保住已接受概念
- `references/asset-context-protocol.md` - 规划用户提供、本地已有、imagegen 生成的资产
- `references/design-memory-consistency.md` - 保留 token、组件决策、spacing、depth 和界面一致性
- `references/visual-quality-rubric.md` - 判断层级、字体、色彩、材质、深度和 AI 味失败
- `references/image-generation-aesthetic-calibration.md` - UI 图片概念的 prompt 与修复
- `references/interaction-grammar.md` - 为 AI 和复杂工作流定义控制关系
- `references/ant-design-product-values.md` - 让企业产品界面保持秩序和可用性
- `references/content-judgment.md` - 决定保留、推迟和删除什么
- `references/desire-minimalism-psychology.md` - 构建有产品欲望的极简 UI
- `references/market-calibration.md` - 用真实市场预期校准商业页面
- `references/signature-aesthetic-systems.md` - 建立完整视觉世界和连续性
- `references/react-bits-motion-layer.md` - 把 React 动效作为受控强调层
- `references/execution-discipline.md` - 让实现扎根于本地上下文
- `references/anti-patterns.md` - 避免常见 AI UI 失败
- `references/verification.md` - 最终渲染验证

## 工具

```bash
node scripts/ui-pattern-scan.mjs <project-or-src-dir>
```

scanner 会标记前端项目里的常见视觉反模式。把输出当作 warning，然后用视觉检查确认。

## 验证

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/product-composer
python3 tests/test_skill_guidance_structure.py
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
