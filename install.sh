#!/usr/bin/env bash
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main"
TARGET_DIR="${COVER_SKILLS_TARGET:-$HOME/.shared-skills}"
BACKUP_DIR="${COVER_SKILLS_BACKUP_DIR:-$TARGET_DIR/.cover-prompt-skills-backup}"

# Update this list when skills are added or removed
ALL_SKILLS=(
  cover-black-white-minimal
  cover-budapest-poster
  cover-editorial-collage
  cover-giant-perspective-poster
  cover-midnight-studio
  cover-pixel-avatar
  cover-light-product
  cover-mckinsey-briefing-style
  cover-tea-oriental
  cover-tips
  cover-trendy-color-poster
)

has_local_project() {
  [[ -d "plugins" && -x "scripts/install.sh" ]]
}

backup_existing_target() {
  local name="$1" dst="$2" stamp backup
  stamp="$(date +%Y%m%d%H%M%S)"
  backup="$BACKUP_DIR/$stamp/$name"
  mkdir -p "$(dirname "$backup")"
  mv "$dst" "$backup"
  echo "Backed up: $dst -> $backup"
}

install_from_local() {
  COVER_SKILLS_TARGET="$TARGET_DIR" scripts/install.sh "$@"
}

install_skill_remote() {
  local name="$1"
  local src_url="$REPO_RAW/plugins/$name/skills/$name/SKILL.md"
  local dst="$TARGET_DIR/$name"

  echo "Downloading $name..."

  mkdir -p "$TARGET_DIR"

  if [[ -L "$dst" ]]; then
    rm "$dst"
  elif [[ -d "$dst" ]]; then
    backup_existing_target "$name" "$dst"
  fi

  mkdir -p "$dst"
  if ! curl -fsSL "$src_url" -o "$dst/SKILL.md"; then
    echo "Failed to download: $name" >&2
    rm -rf "$dst"
    return 1
  fi
  echo "Installed: $name -> $dst"
}

main() {
  if has_local_project; then
    install_from_local "$@"
    return
  fi

  local requested=("$@")
  if [[ ${#requested[@]} -eq 0 || "${requested[0]}" == "cover" || "${requested[0]}" == "all" ]]; then
    requested=("${ALL_SKILLS[@]}")
  elif [[ ${#requested[@]} -eq 1 && "${requested[0]}" == "cover-tips" ]]; then
    echo "cover-tips cannot be installed alone." >&2
    echo "It is a navigator skill and depends on concrete cover style skills." >&2
    echo "Install all skills instead: ./install.sh" >&2
    exit 1
  fi

  for skill in "${requested[@]}"; do
    install_skill_remote "$skill"
  done

  local try_command="\$cover-tips 撕纸剪贴"
  if [[ $# -gt 0 && "${1:-}" != "cover" && "${1:-}" != "all" ]]; then
    if [[ "$*" != *"cover-tips"* ]]; then
      try_command="\$${1}"
    fi
  fi

  cat <<EOF

Done.

Installed skills target:
  $TARGET_DIR

Try:
  $try_command

  主题：可以洗稿，但不能被洗脑
  副标题：AI 时代的内容判断力
  用途：X封面
EOF
}

main "$@"
