# 架构词汇表

本 skill 所有建议统一使用以下术语。不要用框架专属词（"component"、"service"、"bean"、"handler"、"API"、"boundary"）替代这里的通用架构概念。术语一致是这套方法论的核心。

## 术语定义

**Module（模块）**
任何有接口和实现的单元。刻意不绑定规模和技术栈——适用于函数、类、包、Spring bean cluster、Go package、生成的客户端封装，或跨层切片。
_避免_：unit、component、service、bean、handler、package（当你指的是通用概念而非语言级别的 package 时）。

**Interface（接口）**
调用者为了正确使用模块所必须知道的一切。包括类型签名，也包括不变量、调用顺序约束、错误模式、必要配置和性能特征。
_避免_：API、signature、Java `interface`、Go `interface`（太窄——那些只指一种语言级别的表面）。

**Implementation（实现）**
模块内部的代码体。与 Adapter 不同：一个东西可以是小 adapter 但有大实现（Postgres repo），也可以是大 adapter 但实现很小（内存 fake）。当话题是 seam 时用 adapter；其他情况用 implementation。

**Depth（深度）**
接口上的杠杆——调用者（或测试）每学一个单位接口能驾驭多少行为。当大量行为隐藏在小接口后面时，模块是 **deep（深）** 的；当接口几乎和实现一样复杂时，模块是 **shallow（浅）** 的。

**Seam（缝合点）** _（源自 Michael Feathers）_
可以在不原地修改的情况下替换行为的位置。模块接口所在的位置。选择 seam 的位置是独立的设计决策，与 seam 后面放什么是分开的。
_避免_：boundary（与 DDD 的 bounded context 重名）。

**Adapter（适配器）**
满足 seam 处接口的具体实现。描述的是角色（它填充了哪个槽位），而不是内容（里面是什么）。

**Leverage（杠杆）**
调用者从 depth 获得的收益。每个接口单位能驾驭更多能力。一个实现在 N 个调用方和 M 个测试中复用。

**Locality（局部性）**
维护者从 depth 获得的收益。变化、bug、知识和验证集中在一处，而不是扩散到调用方。修一处，处处修。

## 核心原则

- **Depth 是接口的属性，不是实现的属性。** 深模块内部可以由小的、可 mock 的、可替换的部分组成——它们只是不暴露在接口上。模块可以有**内部 seam**（私有于实现，供自身测试使用），也有**外部 seam**（在接口处）。
- **删除测试。** 想象删除这个模块。如果复杂度消失了，模块什么都没隐藏（它是一个转发层）。如果复杂度重新散落到 N 个调用方，模块正在创造价值。
- **接口就是测试表面。** 调用者和测试穿过同一个 seam。如果你想测试接口之后的东西，模块可能形状不对。
- **一个 adapter 意味着假设的 seam，两个 adapter 才是真实的 seam。** 除非 seam 两侧真的有东西在变化，否则不要引入 seam。
- **框架名称本身不是架构。** Spring `Service`、Go `Handler`、Rails `Model`、TypeScript `Client` 只有在创造 leverage 和 locality 时才有架构价值。

## 术语关系

- **Module** 有且只有一个 **Interface**（它向调用者和测试呈现的表面）。
- **Depth** 是 **Module** 的属性，相对于其 **Interface** 来衡量。
- **Seam** 是 **Module** 的 **Interface** 所在的位置。
- **Adapter** 位于 **Seam** 处，满足 **Interface**。
- **Depth** 为调用者产生 **Leverage**，为维护者产生 **Locality**。

## 被拒绝的框架

- **Depth 等于实现行数除以接口行数**（Ousterhout）：这会鼓励填充实现。这里用 depth-as-leverage 替代。
- **"Interface" 即 TypeScript `interface` 关键字或类的公共方法**：太窄——这里的接口包括调用者必须知道的每一个事实。
- **"Interface" 即 Java 或 Go 语言结构**：太窄——语言级别的 interface 可以是有用的 seam，也可以是仪式。以变化量、leverage 和测试表面来判断。
- **"Boundary"**：与 DDD 的 bounded context 重名。用 **seam** 或 **interface** 代替。
