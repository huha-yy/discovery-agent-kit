#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_BASE="${1:-${HOME}/.codex/skills/discovery-agent-kit}"

mkdir -p "${TARGET_BASE}"
rsync -a --delete "${ROOT_DIR}/skills/" "${TARGET_BASE}/"

echo "Synced skills to ${TARGET_BASE}"
