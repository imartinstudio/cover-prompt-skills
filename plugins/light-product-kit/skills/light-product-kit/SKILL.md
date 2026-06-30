---
name: light-product-kit
description: Create coordinated cover + illustration briefs for the light-product visual family, combining cover-light-product and illustration-light-product with shared cream-white base, warm-cool dual color fusion, refined SaaS UI modules, agent workspace narrative, and consistent product terminology. Use when the user asks for 浅色产品视觉套件, SaaS封面加插图, AI产品文章配套视觉, product visual package, cover plus product illustrations, agent workflow visual kit, product education visual system, or coordinated light product assets.
---

# Light Product Kit

Use this skill when the user wants a coordinated visual package rather than a single image. It does not generate one mixed image. It produces a decision-ready brief set:

- One cover brief for `cover-light-product`.
- One or more illustration briefs for `illustration-light-product`.
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
使用 $light-product-kit 生成一套封面+插图视觉方案
主题：{topic}
封面用途：{cover_use_case}
插图用途：{illustration_use_case}
插图数量：{illustration_count}
语言：{language}
产品/场景：{product_context}
画幅比例：{ratios}
内容结构：{content_structure}
补充背景：{context}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Cover use case: X header, WeChat header, blog header, product launch cover, SaaS landing hero, PPT cover, LinkedIn cover.
- Illustration use case: tutorial inline images, product docs, feature walkthroughs, X article illustrations, product education graphics.
- Illustration count: when omitted, infer from the article/content structure and use at least `5`. Use the exact count if the user provides one.
- Language: Chinese, English, or mixed Chinese-English.
- Product context: AI product, agent workspace, SaaS workflow, automation system, coding agent, research assistant, dashboard, knowledge base, product feature, or product story.
- Ratios: infer separately for cover and illustrations if the user provides only platforms.
- Content structure: article outline, tutorial steps, feature list, product flow, workflow stages, or capability framework; infer a compact structure when omitted.
- Extra context: optional.

## Brief Output

For brief mode, output exactly these sections:

```text
【封面 brief】
调用：$cover-light-product
主题词：
副标题：
用途：
画幅比例：
语言：
视觉主体：
构图模式：
暖色比例：
冷色比例：
基底色调：
强调色倾向：
UI元素：
系统微文案：
补充语境：
禁用元素：

【插图 brief 1】
调用：$illustration-light-product
主题：
说明：
画幅比例：
用途：
产品/场景：
重点模块：
图解模式：
UI元素：
系统微文案：
补充背景：
禁用元素：

【一致性约束】
标题语气：
暖冷配色：
基底色调：
UI模块语言：
系统微文案：
术语统一：

【差异化约束】
封面职责：
插图职责：
避免重复：
```

Repeat the illustration brief section for the requested illustration count.

## Coordination Rules

- Cover role: product story, overall promise, premium first impression, shareability, AI-native workspace narrative.
- Illustration role: specific feature explanation, workflow clarity, module anatomy, three-second comprehension.
- Shared family: cream-white base, low saturation, warm/cool dual accents, refined SaaS UI modules, soft depth, precise typography.
- Shared terminology: keep product names, feature names, workflow stages, and agent labels identical across assets.
- Avoid duplication: the cover should not become a dense tutorial diagram; illustrations should not become mini hero banners.
- Sequence: if the user gives an article outline, map the cover to the whole thesis and illustrations to the most teachable sections.

## Visual System

Use these constraints across all briefs and prompts:

- Base: cream white, rice white, warm gray white, or cool gray white.
- Color: Claude-like warm accents plus Codex-like cool accents, balanced 4:6 or 6:4.
- Accent coverage: 10-20% of canvas; most of the image stays neutral.
- UI: product-quality cards, panels, workflow lines, status chips, dashboards, agent nodes, browser/editor/terminal fragments when relevant.
- Typography: modern product/editorial hierarchy, not decorative or handwritten.
- Mood: professional, warm, precise, future-workflow, premium SaaS.

Avoid dark mode, cyberpunk, cheap AI poster art, stock business illustration, e-commerce banner feel, fluorescent gradients, only warm colors, only cool colors, coffee cups, laptops, hands typing, robots, glowing brains, chips/circuit boards, space backgrounds, and unreadable UI clutter.

## Prompt Output

For prompt or all mode, convert each brief into a generic image-generation prompt using the appropriate target skill's rules. Keep prompts provider-neutral and include exact ratio, visual goal, structure, style constraints, and avoid list for every asset.
