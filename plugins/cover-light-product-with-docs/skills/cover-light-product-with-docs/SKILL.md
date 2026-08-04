---
name: cover-light-product-with-docs
description: Create a coordinated article cover plus inline visual package in the light-product family from pasted article text, Markdown files, or plain-text files. Output one cream-white premium SaaS-style cover and section-bound article-inline briefs or prompts with warm-cool dual accents, refined UI modules, and agent workflow storytelling. Use when the user asks for 浅色产品文章配图, light product article package, SaaS cover plus inline visuals, AI product education visuals, product workflow article graphics, or agent workspace article illustrations.
---

# Light Product With Docs

Use this skill when one article needs both a cover and section-bound inline
visuals in the light-product family. This skill is self-contained. Do not
route runtime work to `cover-light-product`, `light-product-kit`, or
`illustration-light-product`.

## Hard Boundaries

- Accepted article sources: pasted article text, Markdown files, or plain-text
  files.
- Do not claim DOCX, PDF, remote article, or web-page ingestion support.
- Treat the article source as read-only.
- If no valid article content is available, ask the user for pasted content or
  a Markdown/plain-text path. Do not fall back to a single cover.
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
使用 $cover-light-product-with-docs 生成一套文章封面+正文配图方案
文章来源：{article_source}
输出类型：{out_type}
封面用途：{cover_use_case}
正文配图用途：{inline_use_case}
正文配图数量：{inline_count}
语言：{language}
封面画幅比例：{cover_ratio}
正文主画幅比例：{inline_ratio}
产品/场景：{product_context}
已有图片处理：{image_handling}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Article source: required.
- Topic / article thesis: required.
- Cover use case: X header, WeChat article cover, blog header, SaaS launch
  cover, PPT cover, LinkedIn header.
- Inline use case: product docs, feature walkthrough, article inline image,
  workflow explainer, module explanation.
- Inline count: this is a hard constraint. If `正文配图数量` is omitted, use
  `3`. If it is explicitly supplied, accept only an integer from `1` to `5`.
  Validate this before producing any template, brief, prompt, or image. An
  explicit `0`, negative number, non-integer, or value above `5` must fail with
  a clear request to use an integer from `1` to `5`; never clamp, round,
  expand, truncate, omit, or route to the base cover skill or cover-only
  behavior.
- Language: Chinese, English, or mixed Chinese-English.
- Product context: AI product, agent workspace, research flow, coding workflow,
  automation system, dashboard, knowledge base, or feature module.
- Cover ratio and inline ratio: optional; infer from use case when omitted.
- Extra context: optional.
- Forbidden elements: optional.

## Article Readiness Workflow

1. Confirm the article source is pasted text or a readable Markdown/plain-text
   file.
2. Extract the main thesis, key modules, workflows, feature names, and section
   order.
3. Detect existing image references such as `![](...)`, reference-style
   Markdown images, or `<img ...>` tags.
4. Use those image references as editorial signals and avoid planning duplicate
   subject matter unless the user asks for replacement.
5. Map the cover to the whole product story. Map every `article-inline` asset to
   one concrete section or paragraph and one reading problem.
6. Prefer sections with the highest explanatory leverage: feature anatomy,
   workflow sequence, dashboard slice, architecture layer, or before/after.
7. Enforce the inline count exactly as requested when it is valid. Never output
   fewer than `1` or more than `5` inline assets.

## Aspect Ratio Defaults

- Cover:
  - X / LinkedIn header: `5:2`
  - WeChat article cover: `2.35:1`
  - Blog header / launch cover / PPT cover: `16:9`
  - Product poster: `4:5`
- Inline:
  - Product docs / article inline: `16:9`
  - WeChat inline: `4:3`
  - Knowledge card: `1:1`
  - Vertical module explainer: `3:4`

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
产品/场景：
产品叙事：
视觉主体：
构图模式：
UI元素：
系统微文案：
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
产品/场景：
重点模块：
图解模式：
UI元素：
系统微文案：
提示词约束：
避免与已有图片重复：

【一致性约束】
标题语气：
暖冷配色：
基底色调：
UI模块语言：
术语统一：

【差异化约束】
封面职责：
正文配图职责：
避免重复：
```

Repeat the `正文配图 brief` section for the planned inline count.

## Visual System

Apply these rules across cover and inline assets:

- Background: cream white, rice white, warm gray white, or cool gray white.
- Color: mostly neutral canvas plus balanced warm/cool accents.
- Warm accents: soft orange, terracotta, warm gold. Cool accents: indigo blue,
  purple blue, cool gray blue.
- Accent coverage: only 10-20% of the canvas should be colored.
- UI treatment: simplified premium SaaS modules, workflow cards, dashboards,
  panels, status chips, and agent nodes. Never use raw screenshots.
- Typography: refined product/editorial hierarchy, not handwritten.
- Depth: shallow layered cards and soft shadows, not glossy 3D.

Avoid dark mode, cyberpunk, stock business illustration, cheap ad banners,
fluorescent gradients, coffee-cup startup clichés, robots, glowing brains,
chips/circuit boards, crowded dashboards, and unreadable UI clutter.

## Role Split

- Cover role: carry the overall product narrative and first impression.
- Inline role: explain one feature, one workflow, one module, or one
  architectural slice quickly and concretely.
- Shared family: cream-white base, warm-cool dual accents, modular SaaS UI,
  premium editorial restraint.
- Avoid duplication: the cover must not become a dense tutorial dashboard;
  inline assets must not become mini hero banners.

## Prompt Output

For prompt or all mode, convert each brief into a provider-neutral image prompt.
Do not mention provider names, model names, or runtime syntax unless the user
explicitly asks.

### Cover Prompt Requirements

Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and product story.
3. One composition mode and why it fits.
4. One visual subject with 1-3 concrete anchors.
5. Title hierarchy, UI microcopy, and text-image relationship.
6. Cream-white base, warm-cool accent balance, refined SaaS UI modules, and
   shallow layered depth.
7. A concise avoid list.

### Inline Prompt Requirements

Every inline prompt must include:

1. Exact canvas ratio and size.
2. Bound section or paragraph, reading problem, and insertion location.
3. One explanatory target only: feature module, workflow, dashboard slice,
   before/after, or architecture layer.
4. Simplified UI structure and what to remove.
5. Callout and system microcopy plan.
6. Cream-white background, warm-cool accent balance, and premium product
   illustration discipline.
7. A concise avoid list plus a note on how it differs from existing article
   images.

## Direct Generation Rule

Only generate final images when the user explicitly asks for image output. Keep
analysis internal and output only the generated asset result.
