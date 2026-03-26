---
name: discovery-pack-development
description: Use when adding or revising a Discovery-style resource pack, adapter, version registration, online-offline behavior, and the related tests and documents.
---

# Discovery Pack Development

Use this skill when implementing a new resource type or updating an existing pack-based integration.

## What This Skill Covers

- adapter contract checks
- pack metadata design
- pack version registration
- online and offline behavior
- resource model alignment
- test and document updates

## Workflow

1. Read `references/adapter-contract.md`.
2. Read `references/resource-model-mapping.md`.
3. Define pack metadata:
   vendor, resource domain, resource type, auth mode, sdk entry.
4. Implement or update the adapter.
5. Register the pack version and decide expected online state.
6. Verify task binding behavior for online and offline versions.
7. Add or update tests.
8. Update project specification, API, database, and acceptance documents if behavior changed.

## Guardrails

- A pack is not complete until version behavior is validated.
- Do not describe a resource as supported if only metadata exists and adapter execution is missing.
- Keep mapping logic deterministic and traceable.
- Separate real-cloud validation evidence from unit-test evidence.

## Bundled Resources

- `references/adapter-contract.md`
- `references/pack-versioning.md`
- `references/resource-model-mapping.md`
- `scripts/scaffold_pack.py`
