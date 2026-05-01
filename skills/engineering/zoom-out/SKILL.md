---
name: zoom-out
description: >
  暂停当前任务，上升一层抽象，给出当前代码区域的系统地图：相关模块、调用者、
  依赖方向，使用项目领域词汇。当不熟悉某段代码或需要理解它在系统中的位置时触发。
disable-model-invocation: true
---

# Big Picture

我不熟悉这段代码。上升一层抽象。用项目的领域词汇，给我绘制相关模块和调用者的地图。

## 执行步骤

### 1. 读取领域词汇

优先读取 `CONTEXT.md`；若无，从 README 或目录结构推断术语。不用框架名（`Controller`、`Service`、`Handler`）替代领域术语——它们是标签，不是地图。

### 2. 定位当前位置

- 当前代码属于哪个模块。
- 它处于哪个架构层：Interface / Application / Domain / Infrastructure。
- 对应 CONTEXT.md 中的哪个领域术语。

### 3. 向上追溯调用者

- 直接调用者（函数、方法）。
- 入口点（HTTP handler、CLI 命令、事件监听、定时任务）。
- 调用者超过 5 个时，只列最重要的 3 个并说明原因。

### 4. 向下列出依赖

- 核心依赖：对行为有实质影响的模块。
- 技术依赖：DB、网络、第三方库，标注为 Infrastructure。
- 超过 5 个时分组列出。

### 5. 评估模块深度

- 接口方法数和参数数。
- 接口背后封装了多少复杂度（Deep / Shallow）。
- 是否存在穿透方法：仅转发调用、不封装任何复杂度。

## 输出格式

```text
当前模块：<名称>
层级：<Interface / Application / Domain / Infrastructure>
领域术语：<CONTEXT.md 对应词>

调用者：
- <调用者> → 通过 <接口/方法> → 目的：<一句话>

依赖：
- <依赖> [层级] → 提供：<一句话>

模块深度：
- 接口：<方法数 / 参数数>
- 封装：<Deep / Shallow>
- 穿透方法：<有 / 无，如有列出>

架构摩擦（如有）：
- <一句话>
```

## 衔接

- 发现架构摩擦 → `engineering/improve-architecture`
- 术语不一致、模块边界模糊 → `decision/decision-forge`
- 看清上下文后继续实现 → `engineering/tdd`

## 禁止行为

- 不读代码就绘制地图。
- 用框架名替代领域术语。
- 把这个 skill 当架构改进用——它只负责"看清楚"，不负责"改好"。
