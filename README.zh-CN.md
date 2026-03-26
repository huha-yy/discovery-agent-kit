# Discovery Agent Kit

[English](./README.en.md) | [简体中文](./README.zh-CN.md)

Discovery Agent Kit 是一个从企业级多云资源发现项目中抽取出来的、可复用的智能体资产仓库。

它面向需要在多个项目之间复用统一工作方法的团队，而不仅仅服务于单一业务代码库。

## 仓库结构

- `skills/`：可复用的智能体能力
- `workflows/`：标准化执行流程
- `templates/`：交付、验收、验证类模板
- `workspace/`：新项目初始化上下文模板
- `install/`：本地安装到 Codex 兼容目录的脚本

## 适用场景

当你希望智能体在以下任务上保持一致的方法和输出时，可以使用这个仓库：

- 云账号接入与校验
- 资源 Pack 开发与版本管理
- SOW 覆盖核对与验收证据整理
- 真实云验证计划与结果沉淀
- 启动异常、运行时异常、同步失败排障
- 规格、设计、实现、验收文档闭环

## 当前能力清单

- `discovery-account-onboarding`
- `discovery-pack-development`
- `discovery-sow-audit`
- `discovery-doc-sync`
- `discovery-release-review`
- `discovery-real-cloud-validation`
- `discovery-runtime-troubleshooting`

## 本地安装

```bash
cd /Users/yangshuyun/Desktop/discovery-agent-kit
./install/install_to_codex.sh
```

默认会把本仓库中的 skills 同步到 `~/.codex/skills/discovery-agent-kit`。

## 版本规则

本仓库使用轻量级语义化版本规则：

- `MAJOR`：目录结构或兼容性存在破坏性变化
- `MINOR`：新增可复用 skill、workflow 或 template
- `PATCH`：文案修订、元数据修订、非破坏性脚本修复

当前推荐公开发布版本为 `v0.2.0`。

## 发布快捷流程

```bash
git add .
git commit -m "feat: prepare discovery-agent-kit for v0.2.0 release"
git tag -a v0.2.0 -m "discovery-agent-kit v0.2.0"
git push origin main --tags
```

完整发布检查请参考 `PUBLISHING.md`。

## 编写原则

不要把项目私有数据放进这个共享仓库。真实账号、任务编号、截图、数据库路径和客户验收证据应保留在业务项目仓库中。

## License

本仓库采用 Apache-2.0 许可证，见 `LICENSE`。
