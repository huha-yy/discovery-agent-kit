---
name: discovery-runtime-troubleshooting
description: Use when diagnosing a Discovery-style project's startup failure, runtime execution error, sync exception, adapter issue, worker or scheduler problem, or environment-specific operational regression.
---

# Discovery Runtime Troubleshooting

Use this skill when a Discovery-style project is failing at startup, during task execution, or while syncing live resources.

## What This Skill Covers

- startup failure triage
- worker and scheduler diagnostics
- adapter and pack execution failure analysis
- environment versus implementation fault isolation
- recovery recommendation and incident summary writing

## Workflow

1. Read `references/triage-model.md`.
2. Read `references/failure-taxonomy.md`.
3. Read `references/recovery-checklist.md`.
4. Identify the failing path:
   startup, account verify, region sync, plan execution, task retry, resource query, or UI/API action.
5. Capture the minimum incident facts:
   time, environment, account or vendor, pack version, task id, endpoint, and visible error.
6. Classify the issue as:
   configuration, dependency, credential, pack-state, adapter bug, data-shape mismatch, concurrency, or external-cloud limitation.
7. Verify the most likely layer with concrete evidence:
   logs, API response, database state, process state, or vendor response shape.
8. Produce a concise recovery plan that separates immediate workaround, code fix, and follow-up validation.

## Guardrails

- Do not jump to adapter-code conclusions before checking pack state, credentials, and runtime dependencies.
- Do not describe an environment outage as a code bug unless the execution evidence proves it.
- Do not hide the exact failing layer when writing customer-facing or handoff notes.
- Keep secrets, tokens, and full credential payloads out of logs and incident summaries.

## Bundled Resources

- `references/triage-model.md`
- `references/failure-taxonomy.md`
- `references/recovery-checklist.md`
- `scripts/build_incident_summary.py`
