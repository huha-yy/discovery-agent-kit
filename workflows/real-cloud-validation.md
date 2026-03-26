# Real-Cloud Validation Workflow

Use this workflow when a Discovery-style project needs customer-facing proof that live account execution paths really work.

## Inputs

- SOW or scope baseline
- supported resource inventory
- available real accounts by vendor
- pack online status
- region and zone inventory

## Steps

1. Build the validation target list by vendor, account, resource type, and region.
2. Prioritize accounts that have the richest real resource coverage.
3. Confirm credentials, pack status, and runtime dependencies.
4. Execute each target through the intended runtime path.
5. Record task ids, counts, and result messages.
6. Classify each row as real-cloud, empty-result, blocked by environment, or failed.
7. Summarize remaining gaps without overstating delivery.

## Output

- validation target table
- execution evidence list
- customer-facing summary with residual risks
