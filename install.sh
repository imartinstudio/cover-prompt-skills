#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${COVER_PROMPT_SKILLS_REPO:-https://github.com/imartinstudio/cover-prompt-skills.git}"
INSTALL_DIR="${COVER_PROMPT_SKILLS_HOME:-$HOME/.cover-prompt-skills}"
TARGET_DIR="${COVER_SKILLS_TARGET:-$HOME/.shared-skills}"

has_local_project() {
  [[ -d "skills" && -x "scripts/install.sh" ]]
}

ensure_git() {
  if ! command -v git >/dev/null 2>&1; then
    echo "git is required but was not found." >&2
    exit 1
  fi
}

install_from_local_project() {
  COVER_SKILLS_TARGET="$TARGET_DIR" scripts/install.sh "$@"
}

install_from_repo() {
  ensure_git

  if [[ -d "$INSTALL_DIR/.git" ]]; then
    echo "Updating Cover Prompt Skills in $INSTALL_DIR"
    git -C "$INSTALL_DIR" pull --ff-only
  elif [[ -e "$INSTALL_DIR" ]]; then
    echo "Install path exists but is not a git repository: $INSTALL_DIR" >&2
    echo "Move it away or set COVER_PROMPT_SKILLS_HOME to another path." >&2
    exit 1
  else
    echo "Cloning Cover Prompt Skills into $INSTALL_DIR"
    git clone "$REPO_URL" "$INSTALL_DIR"
  fi

  COVER_SKILLS_TARGET="$TARGET_DIR" "$INSTALL_DIR/scripts/install.sh" "$@"
}

main() {
  if has_local_project; then
    install_from_local_project "$@"
  else
    install_from_repo "$@"
  fi

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
