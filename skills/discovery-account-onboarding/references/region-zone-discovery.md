# Region And Zone Discovery

Use region and zone discovery after credential verification, not before.

Expected outcomes:

- `region_scope`: supported regions for the account
- `zone_scope`: supported zones across regions
- `region_zone_mapping`: region-to-zone map

Acceptance notes:

- real-cloud validation: SDK call succeeds against the vendor account
- empty result is not success unless the platform genuinely supports no regions or mock mode
- unsupported vendors must be marked explicitly, not silently skipped
