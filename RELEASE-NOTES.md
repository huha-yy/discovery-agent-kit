# Release Notes

## v0.2.0

Recommended next public release.

### Included in this release

- reusable skill: `discovery-real-cloud-validation`
- reusable skill: `discovery-runtime-troubleshooting`
- workflow: `workflows/real-cloud-validation.md`
- workflow: `workflows/runtime-troubleshooting.md`
- template: `templates/real-cloud-validation-plan-template.md`
- template: `templates/runtime-incident-template.md`
- publish-ready repository metadata:
  - `LICENSE`
  - `PUBLISHING.md`
  - `README.md` versioning and publish guidance

### Release intent

This release moves the repository from an internal starter state to a shareable, publish-ready reusable asset kit.

## v0.1.2

### Added

- reusable skill: `discovery-runtime-troubleshooting`
- workflow: `workflows/runtime-troubleshooting.md`
- template: `templates/runtime-incident-template.md`

### Intent

This update adds a reusable troubleshooting path for startup failures, task execution failures, adapter issues, and evidence-friendly incident summaries.

## v0.1.1

### Added

- reusable skill: `discovery-real-cloud-validation`
- workflow: `workflows/real-cloud-validation.md`
- template: `templates/real-cloud-validation-plan-template.md`

### Intent

This update adds a standard way to plan, classify, and summarize live-account validation without mixing real-cloud evidence with mock-only support.

## v0.1.0

Initial standalone release of `discovery-agent-kit`.

### Included in this release

- repository-level guidance:
  - `README.md`
  - `AGENTS.md`
- reusable skills:
  - `discovery-account-onboarding`
  - `discovery-pack-development`
  - `discovery-sow-audit`
  - `discovery-doc-sync`
  - `discovery-release-review`
- reusable workflows:
  - account onboarding
  - pack development
  - SOW acceptance
  - document closure
  - release check
- reusable templates:
  - project specification
  - API design
  - database design
  - SOW coverage matrix
  - cloud validation report
- workspace templates:
  - workspace baseline
  - project onboarding
  - known limitations
- local install scripts for syncing skills into Codex-compatible directories

### Release intent

This release establishes the repository as a reusable agent-method asset kit for Discovery-style multi-cloud resource discovery projects. It is designed to separate project-specific runtime evidence from reusable agent knowledge, workflows, and templates.

### Known limits

- no packaged distribution yet
- no automated validation pipeline yet
- no icons or extended UI metadata beyond basic `openai.yaml`
- installation currently assumes a local Codex-style directory layout

### Recommended initial tag

`v0.1.0`

### Recommended first commit message

`feat: initialize discovery-agent-kit with reusable skills, workflows, and templates`
