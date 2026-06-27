---
name: cover-3d-eye
description: Generate dark 3D Eye cover/poster image prompts or final images with black grid backgrounds, neon green terminal glow, cream-white condensed titles, privacy/offline motifs, and a blue-white hand-drawn eyeball mascot system. Use when the user asks for 本地AI封面, local AI cover, uncensored AI, offline AI, Ollama tutorial cover, terminal poster, privacy-first AI cover, neon green dark tech poster, or black-green tutorial cover.
---

# 3D Eye Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should feel like a premium dark-mode tutorial poster for running local AI: bold, private, terminal-native, slightly rebellious, and easy to understand at social-feed speed.

This is the cover/poster member of the `3d-eye` visual family. Pair it with `illustration-3d-eye` when the same tutorial also needs step-by-step diagrams, hardware maps, privacy comparisons, or quantization explainers. Use `3d-eye-kit` for a full cover + illustration package.

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
使用 $cover-3d-eye 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
核心钩子：{hook}
视觉主体：{hero_subject}
补充背景：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: optional; infer from use case when omitted.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, WeChat cover, blog header, tutorial cover, YouTube thumbnail, product education poster, knowledge card.
- Core hook: privacy, uncensored, offline, local ownership, hardware fit, quantization, speed, cost, safety mode off, no cloud, no account, no logs.
- Hero subject: terminal window, lock, hardware card, local-vs-cloud split, workflow strip, 3D Eye mascot, torn censorship tape, model file, API endpoint.
- Extra context: optional.
- Forbidden elements: optional; combine with style defaults.

## Aspect Ratio Defaults

- X article cover / X header: `5:2`.
- WeChat article cover: `2.35:1`.
- Blog header / tutorial cover: `16:9`.
- YouTube thumbnail: `16:9`.
- Knowledge card / social post: `1:1`.
- Poster: `3:4` or `4:5`.

State the exact ratio and canvas size in the first line of prompt-only output.

## Visual System

Use these rules strictly:

- Background: deep black or near-black `#050707`, subtle blueprint grid, faint scan lines, corner registration marks, restrained film grain.
- Color: black, off-white title text, neon terminal green `#39FF73`, dim gray secondary text, small red warning accents only when the subject needs error/risk.
- Green usage: terminal command text, active borders, arrows, checkmarks, selected cards, glow around the lock/mascot/focus item.
- Typography: huge condensed bold sans title, cream-white, poster-like; secondary text can use monospaced terminal style.
- UI language: rounded terminal windows, command prompts, CLI cursors, step cards, hardware memory cards, lock/shield icons, cloud/local comparison panels, API endpoint labels.
- Mascot system: optional but recommended for series continuity. Use the 3D Eye mascot as a friendly hand-drawn white eyeball character with a rich blue iris, black sketch outlines, thick expressive eyebrows, black rubber arms/legs, white cartoon gloves, and small black shoes. It should feel intelligent, warm, focused, and action-oriented rather than robotic. Preferred poses: waving welcome, running forward, pointing direction, holding a blue skill card, thumbs-up, open palm, or confident center pose. Keep the mascot blue-white-black with small light-blue motion marks; do not add headset/cap/tool-belt variants unless the user explicitly asks.
- Composition: strong title layer, one clear hero scene, 1-3 supporting UI/diagram elements, generous dark negative space, bright green focus path.
- Mood: private, local, hacker-clean, educational, confident, a little defiant.

Avoid generic cyberpunk city backgrounds, purple/blue neon, RGB gaming rooms, Matrix code rain, robot faces, stock hacker hoodies, photoreal people, cluttered dashboards, random circuit-board backgrounds, cheap 3D icons, illegible microtext, official product logos unless the user explicitly asks, and copying existing case-image text verbatim.

## Cover Composition Modes

Pick one mode unless the user specifies one:

- Censored breakthrough: huge title, torn black tape, green crack/glow, lock or terminal revealing the thesis.
- Local ownership hero: terminal plus unlocked lock/shield, with install-run-own workflow strip.
- Split world: local device vs cloud server, with local highlighted and cloud dimmed.
- Mascot explainer: 3D Eye mascot points to a terminal, card, or lock while title carries the argument.
- Hardware promise: memory/VRAM card, model size, speed tag, local machine emphasis.
- Danger/mistakes poster: red warning bullets with mascot reaction, but keep green as the dominant accent.

## Prompt Output

For prompt-only mode, produce a provider-neutral image-generation prompt. Do not mention provider names, model names, or runtime-specific syntax unless the user explicitly asks.

Include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and core hook.
3. Selected composition mode and why it fits.
4. Hero subject and 1-3 concrete visual anchors.
5. Title hierarchy and text placement plan.
6. Background, terminal UI, neon green color system, typography, mascot usage.
7. A concise avoid list.

If generating directly, keep all analysis internal and output only the generated image result.
