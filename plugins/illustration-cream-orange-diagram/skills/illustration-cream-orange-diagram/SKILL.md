---
name: illustration-cream-orange-diagram
description: Generate cream-orange technical article illustration prompts or final images with warm paper background, charcoal linework, burnt-orange arrows, UI-like panels, workflow diagrams, feedback loops, architecture modules, before-after comparisons, and AI engineering explainer visuals. Use when the user asks for 奶油橙文章配图, AI工程配图, 技术解释插图, workflow diagram, feedback loop illustration, architecture module graphic, tutorial inline image, X article illustration, or product education diagram.
---

# Cream Orange Diagram Illustration

Use this skill to create inline article illustration prompts, or generate final images when the user explicitly asks for direct image generation. The result should explain one idea quickly: a workflow step, architecture slice, comparison, evaluation loop, UI state, or decision point.

This is the illustration member of the `cream-orange-knowledge` visual family. Pair it with `cover-cream-orange-knowledge-poster` for article covers, and use `kit-cream-orange-knowledge` when the user wants a coordinated cover + illustration package arranged from article content.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the invocation template only.
- `--out-type prompt`: output the final image prompt only.
- `--out-type all`: output the template first, then the final image prompt.
- Omitted `--out-type`: default to `template`.

Treat `直接生成`, `生成插图`, `生成配图`, `出图`, and `生成图片` as direct image generation when an image tool is available.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $illustration-cream-orange-diagram 生成一张配图
主题：{topic}
说明：{description}
画幅比例：{ratio}
用途：{use_case}
图解模式：{diagram_mode}
重点区域：{focus_area}
视觉锚点：{visual_anchor}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Description: what the illustration should explain; infer when omitted.
- Aspect ratio: optional; infer from use case.
- Use case: article inline image, tutorial step image, X article illustration, WeChat inline image, product education graphic, architecture explainer.
- Diagram mode: single concept, workflow step, before/after, loop cycle, architecture slice, UI workflow, decision checklist, metric dashboard.
- Focus area: the most important node, arrow, panel, control, metric, or outcome.
- Visual anchor: interface panel, loop arrow, ladder step, control gate, architecture block, chart, checklist, or infer from topic.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- Article inline image / X article illustration: `16:9`, 2048x1152.
- WeChat inline illustration: `4:3`, 1600x1200.
- Knowledge card: `1:1`, 1536x1536.
- Vertical tutorial card: `3:4`, 1536x2048.
- Wide comparison strip: `5:2`, 1500x600.

State the exact ratio and canvas size in prompt-only output.

## Visual System

Use these rules strictly:

- Background: warm cream paper with subtle grid, paper grain, or faint notebook texture.
- Color: cream base, charcoal black, warm gray, burnt orange, muted terracotta.
- Orange usage: the true focus area, primary arrows, important state, active loop segment, selected metric, or key callout.
- Linework: clean charcoal outlines, lightly hand-drawn edges, technical but approachable.
- Typography: short labels only; use bold uppercase section labels and handwritten micro-labels.
- Panels: rounded or squared paper cards, browser-like windows, checklist boards, metric panels, architecture blocks, status chips.
- Arrows: directional, readable, limited to the required logic path.
- Density: lower than a cover; explain one concept, not the whole article.

Avoid full article diagrams, dense tiny text, decorative arrows with no logic, dark mode, blue-purple gradients, glossy SaaS UI, photoreal screenshots, 3D render style, mascot-heavy compositions, and random technology filler.

## Diagram Mode Selection

Pick one mode unless the user specifies one:

- Single concept: one central object with 2-4 callouts.
- Workflow step: 3-5 connected blocks showing input, action, output, feedback.
- Before/after: two columns with one clear contrast.
- Loop cycle: circular or figure-eight feedback process with 3-5 states.
- Architecture slice: stacked modules or hub-and-spoke components for one subsystem.
- UI workflow: simplified interface panels showing clarification, progress, review, approval, or confidence.
- Decision checklist: criteria, risks, metrics, and a final recommendation path.
- Metric dashboard: charts, signals, evals, failures, user feedback, and improvement action.

## Prompt Output

For prompt-only mode, produce a provider-neutral image-generation prompt. Do not mention providers, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, description, use case, diagram mode, focus area, and visual anchor.
3. Simplified composition plan.
4. Arrow/callout plan with the orange emphasis.
5. Background, linework, typography, panels, and color system.
6. A concise avoid list.

If generating directly, keep analysis internal and output only the generated image result.
