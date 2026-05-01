---
name: repo-health
description: >
  从企业或维护者视角检查代码仓库健康度，包括 ownership、依赖、安全、
  ADR/CONTEXT 新鲜度、架构漂移、测试质量和质量门禁。
---

# Repo Health

Repo Health 用于轻量治理代码仓库，帮助维护者和管理者知道仓库是否可持续演进。

它不是审计表演，而是发现会阻碍交付、协作和维护的真实风险。

## 核心原则

- 治理服务于可持续交付。
- 只记录可行动问题。
- 风险必须有证据。
- 优先发现长期认知成本和变更风险。
- 不用通用最佳实践覆盖项目已有 ADR。

## 检查维度

### 1. Ownership

- 是否有明确维护者。
- 关键模块是否有人负责。
- 交接文档是否足够。

### 2. Architecture drift

- 代码是否偏离 CONTEXT、ADR 或 README 中的约定。
- 是否出现浅模块、跨层调用、抽象泄露。
- 是否需要 `engineering/architecture`。

### 3. Quality gates

- 测试是否可运行。
- CI 或本地校验是否清楚。
- 发布前检查是否定义。

### 4. Dependencies and security

- 依赖是否过旧或无人维护。
- 是否有已知安全风险。
- 密钥、权限、配置是否有泄露风险。

### 5. Documentation freshness

- README、CONTEXT、ADR、agents 配置是否反映当前代码。
- 过时文档是否会误导 agent 或开发者。

## 输出格式

```markdown
## 仓库健康报告

总体状态：健康 | 观察 | 高风险

发现：
1. <标题>
   证据：
   风险：
   推荐 skill：
   建议行动：

快速改进项：

需要重新审视的决策：

未检查项：
```

## 分流规则

- 架构问题 -> `engineering/architecture`。
- 决策冲突 -> `decision/decision-forge`。
- 运行风险 -> `operations/operate`。
- 发布风险 -> `operations/release`。
- 任务拆解 -> `governance/issue-breakdown`。

## 禁止行为

- 没有证据就打分。
- 把风格偏好当成治理问题。
- 忽略已有 ADR。
- 列出无法行动的大而空建议。

