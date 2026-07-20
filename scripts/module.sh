#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    LEGACY="$(cd "$ROOT/.." && pwd)/verification_planning_management"
    if [[ -d "$LEGACY" ]]; then
      echo "[OK] legacy course present: $LEGACY"
    else
      echo "[INFO] legacy verification_planning_management not checked out"
    fi
    [[ -f "$MOD_DIR/EXAMPLES.md" ]] && echo "[OK] EXAMPLES.md"
    [[ -f "$MOD_DIR/CHECKLIST.md" ]] && echo "[OK] CHECKLIST.md"
    [[ -f "$MOD_DIR/transcript.md" ]] && echo "[OK] transcript.md (module-slides)"
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
