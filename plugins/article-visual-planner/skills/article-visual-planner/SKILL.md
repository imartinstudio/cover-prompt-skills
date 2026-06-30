---
name: article-visual-planner
description: Automatically plan article cover and inline visual prompts by reading article content, counting existing images, mapping sections to visual assets, and chaining each planned asset to a selected cover-* visual style skill. Use when the user asks for 自动规划文章配图, article visual planner, article cover and inline visuals, generate cover plus inline image prompts from an article, plan visuals for an X article, WeChat article, blog post, newsletter, tutorial, or when using slash syntax like /article-visual-planner:cover-cream-orange-knowledge-poster.
---

# Article Visual Planner

Use this skill when the user wants a complete visual plan for an article rather than one standalone image. This skill does not define a visual style. It reads article content, decides which visual assets are needed, and chains every asset to a selected `cover-*` style skill.

Preferred Claude CLI syntax:

```text
/article-visual-planner:cover-cream-orange-knowledge-poster
```

This means:

- Planner: `article-visual-planner`
- Style skill: `cover-cream-orange-knowledge-poster`

Also support field syntax:

```text
使用 $article-visual-planner 自动规划文章配图
文章：{article_path_or_content}
视觉风格：{cover_style_skill}
输出类型：{out_type}
平台：{platform}
资产范围：{asset_scope}
```

## Chain Contract

The selected style must be a `cover-*` skill. Treat every `cover-*` skill as a visual style generator, even if its legacy wording says "cover". Pass each planned asset to the selected style with an explicit `资产类型` field:

- `cover`: article cover, header, hero, or share image.
- `article-inline`: normal article inline visual.
- `workflow-diagram`: process, flow, or tutorial step.
- `comparison`: before/after, old/new, pros/cons, risks/tradeoffs.
- `architecture`: system stack, module map, data flow, Agent/RAG/tooling diagram.
- `long-infographic`: dense vertical or poster-like article summary.
- `social-card`: square or vertical excerpt card.

When outputting prompts directly, apply the selected style skill's visual system to each asset brief and adapt composition to the asset type.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the invocation template only.
- `--out-type brief`: output the visual asset plan and chain briefs.
- `--out-type prompt`: output final image prompts for all planned assets.
- `--out-type all`: output briefs first, then final prompts.
- Omitted `--out-type`: default to `brief`.

If the user asks to generate images directly, produce the plan first unless they explicitly ask to generate one concrete asset now.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $article-visual-planner 自动规划文章配图
文章：{article_path_or_content}
视觉风格：{cover_style_skill}
输出类型：{template|brief|prompt|all}
平台：{platform}
资产范围：{asset_scope}
语言：{language}
配图数量：{visual_count}
补充背景：{context}
```

## Required Inputs

Extract or infer:

- Article: path, Markdown content, outline, or topic. Required.
- Style skill: a `cover-*` skill. Required; if omitted, ask for the style.
- Output type: template, brief, prompt, or all. Default `brief`.
- Platform: X article, WeChat article, blog, newsletter, documentation, tutorial, or infer.
- Asset scope: default `cover + inline visuals`.
- Language: Chinese, English, or mixed Chinese-English; infer from article.
- Content visual count: default `max(article content images, structure count, 5)` unless user gives an exact count.
- Extra context: optional.

## Source Article Analysis

When the user provides an article path or Markdown content:

1. Read the article.
2. Count image references: Markdown `![...](...)`, HTML `<img ...>`, or equivalent.
3. Treat the first image as the existing cover when it appears at the top or before the first major heading.
4. Count remaining images as content visuals (`N_article`).
5. Identify major sections and infer `N_structure`: sections whose argument benefits from a visual.
6. Use `max(N_article, N_structure, 5)` as the content visual count unless the user gives an exact count.
7. Map the cover to the full thesis and each content visual to one section-level idea.
8. If a source section already has an image, preserve that editorial judgment by assigning a replacement visual to that section.

## Brief Output

For brief mode, output exactly these sections:

```text
【文章分析】
标题：
平台：
语言：
原文图片总数：
封面图片：
内容配图数：
结构推断配图数：
最终配图数：

【链式调用设置】
规划器：$article-visual-planner
视觉风格：${cover_style_skill}
调用格式：/article-visual-planner:{cover_style_skill}

【封面 brief】
调用：${cover_style_skill}
资产类型：cover
主题：
说明：
画幅比例：
用途：
内容结构：
视觉重点：
补充背景：
禁用元素：

【配图 brief 1】
调用：${cover_style_skill}
资产类型：
章节：
主题：
说明：
画幅比例：
用途：
内容结构：
视觉重点：
补充背景：
禁用元素：

【文章配图编排】
配图分布逻辑：
章节到配图映射：
图注语气：
阅读节奏：

【一致性约束】
术语统一：
标题语气：
风格一致：
重复规避：
```

Repeat the `配图 brief` section for the final content visual count.

## Prompt Output

For prompt or all mode, convert every planned asset into a provider-neutral image-generation prompt using the selected `cover-*` style. Do not mention provider names, model names, or runtime-specific syntax.

Every prompt must include:

1. Asset type.
2. Exact canvas ratio and recommended size.
3. Topic, article section, use case, and language.
4. The selected style skill name.
5. Section-specific content structure.
6. Visual focus and text hierarchy.
7. Style-specific visual system adapted from the selected `cover-*` skill.
8. A concise avoid list.

Use this output shape:

```text
【封面 prompt】
<prompt>

【配图 prompt 1/N】
<prompt>

【文章配图映射】
<section-to-asset mapping>
```

## Defaults

- Cover ratio: X article `5:2`, WeChat cover `2.35:1`, blog/tutorial `16:9`.
- Inline visual ratio: default `16:9`.
- WeChat inline ratio: `4:3`.
- Social card ratio: `1:1` or `4:5`.
- Long infographic ratio: `3:4` or `4:5`.

## Guardrails

- Do not invent a visual style. Always chain to a selected `cover-*` style.
- Do not produce fewer content visuals than the article already has.
- Do not make every content visual a mini cover.
- Do not repeat the same full-article map in every section.
- Keep product names, terms, feature names, and stage labels identical across all assets.
- If the user provided `/article-visual-planner:{style}`, preserve that style name exactly in every chain brief.
