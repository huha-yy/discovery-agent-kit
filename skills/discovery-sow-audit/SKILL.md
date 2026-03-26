---
name: discovery-sow-audit
description: Use when auditing SOW coverage for a Discovery-style project, classifying evidence into real-cloud validation, empty-result validation, and mock-only validation, and producing coverage matrices or acceptance summaries.
---

# Discovery SOW Audit

Use this skill when you need to judge whether a project really satisfies a discovery-system SOW.

## What This Skill Covers

- normalize resource inventory from SOW
- compare implementation scope against SOW scope
- classify evidence levels
- build coverage matrix and summary
- identify true gaps versus environment-limited gaps

## Workflow

1. Read `references/coverage-rules.md`.
2. Read `references/acceptance-levels.md`.
3. Read `references/evidence-checklist.md`.
4. Build the expected resource and capability matrix from the SOW.
5. Check implementation evidence:
   code, tests, real-cloud runs, reports, UI, API, and documents.
6. Classify each row:
   real-cloud validated, empty-result validated, mock-only, or missing.
7. Summarize gaps by vendor and by capability.
8. Produce a decision statement that clearly separates implementation completeness from environment limitations.

## Guardrails

- Do not call mock-only support "delivered" if the acceptance standard requires real-cloud proof.
- Do not downgrade empty-result validation when the runtime path truly executed successfully.
- Separate resource support from functional support. A project can support a resource type but still miss acceptance evidence.
- Always list remaining blockers explicitly.

## Bundled Resources

- `references/coverage-rules.md`
- `references/acceptance-levels.md`
- `references/evidence-checklist.md`
- `scripts/build_coverage_matrix.py`
