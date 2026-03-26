# Discovery Agent Kit

[English](./README.en.md) | [简体中文](./README.zh-CN.md)

Reusable agent skills, workflows, and templates for Discovery-style multi-cloud resource discovery projects.

## Overview

Discovery Agent Kit packages reusable agent methods extracted from enterprise Discovery projects so teams can reuse the same delivery logic across multiple repositories.

## Features

- reusable `skills/` for account onboarding, pack development, SOW audit, validation, and troubleshooting
- SOP-style `workflows/` for repeatable execution and review
- `templates/` for specification, validation, acceptance, and incident outputs
- `workspace/` bootstrap context files for new project setup
- `install/` scripts for local Codex-compatible installation

## Included Skill Set

- `discovery-account-onboarding`
- `discovery-pack-development`
- `discovery-sow-audit`
- `discovery-doc-sync`
- `discovery-release-review`
- `discovery-real-cloud-validation`
- `discovery-runtime-troubleshooting`

## Typical Use Cases

- standardize agent behavior across Discovery-style projects
- bootstrap a new multi-cloud discovery workspace quickly
- reuse acceptance, validation, and troubleshooting methods
- keep reusable agent knowledge separate from customer-private evidence

## Quick Start

```bash
cd /Users/yangshuyun/Desktop/discovery-agent-kit
./install/install_to_codex.sh
```

## Documentation

For full usage, publishing, and versioning details:

- English: `README.en.md`
- 中文: `README.zh-CN.md`
- publishing: `PUBLISHING.md`
- release notes: `RELEASE-NOTES.md`
- contribution guide: `CONTRIBUTING.md`

## License

Apache-2.0. See `LICENSE`.
