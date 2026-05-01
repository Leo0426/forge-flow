## 项目概述

ForgeFlow 是面向个人开发者的轻量工程能力框架。核心概念见 `meta/CONTEXT.md`。

Skills 是唯一的资产类型，存放于 `skills/<bucket>/<name>/SKILL.md`，通过插件分发给 Claude Code / Codex。

## 目录结构

```
skills/     可复用 skill，按 bucket 分类
meta/       项目文档
  CONTEXT.md     领域语言与概念模型
  PHILOSOPHY.md  设计思路
  METHODOLOGY.md 方法论
  docs/          图片与参考资料
```

## Skill 组织规范

### Bucket 分类

| Bucket | 用途 |
|--------|------|
| `engineering/` | 日常编码工作 |
| `decision/` | 设计与工程决策 |
| `governance/` | 项目治理（诊断、健康检查、任务管理） |
| `operations/` | 发布与运维 |
| `product/` | 产品发现与需求 |
| `misc/` | 低频但保留 |

### 文件格式

在 `skills/<bucket>/<name>/SKILL.md` 创建文件，必须包含 YAML frontmatter：

```yaml
name: <name>
description: <一句话描述>
```

### 添加 Skill 检查清单

每个新 skill 必须同时满足：

1. **顶层 `README.md`**：有对应条目，skill 名称链接到其 `SKILL.md`
2. **`.claude-plugin/plugin.json`**：有对应条目
3. **所在 bucket 的 `README.md`**：有一行描述，skill 名称链接到其 `SKILL.md`

## Agent 运行时

### Issue tracker
Issues 以 markdown 文件形式存放在 `.scratch/` 目录下，每个功能一个子目录。

### Triage labels
使用六个规范 role 字符串（needs-triage、needs-info、ready-for-agent、ready-for-human、wontfix、resolved）。
