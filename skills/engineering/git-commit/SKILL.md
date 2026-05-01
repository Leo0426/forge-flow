---
name: git-commit
description: 从当前变更中提炼最小一致性提交，并生成高质量 git commit。
command: true
---

# /git-commit

从当前工作区生成一个最小且语义清晰的 git commit。

## 输入参数

- `message`：直接使用的 commit message（可选）
- `scope`：限定提交范围（路径 / 模块 / 变更域）（可选）
- `dry-run`：仅分析，不执行 commit（可选）

## 原则

- 最小单元：一次 commit 只表达一个意图。
- 语义优先：commit 描述为什么，不只是列出做了什么。
- 不污染历史：不混入无关改动。
- 已暂存优先：staged 视为用户已确认意图。
- 失败优先：无法保证质量时拒绝提交。

## 预检

```bash
git rev-parse --is-inside-work-tree
git status --short
```

终止条件：

- 非 git 仓库。
- 无任何变更。

## 分析

```bash
git diff --stat
git diff
git diff --cached --stat
git diff --cached
```

提取结构化信息：

| 维度 | 内容 |
| --- | --- |
| 变更类型 | feat / fix / refactor / test / docs / chore |
| 影响范围 | 模块 / 包 / 子系统 |
| 文件分布 | 是否集中 |
| 调用关系 | 是否同一调用链 |

## 一致性判定

最小一致变更集合必须满足至少两条：

- 同一目录 / 模块。
- 同一变更类型。
- 修改同一调用链。
- 围绕同一问题。

否则判定为多主题修改，只提交用户指定或最清晰的一组变更，并留下其余改动。

## 类型与 Scope 推断

type 判定优先级：

1. `fix`：修复错误 / 测试失败。
2. `feat`：新增能力。
3. `refactor`：不改变行为。
4. `test` / `docs` / `chore`。

scope 推断规则：

- 优先使用顶级目录或主要模块名。
- 多模块时使用最小公共路径。
- 无法判断时省略 scope。

## Staged 策略

- staged 视为用户明确选择。
- 仅使用 staged，除非 `scope` 明确命中其他文件。

拒绝条件：

- staged 文件属于多个意图。
- staged 与 unstaged 在同一文件里互相冲突。

## 决策

创建 commit 前输出：

- 是否可提交。
- commit 类型与 scope。
- files 候选。
- message 草案。

## 执行

只使用非交互式 git 命令：

```bash
git add <selected-files>
git diff --cached --stat
git commit -m "<message>"
```

不要使用 `git reset --hard`、`git checkout --`、`git clean` 等破坏性命令。

## 验证

```bash
git log -1 --oneline
git status --short
```

## 输出

- commit hash 和 message。
- 本次提交包含的文件。
- 剩余未提交改动。
