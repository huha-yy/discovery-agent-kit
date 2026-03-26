# Resource Model Mapping

Minimum mapped fields:

- `cloud_vendor`
- `account_id`
- `resource_domain`
- `resource_type`
- `resource_id`

Strongly recommended mapped fields:

- `resource_name`
- `display_name`
- `status`
- `raw_status`
- `tags`
- `spec_json`
- `network_json`
- `security_json`
- `relationships_json`
- `raw_payload`
- `source_pack_code`
- `source_pack_version`

Mapping rule:

Put common queryable fields into first-class columns. Keep vendor-specific detail in JSON blobs.
