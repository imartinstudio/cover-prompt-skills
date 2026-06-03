#!/usr/bin/env bash
#
# setup-dev.sh — Configure the local repo for development.
#   Run this once after cloning.
#
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

echo "⚙️  Setting up development environment..."

# ---- git hooks -------------------------------------------------------
echo "  → Configuring git hooks path..."
git config core.hooksPath .githooks
green "    ✓ Git hooks active (.githooks/)"

# ---- verify tools ----------------------------------------------------
echo "  → Checking required tools..."

check_tool() {
  if command -v "$1" &>/dev/null; then
    green "    ✓ $1 found"
  else
    red "    ✗ $1 not found — some lint checks may be skipped"
  fi
}

red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }

check_tool python3
check_tool node      # for npx markdownlint-cli2
check_tool bash

echo ""
echo "============================================================"
green "  ✅  Development environment ready!"
echo ""
echo "  Git hooks installed:"
echo "    pre-commit  — lint check (JSON, Markdown, shell)"
echo "    pre-push    — lint check + block direct push to main"
echo ""
echo "  Features:"
echo "    • Direct push to 'main' is blocked — use PRs instead"
echo "    • JSON / Markdown / shell lint runs before commit & push"
echo "============================================================"
