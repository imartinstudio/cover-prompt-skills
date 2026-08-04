# Task 2 Report

- 状态：DONE
- commit：`feat: add with-docs article visual skills`

## 新增目录

- `plugins/cover-sketch-knowledge-poster-with-docs`
- `plugins/cover-light-product-with-docs`
- `plugins/cover-cream-orange-knowledge-poster-with-docs`
- `plugins/cover-3d-eye-with-docs`

## 实现摘要

- 为四个 with-docs 风格各自新增了独立的 Claude manifest、Codex manifest
  和 `skills/<name>/SKILL.md`。
- 四个 `SKILL.md` 都改为自包含文章视觉包入口：默认 `--out-type brief`，
  支持 `template | brief | prompt | all`，且只接受粘贴文章、Markdown 文件
  或纯文本文件。
- 每个技能都显式要求：
  - 文章源只读；
  - 无有效文章时直接要求补充文章，不降级到基础 cover skill；
  - 默认输出封面 + 正文配图 brief / prompt，而不是直接生图；
  - 正文配图必须绑定章节/段落、建议插入位置、阅读问题、画幅比例与提示词约束；
  - 读取已有图片引用并避免重复主题；
  - 不在运行时依赖基础 cover skill、`article-visual-planner` 或
    illustration skill。

## 运行过的检查

1. Frontmatter 检查
   - 命令：自定义 `python3` 脚本检查 4 个新 `SKILL.md` 是否存在 frontmatter，
     且 `name` 与目录名一致。
   - 结果：通过，`frontmatter-ok 4 skills`。

2. JSON 检查
   - 命令：`python3 -m json.tool` 校验 8 个新 plugin manifest。
   - 结果：通过，`json-ok 8 manifests`。

3. Markdown 检查
   - 命令：`markdownlint-cli2` 校验 4 个新 `SKILL.md` 与本报告文件。
   - 结果：通过，`Summary: 0 issues in 0 files`。

## 未解决疑问

- 无
