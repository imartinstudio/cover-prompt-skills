# Usage

## Choose the entry point

Use `cover-tips` when the visual style or the required asset scope is still unclear. It is a two-stage selector:

1. Confirm the visual style. If the user has not named one, propose 1–3 candidates and wait for confirmation.
2. Confirm the asset scope: **single cover** or **cover + inline visuals**.

The single-cover route calls the selected independent `cover-X` skill. The article-package route shows only the four styles that have a published `with-docs` sibling:

| Base style | Article-package route |
|---|---|
| `cover-3d-eye` | `cover-3d-eye-with-docs` |
| `cover-cream-orange-knowledge-poster` | `cover-cream-orange-knowledge-poster-with-docs` |
| `cover-light-product` | `cover-light-product-with-docs` |
| `cover-sketch-knowledge-poster` | `cover-sketch-knowledge-poster-with-docs` |

If a style has no row in this table, it remains available for a single cover only. Do not silently substitute another style.

## CoverTips examples

Ask for a style recommendation first:

```text
$cover-tips
主题：如何在本地运行一个 AI 模型
资产范围：先推荐风格
```

After the user confirms the style and scope, route to the concrete skill:

```text
$cover-3d-eye-with-docs
文章来源：/path/to/article.md
输出类型：brief
正文配图数量：3
```

For a single cover:

```text
$cover-3d-eye
输出类型：template
主题词：本地 AI
用途：教程封面
```

CoverTips supports `template | prompt | all` for the cover-organizing route. If `--out-type` is omitted, it returns the `template` output. `brief` belongs to the article-package skills.

## Independent base cover skills

Call a concrete base skill directly when the style is already known:

```text
$cover-editorial-collage --out-type prompt
主题词：提示词
副标题：好的提示，不只是命令，更是设计
画幅比例：5:2
用途：X 封面
```

All base `cover-X` skills are independently installable and callable. They support `template | prompt | all` and default to `template`.

The current base inventory is:

```text
cover-black-white-minimal
cover-trendy-color-poster
cover-budapest-poster
cover-editorial-collage
cover-tea-oriental
cover-giant-perspective-poster
cover-cream-orange-knowledge-poster
cover-sketch-knowledge-poster
cover-3d-eye
cover-midnight-studio
cover-light-product
cover-mckinsey-briefing-style
```

## Article visual packages

Use one of the four independent `with-docs` skills after the style and scope are confirmed. A `with-docs` skill owns the article cover and its section-bound inline visuals; it does not call the base skill, a universal planner, or an illustration skill at runtime.

### Accepted article sources

The first release accepts only:

- pasted article content;
- a Markdown file;
- a plain-text file.

DOCX and PDF are not included. Remote articles, web scraping, and web-page ingestion are not part of this input contract either.

The article source is read-only. The default response is planning output in the conversation; write a file only when the user explicitly provides an output path.

### Output and count contract

All four `with-docs` skills support:

```text
template | brief | prompt | all
```

The default is `brief`. The default package contains 1 cover and 3 inline visuals. The inline count may be explicitly set to an integer from 1 through 5; the cover is counted separately. Every inline visual must state:

- the bound section or paragraph;
- the suggested insertion position;
- the reading problem it solves;
- the aspect ratio;
- the style and prompt constraints.

Existing Markdown image references are read as editorial signals so the skill can avoid duplicate topics. Missing, empty, or unreadable article input must fail clearly; it must not fall back to a single-cover skill.

Example with pasted content:

```text
$cover-sketch-knowledge-poster-with-docs
文章来源：用户粘贴的文章正文
输出类型：brief
```

Example with a Markdown file and an explicit inline count:

```text
$cover-light-product-with-docs
文章来源：/path/to/product-workflow.md
输出类型：all
正文配图数量：4
```

Example with plain text:

```text
$cover-cream-orange-knowledge-poster-with-docs
文章来源：/path/to/architecture.txt
输出类型：prompt
```

The 3D Eye route is the same contract:

```text
$cover-3d-eye-with-docs
文章来源：/path/to/local-ai.md
封面用途：教程封面
正文配图用途：隐私对比、硬件适配、安装流程
输出类型：brief
```

Unless the user explicitly asks for image generation, these skills return briefs or prompts and do not generate images.

## Direct image generation

For a concrete base style, a user can ask directly for the final cover:

```text
$cover-editorial-collage 直接生成一张 5:2 的 X 封面，主题是“提示词”，副标题是“好的提示，不只是命令，更是设计”。整体要撕纸剪贴、杂志感、讽刺一点。
```

For an article package, direct generation must name the corresponding `with-docs` skill and explicitly ask for images. Otherwise keep the normal brief/prompt workflow.

## Migration

Old `article-visual-planner` invocations should become either:

```text
$cover-tips
-> confirm the style
-> choose single cover or cover + inline visuals
-> call the selected cover-X or available cover-X-with-docs skill
```

or a direct call to an actual `cover-X-with-docs` sibling. If the old style has no sibling, use its base `cover-X` for a single cover; do not auto-replace it with another style.

`cover-pixel-avatar` is outside the current release inventory. It is intentionally absent from the current style table, routing instructions, marketplace entries, and install indexes.
