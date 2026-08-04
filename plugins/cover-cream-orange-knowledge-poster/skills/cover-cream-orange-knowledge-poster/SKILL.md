---
name: cover-cream-orange-knowledge-poster
description: Generate cream-orange technical knowledge poster cover prompts or final images with editorial infographic layout, warm paper background, charcoal typography, burnt-orange highlights, system architecture diagrams, feedback loops, maturity ladders, comparison frameworks, and AI engineering visual language. Use when the user asks for 奶油橙知识海报, AI工程封面, 系统架构封面, loop-first systems poster, technical infographic cover, X article cover, WeChat cover, AI agent workflow poster, or architecture explainer cover.
---

# Cream Orange Knowledge Poster Cover

Use this skill to create a cover/poster prompt, or generate the final image when the user explicitly asks for direct image generation. The result should feel like a premium editorial technical infographic: warm paper, strong headline, clear system logic, hand-drawn diagram energy, and enough detail to reward close reading.

This is the visual style member of the `cream-orange-knowledge` family. Use it directly for covers/posters. When the user wants a coordinated article package, route planning through the matching available with-docs sibling for this style if it exists.

## Output Type

Use the explicit `--out-type` parameter to decide what to output.

- `--out-type template`: output the invocation template only.
- `--out-type prompt`: output the final image prompt only.
- `--out-type all`: output the template first, then the final image prompt.
- Omitted `--out-type`: default to `template`.

Treat `直接生成`, `生成海报`, `生成封面`, `出图`, and `生成图片` as direct image generation when an image tool is available.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-cream-orange-knowledge-poster 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
信息结构：{information_structure}
核心视觉隐喻：{visual_metaphor}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: optional; infer from use case.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X article cover, WeChat cover, blog header, tutorial cover, technical infographic, knowledge poster, PPT title visual.
- Information structure: stage progression, before/after comparison, system architecture, feedback loop, maturity ladder, decision framework, bounded vs unbounded contrast.
- Visual metaphor: loop, ladder, control room, architecture stack, map, flywheel, pipeline, dashboard, board diagram, or infer from topic.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- X article cover / X header: `5:2`, 1500x600.
- WeChat article cover: `2.35:1`, 1640x700.
- Blog header / tutorial cover: `16:9`, 2048x1152.
- Technical infographic / knowledge poster: `4:3`, 1600x1200.
- Square knowledge card: `1:1`, 1536x1536.
- Vertical poster: `4:5`, 1600x2000.
- PPT cover: `16:9`, 1920x1080.

State the exact ratio and canvas size in prompt-only output.

## Visual System

Use these rules strictly:

- Background: warm cream paper, soft off-white, subtle grid or paper grain, light scan texture, faint shadowed border when useful.
- Color: cream base, charcoal black, warm gray, burnt orange, muted terracotta, small beige accents.
- Orange usage: headline keyword, stage tabs, arrows, loop segments, important nodes, chart bars, callout badges, status chips.
- Linework: black/charcoal marker outlines with clean editorial control, slightly hand-drawn but more polished than whiteboard sketches.
- Typography: bold condensed editorial headline for the title, hand-drawn or notebook labels for diagram details, clear hierarchy.
- Icons: simple unified line icons such as prompt bubble, LLM brain, database, code window, gear, checklist, chart, magnifier, user, shield, memory, API, tool, human review.
- Layout: strong title layer, structured diagram body, visible reading path, modular panels, clear arrows, no random decoration.
- Texture: use light dot grids, corner marks, thin dividers, paper tape, ruler-like lines, or small circuit traces sparingly.

Avoid dark/cyberpunk backgrounds, blue-purple AI gradients, glossy 3D, neon tech, realistic robots, stock business people, photoreal UI screenshots, chaotic arrows, unreadable microtext, fake dense paragraphs, random circuit-board filler, and palettes that drift away from cream/orange/charcoal.

## Information Structure Selection

Pick one primary structure unless the user specifies one:

- Stage progression: for evolution, roadmap, maturity, migration, learning paths.
- Before/after comparison: for prompt-first vs loop-first, old vs new workflows, risk comparisons.
- System architecture: for AI agents, RAG, tool use, memory, observability, orchestration.
- Feedback loop: for evaluation, monitoring, continuous improvement, product iteration.
- Maturity ladder: for capability levels, organizational adoption, system sophistication.
- Decision framework: for practical team choices, tradeoffs, evaluation criteria.
- Bounded vs unbounded contrast: for safety, guardrails, autonomy, human review.

## Prompt Output

For prompt-only mode, produce a provider-neutral image-generation prompt. Do not mention provider names, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, and language.
3. Selected information structure and why it fits.
4. Visual metaphor with 1-3 concrete anchors.
5. Text-image relationship and title hierarchy.
6. Background, linework, typography, and cream-orange-charcoal color system.
7. Diagram logic: panels, arrows, loop direction, labels, and hierarchy.
8. A concise avoid list.

If generating directly, keep analysis internal and output only the generated image result.
