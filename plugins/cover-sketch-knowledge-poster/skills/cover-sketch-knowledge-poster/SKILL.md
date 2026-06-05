---
name: cover-sketch-knowledge-poster
description: Generate hand-drawn sketch knowledge map cover/poster image prompts or final images with warm paper texture, black marker linework, Anthropic orange highlights, sketchnote typography, and information-architecture diagrams. Use when the user asks for 手绘知识图谱风, sketch knowledge poster, whiteboard framework cover, sketchnote infographic, product education poster, AI tool map, capability map, tutorial cover, knowledge map, X article cover, WeChat cover, or collectible educational diagram covers.
---

# Sketch Knowledge Poster Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result must feel like an expert's hand-drawn knowledge map on warm paper: clear, collectible, educational, and highly shareable.

This is the cover/poster member of the `sketch-knowledge` visual family. Pair it with `illustration-sketch-ui` when the same article or tutorial also needs product UI explanation illustrations, and use `sketch-knowledge-kit` when the user wants a full cover + illustration package.

## Output Type

Use the explicit `--out-type` parameter to decide what to output. Read `--out-type` only as a control parameter, not as part of the user's topic.

- `--out-type template`: output the invocation template only.
- `--out-type prompt`: output the final image prompt only.
- `--out-type all`: output the template first, then the final image prompt.
- Omitted `--out-type`: default to `template`.

Treat `直接生成`, `生成海报`, `生成封面`, `出图`, and `生成图片` as direct image generation when an image tool is available.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-sketch-knowledge-poster 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
知识结构：{knowledge_structure}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: optional; infer from use case when omitted.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X article cover, WeChat cover, knowledge map, tutorial cover, product education poster, knowledge card, PPT title visual, blog header.
- Knowledge structure: hub-and-spoke, workflow, before/after, framework diagram, knowledge map, tree, layered architecture; optional, infer from topic.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- X article cover / X header: `5:2`.
- WeChat article cover: `2.35:1`.
- WeChat post image: `3:2`.
- Tutorial cover / blog header: `16:9`.
- Knowledge map / knowledge card: `1:1` or `4:5`; use `1:1` if platform is unspecified.
- Poster: `3:4` or `4:5`.
- PPT cover: `16:9`.

State the exact ratio and canvas size in the first line of prompt-only output.

## Visual System

Use these rules strictly:

- Background: warm white paper, slight paper grain, subtle fold marks, light scan feel, real paper shadow.
- Color: paper white, black, and Anthropic orange `#E67E22` only.
- Orange usage: key words, underlines, numbers, important arrows, key nodes, core conclusions, callout circles.
- Linework: black fine marker, hand-drawn, slightly irregular, lightly tilted, human, not geometrically perfect.
- Typography: handwritten/sketchnote style inspired by Patrick Hand, Architect Daughter, notebook handwriting.
- Icons: simple unified black line icons such as folders, terminal, code window, document, database, brain, memory, skills, books, lightbulb, calendar, chat, people, workflow, tools, research, analysis, writing, learning, Agent, Claude, Codex.
- Layout: clear title layer, central knowledge structure, concise support notes, generous whitespace, strong hierarchy.

Avoid pure white backgrounds, dark/gradient/tech/cyberpunk backgrounds, multicolor palettes, tech blue, purple, green, red, gold, 3D icons, CAD style, perfect vector geometry, corporate icon libraries, blackletter/futuristic/esports fonts, PPT templates, SaaS banners, commercial ad layouts, unreadable small text, and cluttered information piles.

## Knowledge Structure Selection

Pick one structure unless the user specifies one:

- Hub-and-spoke: for capability maps, tool maps, use-case lists, feature collections.
- Workflow diagram: for tutorials, routes, setup processes, build flows, agent workflows.
- Before/after: for old vs new methods, prompt comparisons, product/agent upgrades.
- Framework diagram: for pillars, architecture layers, product models, capability models.
- Knowledge map: for ecosystems, tool collections, technology routes, industry maps.
- Tree: for taxonomies, learning paths, capability systems.

## Prompt Output

For prompt-only mode, produce a generic image-generation prompt. Do not mention providers, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, and language.
3. Selected knowledge structure and why it fits.
4. Visual metaphor with 1-3 concrete anchors.
5. Text-image relationship and title hierarchy.
6. Background, linework, typography, and black/orange color system.
7. A concise avoid list.

If generating directly, keep all analysis internal and output only the generated image result.
