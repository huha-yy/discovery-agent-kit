# Contributing

Thanks for improving `discovery-agent-kit`.

## Scope

This repository is for reusable agent assets only:

- skills
- workflows
- templates
- workspace bootstrap files
- install helpers

Do not add customer-private runtime data such as credentials, screenshots, task IDs, database paths, or project-specific acceptance evidence.

## Contribution Rules

- keep assets project-agnostic
- prefer concise `SKILL.md` files and move detail into `references/`
- use ASCII filenames for portability
- update top-level docs when adding a new reusable asset
- keep scripts small, deterministic, and executable when needed

## Recommended Flow

1. Create or update the target skill, workflow, template, or workspace file.
2. Verify the asset is still reusable outside one specific project.
3. Run lightweight checks:

```bash
find skills -name SKILL.md | sort
find skills -path '*/agents/openai.yaml' | sort
find workflows templates workspace -type f | sort
```

4. If you changed helper scripts, run a minimal sample input through them.
5. Update `README.md`, `README.en.md`, `README.zh-CN.md`, or `RELEASE-NOTES.md` when the repository capability changes.

## Commit Style

Preferred commit prefixes:

- `feat:`
- `docs:`
- `fix:`
- `refactor:`
- `test:`

Examples:

- `feat: add discovery-runtime-troubleshooting skill`
- `docs: refresh bilingual README`
- `fix: correct release publishing instructions`

## Publishing Notes

If the change affects a public release:

- update `RELEASE-NOTES.md`
- review `PUBLISHING.md`
- choose the next version using the versioning rule in `README.en.md`

## Review Checklist

Before submitting, confirm:

- the asset trigger and purpose are clear
- wording is reusable and not tied to one client project
- no sensitive data is included
- related docs are updated
