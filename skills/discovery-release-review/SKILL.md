---
name: discovery-release-review
description: Use when preparing a Discovery-style project for customer review, release, or staged acceptance, including startup checks, key path verification, evidence packaging, and residual risk recording.
---

# Discovery Release Review

Use this skill before customer demos, staged delivery, release packaging, or acceptance walkthroughs.

## What This Skill Covers

- startup and runtime checks
- API and UI smoke checks
- evidence packaging
- residual risk capture
- environment-limited scope labeling

## Workflow

1. Read `references/pre-release-checklist.md`.
2. Read `references/evidence-package.md`.
3. Confirm the intended release scope and excluded items.
4. Validate startup path:
   environment, database, port, worker, scheduler.
5. Validate key paths:
   account, pack, plan, task, resource, audit.
6. Confirm acceptance evidence:
   tests, screenshots, task records, resource counts, validation reports.
7. Record residual risks and environment-limited items explicitly.
8. Produce a release or handoff summary that distinguishes:
   delivered, deferred, and limited-by-environment items.

## Guardrails

- Do not call a path releasable if startup and key-path smoke checks were skipped.
- Do not mix customer-facing evidence with internal-only secrets or raw credentials.
- Do not hide known limitations to make the release summary look cleaner.

## Bundled Resources

- `references/pre-release-checklist.md`
- `references/evidence-package.md`
- `scripts/release_gate.sh`
