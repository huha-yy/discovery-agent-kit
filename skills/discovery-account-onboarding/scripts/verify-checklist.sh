#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
Discovery account onboarding checklist
1. Confirm cloud vendor and credential type
2. Normalize credential keys
3. Create or update account record
4. Run credential verification
5. Record verify_result and message
6. Run region/zone discovery if supported
7. Capture acceptance evidence without secrets
EOF
