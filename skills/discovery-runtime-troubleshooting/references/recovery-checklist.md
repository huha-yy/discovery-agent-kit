# Recovery Checklist

## Immediate containment

- confirm whether the issue blocks startup, a single task, or one vendor only
- preserve the first clear error message before retrying repeatedly
- avoid changing multiple layers at once during diagnosis

## Quick recovery options

- restart the app, worker, or scheduler after confirming configuration
- bring the required pack version online
- re-run account verification after credential correction
- retry the task only after the root cause is narrowed

## Code-fix follow-up

After a fix, verify:

- startup and health check
- the original failing path
- one adjacent path that uses the same shared service
- documentation or acceptance evidence if operational behavior changed

## Recommended incident summary fields

- issue title
- impact scope
- failing layer
- root cause
- workaround
- permanent fix
- validation result
- residual risk
