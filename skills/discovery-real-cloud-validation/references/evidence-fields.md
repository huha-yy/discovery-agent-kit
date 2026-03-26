# Evidence Fields

Capture these fields for each validation row:

- vendor
- account code
- resource type
- pack code or pack version
- region
- zone
- validation date
- execution entrypoint: UI, API, script, or scheduler
- task id or request id
- result status
- returned count
- evidence level
- failure reason or limitation note

## Output shape

A concise validation table usually needs these columns:

| vendor | account_code | resource_type | region | zone | result | returned_count | evidence_level | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Summary rule

Always provide both:

- a row-level detail table
- a short overall summary by vendor and by evidence level
