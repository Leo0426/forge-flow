---
name: personal-skill-builder
description: >
  创建、优化和评审结构化 agent skills，输出符合 ForgeFlow 实际模式的 SKILL.md
  和可选参考文档。当用户想创建新 skill、重构 prompt 或沉淀可复用工程能力时使用。
---

# Personal Skill Builder

把"想法 / prompt / 工作流"转化为可复用的 ForgeFlow skill（工程产物）。

输出的 skill 必须和仓库中已有 skill 保持结构一致——新 skill 应该长得像 `tdd`、`diagnose-lite` 或 `decision-forge`，而不是通用 AI 工具的 prompt 模板。

## 核心原则

- 能推断 → 直接起草，不追问。信息缺失时最多问 1 个关键问题。
- 结构服从功能：长度由内容决定，不设上限。
- 生成内容必须可直接写入文件，无解释性文本混入。
- 自检失败时自动修复，不输出"需要用户确认"。

## 工作流

### 1. 明确 skill 定位

确认：

- 这个 skill 解决什么具体问题，和已有 skill 有什么边界。
- 触发时机：用户在什么场景下会调用它。
- 调用控制：是否需要 `disable-model-invocation: true`（只有用户才能触发，Claude 不自动使用）。
- 是否需要参考文档：复杂参考内容单独放 `*.md` 文件，SKILL.md 只放链接。

### 2. 生成 SKILL.md

按以下模板生成，所有 `[]` 占位必须替换为真实内容：

```markdown
name: skill-name
description: >
  [一句话说明 skill 做什么]。[第二行说明适用场景或触发时机]。
[disable-model-invocation: true  # 仅用户可触发时加这行]

# Skill 名称

[1-2 句定位：这个 skill 是什么，核心主张是什么。]

## 核心原则

- [原则 1]
- [原则 2]

## 工作流 / 使用流程

### 1. [步骤名]

[叙述性描述，说明做什么、为什么、如何判断。可以包含 bullet list 或代码块。]

### 2. [步骤名]

[...]

## 输出格式

\`\`\`text
[模板，用占位符标出结构]
\`\`\`

## 禁止行为

- [明确列出不该做的事]
- [...]

## 一句话原则

[一句话总结 skill 的最高判断标准。]
```

#### Description 写法

- 用 YAML `>` 多行格式，2–3 行。
- 第一行：能力动词 + 核心输出。
- 第二行：适用场景或触发时机。
- 必须有区分性，避免和已有 skill 描述重叠。
- 不用泛化词：处理、分析、优化。

#### 工作流步骤写法

- 用叙述段落 + bullet list，不用"动作 → 输入 → 输出"表格。
- 每个步骤说清楚：做什么、判断标准、边界条件。
- 步骤之间的衔接条件要明确（什么情况下进入下一步，什么情况下停止）。

### 3. 判断扩展文件

| 情况 | 处理 |
| --- | --- |
| 参考内容（示例、checklist、语言规范）超过 30 行 | 单独放 `reference-name.md`，SKILL.md 中用链接引用 |
| 确定性逻辑需要脚本 | 放 `scripts/`，说明输入、输出、错误处理 |
| 无扩展需求 | 只输出 `SKILL.md` |

### 4. 自检并修复

生成后逐项检查，不满足则自动修复再输出：

```text
[ ] description 使用 YAML > 多行格式
[ ] description 有区分性，无泛化词
[ ] H1 标题 + 定位语存在
[ ] 有"核心原则"或等价的哲学/判断标准章节
[ ] 工作流步骤用叙述段落，不是表格
[ ] 有"输出格式"章节（含 ```text 模板）
[ ] 有"禁止行为"章节
[ ] 以"一句话原则"结尾
[ ] 无占位符残留
[ ] 可直接写入文件，无解释性文本混入
```

## 输出格式

```text
skill-name/
 SKILL.md         # 必需

# 按需追加：
 reference-name.md
 scripts/
     script-name.py
```

每个文件用独立代码块包裹，标注文件路径。

## 禁止行为

- 用"快速开始"替代"核心原则"——ForgeFlow skill 不用这个章节。
- 设置行数上限。长度由内容决定；`tdd` 150 行，`diagnose-lite` 140 行，都是合理的。
- 工作流步骤用"动作/输入/输出"三列表格——ForgeFlow 用叙述风格。
- description 用单行字符串而不是 YAML `>` 多行。
- 输出解释性文本和 skill 内容混在一起。
- 生成和已有 skill 边界模糊的重复 skill。

## 一句话原则

生成的 skill 应该长得像仓库里已有的 skill，而不是通用 AI 工具的 prompt 模板。
