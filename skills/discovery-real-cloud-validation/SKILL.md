---
name: discovery-real-cloud-validation
description: Use when planning or executing real-cloud validation for a Discovery-style project, including account readiness checks, resource-by-resource validation targets, empty-result evidence, and customer-facing validation summaries.
---

# Discovery Real-Cloud Validation

Use this skill when you need to prove that a Discovery-style system really works against live cloud accounts.

## What This Skill Covers

- validation target planning by vendor and resource type
- account and region readiness checks
- distinction between real-cloud, empty-result, and mock-only evidence
- evidence capture for execution results
- customer-facing validation summary writing

## Workflow

1. Read `references/validation-strategy.md`.
2. Read `references/empty-result-rules.md`.
3. Read `references/evidence-fields.md`.
4. Identify the validation scope:
   vendor, account, resource type, region, zone, and expected result.
5. Confirm the runtime path is ready:
   credentials, pack status, scheduler or worker requirements, and API or UI entrypoint.
6. Execute validation and capture:
   task id, start and end time, result, returned count, and failure message if any.
7. Classify each result as:
   real-cloud validated, empty-result validated, blocked by environment, or failed.
8. Produce a concise summary that clearly separates delivered capability from account-limited evidence.

## Guardrails

- Do not claim validation only from adapter code or unit tests.
- Do not downgrade a successful empty-result run if the real runtime path completed.
- Do not mix environment problems with implementation bugs in the same conclusion.
- Keep raw secrets, temporary tokens, and full credential payloads out of evidence files.

## Bundled Resources

- `references/validation-strategy.md`
- `references/empty-result-rules.md`
- `references/evidence-fields.md`
- `scripts/build_validation_targets.py`
