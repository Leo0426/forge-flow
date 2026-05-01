# CONTEXT-FORMAT.md
> CONTEXT = 定义领域语言（Ubiquitous Language）
> 只记录“是什么”，不记录“怎么实现”

# 作用
- 统一术语（唯一语义）
- 约束设计与代码
- 为 coding 提供判断依据

# 结构
## 1. Context
```
# {Context Name}
{1-2 句话：这个上下文是什么 + 为什么存在}
```

## 2. 语言（Language）
> 一词一义，定义必须一句话
### Aggregates
```
**Order**:
订单聚合根，负责订单生命周期与不变式。
_Avoid_: Cart, PurchaseIntent
```

### Entities
```
**OrderItem**:
Order 内实体，表示商品、数量及价格快照。
_Avoid_: LineItem
```

### Value Objects
```
**Money**:
不可变金额对象（currency + amount）。
_Avoid_: Price
```

### Roles
```
**Customer**:
发起订单并承担支付责任的主体。
_Avoid_: User, Account
```

### Domain Events

```
**OrderPlaced**:
订单已创建。
**PaymentSucceeded**:
支付成功。
```

## 3. 关系（Relations）
```
- 一个 **Customer** → 创建多个 **Order**
- 一个 **Order** → 包含多个 **OrderItem**
- 一个 **Order** → 关联多个 **Payment**
```

## 4. 状态（States）

```
**OrderState**:
- Created
- Paid
- Cancelled

转换:
- Created -> Paid
- Created -> Cancelled
```

## 5. 不变式（Invariants）
```
- Order 必须至少包含一个 OrderItem
- Payment ≤ Order 总金额
```

## 6. 示例对话（Example Dialogue）
```
> Dev: “Payment 失败后 Order 会取消吗？”
> Expert: “不会，Order 仍然是 Created，可重试 Payment。”
```

## 7. 已知歧义（Known Ambiguities）
```
- account 曾表示 Customer / User → 已拆分
- transaction 曾表示 Payment / Refund → 已拆分
```

# 写入规则（必须全部满足）
* 可一句话定义
* 无歧义
* 边界清晰
* 在对话中被重复使用

# 禁止
* 实现细节（DB / API / code）
* 通用技术概念（retry / timeout）
* 模糊术语（如“处理…”）
* 未稳定概念

# 多上下文支持
## 单上下文
```
/
 CONTEXT.md
 engine/
```

## 多上下文
```
/
 CONTEXT-MAP.md
 engine/
     ordering/CONTEXT.md
     billing/CONTEXT.md
```

# CONTEXT-MAP.md 示例
```
# Context Map
## Contexts

- Ordering — 处理订单
- Billing — 处理支付

## Relations

- Ordering → Billing: OrderPlaced event
```

# 与 ADR 的关系
* CONTEXT：定义“是什么”
* ADR：定义“为什么这样做”

# 一句话原则
> CONTEXT 是语义层，是所有决策与实现的约束源。
