---
name: illustration-sketch-ui
description: Generate hand-drawn sketch UI product education illustration prompts or final images with warm paper texture, black marker UI redraws, Anthropic orange highlights, large whitespace, arrows, and simplified interface explanation. Use when the user asks for 产品 UI 插图, tutorial illustration, product feature illustration, sketch UI, Claude product illustration, hand-drawn interface, 功能讲解图, 教程配图, X article illustration, product explanation graphic, or UI walkthrough images.
---

# Sketch UI Illustration

Use this skill to create a product education illustration prompt, or call an image generation tool directly when the user asks to generate the final illustration. The result must not be a screenshot, SaaS banner, UI mockup, or product ad. It should look like a product designer redrew the important part of a real interface on warm paper with black marker and orange highlighter.

This is the illustration member of the `sketch-knowledge` visual family. Pair it with `cover-sketch-knowledge-poster` for the cover of the same article/tutorial, and use `sketch-knowledge-kit` when the user wants a coordinated cover + illustration package.

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
使用 $illustration-sketch-ui 生成一张插图
主题：{topic}
说明：{description}
画幅比例：{ratio}
用途：{use_case}
界面来源/产品场景：{product_context}
重点区域：{focus_area}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Description: what the illustration should explain; optional but infer from topic when possible.
- Aspect ratio: optional; infer from use case.
- Use case: tutorial illustration, product feature explanation, X article illustration, product documentation image, onboarding image, function walkthrough.
- Product context: product name, interface source, feature area, or user flow.
- Focus area: the one button, menu, panel, state, setting, or interaction that matters most.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- Tutorial illustration / product docs: `16:9`.
- X article illustration: `16:9`.
- WeChat inline illustration: `4:3`.
- Knowledge card / social post: `1:1`.
- Vertical tutorial card: `3:4`.

State the exact ratio and canvas size in prompt-only output.

## Visual System

Use these rules strictly:

- Background: warm white paper, slight paper texture, subtle folds, light scan feel.
- Color: paper white, black, and Anthropic orange `#E67E22` only.
- Orange usage: important button, key feature, focus area, key label, important state, callout mark, arrow highlight.
- UI treatment: redraw the real interface as simplified hand-drawn UI, not a screenshot and not high fidelity.
- Linework: black fine marker, hand-drawn borders, buttons, inputs, menus, nav bars, icons, and arrows.
- Typography: handwritten/notebook/sketchnote style; clear, warm, educational.
- Whitespace: roughly 80% whitespace and 20% content.
- Arrows: use clear hand-drawn arrows to guide attention toward the focus area.

Avoid real screenshots, high-fidelity UI, Figma/Dribbble/modern marketing page style, tech gradients, glassmorphism, dark backgrounds, cyberpunk lighting, colorful UI systems, 3D, complex flow lines, decorative curves, crowded layouts, and unnecessary interface details.

## Simplification Workflow

When transforming a product interface:

1. Preserve the real layout structure.
2. Remove secondary controls, repeated text, decorative UI, and noise.
3. Keep only the focus area and the minimum surrounding context needed to understand it.
4. Use orange to mark the true point of attention.
5. Add one short handwritten label or arrow explanation if needed.

## Composition Selection

Pick one mode unless the user specifies one:

- Single feature explanation: simplified UI block, arrow, highlighted feature.
- Feature entry explanation: partial interface, enlarged focus area, arrow callout.
- Function walkthrough: 2-4 simplified states connected by clear arrows.
- Before/after UI: old state and new state with orange emphasis on the change.
- Conceptual UI diagram: interface fragments plus short explanatory labels.

## Prompt Output

For prompt-only mode, produce a generic image-generation prompt. Do not mention providers, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, description, use case, product context, and focus area.
3. Selected composition mode.
4. Simplified UI structure and what to remove.
5. Arrow/callout plan.
6. Background, linework, typography, and black/orange color system.
7. A concise avoid list.

If generating directly, keep all analysis internal and output only the generated image result.
