# Discovery Agent Kit

Discovery Agent Kit is a standalone repository for reusable agent assets extracted from enterprise multi-cloud discovery projects.

It is intended for teams that need repeatable agent behavior across projects, not just inside one codebase. The repository separates:

- `skills/`: reusable agent capabilities
- `workflows/`: fixed SOP-style execution flows
- `templates/`: reusable delivery and acceptance templates
- `workspace/`: project bootstrap context templates
- `install/`: scripts for syncing skills into local Codex-compatible directories

## Intended Use

Use this repository when you want an agent to work consistently on tasks such as:

- onboarding cloud accounts
- developing and registering new resource packs
- auditing SOW coverage and acceptance evidence
- planning and packaging real-cloud validation runs
- troubleshooting startup, runtime, and sync failures
- closing specification and design document drift

## Current Asset Set

- `discovery-account-onboarding`
- `discovery-pack-development`
- `discovery-sow-audit`
- `discovery-doc-sync`
- `discovery-release-review`
- `discovery-real-cloud-validation`
- `discovery-runtime-troubleshooting`

## Local Installation

```bash
cd /Users/yangshuyun/Desktop/discovery-agent-kit
./install/install_to_codex.sh
```

By default, this copies the repository skills into `~/.codex/skills/discovery-agent-kit`.

## Versioning

This repository follows a lightweight semantic versioning rule:

- `MAJOR`: breaking structure or compatibility changes
- `MINOR`: new reusable skills, workflows, or templates
- `PATCH`: wording fixes, metadata fixes, or non-breaking script updates

The recommended next public release is `v0.2.0` because the repository now includes two additional reusable skills and their matching workflow and template assets.

## Publishing Quick Path

```bash
git add .
git commit -m "feat: prepare discovery-agent-kit for v0.2.0 release"
git tag -a v0.2.0 -m "discovery-agent-kit v0.2.0"
git push origin main --tags
```

For the full release checklist, see `PUBLISHING.md`.

## License

This repository is prepared for publication under the Apache-2.0 license. See `LICENSE`.

## Authoring Rule

Keep project-specific data out of this repository. Real account IDs, task IDs, screenshots, and project-private acceptance evidence should remain in the business project repository.
