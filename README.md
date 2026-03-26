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
- closing specification and design document drift

## Initial Asset Set

- `discovery-account-onboarding`
- `discovery-pack-development`
- `discovery-sow-audit`

## Local Installation

```bash
cd /Users/yangshuyun/Desktop/discovery-agent-kit
./install/install_to_codex.sh
```

By default, this copies the repository skills into `~/.codex/skills/discovery-agent-kit`.

## Authoring Rule

Keep project-specific data out of this repository. Real account IDs, task IDs, screenshots, and project-private acceptance evidence should remain in the business project repository.
