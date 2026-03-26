#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
Discovery document sync checklist
1. Identify baseline requirement files
2. Identify design files
3. Identify implementation sources
4. Compare API, module names, runtime defaults, and scope statements
5. Mark each mismatch as stale doc, missing implementation, deferred scope, or validation gap
6. Update wording without overstating delivery
EOF
