---
name: feedback-to-roadmap
description: >
  将 MVP 结果、用户反馈、bug、使用数据和复盘结论整理成下一轮 roadmap。
  用于发布后判断继续投入、调整方向、拆分下一批可验证任务。
---

# Feedback To Roadmap

Feedback To Roadmap 负责把发布后的事实转成下一轮工程输入。

它不是愿望清单整理器，而是用反馈验证 Discovery 和 PRD 中的假设。

## 核心原则

- 反馈必须关联目标：先看 MVP 成功指标是否达成。
- 事实和观点分开：数据、用户原话、推测分别记录。
- 先分类，再排优先级。
- 下一轮 roadmap 必须可切片、可验证。
- 保留不做的理由，避免反复讨论。

## 输入

- 用户反馈、访谈、issue、support 记录。
- 使用数据、错误日志、性能指标。
- Release notes、诊断记录、incident 记录。
- Discovery Brief、PRD、ADR 和当前 roadmap。

## 使用流程

### 1. 汇总反馈

按来源记录：

- 用户请求。
- bug 或稳定性问题。
- 体验阻塞。
- 性能或成本问题。
- 内部维护痛点。

### 2. 分类判断

使用以下类别：

- `keep`：继续强化当前方向。
- `fix`：必须修复的正确性或稳定性问题。
- `improve`：增强现有体验。
- `learn`：需要补充验证的未知。
- `drop`：不再投入或明确不做。

### 3. 形成 roadmap

每个 roadmap item 必须包含：

- 用户或维护者价值。
- 对应证据。
- 成功标准。
- 建议切片方向。
- 是否需要 Discovery、Decision Forge 或 Architecture review。

### 4. 交接到任务

- 可直接实现 -> `governance/issue-breakdown`。
- 需要重新验证 -> `product/discovery`。
- 需要架构决策 -> `decision/decision-forge`。
- 需要重构判断 -> `engineering/architecture`。

## 输出格式

```markdown
## Feedback Summary

MVP metric result:

Signals:
- keep:
- fix:
- improve:
- learn:
- drop:

Roadmap:
1. <item>
   Evidence:
   Success metric:
   Next skill:

Not doing:
- <item> because <reason>
```

## 禁止行为

- 把所有反馈都变成需求。
- 不区分 bug、增强和新方向。
- 没有证据就提高优先级。
- 忽略已确认的范围外决策。

