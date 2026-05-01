---
name: operate
description: >
  管理上线后的运行维护生命周期，包括 observability、runbook、incident intake、
  性能和错误监控、维护节奏与反馈交接。
---

# Operate

Operate 用于回答：系统上线后如何被观察、维护和改进。

它把生产问题、运行信号和维护任务连接到诊断、反馈和治理流程。

## 核心原则

- 先能观察，再谈优化。
- Incident 先恢复服务，再做根因分析。
- Runbook 必须让下一个人更快处理同类问题。
- 运行信号应进入反馈和 roadmap。
- 维护节奏要轻量、可持续。

## 使用流程

### 1. 建立运行视图

记录：

- 核心用户路径。
- 关键健康信号：错误率、延迟、任务失败、资源使用、业务指标。
- 日志、指标、trace 或手动检查入口。
- 外部依赖和降级方式。

### 2. 编写 runbook

每个关键问题至少包含：

- 症状。
- 快速确认方式。
- 缓解步骤。
- 升级条件。
- 相关 dashboard、日志或命令。

### 3. Incident intake

当出现问题：

- 记录影响范围和开始时间。
- 先恢复或缓解。
- 使用 `governance/diagnose-lite` 查根因。
- 修复后记录复盘和回归测试。

### 4. 维护和交接

- 稳定性问题 -> `governance/diagnose-lite`。
- 用户反馈 -> `product/feedback-to-roadmap`。
- 架构性运行摩擦 -> `engineering/architecture`。
- 仓库治理问题 -> `governance/repo-health`。

## 输出格式

```markdown
## Operations Notes

Health signals:

Runbook:
- Symptom:
- Check:
- Mitigation:
- Escalation:

Incidents:

Maintenance cadence:

Follow-up:
```

## 禁止行为

- 只在事故后临时找日志。
- 把恢复服务和根因分析混为一谈。
- Incident 修完不补回归验证。
- 运行反馈不交接到 roadmap。

