---
name: cover-3d-eye-with-docs
description: Create a coordinated article cover plus inline visual package in the 3D Eye family from pasted article text, Markdown files, or plain-text files. Output one dark local-AI cover and section-bound article-inline briefs or prompts with black grids, neon green terminal glow, cream-white titles, optional blue-white mascot continuity, and tutorial-grade local-AI explanation logic. Use when the user asks for 本地AI文章配图, 3D Eye article package, local AI cover plus inline visuals, Ollama tutorial visuals, privacy-first article graphics, hardware-fit article diagrams, or terminal-style article illustrations.
---

# 3D Eye With Docs

Use this skill when one article needs both a cover and section-bound inline
visuals in the 3D Eye family. This skill is self-contained. Do not route
runtime work to `cover-3d-eye`, `article-visual-planner`, or any illustration
skill.

## Hard Boundaries

- Accepted article sources: pasted article text, Markdown files, or plain-text
  files.
- Do not claim DOCX, PDF, remote article, or web scraping support.
- Treat the article source as read-only.
- If no valid article content is available, ask for pasted text or a
  Markdown/plain-text path. Do not downgrade to cover-only behavior.
- Default output is planning material, not direct image generation.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the invocation template only.
- `--out-type brief`: output the article visual brief set only.
- `--out-type prompt`: output final image prompts for every planned asset.
- `--out-type all`: output the brief set first, then the prompts.
- Omitted `--out-type`: default to `brief`.

Treat `直接生成`, `出图`, `生成封面和配图`, and `开始生图` as direct image
generation only when the user explicitly asks for images.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-3d-eye-with-docs 生成一套文章封面+正文配图方案
文章来源：{article_source}
输出类型：{out_type}
封面用途：{cover_use_case}
正文配图用途：{inline_use_case}
正文配图数量：{inline_count}
语言：{language}
封面画幅比例：{cover_ratio}
正文主画幅比例：{inline_ratio}
核心钩子：{core_hook}
已有图片处理：{image_handling}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Article source: required.
- Topic / thesis: required.
- Cover use case: X article cover, WeChat cover, blog header, tutorial cover,
  YouTube thumbnail, local AI poster.
- Inline use case: install guide visual, hardware map, privacy comparison,
  quantization explainer, workflow strip, mistake checklist, cost comparison.
- Inline count: must be an integer from `1` to `5`. If omitted, default to `3`.
  If the user explicitly requests `0`, a negative number, a non-integer, or any
  value above `5`, fail and ask them to choose a count from `1` to `5`. Do not
  clamp, expand, truncate, or silently fall back.
- Language: Chinese, English, or mixed Chinese-English.
- Core hook: privacy, offline, local ownership, no cloud, hardware fit,
  quantization, speed, cost, mistakes, workflow clarity.
- Cover ratio and inline ratio: optional; infer from use case when omitted.
- Extra context: optional.
- Forbidden elements: optional.

## Article Readiness Workflow

1. Confirm the article source is pasted text or a readable Markdown/plain-text
   file.
2. Extract the main thesis, section goals, tutorial steps, tradeoffs, warning
   points, hardware terms, and local-vs-cloud contrasts.
3. Detect existing image references such as `![](...)`, reference-style
   Markdown images, or `<img ...>` tags.
4. Use those image references as editorial signals and avoid planning duplicate
   local-AI visuals unless the user asks for replacement.
5. Map the cover to the emotional hook and whole thesis. Map every
   `article-inline` asset to one concrete section or paragraph and one reading
   problem.
6. Prefer the clearest educational leverage: installation, hardware fit,
   privacy, quantization, workflow, errors, or comparison.
7. Enforce the inline count exactly as requested when it is valid. Never output
   fewer than `1` or more than `5` inline assets.

## Aspect Ratio Defaults

- Cover:
  - X article cover: `5:2`
  - WeChat article cover: `2.35:1`
  - Blog header / tutorial cover / YouTube thumbnail: `16:9`
  - Poster: `3:4` or `4:5`
- Inline:
  - Tutorial inline / workflow / comparison: `16:9`
  - WeChat inline: `4:3`
  - Knowledge card: `1:1`
  - Vertical warning poster: `4:5`

State exact ratios in prompt mode.

## Brief Output

For brief mode, output exactly these sections:

```text
【文章输入检查】
文章标题：
文章来源：
语言：
正文配图数量：
现有图片引用：
图片处理策略：

【封面 brief】
资产类型：cover
主题词：
副标题：
用途：
画幅比例：
语言：
核心钩子：
主论点：
构图模式：
视觉主体：
是否使用3D Eye吉祥物：
封面职责：
补充背景：
禁用元素：

【正文配图 brief 1】
资产类型：article-inline
绑定章节/段落：
建议插入位置：
要解决的阅读问题：
画幅比例：
主题：
说明：
图解类型：
核心钩子：
视觉锚点：
是否使用3D Eye吉祥物：
提示词约束：
避免与已有图片重复：

【一致性约束】
标题语气：
黑绿终端体系：
终端/UI语言：
吉祥物连续性：
术语统一：

【差异化约束】
封面职责：
正文配图职责：
避免重复：
```

Repeat the `正文配图 brief` section for the planned inline count.

## Visual System

Apply these rules across cover and inline assets:

- Background: near-black grid, subtle scan lines, corner registration marks,
  restrained film grain.
- Color: black, cream-white, neon green `#39FF73`, dim gray, and small red only
  for warnings or errors.
- Typography: oversized condensed title plus monospaced terminal microcopy.
- UI language: terminal windows, CLI cursors, lock/shield icons, hardware
  cards, comparison panels, dotted arrows, checklists, and status labels.
- Mascot continuity: optional but recommended. The 3D Eye mascot stays
  blue-white-black and should feel warm, focused, and useful rather than goofy.
- Composition: one hero scene plus 1-3 supporting educational elements.

Avoid purple-blue neon, cyberpunk cityscapes, RGB gaming rooms, Matrix code
rain, robot faces, stock hacker hoodies, photoreal people, cluttered dashboards,
cheap 3D icons, and official logos unless explicitly requested.

## Role Split

- Cover role: carry the emotional hook and the whole local-AI thesis.
- Inline role: explain one step, one tradeoff, one mistake, one hardware fit,
  one privacy comparison, or one quantization point at a time.
- Shared family: black grid, neon green terminal focus, cream-white titles,
  local-AI clarity, optional mascot continuity.
- Avoid duplication: the cover must not become a full checklist; inline assets
  must not restate the same hero argument.

## Prompt Output

For prompt or all mode, convert each brief into a provider-neutral image prompt.
Do not mention provider names, model names, or runtime syntax unless the user
explicitly asks.

### Cover Prompt Requirements

Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and core hook.
3. One composition mode and why it fits.
4. One hero subject with 1-3 concrete anchors.
5. Title hierarchy, terminal microcopy, and mascot usage decision.
6. Near-black grid background, neon green terminal glow, cream-white type, and
   local-AI educational mood.
7. A concise avoid list.

### Inline Prompt Requirements

Every inline prompt must include:

1. Exact canvas ratio and size.
2. Bound section or paragraph, reading problem, and insertion location.
3. One educational target only: install step, workflow, comparison, hardware
   map, quantization chart, warning checklist, or privacy frame.
4. Terminal/UI/diagram plan with one focus path.
5. Visual anchors and mascot usage decision.
6. Near-black grid, neon green emphasis, cream-white titles, and restrained
   red warnings only when needed.
7. A concise avoid list plus a note on how it differs from existing article
   images.

## Direct Generation Rule

Only generate final images when the user explicitly asks for image output. Keep
analysis internal and output only the generated asset result.
