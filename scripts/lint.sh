#!/usr/bin/env bash
#
# lint.sh — Lint all files in this repo
#   JSON   — python3 -m json.tool
#   MD     — markdownlint-cli2 (npx)
#   SH/BASH — bash -n syntax check
#
# Exit 0 on success, 1 on any lint error.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

HAS_ERROR=0

# ---- helpers ---------------------------------------------------------
red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }
dim()   { printf '\033[2m%s\033[0m\n' "$*"; }

section() {
  echo ""
  echo "============================================================"
  echo "  $*"
  echo "============================================================"
}

# ---- JSON -----------------------------------------------------------
lint_json() {
  section "JSON validation (python3 -m json.tool)"
  local files
  files=$(find . -name '*.json' -not -path './.git/*' -not -path './node_modules/*' -not -path './.playwright-mcp/*' | sort)

  if [ -z "$files" ]; then
    dim "  No JSON files found."
    return
  fi

  local ok=0 fail=0
  for f in $files; do
    if python3 -m json.tool "$f" /dev/null 2>/dev/null; then
      green "  OK  $f"
      ok=$((ok + 1))
    else
      red "  FAIL $f"
      fail=$((fail + 1))
    fi
  done
  echo ""
  echo "  JSON: $ok ok, $fail failed"
  [ "$fail" -eq 0 ] || HAS_ERROR=1
}

# ---- Markdown -------------------------------------------------------
lint_markdown() {
  section "Markdown lint (markdownlint-cli2)"
  local files
  files=$(find . -name '*.md' -not -path './.git/*' -not -path './node_modules/*' -not -path './.playwright-mcp/*' | sort)

  if [ -z "$files" ]; then
    dim "  No Markdown files found."
    return
  fi

  # markdownlint-cli2 exits non-zero on any warning; we capture and decide.
  if npx --yes markdownlint-cli2 $files 2>&1; then
    green "  Markdown: all OK"
  else
    red "  Markdown: lint errors found (see above)"
    HAS_ERROR=1
  fi
}

# ---- Shell scripts ---------------------------------------------------
lint_shell() {
  section "Shell script syntax check (bash -n)"
  local files
  files=$(find . -name '*.sh' -not -path './.git/*' -not -path './node_modules/*' -not -path './.playwright-mcp/*' | sort)

  if [ -z "$files" ]; then
    dim "  No shell scripts found."
    return
  fi

  local ok=0 fail=0
  for f in $files; do
    if bash -n "$f" 2>&1; then
      green "  OK  $f"
      ok=$((ok + 1))
    else
      red "  FAIL $f"
      fail=$((fail + 1))
    fi
  done
  echo ""
  echo "  Shell: $ok ok, $fail failed"
  [ "$fail" -eq 0 ] || HAS_ERROR=1
}

# ---- main ------------------------------------------------------------
main() {
  echo ""
  echo "  ╔══════════════════════════════════════════════════════╗"
  echo "  ║            🔍  Lint Check — Cover Prompt Skills      ║"
  echo "  ╚══════════════════════════════════════════════════════╝"

  lint_json
  lint_markdown
  lint_shell

  echo ""
  echo "============================================================"
  if [ "$HAS_ERROR" -eq 0 ]; then
    green "  ✅  All lint checks passed!"
    exit 0
  else
    red "  ❌  Lint errors found. Please fix them before committing."
    exit 1
  fi
}

main "$@"
