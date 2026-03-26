---
name: discovery-doc-sync
description: Use when aligning a Discovery-style project's requirement, design, implementation, and acceptance documents so that the spec chain matches the actual system behavior and scope.
---

# Discovery Document Sync

Use this skill when a discovery project has drift between requirement documents, design documents, implementation, and acceptance artifacts.

## What This Skill Covers

- identify document drift
- align requirement and design layers
- align design and implementation layers
- distinguish delivered scope from deferred scope
- update closure and acceptance wording

## Workflow

1. Read `references/spec-chain.md`.
2. Read `references/drift-checklist.md`.
3. Identify the baseline documents:
   SOW, project specification, design docs, acceptance docs.
4. Identify the implementation sources:
   code, API routes, UI flows, tests, scripts, and runtime behavior.
5. Compare by layer:
   requirement -> design -> implementation -> acceptance.
6. Mark each mismatch as one of:
   outdated doc, missing implementation, deferred scope, environment-limited validation.
7. Update documents with current truth and preserve scope boundaries.
8. Confirm no document still claims an undelivered class, module, workflow, or validation result.

## Guardrails

- Do not "fix" drift by overstating implementation.
- Keep deferred items explicit instead of silently removing them.
- Separate default-disabled capability from truly unimplemented capability.
- When multiple documents disagree, prefer current code and validated evidence, then update the spec chain to match.

## Bundled Resources

- `references/spec-chain.md`
- `references/drift-checklist.md`
- `scripts/doc_sync_check.sh`
