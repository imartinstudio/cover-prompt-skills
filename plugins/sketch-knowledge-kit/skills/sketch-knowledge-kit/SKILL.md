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
- Illustration count: default `3` when omitted.
- Language: Chinese, English, or mixed Chinese-English.
- Ratios: infer separately for cover and illustrations if the user provides only platforms.
- Content structure: article outline, tutorial steps, feature list, product flow, or knowledge framework; infer a compact structure when omitted.
- Extra context: optional.

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

## Prompt Output

For prompt or all mode, convert each brief into a generic image-generation prompt using the appropriate target skill's rules. Keep prompts provider-neutral and include exact ratio, visual goal, structure, style constraints, and avoid list for every asset.
