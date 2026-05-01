# ADR-FORMAT
> ADR = 记录“我们为什么这样做”

# 作用
- 记录关键工程决策
- 防止重复讨论
- 为 CONTEXT 提供因果解释（why）

# 位置
```
./docs/adr/
```

# 命名
```
0001-short-title.md
0002-short-title.md
```
- 编号递增（扫描当前最大值 +1）
- kebab-case
- 标题必须表达“决策点”

# 最小模板
```
# {short-title}
{1-3 句话：背景 + 决策 + 原因}
```

# 示例
```
# use-event-sourcing-for-orders
订单需要完整历史与可回放能力，我们采用 event sourcing，
因为它支持审计与重建状态，优于传统 CRUD。
```

# 可选增强
## Status
```
Status: proposed | accepted | deprecated | superseded by 000X
```

## Considered Options
仅当存在真实 trade-off：
```
Event Sourcing:
  优点: 可审计、可回放
  缺点: 复杂度高

CRUD:
  优点: 简单
  缺点: 无历史
```

## Consequences
仅当存在非显而易见影响：
```
- 写路径复杂度增加
- 需要事件版本管理
```

# 创建规则（必须全部满足）
|条件|说明|
|------------|--------|
|难以反转|修改成本高|
|无上下文会困惑|未来读者无法理解|
|存在 trade-off|至少两个合理方案|
否则：
```
不要创建 ADR
```

# 修改规则
禁止修改已有 ADR。
必须：
1. 创建新 ADR
2. 标记旧 ADR：
```
Status: superseded by 000X
```

# 与 CONTEXT 的关系
* CONTEXT → 定义“是什么”（语义层）
* ADR → 解释“为什么这样做”（决策层）

# 写作规则
## 必须
* 一句话可读懂
* 明确因果：
```
X -> Y
```
- 写“为什么”，不是“做了什么”

## 禁止
- 模糊表达（可能 / 也许）
- 无理由结论
- 模板填充
- 实现细节堆砌

# 惰性策略
- 不提前创建 `./docs/adr/`
- 不为“可能需要”写 ADR
- 只在**决策发生时**记录

# 一句话原则
> ADR 是决策的因果记录层，用于防止未来重复决策。
