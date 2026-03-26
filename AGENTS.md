# Repository Guidelines

## Purpose

This repository stores reusable agent assets for Discovery-style multi-cloud resource discovery projects. It is not a business system repository and should not contain project-private runtime data.

## Structure

```text
skills/      reusable agent skills
workflows/   fixed project execution flows
templates/   reusable delivery templates
workspace/   project bootstrap context templates
install/     local installation and sync scripts
```

## Authoring Rules

- Prefer reusable instructions over project-specific history.
- Keep `SKILL.md` concise and move detail into `references/`.
- Use ASCII filenames for portability.
- Do not store real credentials, task IDs, screenshots, or local database paths from a client project.
- When a workflow depends on a tool or script, document the expected inputs and outputs explicitly.

## Validation

Before publishing changes:

```bash
find skills -name SKILL.md
find skills -path '*/agents/openai.yaml'
find workflows templates workspace -type f
```

Review every changed skill for:

- trigger clarity
- workflow completeness
- project-agnostic wording
- reusable evidence and template coverage
- absence of sensitive project data
