---
name: illustration-3d-eye
description: Generate dark 3D Eye tutorial illustration prompts or final images with black grid boards, neon green diagram lines, terminal UI cards, hardware/quantization/privacy explainers, and a blue-white hand-drawn eyeball mascot system. Use when the user asks for 本地AI配图, local AI tutorial illustration, Ollama setup diagram, hardware map, quantization chart, local vs cloud comparison, privacy flow, terminal workflow graphic, or black-green explainer image.
---

# 3D Eye Illustration

Use this skill to create a tutorial or product-education illustration prompt, or call an image generation tool directly when the user asks to generate the final illustration. The result should explain one concrete idea in the `3d-eye` visual family: dark board, neon green focus path, terminal-native UI, and an optional recurring 3D Eye mascot.

This is the illustration member of the `3d-eye` family. Pair it with `cover-3d-eye` for the cover of the same article/tutorial. Use `3d-eye-kit` when the user wants a coordinated cover + illustration package.

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
使用 $illustration-3d-eye 生成一张配图
主题：{topic}
说明：{description}
画幅比例：{ratio}
用途：{use_case}
图解类型：{diagram_type}
重点区域：{focus_area}
连续角色：{mascot_role}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Description: what the illustration should explain; optional but infer from topic when possible.
- Aspect ratio: optional; infer from use case.
- Use case: tutorial inline image, product documentation image, X article illustration, carousel slide, knowledge card, feature walkthrough.
- Diagram type: flow, step cards, local-vs-cloud comparison, hardware map, quantization chart, mistake checklist, privacy path, customization options, terminal state.
- Focus area: the single step, comparison, card, metric, warning, or command that matters most.
- Mascot role: waving welcome, running action, pointing guidance, skill-card helper, thumbs-up, open-palm explanation, confident center pose, surprised reaction, absent/minimal.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- Tutorial illustration / product docs: `16:9`.
- X article illustration: `16:9`.
- WeChat inline illustration: `4:3`.
- Knowledge card / carousel slide: `1:1`.
- Vertical tutorial card: `3:4`.

State the exact ratio and canvas size in prompt-only output.

## Visual System

Use these rules strictly:

- Background: black or near-black grid board, subtle technical blueprint lines, corner crop marks, restrained grain and glow.
- Color: black base, off-white headings, neon green `#39FF73` for active paths and emphasis, dim gray for inactive/cloud/secondary elements, red only for errors or warnings.
- Typography: large cream-white condensed headings, monospaced terminal labels, short readable phrases only.
- UI elements: terminal windows, command prompts, step cards, comparison panels, memory chips, file cards, sliders, checklists, bar charts, lock/shield/cloud/device icons.
- Lines: dotted arrows, solid green active arrows, highlighted card borders, bracket labels, terminal cursor blocks.
- Mascot system: optional but useful for continuity. Use the 3D Eye mascot as a friendly hand-drawn white eyeball character with a rich blue iris, black sketch outlines, thick expressive eyebrows, black rubber arms/legs, white cartoon gloves, and small black shoes. Choose the pose that supports the diagram: waving for onboarding, running for action/automation, pointing for direction, holding a blue skill card for skills/capabilities, thumbs-up for success, open palm for explanation, or surprised reaction for mistakes. Keep the mascot blue-white-black with small light-blue motion marks. Do not let the mascot replace the explanatory diagram.
- Information density: one idea per image. Big labels, clear path, no tiny unreadable paragraphs.

Avoid generic cyberpunk, Matrix rain, blue/purple neon, photoreal people, stock 3D robots, busy dashboards, official logos unless requested, dense code blocks, fake screenshots, random charts, and copying exact case-image copy or layout without adapting to the user's topic.

## Diagram Selection

Pick one mode unless the user specifies one:

- Whole flow: terminal start, 4-6 cards, final highlighted result.
- Local vs cloud: two lanes or two panels; local bright green, cloud dim gray.
- Hardware map: memory/VRAM rows mapped to model sizes, one highlighted sweet spot.
- Quantization chart: bars or file-size comparison, one green highlighted compromise.
- Privacy path: what leaves the machine vs what stays local.
- Mistake checklist: 3-5 warning cards, red bullets, mascot reaction.
- Customization options: three large cards along an effort arrow.
- Terminal state: terminal window plus lock/shield/status tag.

## Prompt Output

For prompt-only mode, produce a provider-neutral image-generation prompt. Do not mention provider names, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, description, use case, diagram type, focus area, and mascot role.
3. Selected diagram structure and the reading path.
4. Specific UI/diagram elements to include and which elements are inactive/dimmed.
5. Green highlight plan and any red warning accents.
6. Background, typography, terminal UI, and mascot constraints.
7. A concise avoid list.

If generating directly, keep all analysis internal and output only the generated image result.
