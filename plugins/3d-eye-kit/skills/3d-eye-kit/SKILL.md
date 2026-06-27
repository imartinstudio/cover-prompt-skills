---
name: 3d-eye-kit
description: Create coordinated cover + illustration briefs for the 3d-eye visual family, combining cover-3d-eye and illustration-3d-eye with shared black grid backgrounds, neon green terminal glow, privacy/offline motifs, and a blue-white hand-drawn eyeball mascot system. Use when the user asks for 本地AI整套封面配图, local AI visual kit, cover plus illustrations, Ollama tutorial visual package, privacy-first AI article visuals, or black-green terminal tutorial assets.
---

# 3D Eye Kit

Use this skill when the user wants a coordinated visual package rather than a single image. It does not generate one mixed image. It produces a decision-ready brief set:

- One cover brief for `cover-3d-eye`.
- One or more illustration briefs for `illustration-3d-eye`.
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
使用 $3d-eye-kit 生成一套封面+配图视觉方案
主题：{topic}
封面用途：{cover_use_case}
配图用途：{illustration_use_case}
配图数量：{illustration_count}
语言：{language}
核心钩子：{hook}
内容结构：{content_structure}
连续角色：{mascot_plan}
补充背景：{context}
```

## Required Inputs

Extract or infer:

- Topic: required.
- Cover use case: X article cover, WeChat cover, blog header, tutorial cover, YouTube thumbnail.
- Illustration use case: tutorial inline images, product documentation, X article images, carousel slides, knowledge cards.
- Illustration count: default `5` when omitted for local AI tutorial packages. Use `3` only for short articles, and use the exact count if the user provides one.
- Language: Chinese, English, or mixed Chinese-English.
- Core hook: uncensored, local ownership, no cloud, offline, privacy, hardware match, quantization, API serving, customization, mistake avoidance.
- Content structure: tutorial outline, setup steps, comparison sections, hardware/quantization/privacy chapters, or feature list; infer a compact structure when omitted.
- Mascot plan: recurring 3D Eye mascot system present in all assets, selected subset only, or absent/minimal.
- Extra context: optional.

## Brief Output

For brief mode, output exactly these sections:

```text
【封面 brief】
调用：$cover-3d-eye
主题词：
副标题：
画幅比例：
语言：
用途：
核心钩子：
视觉主体：
补充背景：
禁用元素：

【配图 brief 1】
调用：$illustration-3d-eye
主题：
说明：
画幅比例：
用途：
图解类型：
重点区域：
连续角色：
补充背景：
禁用元素：

【一致性约束】
标题语气：
黑绿比例：
终端/网格质感：
角色连续性：
图标线稿：
术语统一：

【差异化约束】
封面职责：
配图职责：
避免重复：
```

Repeat the illustration brief section for the requested illustration count.

## Coordination Rules

- Cover role: thesis, promise, emotional hook, shareability, saved-collection value.
- Illustration role: one teachable idea per image: workflow, hardware fit, quantization, privacy path, customization, mistake list, API serving.
- Shared family: near-black grid board, neon green terminal glow, off-white condensed title, monospaced labels, terminal UI panels, crop marks, optional 3D Eye mascot system.
- Shared terminology: keep model names, commands, hardware sizes, privacy claims, and step labels identical across assets.
- Mascot continuity: use the same 3D Eye mascot identity if present: friendly hand-drawn white eyeball body, rich blue iris, black sketch outlines, thick expressive eyebrows, black rubber limbs, white cartoon gloves, and small black shoes. Vary hand poses and action posture by asset, not the base identity.
- Mascot poses: confident center pose for the cover, waving for onboarding, running for action/automation, pointing for direction, holding a blue skill card for skills/capabilities, thumbs-up for success, open palm for explanation, surprised reaction for mistakes.
- Avoid duplication: the cover should not become a dense step-by-step chart; illustrations should not become mini covers with giant marketing headlines.
- Sequence: if the user gives an article outline, map the cover to the whole thesis and the illustrations to the highest-information sections.
- Red accent discipline: red is only for mistakes, warnings, errors, or "safe mode off" tags; green remains the main accent.

## Suggested Package Shape

For a typical "run your own local AI" article, prefer:

1. Cover: big thesis, terminal + lock/mascot, install-run-own promise.
2. Whole flow: pick engine, match hardware, pull model, run UI, customize, serve API.
3. Local vs cloud: what stays on device, what leaves for cloud.
4. Hardware map: RAM/VRAM mapped to model sizes and speed expectations.
5. Quantization: file size vs quality tradeoff with one highlighted sweet spot.
6. Mistakes/customization/API: choose based on the article's outline.

## Prompt Output

For prompt or all mode, convert each brief into a final provider-neutral image-generation prompt. Do not mention provider names, model names, or runtime-specific syntax unless the user explicitly asks.

### Cover Prompt

For the cover, follow `cover-3d-eye` rules. Every cover prompt must include:

1. Exact canvas ratio and size.
2. Topic, subtitle, use case, language, and core hook.
3. Selected cover composition mode.
4. Hero subject and concrete visual anchors.
5. Title hierarchy and text placement plan.
6. Black grid background, neon green terminal glow, off-white condensed typography, terminal UI, mascot plan.
7. A concise avoid list.

```text
【封面 prompt】
<provider-neutral image prompt following the 7 rules above>
```

### Illustration Prompt

For each illustration, follow `illustration-3d-eye` rules. Every illustration prompt must include:

1. Exact canvas ratio and size.
2. Topic, description, use case, diagram type, focus area, and mascot role.
3. Diagram structure and reading path.
4. UI/diagram elements, inactive/dimmed elements, and labels.
5. Neon green highlight plan and red warning accents if needed.
6. Black grid background, terminal UI, typography, mascot constraints.
7. A concise avoid list.

```text
【配图 prompt 1/ N】
<provider-neutral image prompt following the 7 rules above>

【配图 prompt 2/ N】
...
```

### Consistency Across Prompts

- All prompts share the same black grid board, neon green terminal glow, off-white titles, monospaced labels, and blue-white hand-drawn 3D Eye mascot identity.
- Keep the 3D Eye mascot identity stable if used.
- Product names, commands, model names, hardware numbers, and core claims must use identical wording across assets.
- Cover prompt must not describe a dense tutorial chart. Illustration prompts must not describe a giant viral headline unless the user asks for a carousel cover slide.
