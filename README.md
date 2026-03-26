# Discovery Agent Kit

[简体中文](./README.md) | [English](./README.en.md)

Discovery Agent Kit 是一个面向 Discovery 风格多云资源发现项目的智能体资产仓库，用于沉淀和复用在实际项目中形成的通用能力。

仓库提供可复用的技能（`skills/`）、标准执行流程（`workflows/`）、交付模板（`templates/`）、项目初始化上下文（`workspace/`）以及本地安装脚本（`install/`），帮助团队在不同项目之间复用统一的方法论和交付方式，降低重复建设成本，提升研发、验收与运维协同效率。

## 核心特性

- 可复用 `skills/`：覆盖账号接入、Pack 开发、SOW 核对、真实云验证、运行时排障等高频任务
- 标准化 `workflows/`：沉淀可复用的执行流程，便于跨项目复制
- 结构化 `templates/`：统一规格、验证、验收、事件摘要等交付输出
- `workspace/` 初始化资产：帮助新项目快速建立上下文和协作基线
- `install/` 安装脚本：便于同步到本地 Codex 兼容环境

## 当前能力清单

- `discovery-account-onboarding`
- `discovery-pack-development`
- `discovery-sow-audit`
- `discovery-doc-sync`
- `discovery-release-review`
- `discovery-real-cloud-validation`
- `discovery-runtime-troubleshooting`

## 适用场景

- 云账号接入与校验
- 资源 Pack 开发与版本管理
- SOW 覆盖核对与验收证据整理
- 真实云验证计划与结果沉淀
- 启动异常、运行时异常、同步失败排障
- 规格、设计、实现、验收文档闭环

## 快速开始

```bash
cd /Users/yangshuyun/Desktop/discovery-agent-kit
./install/install_to_codex.sh
```

## 文档导航

- 英文文档：`README.en.md`
- 发布说明：`PUBLISHING.md`
- 版本记录：`RELEASE-NOTES.md`
- 贡献指南：`CONTRIBUTING.md`

## 使用边界

该仓库只保存可复用的智能体方法资产，不保存客户私有数据、真实凭证、运行截图、数据库文件或项目专属验收证据。

## License

本仓库采用 Apache-2.0 许可证，见 `LICENSE`。
