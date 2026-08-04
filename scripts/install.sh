#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGINS_DIR="$ROOT_DIR/plugins"
INSTALL_INDEX="$ROOT_DIR/generated/install-index.sh"
TARGET_DIR="${COVER_SKILLS_TARGET:-$HOME/.shared-skills}"
BACKUP_DIR="${COVER_SKILLS_BACKUP_DIR:-$TARGET_DIR/.cover-prompt-skills-backup}"

if [[ ! -f "$INSTALL_INDEX" ]]; then
  echo "Generated install inventory is missing: $INSTALL_INDEX" >&2
  echo "Run: python3 scripts/skill_registry.py generate" >&2
  exit 1
fi

# This file is generated from the plugin directories and manifests.  Both the
# local installer and the remote root installer consume this same file.
# shellcheck source=/dev/null
source "$INSTALL_INDEX"

usage() {
  cat <<'USAGE'
Usage:
  scripts/install.sh                        Install all generated skills
  scripts/install.sh <skill-name>            Install one generated skill
  scripts/install.sh all                    Install all skills

Environment:
  COVER_SKILLS_TARGET=~/.shared-skills
  COVER_SKILLS_BACKUP_DIR=~/.shared-skills/.cover-prompt-skills-backup

Existing non-symlink skill directories are moved to a timestamped backup
directory before installing symlinks.
USAGE
}

backup_existing_target() {
  local name="$1"
  local dst="$2"
  local stamp
  local backup

  stamp="$(date +%Y%m%d%H%M%S)"
  backup="$BACKUP_DIR/$stamp/$name"
  mkdir -p "$(dirname "$backup")"
  mv "$dst" "$backup"
  echo "Backed up existing target: $dst -> $backup"
}

is_known_skill() {
  local candidate="$1"
  local skill
  for skill in "${ALL_SKILLS[@]}"; do
    if [[ "$skill" == "$candidate" ]]; then
      return 0
    fi
  done
  return 1
}

install_skill() {
  local name="$1"
  local src="$PLUGINS_DIR/$name"
  local dst="$TARGET_DIR/$name"

  if ! is_known_skill "$name" || [[ ! -d "$src" ]]; then
    echo "Skill is not in the generated inventory: $name" >&2
    exit 1
  fi

  mkdir -p "$TARGET_DIR"

  if [[ -L "$dst" ]]; then
    rm "$dst"
  elif [[ -e "$dst" ]]; then
    backup_existing_target "$name" "$dst"
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
  if [[ ${#requested[@]} -eq 0 || "${requested[0]}" == "all" ]]; then
    requested=("${ALL_SKILLS[@]}")
  fi

  for skill in "${requested[@]}"; do
    install_skill "$skill"
  done
}

main "$@"
