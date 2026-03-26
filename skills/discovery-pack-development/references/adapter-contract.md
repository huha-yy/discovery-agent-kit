# Adapter Contract

A Discovery-style adapter should implement:

- `verify(account, context) -> tuple[bool, str]`
- `list_resources(account, context) -> list[dict[str, Any]]`
- `get_resource(account, context) -> dict[str, Any] | None`

Required outcomes:

- verification returns a clear success flag and message
- full sync returns items ready for unified resource persistence
- single sync returns one mapped item or `None`

The adapter should not:

- write directly to HTTP responses
- manage UI state
- bypass pack version resolution rules
