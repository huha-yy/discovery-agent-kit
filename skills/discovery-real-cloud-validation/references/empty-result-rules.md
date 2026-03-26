# Empty-Result Rules

## Treat empty results as valid only when

- real credentials were used
- the execution path completed successfully
- the selected region or zone was actually queried
- logs or task records show a normal completion state
- the summary explicitly says that no resources were present

## Do not treat empty results as valid when

- verification failed before execution
- the pack version was offline or missing
- the task stopped before vendor API calls completed
- filtering was wrong and accidentally excluded the target scope
- the result is inferred only from code review or mocks

## Recommended wording

Use phrases like:

- "real-cloud empty-result validation completed successfully"
- "runtime path verified with no resources returned in the selected scope"
- "environment-limited proof remains because the account has no instances of this type"
