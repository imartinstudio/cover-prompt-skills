---
name: sketch-knowledge-kit
description: Create coordinated cover + illustration briefs for the sketch-knowledge visual family, combining cover-sketch-knowledge-poster and illustration-sketch-ui with shared warm paper, black marker linework, Anthropic orange highlights, sketchnote typography, and consistent terminology. Use when the user asks for a 配套封面和插图, cover plus illustrations, article visual package, tutorial visual kit, X article cover and inline illustrations, product education visual system, or coordinated sketch knowledge assets.
---

# Sketch Knowledge Kit

Use this skill when the user wants a coordinated visual package rather than a single image. It does not generate one mixed image. It produces a decision-ready brief set:

- One cover brief for `cover-sketch-knowledge-poster`.
- One or more illustration briefs for `illustration-sketch-ui`.
- Shared consistency constraints.
- Difference constraints that keep the cover and illustrations from doing the same job.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the kit invocation template only.
- `--out-type brief`: output the coordinated cover + illustration briefs.
- `--out-type prompt`: output final image prompts for every asset.
- `--out-type all`: output briefs first, then final prompts.
- Omitted `--out-type`: default to `brief`.

If the user asks to generate images directly, produce the brief set first unless they explicitly ask for one concrete asset to be generated now.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $sketch-knowledge-kit 生成一套封面+插图视觉方案
主题：{topic}
封面用途：{cover_use_case}
插图用途：{illustration_use_case}
插图数量：{illustration_count}
语言：{language}
画幅比例：{ratios}
内容结构：{content_structure}
补充背景：{context}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Cover use case: X article cover, WeChat cover, tutorial cover, blog header, knowledge map.
- Illustration use case: tutorial inline images, product documentation, function walkthrough, X article images.
- Illustration count: default `3` when omitted and no source article images exist. When the user provides a source article that already contains images (detected via `![](...)` in Markdown or `<img>` tags), count the content images (exclude the cover/first image) and use that count as the minimum — do not go below it. If the article's image count is higher than 3, match it. The article's existing image distribution reflects the author's editorial judgment about which sections have enough information density to warrant a visual; that judgment is more authoritative than the mechanical default.
- Language: Chinese, English, or mixed Chinese-English.
- Ratios: infer separately for cover and illustrations if the user provides only platforms.
- Content structure: article outline, tutorial steps, feature list, product flow, or knowledge framework; infer a compact structure when omitted.
- Extra context: optional.

## Deriving Illustration Count from Source Article

When the user provides a path to a source article:

1. Read the article and count all image references (`![...](...)`, `<img ...>`, or equivalent Markdown/HTML patterns).
2. Identify the first image — treat it as the existing cover. The remaining images are content illustrations.
3. Count the content illustrations (`N_article`). Compare with the default (`N_default = 3`).
4. Use `max(N_article, N_default)` as the illustration count for this kit.
5. Do not mechanically skip sections that have images or inflate sections that have none. Instead: for each section that has a source image, produce an illustration brief anchored to that image's visual reference and the section's core argument. For key sections that lack a source image but carry high information density, consider adding an illustration brief beyond the source count — but justify it explicitly.
6. When the source article has multiple images in one section (e.g. an architecture chapter with separate diagrams for integration, layered stack, and CI/CD), keep them as separate illustrations. The author split them for a reason — do not collapse them.

## Illustration Count Report

When the source article has images, include a short count report before the briefs or prompts:

```text
【图片来源分析】
原文图片总数：{N_total}
封面图片（第一张）：{cover_image_path}
内容插图：{N_article} 张
本套件插图数量：{N_final} 张（原文{N_article}张 + 补充{N_added}张）
补充原因：{reason_for_each_added}
```

## Brief Output

For brief mode, output exactly these sections:

```text
【封面 brief】
调用：$cover-sketch-knowledge-poster
主题词：
副标题：
画幅比例：
语言：
用途：
知识结构：
补充背景：
禁用元素：

【插图 brief 1】
调用：$illustration-sketch-ui
主题：
说明：
画幅比例：
用途：
界面来源/产品场景：
重点区域：
补充背景：
禁用元素：

【一致性约束】
标题语气：
黑橙比例：
纸张质感：
图标线稿：
术语统一：

【差异化约束】
封面职责：
插图职责：
避免重复：
```

Repeat the illustration brief section for the requested illustration count.

## Coordination Rules

- Cover role: total view, conceptual map, shareability, saved-collection value.
- Illustration role: specific feature explanation, action focus, 3-second comprehension.
- Shared family: warm paper, black marker, Anthropic orange, hand-drawn typography, slight scan feel, generous whitespace.
- Shared terminology: keep product names, feature names, and core concepts identical across assets.
- Avoid duplication: the cover should not become a UI walkthrough; illustrations should not become mini covers.
- Sequence: if the user gives an article outline, map the cover to the whole thesis and illustrations to the most teachable sections.
- Source images as floor: when the source article already has images, the kit's illustration count must not be lower than the article's content image count. The original author's image placement — which sections got visual support, which got multiple diagrams — reflects editorial judgment about information density. Respect it; don't override it with a generic default.
- Image anchoring: every illustration prompt that corresponds to an existing article image must reference that image's visual content (subject, composition, UI elements) as a concrete anchor, not as a vague inspiration.

## Prompt Output

For prompt or all mode, convert each brief into a generic image-generation prompt using the appropriate target skill's rules. Keep prompts provider-neutral and include exact ratio, visual goal, structure, style constraints, and avoid list for every asset.
