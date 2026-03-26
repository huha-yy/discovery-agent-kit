# Failure Taxonomy

## Configuration

Typical signs:

- wrong port
- missing `.env` value
- invalid SQLite path
- duplicate process using the same runtime files

## Dependency

Typical signs:

- package import error
- missing SDK
- startup crash before application routing is available

## Credential

Typical signs:

- account verification fails
- vendor API returns auth or signature errors
- token or key fields are incomplete

## Pack-state

Typical signs:

- verification or task behavior changes when a pack version is offline
- new tasks cannot bind the expected version
- runtime resolves to the wrong version

## Adapter bug

Typical signs:

- real API shape differs from code expectation
- pagination or nested field parsing fails
- only one vendor or resource type breaks

## Data-shape mismatch

Typical signs:

- schema validation fails
- repository write fails after a successful adapter call
- UI expects fields that the API no longer returns

## Concurrency or runtime state

Typical signs:

- SQLite lock
- duplicate worker execution
- task remains pending or retrying unexpectedly

## External-cloud limitation

Typical signs:

- current account has no resources
- permission scope is incomplete
- cloud-side quota, region, or API availability blocks proof
