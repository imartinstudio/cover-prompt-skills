---
name: illustration-light-product
description: Generate light-theme AI-native SaaS product explanation illustration prompts or final images with cream-white base, refined UI modules, warm-cool dual color fusion, agent workflow diagrams, and premium product education aesthetics. Use when the user asks for 浅色产品插图, SaaS产品插图, AI产品功能讲解图, agent workflow illustration, product education graphic, feature explanation image, UI module illustration, workflow diagram, or light product tutorial illustration.
---

# Light Product Illustration

Use this skill to create a product education illustration prompt, or call an image generation tool directly when the user asks to generate the final illustration. The result must feel like a premium AI SaaS product education visual: cream-white, precise, warm, modular, and useful. It is not a cover, ad banner, screenshot, or generic stock illustration.

This is the illustration member of the `light-product` visual family. Pair it with `cover-light-product` for the cover of the same article/tutorial, and use `light-product-kit` when the user wants a coordinated cover + illustration package.

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
使用 $illustration-light-product 生成一张插图
主题：{topic}
说明：{description}
画幅比例：{ratio}
用途：{use_case}
产品/场景：{product_context}
重点模块：{focus_module}
图解模式：{diagram_mode}
UI元素：{ui_elements}
系统微文案：{system_microcopy}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Description: what the illustration should explain; optional but infer from topic when possible.
- Aspect ratio: optional; infer from use case.
- Use case: tutorial inline image, product documentation, feature explanation, X article illustration, onboarding image, product update graphic, workflow explanation.
- Product context: product name, feature area, agent workflow, dashboard, automation system, knowledge base, coding workflow, research pipeline, or design workspace.
- Focus module: the one module, card, panel, node, action, state, or workflow segment that matters most.
- Diagram mode: feature module, workflow diagram, before/after, capability map, dashboard slice, system architecture, step sequence; infer from topic.
- UI elements: cards, task panels, workflow lines, status chips, document panels, browser windows, terminal panels, data cards, progress rings, agent nodes, knowledge graph nodes.
- System microcopy: 1-3 short labels such as AGENT, WORKFLOW, RUNNING, COMPLETED, AUTOMATION, MEMORY, CONTEXT, DEPLOY, ANALYZE.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- Tutorial illustration / product docs: `16:9`.
- X article illustration: `16:9`.
- WeChat inline illustration: `4:3`.
- Knowledge card / social post: `1:1`.
- Product update card: `3:2`.
- Vertical tutorial card: `3:4`.

State the exact ratio and canvas size in prompt-only output.

## Visual System

Use these rules strictly:

- Background: cream white, rice white, warm gray white, or cool gray white; light-first only.
- Color: neutral canvas plus balanced warm/cool accents. Warm side uses soft orange, terracotta, warm gold. Cool side uses indigo blue, purple blue, cool gray blue.
- Accent coverage: color should cover only 10-20% of the canvas; 80-90% stays neutral.
- Warm/cool balance: both warm and cool accents must appear in every image, balanced around 4:6 or 6:4.
- UI treatment: simplified premium product UI modules, not screenshots and not high-fidelity app captures.
- Linework: thin precise dividers, soft shadows, clean rounded UI cards, subtle glass layers, refined SaaS diagram lines.
- Typography: modern product typography, clear hierarchy, compact labels, no decorative fonts.
- Whitespace: generous; one illustration should explain one product idea in three seconds.
- Depth: shallow layered cards and modules are allowed, but avoid heavy 3D.

Avoid dark mode, cyberpunk, cheap AI poster art, stock business illustrations, e-commerce banner style, fluorescent gradients, only warm colors, only cool colors, coffee cups, laptops, hands typing, robots, glowing brains, chips/circuit boards, space backgrounds, crowded dashboards, unreadable microtext, and raw screenshots.

## Diagram Mode Selection

Pick one mode unless the user specifies one:

- Feature module: one product feature, one central module, 1-2 callouts.
- Workflow diagram: 3-5 connected steps showing an agent or automation flow.
- Before/after: old workflow vs AI-native workflow, with clear improvement.
- Capability map: a compact set of feature cards around one product goal.
- Dashboard slice: a partial dashboard focused on status, progress, or output.
- System architecture: layers such as input, context, agent, tools, output.
- Step sequence: 2-4 UI states connected by clean arrows.

## Prompt Output

For prompt-only mode, produce a generic image-generation prompt. Do not mention providers, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, description, use case, product context, and focus module.
3. Selected diagram mode.
4. Simplified UI structure and what to remove.
5. Callout, label, and microcopy plan.
6. Background, color, typography, depth, and warm/cool balance.
7. A concise avoid list.

If generating directly, keep all analysis internal and output only the generated image result.
