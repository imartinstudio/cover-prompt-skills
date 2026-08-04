---
name: cover-cream-orange-knowledge-poster-with-docs
description: Create a coordinated article cover plus inline visual package in the cream-orange knowledge family from pasted article text, Markdown files, or plain-text files. Output one cream-paper editorial technical cover and section-bound article-inline briefs or prompts with charcoal typography, burnt-orange emphasis, architecture diagrams, feedback loops, comparison frames, and decision-logic visual language. Use when the user asks for 奶油橙文章配图, cream orange knowledge article package, AI engineering article visuals, architecture article cover plus inline diagrams, feedback-loop article graphics, or technical infographic article assets.
---

# Cream Orange Knowledge Poster With Docs

Use this skill when one article needs both a cover and section-bound inline
visuals in the cream-orange knowledge family. This skill is self-contained. Do
not route runtime work to `cover-cream-orange-knowledge-poster`,
`article-visual-planner`, or any illustration skill.

## Hard Boundaries

- Accepted article sources: pasted article text, Markdown files, or plain-text
  files.
- Do not claim DOCX, PDF, remote article, or web scraping support.
- Treat the article source as read-only.
- If no valid article content is available, ask for pasted text or a
  Markdown/plain-text path. Do not fall back to cover-only behavior.
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
使用 $cover-cream-orange-knowledge-poster-with-docs 生成一套文章封面+正文配图方案
文章来源：{article_source}
输出类型：{out_type}
封面用途：{cover_use_case}
正文配图用途：{inline_use_case}
正文配图数量：{inline_count}
语言：{language}
封面画幅比例：{cover_ratio}
正文主画幅比例：{inline_ratio}
信息结构主线：{information_structure}
已有图片处理：{image_handling}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Article source: required.
- Topic / article thesis: required.
- Cover use case: X article cover, WeChat cover, blog header, tutorial cover,
  technical knowledge poster, PPT title visual.
- Inline use case: architecture explainer, workflow diagram, comparison panel,
  decision logic visual, feedback-loop inline image.
- Inline count: explicit user number wins. Otherwise default to `3` and
  auto-expand up to `5` only when article density or existing image placement
  justifies it.
- Language: Chinese, English, or mixed Chinese-English.
- Information structure: stage progression, before/after comparison, system
  architecture, feedback loop, maturity ladder, decision framework, bounded vs
  unbounded contrast.
- Cover ratio and inline ratio: optional; infer from use case when omitted.
- Extra context: optional.
- Forbidden elements: optional.

## Article Readiness Workflow

1. Confirm the article source is pasted text or a readable Markdown/plain-text
   file.
2. Extract the article thesis, section goals, architectural entities, decision
   branches, loops, comparisons, and recurring terminology.
3. Detect existing image references such as `![](...)`, reference-style
   Markdown images, or `<img ...>` tags.
4. Use those image references as editorial signals and avoid planning duplicate
   diagrams unless the user asks for replacement.
5. Map the cover to the system-level thesis. Map every `article-inline` asset to
   one concrete section or paragraph and one reading problem.
6. Prefer sections that benefit from clear logic diagrams rather than decoration.

## Aspect Ratio Defaults

- Cover:
  - X article cover: `5:2`
  - WeChat article cover: `2.35:1`
  - Blog header / tutorial cover / PPT cover: `16:9`
  - Technical infographic: `4:3`
  - Vertical poster: `4:5`
- Inline:
  - Architecture / workflow / comparison inline: `16:9`
  - WeChat inline: `4:3`
  - Square framework card: `1:1`
  - Vertical decision ladder: `4:5`

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
信息结构：
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
信息结构角色：
图解类型：
视觉锚点：
提示词约束：
避免与已有图片重复：

【一致性约束】
标题语气：
奶油橙黑灰体系：
图解阅读路径：
箭头/标签语言：
术语统一：

【差异化约束】
封面职责：
正文配图职责：
避免重复：
```

Repeat the `正文配图 brief` section for the planned inline count.

## Visual System

Apply these rules across cover and inline assets:

- Background: warm cream paper, soft off-white, subtle grid or paper grain,
  faint border shadows when useful.
- Color: cream base, charcoal black, warm gray, burnt orange, muted terracotta,
  and small beige accents.
- Orange usage: headline keywords, stage tabs, arrows, loop segments, important
  nodes, comparison emphasis, and badges.
- Linework: charcoal marker outlines with editorial control; slightly hand-drawn
  but cleaner than whiteboard sketches.
- Typography: bold condensed editorial title plus smaller diagram labels with a
  clear reading path.
- Layout: modular panels, loops, stacks, ladders, or comparison frames with
  obvious hierarchy.

Avoid dark cyberpunk backgrounds, blue-purple AI gradients, real product
screenshots, glossy 3D, random circuit filler, chaotic arrows, stock business
people, and dense unreadable paragraphs.

## Role Split

- Cover role: carry the system thesis, strategic model, or architecture-level
  story.
- Inline role: explain one architecture slice, one loop, one comparison, one
  decision, or one stage transition at a time.
- Shared family: cream paper, charcoal typography, burnt-orange emphasis,
  editorial technical infographic discipline.
- Avoid duplication: the cover must not become a chapter-by-chapter worksheet;
  inline assets must not restate the same master diagram.

## Prompt Output

For prompt or all mode, convert each brief into a provider-neutral image prompt.
Do not mention provider names, model names, or runtime syntax unless the user
explicitly asks.

### Cover Prompt Requirements

Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and system-level thesis.
3. Selected information structure and why it fits.
4. One visual metaphor with 1-3 concrete anchors.
5. Title hierarchy and diagram reading path.
6. Cream paper, charcoal typography, burnt-orange emphasis, and editorial
   infographic structure.
7. A concise avoid list.

### Inline Prompt Requirements

Every inline prompt must include:

1. Exact canvas ratio and size.
2. Bound section or paragraph, reading problem, and insertion location.
3. One logic unit only: architecture slice, workflow, comparison, ladder,
   decision frame, or feedback loop.
4. Panel, arrow, and label plan.
5. Concrete visual anchors tied to the chosen section.
6. Cream paper, charcoal linework, burnt-orange emphasis, and readable modular
   hierarchy.
7. A concise avoid list plus a note on how it differs from existing article
   images.

## Direct Generation Rule

Only generate final images when the user explicitly asks for image output. Keep
analysis internal and output only the generated asset result.
