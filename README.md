# ForgeFlow

面向个人开发者的 AI 协作软件工程能力框架。把优秀工程师的工作方法协议化，以 Claude Code / Codex 插件形式分发，让 Agent 在固定流程约束下工作，而不是自由发挥。

## 设计思路

AI 的问题不是能力不足，而是缺乏约束——不知道何时停下来问、何时写测试、何时从全局看问题。ForgeFlow 的每个 Skill 是一个约束单元，把工程师的判断时机固化成可触发的流程。

详见 [meta/PHILOSOPHY.md](meta/PHILOSOPHY.md) 和 [meta/METHODOLOGY.md](meta/METHODOLOGY.md)。

## Skills

### decision

| Skill | 说明 |
| --- | --- |
| [`decision/decision-forge`](skills/decision/decision-forge/SKILL.md) | 推进复杂设计与工程决策收敛，把模糊想法变成可执行、可追溯的工程决策 |

### engineering

| Skill | 说明 |
| --- | --- |
| [`engineering/coding-with-tdd`](skills/engineering/coding-with-tdd/SKILL.md) | 红绿重构循环实现功能或修复 bug，通过公共接口验证行为 |
| [`engineering/architecture`](skills/engineering/architecture/SKILL.md) | 识别并改进代码库架构复杂度，基于 Deep Module 和分层一致性提出改进候选 |
| [`engineering/code-review`](skills/engineering/code-review/SKILL.md) | 对当前 diff 做正确性、简化/复用和方法论对齐三类审查 |
| [`engineering/zoom-out`](skills/engineering/zoom-out/SKILL.md) | 上升一层抽象，给出当前代码区域的系统地图：相关模块、调用者、依赖方向 |
| [`engineering/git-commit`](skills/engineering/git-commit/SKILL.md) | 从当前变更中提炼最小一致性提交，生成高质量 git commit |

### governance

| Skill | 说明 |
| --- | --- |
| [`governance/issue-breakdown`](skills/governance/issue-breakdown/SKILL.md) | 用垂直切片把 PRD 或计划拆成可独立验证的工程任务 |
| [`governance/diagnose-lite`](skills/governance/diagnose-lite/SKILL.md) | 轻量诊断：最小复现、假设、验证、修复、再验证 |
| [`governance/repo-health`](skills/governance/repo-health/SKILL.md) | 检查仓库健康度：ownership、依赖、安全、架构漂移、测试质量 |

### operations

| Skill | 说明 |
| --- | --- |
| [`operations/release`](skills/operations/release/SKILL.md) | 管理发布生命周期：发布前验收、版本说明、rollback plan、发布后检查 |
| [`operations/operate`](skills/operations/operate/SKILL.md) | 管理运行维护生命周期：observability、runbook、incident intake、维护节奏 |

### product

| Skill | 说明 |
| --- | --- |
| [`product/discovery`](skills/product/discovery/SKILL.md) | 在进入 PRD 前验证问题、用户、替代方案和 MVP 成功指标 |
| [`product/to-prd`](skills/product/to-prd/SKILL.md) | 将想法或对话上下文整理成轻量 PRD |
| [`product/feedback-to-roadmap`](skills/product/feedback-to-roadmap/SKILL.md) | 将发布后反馈、数据和复盘结论整理成下一轮 roadmap |

### misc

| Skill | 说明 |
| --- | --- |
| [`misc/setup-forgeflow`](skills/misc/setup-forgeflow/SKILL.md) | 在新仓库中初始化 ForgeFlow agent runtime 上下文（首次使用前运行） |
| [`misc/personal-skill-builder`](skills/misc/personal-skill-builder/SKILL.md) | 创建、优化和评审结构化 agent skills |
| [`misc/terse-communication`](skills/misc/terse-communication/SKILL.md) | 中英双语极简沟通模式，压缩冗余，保留技术准确性 |

## 工程生命周期

| 阶段 | 推荐 Skill |
| --- | --- |
| 问题验证 | `product/discovery` |
| 需求整理 | `product/to-prd` |
| 决策收敛 | `decision/decision-forge` |
| 任务拆解 | `governance/issue-breakdown` |
| 编码实现 | `engineering/coding-with-tdd` |
| 架构改进 | `engineering/architecture` |
| 问题诊断 | `governance/diagnose-lite` |
| 发布 | `operations/release` |
| 运维 | `operations/operate` |
| 反馈迭代 | `product/feedback-to-roadmap` |
| 仓库治理 | `governance/repo-health` |

## 用法

### 作为 Claude Code 插件

```bash
# 构建插件包
python3 tools/build_plugins.py
```

```bash
# 加载到 Claude Code
claude --plugin-dir ./build/plugins/claude-code/forgeflow
```

加载后在对话中直接使用斜杠命令：

```
/forgeflow:setup-forgeflow      → 初始化仓库运行时上下文（首次使用先运行这个）
/forgeflow:decision-forge       → 决策收敛
/forgeflow:coding-with-tdd      → TDD 红绿重构
/forgeflow:architecture         → 架构改进
/forgeflow:code-review          → diff 审查
/forgeflow:zoom-out             → 系统地图
/forgeflow:git-commit           → 语义化 commit
/forgeflow:issue-breakdown      → 任务拆解
/forgeflow:diagnose-lite        → 问题诊断
/forgeflow:repo-health          → 仓库健康检查
/forgeflow:release              → 发布管理
/forgeflow:operate              → 运维管理
/forgeflow:discovery            → 问题验证
/forgeflow:to-prd               → 轻量 PRD
/forgeflow:feedback-to-roadmap  → 反馈转 roadmap
/forgeflow:terse-communication  → 极简沟通模式
/forgeflow:personal-skill-builder → 创建新 skill
```

### 作为 Codex 插件

```bash
codex plugin marketplace add ./build/plugins/codex
```

## 项目结构

```
skills/         可复用 skill，按 bucket 分类
  decision/
  engineering/
  governance/
  operations/
  product/
  misc/
meta/           设计文档
  PHILOSOPHY.md   核心思路
  METHODOLOGY.md  架构设计方法论
CONTEXT.md      领域术语表
tools/          插件打包脚本
```

## 鸣谢

[mattpocock/skills](https://github.com/mattpocock/skills) — 把工程师工作方式显式化为可触发 Skill 的最佳范例。

## 许可证

MIT
