# Validation Strategy

## Goal

Prove that the actual runtime path works against live cloud accounts.

## Minimum validation chain

For each validation target, try to preserve this chain:

1. account exists and passes verification
2. vendor pack version is online
3. region and zone inputs are known
4. task executes through the real scheduler or execution path
5. resource records or valid empty-result evidence are captured

## Validation levels

- `real-cloud validated`: the task runs successfully with live credentials and returns real records
- `empty-result validated`: the task runs successfully with live credentials but finds no resources
- `blocked by environment`: the code path exists but the current account, region, quota, or permission prevents proof
- `failed`: the runtime path errors and needs triage

## Practical ordering

Validate in this order:

1. accounts with the broadest resource footprint
2. core infrastructure resources first
3. higher-risk or less stable adapters next
4. mock-only vendors last, clearly labeled as non-real-cloud
