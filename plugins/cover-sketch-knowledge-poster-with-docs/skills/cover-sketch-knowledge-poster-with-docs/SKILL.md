---
name: cover-sketch-knowledge-poster-with-docs
description: Create a coordinated article cover plus inline visual package in the sketch-knowledge family from pasted article text, Markdown files, or plain-text files. Output one warm-paper hand-drawn cover and section-bound article-inline briefs or prompts with black marker linework, Anthropic orange highlights, and sketchnote knowledge-map logic. Use when the user asks for 手绘知识图谱文章配图, sketch knowledge article package, tutorial cover plus inline visuals, knowledge-map article visuals, product education sketch package, or whiteboard-style article illustrations.
---

# Sketch Knowledge Poster With Docs

Use this skill when one article needs both a cover and section-bound inline
visuals in the sketch-knowledge family. This skill is self-contained. Do not
route runtime work to `cover-sketch-knowledge-poster`, `article-visual-planner`,
or `illustration-sketch-ui`.

## Hard Boundaries

- Accepted article sources: pasted article text, Markdown files, or plain-text
  files.
- Do not claim DOCX, PDF, Google Docs, web URL, or remote article support.
- Treat the article source as read-only.
- If no valid article content is available, stop and ask the user to provide
  pasted text or a Markdown/plain-text file. Do not downgrade to a cover-only
  skill.
- Default deliverable is planning output, not direct image generation.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the invocation template only.
- `--out-type brief`: output the article visual brief set only.
- `--out-type prompt`: output final image prompts for every planned asset.
- `--out-type all`: output the brief set first, then the prompts.
- Omitted `--out-type`: default to `brief`.

Treat `直接生成`, `出图`, `生成图片`, `生成封面和配图`, and `开始生图` as direct
image generation only when the user explicitly asks for images rather than
briefs/prompts. Unless the user clearly asks for the whole set, generate only
the specific asset they named.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-sketch-knowledge-poster-with-docs 生成一套文章封面+正文配图方案
文章来源：{article_source}
输出类型：{out_type}
封面用途：{cover_use_case}
正文配图用途：{inline_use_case}
正文配图数量：{inline_count}
语言：{language}
封面画幅比例：{cover_ratio}
正文主画幅比例：{inline_ratio}
知识结构主线：{knowledge_structure}
已有图片处理：{image_handling}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Article source: required.
- Article topic / working title: required.
- Cover use case: X 文章封面、微信公众号封面、教程封面、博客头图、知识图谱封面。
- Inline use case: 教程配图、产品教育插图、功能讲解图、章节知识图、X 文章配图。
- Inline count: must be an integer from `1` to `5`. If omitted, default to `3`.
  If the user explicitly requests `0`, a negative number, a non-integer, or any
  value above `5`, fail and ask them to choose a count from `1` to `5`. Do not
  clamp, expand, truncate, or silently fall back.
- Language: Chinese, English, or mixed Chinese-English.
- Cover ratio and inline ratio: optional; infer from use case when omitted.
- Knowledge structure: hub-and-spoke, workflow, framework diagram, knowledge
  map, tree, before/after.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Article Readiness Workflow

1. Confirm the article source is pasted text or a readable Markdown/plain-text
   file.
2. Extract the working title, major sections, section goals, and any explicit
   product or concept names.
3. Detect existing image references such as `![](...)`, reference-style
   Markdown images, or `<img ...>` tags.
4. Use existing image references as editorial signals. Avoid re-planning the
   same subject unless the user explicitly asks to replace or reimagine it.
5. Choose the cover from the whole-article thesis. Choose each `article-inline`
   asset from one concrete section or paragraph and bind it to one reading
   problem.
6. Prefer the most teachable sections, not a mechanical every-section loop.
7. Enforce the inline count exactly as requested when it is valid. Never output
   fewer than `1` or more than `5` inline assets.

## Aspect Ratio Defaults

- Cover:
  - X article cover: `5:2`
  - WeChat article cover: `2.35:1`
  - Tutorial cover / blog header: `16:9`
  - Knowledge map cover: `1:1` or `4:5`
- Inline:
  - Tutorial inline / product docs: `16:9`
  - WeChat inline: `4:3`
  - Knowledge card: `1:1`
  - Vertical tutorial card: `3:4`

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
知识结构：
总论点：
核心视觉隐喻：
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
知识点角色：
视觉锚点：
提示词约束：
避免与已有图片重复：

【一致性约束】
标题语气：
黑橙比例：
纸张质感：
线稿/箭头语言：
术语统一：

【差异化约束】
封面职责：
正文配图职责：
避免重复：
```

Repeat the `正文配图 brief` section for the planned inline count.

## Visual System

Apply these rules across cover and inline assets:

- Background: warm paper, subtle paper grain, light scan feel, slight fold or
  notebook texture.
- Color: paper white, black, and Anthropic orange `#E67E22` only.
- Linework: black fine marker, slightly irregular, human, educational.
- Typography: handwritten or sketchnote style, but title hierarchy must stay
  crisp and readable.
- Icons: simple black line icons such as documents, arrows, folders, terminal
  windows, UI cards, databases, agents, memory, chat, workflow nodes.
- Whitespace: generous. The page should feel collectible and explainable, not
  crowded.

Avoid pure white poster boards, dark tech backgrounds, blue-purple gradients,
glossy UI mockups, realistic screenshots, 3D icons, corporate icon packs,
photoreal people, rainbow palettes, and dense unreadable microtext.

## Role Split

- Cover role: explain the whole article thesis as a knowledge map or tutorial
  overview with shareability and collection value.
- Inline role: explain one specific knowledge point, interface behavior, or
  step in three seconds.
- Shared family: warm paper, black marker, orange emphasis, sketchnote
  hierarchy, educational clarity.
- Avoid duplication: the cover must not become a UI walkthrough; inline assets
  must not become mini covers.

## Prompt Output

For prompt or all mode, convert each brief into a provider-neutral image prompt.
Do not mention provider names, model names, or runtime syntax unless the user
explicitly asks.

### Cover Prompt Requirements

Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and whole-article thesis.
3. Selected knowledge structure and why it fits.
4. One visual metaphor with 1-3 concrete anchors.
5. Title hierarchy and text-image relationship.
6. Warm paper background, black marker linework, handwritten typography, and
   black/orange color system.
7. A concise avoid list.

### Inline Prompt Requirements

Every inline prompt must include:

1. Exact canvas ratio and size.
2. Bound section or paragraph, reading problem, and insertion location.
3. One teachable point only.
4. Simplified sketch UI or knowledge diagram plan with one focus area.
5. Arrow/callout plan and orange emphasis target.
6. Warm paper, black marker, handwritten labels, and large whitespace.
7. A concise avoid list plus a note on how it differs from existing article
   images.

## Direct Generation Rule

Only generate final images when the user explicitly asks for image output. Keep
analysis internal and output only the generated asset result.
