---
name: kit-cream-orange-knowledge
description: Create coordinated cover and inline illustration briefs from article content for the cream-orange knowledge visual family, combining cover-cream-orange-knowledge-poster and illustration-cream-orange-diagram with shared cream paper, charcoal typography, burnt-orange arrows, technical infographic panels, AI engineering diagrams, section-to-image mapping, and consistent terminology. Use when the user asks for 奶油橙视觉套件, 封面配图文章编排, AI工程文章视觉方案, cover plus illustrations, X article visual package, WeChat article visual package, technical infographic kit, or coordinated AI systems explainer assets.
---

# Cream Orange Knowledge Kit

Use this skill when the user wants a coordinated visual package rather than a single image. It reads or infers the article structure, then produces a decision-ready brief set:

- One cover brief for `cover-cream-orange-knowledge-poster`.
- One or more illustration briefs for `illustration-cream-orange-diagram`.
- A section-to-image arrangement that explains why each illustration belongs where it does.
- Shared consistency constraints.
- Difference constraints that keep the cover and illustrations from doing the same job.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the kit invocation template only.
- `--out-type brief`: output coordinated cover + illustration briefs with article-based image arrangement.
- `--out-type prompt`: output final image prompts for the cover and every illustration.
- `--out-type all`: output briefs first, then final prompts.
- Omitted `--out-type`: default to `brief`.

If the user asks to generate images directly, produce the brief set first unless they explicitly ask for one concrete asset to be generated now.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $kit-cream-orange-knowledge 生成一套封面+配图视觉方案
主题：{topic}
平台：{platform}
封面用途：{cover_use_case}
配图用途：{illustration_use_case}
配图数量：{illustration_count}
语言：{language}
画幅比例：{ratios}
文章结构：{article_structure}
目标读者：{audience}
补充背景：{context}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Platform: X article, WeChat article, blog, newsletter, documentation, PPT/article hybrid.
- Cover use case: X article cover, WeChat cover, blog header, tutorial cover, technical infographic, knowledge poster.
- Illustration use case: article inline images, tutorial diagrams, product education graphics, architecture explainers, X article images.
- Illustration count: default `5`. If the user provides a source article with images, use the article content image count as an additional floor.
- Language: Chinese, English, or mixed Chinese-English.
- Ratios: infer separately for cover and illustrations if omitted.
- Article structure: outline, tutorial steps, feature list, architecture layers, maturity stages, decision framework, or infer compactly.
- Audience: AI builders, product teams, founders, technical readers, nontechnical decision makers, or infer.
- Extra context: optional.

## Deriving Illustration Count from Source Article

When the user provides a path to a source article:

1. Read the article and count all image references (`![...](...)`, `<img ...>`, or equivalent Markdown/HTML patterns).
2. Identify the first image as the existing cover when it appears at the top or before the first major heading.
3. Count the remaining images as content illustrations (`N_article`).
4. Infer a structure-based count (`N_structure`) from major sections that need visual support.
5. Use `max(N_article, N_structure, 5)` as the final illustration count unless the user gives a higher count.
6. For each source section that already has an image, anchor one illustration brief to that section's visual role and core argument.
7. When one section has multiple images, keep them as separate illustration briefs if they explain distinct concepts.

## Illustration Count Report

When the source article has images, include a short count report before the briefs or prompts:

```text
【图片来源分析】
原文图片总数：{N_total}
封面图片（第一张）：{cover_image_path}
内容配图：{N_article} 张
结构推断配图：{N_structure} 张
本套件配图数量：{N_final} 张
补充原因：{reason_for_each_added}
```

## Brief Output

For brief mode, output exactly these sections:

```text
【封面 brief】
调用：$cover-cream-orange-knowledge-poster
主题词：
副标题：
画幅比例：
语言：
用途：
信息结构：
核心视觉隐喻：
补充背景：
禁用元素：

【配图 brief 1】
调用：$illustration-cream-orange-diagram
主题：
说明：
画幅比例：
用途：
图解模式：
重点区域：
视觉锚点：
补充背景：
禁用元素：

【文章配图编排】
平台：
文章结构：
配图分布逻辑：
章节到配图映射：
图注语气：
阅读节奏：

【一致性约束】
标题语气：
奶油橙比例：
纸张质感：
图标线稿：
箭头逻辑：
术语统一：

【差异化约束】
封面职责：
配图职责：
避免重复：
```

Repeat the `配图 brief` section for the requested illustration count.

## Coordination Rules

- Cover role: total thesis, memorable system metaphor, shareability, saved-collection value.
- Illustration role: one section, one hard idea, one readable logic path.
- Article arrangement role: decide which article sections deserve images, what each image explains, and how captions guide reading.
- Shared family: cream paper, charcoal headline, burnt-orange highlights, muted gray support, technical infographic panels, arrows, loops, ladders, dashboards, architecture blocks.
- Shared terminology: keep product names, system components, stage names, metric names, and loop labels identical across all assets.
- Avoid duplication: the cover should not become a section-level walkthrough; illustrations should not become mini covers.
- Sequence: if the user gives an article outline, map the cover to the full argument and illustrations to the most teachable sections.
- Source images as floor: when an article already has images, do not produce fewer content illustrations than the article's existing content image count.
- Image anchoring: every illustration that corresponds to an existing article image must reference the image's visual content or editorial role as a concrete anchor.

## Prompt Output

For prompt or all mode, convert each image brief into a provider-neutral image-generation prompt. Do not mention provider names, model names, or runtime-specific syntax.

### Cover Prompt

For the cover, follow `cover-cream-orange-knowledge-poster` rules. Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, and language.
3. Selected information structure and why it fits.
4. Visual metaphor with 1-3 concrete anchors.
5. Text-image relationship and title hierarchy.
6. Background, linework, typography, and cream-orange-charcoal color system.
7. Diagram logic and a concise avoid list.

```text
【封面 prompt】
<provider-neutral image prompt following the rules above>
```

### Illustration Prompt

For each illustration, follow `illustration-cream-orange-diagram` rules. Every illustration prompt must include:

1. Exact canvas ratio and size.
2. Topic, description, use case, diagram mode, focus area, and visual anchor.
3. Simplified composition plan.
4. Arrow/callout plan with orange emphasis.
5. Background, linework, typography, panels, and color system.
6. A concise avoid list.

```text
【配图 prompt 1/ N】
<provider-neutral image prompt following the rules above>

【配图 prompt 2/ N】
...
```

### Article Arrangement Note

After the prompts, include a concise note mapping each illustration prompt to the article section it supports.
