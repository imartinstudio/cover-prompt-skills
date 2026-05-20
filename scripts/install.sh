#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT_DIR/skills"
TARGET_DIR="${COVER_SKILLS_TARGET:-$HOME/.shared-skills}"

usage() {
  cat <<'USAGE'
Usage:
  scripts/install.sh                 Install all skills
  scripts/install.sh cover-tips      Install one skill
  scripts/install.sh cover           Install all cover skills

Environment:
  COVER_SKILLS_TARGET=~/.shared-skills
USAGE
}

install_skill() {
  local name="$1"
  local src="$SKILLS_DIR/$name"
  local dst="$TARGET_DIR/$name"

  if [[ ! -d "$src" ]]; then
    echo "Skill not found: $name" >&2
    exit 1
  fi

  mkdir -p "$TARGET_DIR"

  if [[ -L "$dst" ]]; then
    rm "$dst"
  elif [[ -e "$dst" ]]; then
    echo "Target already exists and is not a symlink: $dst" >&2
    echo "Move it away or remove it before installing." >&2
    exit 1
  fi

  ln -s "$src" "$dst"
  echo "Installed: $name -> $dst"
}

main() {
  if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    exit 0
  fi

  local requested=("$@")
  if [[ ${#requested[@]} -eq 0 || "${requested[0]}" == "cover" || "${requested[0]}" == "all" ]]; then
    mapfile -t requested < <(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)
  fi

  for skill in "${requested[@]}"; do
    install_skill "$skill"
  done
}

main "$@"
