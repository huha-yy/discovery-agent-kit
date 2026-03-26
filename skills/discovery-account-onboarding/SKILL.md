---
name: discovery-account-onboarding
description: Use when onboarding a new cloud account into a Discovery-style multi-cloud resource discovery system, including credential shape checks, account creation flow, verification, region and zone discovery, and evidence capture for acceptance.
---

# Discovery Account Onboarding

Use this skill for account onboarding tasks in multi-cloud discovery projects.

## What This Skill Covers

- normalize credential fields by vendor
- create or update account records
- run verification
- discover regions and zones
- capture acceptance evidence
- distinguish real-cloud validation from mock-only validation

## Workflow

1. Identify vendor, credential type, and intended validation level.
2. Read `references/account-model.md` for minimum account fields.
3. Read `references/credential-patterns.md` for vendor-specific credential keys.
4. If region or zone discovery is required, read `references/region-zone-discovery.md`.
5. Create the account in the target system.
6. Run verification and record result, message, and timestamp.
7. If verification succeeds, run region and zone discovery when supported.
8. Record acceptance evidence:
   account code, vendor, region scope, zone scope, verification result, and any limitations.

## Guardrails

- Do not assume all vendors share the same credential keys.
- Do not claim real-cloud validation if the path only passed with mocks.
- Record whether failure is auth, network, dependency, or unsupported-vendor related.
- Keep raw secrets out of logs, screenshots, and acceptance notes.

## Bundled Resources

- `references/account-model.md`
- `references/credential-patterns.md`
- `references/region-zone-discovery.md`
- `scripts/verify-checklist.sh`
