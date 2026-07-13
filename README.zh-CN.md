# Product Composer Skill

中文 | [English](README.md)

## Positioning

Product Composer 是一个为 UI 工作提供明确审美与创意核心的 Codex skill。它从真实信号推导可追溯的视觉命题，指导一致的 image world 与资产家族，编译可检查的生成提示，在实现中保住已接受的视觉决策，依据渲染证据修复界面，并验证视觉保真度或 artifact maturity。

Runtime authority: root `SKILL.md` only.

本 README 解释包的用途，不重新定义路由契约。

## 什么时候使用

当视觉方向会实质改变结果时使用 Product Composer：

- 创建新的产品、品牌或混合界面
- 大幅重设计已有界面
- 从真实的产品、受众、内容与参考信号推导正向视觉方向
- 指导一致的 image world 或资产家族，并在目标界面中比较候选方案
- 转译已接受的 UI 或图片参考，同时保住其因果设计规则
- 在实现中保住锁定的行为与视觉决策
- 根据实际观察到的证据修复渲染结果
- 验证视觉保真度或 artifact-maturity 声明

如果只是按既有系统完成普通 UI、且没有实质性的艺术方向或保真决策，或只是机械式小改、与视觉无关的工程任务、文档翻译、未要求重设计的 UX 审计，则不应激活本 skill。

## 运行模型

根 skill 选择一个 Phase 和一个 Surface，只添加会改变行为的 Modifiers，并打开完成工作所需的最小 owner-reference window。所有 owner 共同读写同一份 Design Contract。direction-only Explore 停在已接受的方向。已授权实现的新 UI 直接选择 Implement，并在第一个 slice 前建立已选或推断的 DirectionContract、补全 Functional delta，再开始构建。validation-only Explore 只报告证据与 verification gaps，不做修改；Repair 每次只修改一个有证据支持的轴；Verify 为每项声明匹配相应证据。

创意核心把来源信号转成布局、字体、图片、材质与动效上的可见后果。图片工作会建立 Image World Bible、选择合适媒介、锁定资产家族锚点、编译确定性的 prompt contract、比较有边界的候选集，并只针对已诊断的因果变量重拍；当图片并非结果的关键组成时，它不会强制生成图片。

对于品牌站、Landing、SaaS、作品集、电商与实验网站，Product Composer 会把开场 Hero、完整路由和多路由网站分开建模。Hero 可以包含多个内容节拍、区块、媒介和交互状态，但不等于一个全屏区块，也不等于整个网站。内容节拍、区块几何、滚动编排和媒介之间是独立的多对多关系；明确 PC-only 时不会额外强加移动端适配。

完整 owner matrix、reference budget、唯一例外、phase outcome 与 hard gate 只保留在 [`SKILL.md`](SKILL.md)。可执行的激活边界与初始窗口预期由下方文件结构链接。

## 保留的能力

Product Composer 保留产品正确性、本地约定、内容与资产真实性、已选审美立场与视觉 thesis、image world 与资产家族连续性、锁定的实现决策、可访问的状态行为，以及可追踪的验证证据。以下 artifact-maturity 标签用于阻止文字上的越级声明：

- **recipe**：完整但不可运行的方向元数据与验收检查
- **preview**：指定场景、状态和 viewport 的渲染视图，并明确已知限制
- **runnable starter**：具备可执行入口，并为所声明的基础交互提供行为证据
- **tested golden**：适用的行为与渲染检查已经通过的指定场景
- **template**：包含 manifest、入口、可替换输入契约、来源记录、smoke test 与渲染证据的可复用包

这些词表示声明等级，并不表示本仓库已经提供对应 artifact。本包不声称包含 runnable starter、tested golden 或 production template。

## 文件结构

- [`SKILL.md`](SKILL.md) 是唯一 runtime authority。
- [`references/`](references) 存放由 `SKILL.md` 索引的 focused runtime-owner 文档。
- [`scripts/compile-image-prompt.py`](scripts/compile-image-prompt.py) 分流视觉素材与 UI mockup 参考，校验由真实布局派生的挂载契约，实例化单一探索轴，并输出不复制风格词库的可移植 prompt-engine 或 UI-mockup 适配请求。
- [`scripts/ui-pattern-scan.mjs`](scripts/ui-pattern-scan.mjs) 提供可选的确定性 scanner。
- [`tests/`](tests) 包含结构、来源、完整性与 scanner 检查。
- [`evals/discovery-scenarios.md`](evals/discovery-scenarios.md) 与 [`evals/routing-scenarios.md`](evals/routing-scenarios.md) 让激活边界和 reference-window 预期可审查。
- [`evals/source-ledger.json`](evals/source-ledger.json) 是仓库的 provenance evidence，不是 runtime reference。
- [`examples/scenarios/product-composer-routing.md`](examples/scenarios/product-composer-routing.md) 只展示两个紧凑示例，不复制完整路由表。

## Scanner

当视觉代码可能含有已知的 generic-default 信号时，对项目或源码目录运行：

```bash
node scripts/ui-pattern-scan.mjs ./src
```

默认 JSON findings 只是 evidence prompts，不是自动失败。只有在 warning 应使命令失败时才使用 `--strict`，随后仍要对照当前契约和实际渲染结果逐条确认。

## 验证

在仓库根目录运行：

```bash
python3 -B "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$PWD"
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/test_scanner.mjs
```

## License

Apache License 2.0。参见 [LICENSE](LICENSE)。
