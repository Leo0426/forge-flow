---
name: setup-forgeflow
description: 在 CLAUDE.md 和 `docs/agents/` 中搭建 `## Agent skills` 区块，让 ForgeFlow skills 知道此仓库的 issue tracker、triage label 词汇和领域文档布局。在首次使用 `governance/issue-breakdown`、`product/to-prd`、`governance/diagnose-lite`、`engineering/tdd` 或 `engineering/improve-architecture` 前运行；如果这些 skills 看起来缺少运行时上下文，也运行它。
disable-model-invocation: true
---

# 初始化 ForgeFlow

搭建 ForgeFlow skills 每仓库配置：
- **Domain docs** — `CONTEXT.md` 和 ADR 的位置，以及读取它们的规则
- **Issue tracker** — issues 存放在哪里（默认本地 markdown；也支持显式配置 GitHub / GitLab / 其他系统）
- **Triage labels** — 六个规范 triage roles 使用的字符串
这是 prompt 驱动的 skill，不是确定性脚本。先探索，展示发现，与用户确认，然后写入。

## 流程

### 1. 探索
查看当前仓库，理解起始状态。读取已有内容，不要假设：

- `git remote -v` 和 `.git/config` — 是否存在远端仓库，仅作为可选外部 tracker 线索
- 仓库根目录的 `CLAUDE.md` — 是否存在？其中是否已有 `## Agent skills` 区块？
- 仓库根目录的 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 和任何 `src/*/docs/adr/` 目录
- `docs/agents/` — 这个 skill 之前的输出是否已经存在？
- `.scratch/` — 说明本地 markdown issue tracker 约定已在使用

### 2. 展示发现并询问

总结已有内容和缺失内容。然后带用户逐一完成三个决策，**一次一个**——展示一个部分，获得答案，再进入下一个。不要一次性把三个都倒出来。

**A 部分 — Issue tracker**

> Issue tracker 是此仓库 issues 存放的位置。`governance/issue-breakdown`、`product/to-prd` 和 `governance/diagnose-lite` 默认会在 `.scratch/` 下写 markdown 文件。只有你明确选择外部 tracker 时，才使用 `gh issue create`、`glab issue create` 或其他外部工作流。请选择你实际跟踪工作的地方。

默认：建议 **本地 markdown**，即使 `git remote` 指向 GitHub 或 GitLab 也不默认发布到外部系统。仅在用户明确要求时选择外部 tracker：

- **本地 markdown** — issues 作为文件存放在 `.scratch/<feature>/` 下（默认，适合个人项目和离线协作）
- **GitHub 和 GitLab** — 使用模型已有技能获取issues
- **其他**（Jira、Linear 等）— 请用户用一段话描述工作流；

**B 部分 — Triage Labels**

> `governance/issue-breakdown` 和 `agents/triage.md` 通过状态流转处理 issues。它们需要应用与你实际配置相符的 label 字符串。如果你的仓库已使用不同 label 名称（如 `bug:triage` 而非 `needs-triage`），在这里映射，避免创建重复标签。

六个规范 roles：
- `needs-triage` — 维护者需要评估
- `needs-info` — 等待报告者补充信息
- `ready-for-agent` — 已完全明确，Agent 可无人工干预直接领取
- `ready-for-human` — 需要人类处理
- `wontfix` — 不会处理
- `resolved` — 正常处理完毕

默认值：每个 role 的字符串等于其名称。询问用户是否需要覆盖。如果没有既有 label，默认值即可。

**C 部分 — Domain docs**

> `engineering/improve-architecture`、`governance/diagnose-lite` 和 `engineering/tdd` 会读取 `CONTEXT.md` 学习项目领域语言，读取 `docs/adr/` 了解过往架构决策。它们需要知道是单一上下文还是多上下文，才能看对位置。

确认布局：
- **单一上下文** — 仓库根目录有一个 `CONTEXT.md` + `docs/adr/`，大多数仓库是这样
- **多上下文** — 根目录的 `CONTEXT-MAP.md` 指向每个上下文各自的 `CONTEXT.md`（通常是 monorepo）

### 3. 确认并编辑
向用户展示以下草稿：
- 要添加到 `CLAUDE.md` 的 `## Agent skills` 区块
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` 的内容写入前让用户确认和编辑。

### 4. 写入
**选择要编辑的文件：**
- 如果 `CLAUDE.md` 存在，编辑它。
- 如果不存在，询问用户是否创建；不要替他们决定。如果 `CLAUDE.md` 中已有 `## Agent skills` 区块，原地更新内容，不要追加重复区块，不要覆盖用户对周边章节的编辑。

区块格式：

```markdown
## Agent skills
### Issue tracker
[一句话总结 issues 在哪里跟踪]。见 `docs/agents/issue-tracker.md`。
### Triage labels
[一句话总结 label 词汇]。见 `docs/agents/triage-labels.md`。
### Domain docs
[一句话总结布局："单一上下文" 或 "多上下文"]。见 `docs/agents/domain.md`。
```
然后以本 skill 目录下的模板为起点，写入三个 docs 文件：
- [issue-tracker-local.md](issue-tracker-local.md) — 本地 markdown issue tracker
- [triage-labels.md](triage-labels.md) — label 映射
- [domain.md](domain.md) — 领域文档消费规则 + 布局
对于 GitHub、GitLab 或其他 issue tracker，根据用户描述从零编写对应的 `docs/agents/issue-tracker.md`。

### 5. 完成
告诉用户初始化完成，并说明哪些 ForgeFlow skills 现在会读取这些文件。提示他们之后可以直接编辑 `docs/agents/*.md`；只有想切换 issue tracker 或重头开始时才需要重新运行此 skill。
