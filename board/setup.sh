#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -n "${PYTHON:-}" ]]; then
  PYTHON_BIN="$PYTHON"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN=python
else
  printf '%s\n' '需要 Python 3。安装后重试，或设置 PYTHON 为解释器路径。' >&2
  exit 1
fi
exec "$PYTHON_BIN" "$SCRIPT_DIR/import_board.py" "$@"
