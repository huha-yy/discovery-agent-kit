# Publishing Guide

Use this checklist when publishing `discovery-agent-kit` to a shared remote repository.

## Recommended Repository Description

`Reusable agent skills, workflows, and templates for Discovery-style multi-cloud resource discovery projects`

## Recommended Topics

- `agents`
- `skills`
- `workflow`
- `multi-cloud`
- `discovery`
- `codex`
- `templates`

## Version Recommendation

Publish the next public release as `v0.2.0`.

Why:

- `v0.1.0` established the repository
- the current unreleased work adds two new reusable skills
- matching workflows, templates, and release metadata were also added
- these are additive, non-breaking changes, so a minor release is appropriate

## Pre-Release Checklist

Run these checks before tagging:

```bash
find skills -name SKILL.md | sort
find skills -path '*/agents/openai.yaml' | sort
find workflows templates workspace -type f | sort
python3 skills/discovery-real-cloud-validation/scripts/build_validation_targets.py /tmp/in.tsv /tmp/out.csv
python3 skills/discovery-runtime-troubleshooting/scripts/build_incident_summary.py /tmp/in.tsv /tmp/out.csv
git status
```

Also confirm:

- no project-private keys, screenshots, database paths, or task IDs remain
- every skill has a concise trigger description
- top-level docs and release notes mention the latest assets

## Publish Steps

```bash
git add .
git commit -m "feat: prepare discovery-agent-kit for v0.2.0 release"
git tag -a v0.2.0 -m "discovery-agent-kit v0.2.0"
git push origin main
git push origin v0.2.0
```

## Suggested Release Title

`discovery-agent-kit v0.2.0`

## Suggested Release Summary

This release prepares `discovery-agent-kit` for wider reuse across teams and projects. It adds:

- real-cloud validation guidance and planning assets
- runtime troubleshooting guidance and incident templates
- a repository license and a concrete publishing path

## After Publishing

- verify the remote tag exists
- verify `LICENSE`, `README.md`, and `RELEASE-NOTES.md` render correctly
- if the repository will be public, add a short repository homepage/about blurb in the hosting platform
