#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${HOME}/.codex/skills/discovery-agent-kit"

mkdir -p "${TARGET_DIR}"
rsync -a --delete "${ROOT_DIR}/skills/" "${TARGET_DIR}/"

echo "Installed skills to ${TARGET_DIR}"
