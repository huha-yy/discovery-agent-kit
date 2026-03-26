# GitHub 展示文案

## About 区简介

### 一行简介

面向 Discovery 风格多云资源发现项目的可复用智能体技能、工作流与交付模板仓库

### 仓库长描述

`discovery-agent-kit` 是一个面向 Discovery 风格多云资源发现项目的智能体资产仓库，用于沉淀和复用在实际项目中形成的通用能力。仓库提供可复用的技能（skills）、标准执行流程（workflows）、交付模板（templates）、项目初始化上下文（workspace）以及本地安装脚本（install），帮助团队在不同项目之间复用统一的方法论和交付方式，降低重复建设成本，提升研发、验收与运维协同效率。

当前已覆盖的能力包括：

- 云账号接入与校验
- 资源 Pack 开发与版本管理
- SOW 覆盖核对与验收证据整理
- 真实云验证计划与结果沉淀
- 启动异常、运行时异常、同步失败排障
- 规格、设计、实现、验收文档闭环

该仓库只保存可复用的智能体方法资产，不保存客户私有数据、真实凭证、运行截图、数据库文件或项目专属验收证据。

### Topics 建议

- `agents`
- `skills`
- `workflow`
- `multi-cloud`
- `discovery`
- `codex`
- `templates`

## 首个正式 Release

### Release 标题

`discovery-agent-kit v0.2.0`

### Release 正文

本版本是 `discovery-agent-kit` 的首个可对外复用发布版本，目标是将 Discovery 风格多云资源发现项目中沉淀下来的智能体方法资产独立出来，形成可复用、可迁移、可持续演进的共享仓库。

本次版本包含以下内容：

- 可复用技能（skills）
  - `discovery-account-onboarding`
  - `discovery-pack-development`
  - `discovery-sow-audit`
  - `discovery-doc-sync`
  - `discovery-release-review`
  - `discovery-real-cloud-validation`
  - `discovery-runtime-troubleshooting`
- 标准工作流（workflows）
  - 账号接入
  - Pack 开发
  - SOW 验收核对
  - 文档闭环
  - 发布检查
  - 真实云验证
  - 运行时排障
- 交付模板（templates）
  - 项目规格说明模板
  - API 设计模板
  - 数据库设计模板
  - SOW 覆盖矩阵模板
  - 云上验证报告模板
  - 真实云验证计划模板
  - 运行时事件摘要模板
- 项目初始化资产（workspace）
  - 工作区模板
  - 项目接入模板
  - 已知限制模板
- 发布配套资料
  - `LICENSE`
  - `PUBLISHING.md`
  - 双语 README
  - `RELEASE-NOTES.md`
  - `CONTRIBUTING.md`

本版本重点增强：

- 将真实云验证能力标准化，支持验证目标规划、空结果判定、验证证据整理
- 将运行时排障能力标准化，支持启动失败、任务执行失败、同步异常、Pack/适配器问题的分层诊断
- 将仓库整理为可发布状态，补齐许可证、发布说明、贡献指南和双语文档结构

适用场景：

- 希望在多个 Discovery 风格项目之间复用统一智能体方法的团队
- 需要沉淀多云资源发现研发、验收、验证、排障经验的团队
- 希望将项目私有实现与通用方法资产分离管理的团队

注意事项：

- 本仓库只保存可复用方法资产，不保存客户私有数据
- 真实凭证、任务编号、截图、数据库文件和项目专属验收证据应保留在业务项目仓库中
- 当前版本建议从 `README.md` 进入，并根据需要切换 `README.en.md`
