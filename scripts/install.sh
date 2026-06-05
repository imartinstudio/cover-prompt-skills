#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGINS_DIR="$ROOT_DIR/plugins"
TARGET_DIR="${COVER_SKILLS_TARGET:-$HOME/.shared-skills}"
BACKUP_DIR="${COVER_SKILLS_BACKUP_DIR:-$TARGET_DIR/.cover-prompt-skills-backup}"

usage() {
  cat <<'USAGE'
Usage:
  scripts/install.sh                        Install all skills
  scripts/install.sh cover-black-white-minimal
  scripts/install.sh cover-trendy-color-poster
  scripts/install.sh cover-giant-perspective-poster
  scripts/install.sh cover-sketch-knowledge-poster
  scripts/install.sh cover-midnight-studio
  scripts/install.sh cover-pixel-avatar
  scripts/install.sh cover-budapest-poster
  scripts/install.sh cover-editorial-collage
  scripts/install.sh cover-light-product
  scripts/install.sh cover-mckinsey-briefing-style
  scripts/install.sh cover-tea-oriental
  scripts/install.sh illustration-sketch-ui
  scripts/install.sh all                    Install all skills

Environment:
  COVER_SKILLS_TARGET=~/.shared-skills
  COVER_SKILLS_BACKUP_DIR=~/.shared-skills/.cover-prompt-skills-backup

Note:
  cover-tips and sketch-knowledge-kit are navigator/kit skills. They are
  installed with all skills, but cannot be installed by themselves because they
  depend on concrete visual style skills.

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

install_skill() {
  local name="$1"
  local src="$PLUGINS_DIR/$name"
  local dst="$TARGET_DIR/$name"

  if [[ ! -d "$src" ]]; then
    echo "Skill not found: $name" >&2
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
    requested=()
    while IFS= read -r skill; do
      requested+=("$skill")
    done < <(find "$PLUGINS_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)
  elif [[ ${#requested[@]} -eq 1 && ( "${requested[0]}" == "cover-tips" || "${requested[0]}" == "sketch-knowledge-kit" ) ]]; then
    echo "${requested[0]} cannot be installed by itself." >&2
    echo "It is only a navigator/kit. Install all skills instead:" >&2
    echo "  scripts/install.sh" >&2
    echo "Or install a concrete style skill, for example:" >&2
    echo "  scripts/install.sh cover-editorial-collage" >&2
    exit 1
  fi

  for skill in "${requested[@]}"; do
    install_skill "$skill"
  done
}

main "$@"
