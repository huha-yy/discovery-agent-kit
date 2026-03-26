# Account Model

Minimum fields for a Discovery-style account record:

- `account_code`
- `account_name`
- `cloud_vendor`
- `credential_type`
- `credential_content`

Common optional fields:

- `tenant_or_project`
- `region_scope`
- `zone_scope`
- `region_zone_mapping`
- `remarks`

Expected output evidence:

- account created or updated
- verification status
- verification message
- region and zone ranges if discovery is supported
