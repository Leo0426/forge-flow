# ForgeFlow

一套可复用的 Agent Skill 集合，按 Bucket 组织，以 Claude Code / Codex 插件形式分发。Skill 将稳定的工程实践编码为可调用的能力，开发者无需在每次 AI 会话中重复解释自己的工作方式。

## 术语表

**Skill**
可复用的 Agent 能力单元——一个包含 YAML frontmatter（`name`、`description`）及工作方式定义的 `SKILL.md` 文件。Skill 是 ForgeFlow 唯一的资产类型。
_避免使用_：prompt、command、script、template

**Bucket**
`forge/skills/` 下按领域分组相关 Skill 的目录（如 `engineering/`、`product/`、`governance/`）。每个 Bucket 有自己的 `README.md`，列出其中所有 Skill。
_避免使用_：category、folder、namespace、module

**Frontmatter**
`SKILL.md` 顶部以 `---` 分隔的 YAML 块。至少包含 `name` 和 `description`，可包含 `disable-model-invocation` 等可选标志。
_避免使用_：metadata、header、config block

**Plugin**
由 `tools/build_plugins.py` 为特定平台（Claude Code 或 Codex）打包的 Skill 分发包。插件包含 Skill 文件和平台专属的清单文件。
_避免使用_：package、bundle、extension

**Issue tracker**
托管仓库 Issue 的工具——GitHub Issues、Linear、本地 `.scratch/` markdown 约定，或类似工具。`issue-breakdown`、`diagnose-lite`、`repo-health` 等 Skill 会读写其中的内容。
_避免使用_：backlog manager、issue host

**Triage role**
在分诊（triage）过程中应用于 Issue 的规范状态机标签（如 `needs-triage`、`ready-for-agent`、`ready-for-human`）。每个 role 通过 `meta/agents/triage.md` 映射到 Issue tracker 中的具体标签字符串。
_避免使用_：status、tag、label（仅在指代 tracker 中的具体标签时使用 label，不用于指代 role）

**Agent Runtime**
`meta/agents/` 中的一套协议，规定 Agent 在特定仓库中执行 ForgeFlow Skill 时如何读取领域上下文、路由任务。
_避免使用_：agent config、agent framework、agent setup

## 关系

- ForgeFlow 将多个 **Skill** 组织进多个 **Bucket**
- 一个 **Plugin** 将多个 **Skill** 打包用于平台分发
- **Agent Runtime** 配置 **Skill** 在特定仓库中的调用方式
- `issue-breakdown`、`diagnose-lite` 等 Skill 向 **Issue tracker** 生产或消费 **Issue**
- 一个 **Issue** 在同一时刻只持有一个 **Triage role**

## 已澄清的歧义

**"flow" / "workflow"** 曾指 YAML 定义的、将多个 Skill 顺序串联的多步执行计划。_已解决_：flow 已移除；Skill 串联在 Claude Code 对话上下文中自然发生。"flow" 不应再作为领域术语出现。

**"runner"** 曾指调用 Anthropic API 执行 Skill 的 Python 层。_已解决_：已移除；执行完全委托给 Claude Code / Codex。

**"spec"** 曾指 `specs/` 目录下的 prompt、模板和 schema。_已解决_：已移除；所有能力内容都存放在 Skill 中。

**"runtime"** 曾同时用于 Python `RuntimePlan` 执行对象和 Agent 上下文协议。_已解决_：Python 执行层已移除；"runtime" 现在仅指 **Agent Runtime**（即 `meta/agents/` 中的协议）。
