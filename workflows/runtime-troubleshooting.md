# Runtime Troubleshooting Workflow

Use this workflow when a Discovery-style project is failing in startup, sync, task execution, or runtime operations.

## Inputs

- incident time and environment
- visible error message or symptom
- affected vendor, account, or pack
- logs, task id, or API response if available

## Steps

1. Confirm the failing entrypoint and impact scope.
2. Check runtime state: process, port, database, worker, and scheduler.
3. Check pack state, account verification, and environment configuration.
4. Narrow the issue to one layer before editing code.
5. Verify with evidence from logs, API responses, or persisted task state.
6. Apply the smallest safe recovery or code fix.
7. Re-run the failing path and one adjacent shared path.
8. Record the outcome and residual risk.

## Output

- root-cause summary
- workaround or fix plan
- post-fix validation note
