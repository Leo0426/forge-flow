---
name: discovery
description: >
  在进入 PRD 和实现前验证问题、用户、替代方案、MVP 成功指标与是否值得开发。
  用于个人项目的 0-1 价值判断，也适用于企业内部需求进入开发前的轻量发现阶段。
---

# Discovery

Discovery 用于回答一个更早的问题：这个想法是否值得进入 PRD 和开发。

它不追求完整市场研究，而是用最小成本确认问题真实、用户明确、成功标准可验证。

## 核心原则

- 问题优先于方案：先确认痛点，再讨论实现。
- 证据优先于兴奋感：区分事实、观察、假设和直觉。
- MVP 成功指标必须可验证：没有指标就无法判断是否继续。
- 替代方案必须被看见：用户现在一定有某种 workaround。
- 不值得做也是有效结论。

## 使用流程

### 1. 定义问题

整理：

- 目标用户是谁。
- 用户现在遇到什么具体问题。
- 问题出现频率、严重程度和当前代价。
- 用户现在如何绕过这个问题。

### 2. 明确假设

把想法拆成可验证假设：

- 用户假设：谁会用。
- 问题假设：他们真的痛。
- 价值假设：解决后有明显收益。
- 使用假设：他们愿意改变现有行为。
- 技术假设：MVP 能用合理成本实现。

### 3. 设计验证

选择低成本验证方式：

- 用户访谈或内部专家确认。
- 手工 demo、原型、假数据页面。
- 竞品和替代方案对比。
- 小范围 dogfood。
- 只实现一条最窄 workflow 的 spike。

### 4. 给出进入 PRD 的判断

输出 `go / no-go / learn-more`：

- `go`：问题明确，MVP 价值和成功指标清楚。
- `learn-more`：关键假设仍不稳定，需要补证据。
- `no-go`：问题不够痛、用户不明确、成本过高或不符合目标。

## 输出格式

```markdown
## Discovery Brief

Problem:

Target users:

Current alternatives:

Evidence:
- Fact:
- Assumption:
- Unknown:

MVP success metric:

Decision: go | learn-more | no-go

Next step:
```

## 交接规则

Discovery Brief 保存到 `docs/generated/discovery.md`。

- `go` → `product/to-prd` 会读取该文件，将已确认事实直接带入 PRD，不重新收集。
- `learn-more` → 补充验证后更新 `docs/generated/discovery.md`，再进入 PRD。
- `no-go` → 记录原因到文件，不进入开发。

## 禁止行为

- 直接把想法包装成 PRD。
- 用“我觉得有用”替代用户证据。
- 没有成功指标就进入实现。
- 忽略用户已有替代方案。

