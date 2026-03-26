#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
Discovery release gate
1. Confirm release scope and deferred items
2. Start application and verify runtime status
3. Run smoke and key-path tests
4. Verify key GUI/API flows
5. Assemble evidence package
6. Record known limitations and environment-limited items
EOF
