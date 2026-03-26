# Pack Versioning

Pack metadata and pack version are separate concerns.

Pack metadata usually holds:

- `pack_code`
- `pack_name`
- `cloud_vendor`
- `resource_domain`
- `resource_type`

Pack version usually holds:

- `version`
- `auth_mode`
- `sdk_entry`
- optional request and response mapping
- optional config schema

Validation points:

- online version should be resolvable for new tasks
- offline version should not be used for new tasks
- account verification may use a non-online best-fit version if the project explicitly allows it
