# Task 1 报告

- 状态：DONE
- commit：`cc7ce58abf9343479a65d22e6c7d5ce81bfd1abb`（Remove deprecated planner and avatar releases）
- 改动文件：
  - `install.sh`
  - `scripts/install.sh`
  - `plugins/cover-tips/skills/cover-tips/SKILL.md`
  - 删除 `plugins/article-visual-planner/skills/article-visual-planner/SKILL.md`
  - 删除 `plugins/cover-pixel-avatar/skills/cover-pixel-avatar/SKILL.md`
- 运行过的检查及结果：
  - `bash -n install.sh scripts/install.sh`：通过
  - `git diff --check`：通过
  - `rg -n "article-visual-planner|cover-pixel-avatar" install.sh scripts/install.sh plugins/cover-tips/skills/cover-tips/SKILL.md`：无残留匹配
  - 提交钩子自带 lint：
    - JSON 校验：32 ok, 0 failed
    - Markdown lint：0 issues
    - Shell 语法检查：4 ok, 0 failed
- 未解决疑问：无

备注：本任务仅处理发布/安装/运行时入口；README 与迁移说明按简报保留给后续任务。

## Fix round 1/5 复核记录

- 触发原因：审查指出上一版报告对“无残留”的表述过满，且四个废弃 plugin manifest、`cover-tips` 中像素头像入口、以及三处 `article-visual-planner` 死链仍需清理。
- 本轮修复内容：
  - 删除 `plugins/article-visual-planner/.codex-plugin/plugin.json`
  - 删除 `plugins/article-visual-planner/.claude-plugin/plugin.json`
  - 删除 `plugins/cover-pixel-avatar/.codex-plugin/plugin.json`
  - 删除 `plugins/cover-pixel-avatar/.claude-plugin/plugin.json`
  - 从 `plugins/cover-tips/skills/cover-tips/SKILL.md` 移除像素头像入口、默认风格、别名与错误提示
  - 将三处运行时死链改为已确认的 `cover-X-with-docs` 目标：
    - `cover-3d-eye-with-docs`
    - `cover-sketch-knowledge-poster-with-docs`
    - `cover-cream-orange-knowledge-poster-with-docs`
- 实际验证：
  - `bash -n install.sh scripts/install.sh`：通过
  - `git diff --check`：通过
  - 针对本轮改动文件的 `rg` 复核：仅命中新路由文本，废弃 manifest 已不存在
- 结果：本轮问题已修复，无新增疑问

## Fix round 2/5 复核记录

- 触发原因：复审指出上一轮把三份基础 skill 和 `cover-tips` 指向了当前尚未创建的具体 `with-docs` 名称，导致运行时出现悬空入口。
- 本轮修复内容：
  - 保持四个废弃 manifest 的删除状态不变
  - 保持像素头像入口清理状态不变
  - 将 `cover-3d-eye`、`cover-sketch-knowledge-poster`、`cover-cream-orange-knowledge-poster` 中的文章包说明退回为泛化的“匹配的、可用的 with-docs sibling”语义，不再写入具体不存在的 skill 路径
  - 将 `cover-tips` 的文章包说明退回为同样的泛化规则，不再声称当前可直接调用某个不存在的具体目标
- 实际验证：
  - `bash -n install.sh scripts/install.sh`：通过
  - `git diff --check`：通过
  - `rg -n "article-visual-planner|cover-3d-eye-with-docs|cover-sketch-knowledge-poster-with-docs|cover-cream-orange-knowledge-poster-with-docs" plugins/cover-tips/skills/cover-tips/SKILL.md plugins/cover-3d-eye/skills/cover-3d-eye/SKILL.md plugins/cover-sketch-knowledge-poster/skills/cover-sketch-knowledge-poster/SKILL.md plugins/cover-cream-orange-knowledge-poster/skills/cover-cream-orange-knowledge-poster/SKILL.md`：无命中
- 结果：悬空入口已清除，无新增疑问
