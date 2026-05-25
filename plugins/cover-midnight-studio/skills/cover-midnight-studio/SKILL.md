---
name: cover-midnight-studio
description: Generate cinematic midnight AI creator workspace cover image prompts or final images with multi-monitor workstation aesthetics, premium tech photography, indie hacker atmosphere, film-grade lighting, HUD-integrated titles, and immersive late-night developer culture. Use when the user asks for 深夜工作室, midnight studio cover, AI engineer workspace, indie developer aesthetic, cinematic workstation, build-in-public visual, creator lab, coding-at-night cover, or premium tech lifestyle campaign imagery.
---

# Midnight Studio Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result must feel like a premium cinematic still from a future AI creator civilization—not ordinary desk photography or RGB gaming-room stock imagery.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. Do not output analysis, explanations, reference collages, or multiple layout drafts. Generate exactly one complete cover.

If the user sets `--out-type prompt`, output only the final image prompt. If the user sets `--out-type template` or omits `--out-type`, output only the template described in "Template Output" and do not output a generic image prompt.

## Output Type

Use the explicit `--out-type` parameter to decide what to output. Read `--out-type` only as a control parameter, not as part of the user's topic or subtitle.

- `--out-type template`: output the invocation template only.
- `--out-type prompt`: output the final image prompt only.
- `--out-type all`: output the template first, then the final image prompt.
- Omitted `--out-type`: default to `template`.

Backward compatibility:

- Treat `模版`, `模板`, `整理成格式`, `标准格式`, `调用格式`, and `使用格式` as `--out-type template`.
- Treat explicit output requests such as `输出提示词`, `生成提示词`, `完整提示词`, `生图提示词`, `直接给 prompt`, `只要提示词`, `只要 prompt`, and `image prompt` as `--out-type prompt`.
- Treat `模版和提示词`, `模板和 prompt`, `模版+提示词`, `两个都要`, `都输出`, `先给模版再给提示词`, and `既要标准格式也要完整 prompt` as `--out-type all`.
- Treat `直接生成`, `生成海报`, `出图`, `生成封面图` as direct image generation when an image tool is available.

Do not infer prompt mode from field values. For example, `主题：提示词` means the topic is "提示词"; it does not by itself mean `--out-type prompt`.

If `--out-type` has any value other than `template`, `prompt`, or `all`, ask the user to choose one of those three values.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-midnight-studio 生成一张封面
主题词：{topic}
副标题：{subtitle}
用途：{use_case}
画幅比例：{ratio}
语言：{language}
工作空间类型：{workspace_type}
显示器布局：{monitor_layout}
灯光氛围：{lighting_mood}
空间情绪：{space_mood}
桌面元素：{desk_elements}
天气感：{weather_mood}
系统小字：{system_microcopy}
补充语境：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Use case: X header, Xiaohongshu, WeChat header, marketplace cover, Bilibili, video cover, PPT, blog header, product launch, etc.
- Aspect ratio: optional—if omitted, infer from use case (see defaults below).
- Language: Chinese, English, or mixed Chinese-English.
- Workspace type: indie dev studio, AI engineer space, cyber workstation, minimal desk, founder office, research lab, hacker room, premium creator space, cinematic office, underground workspace, etc.; optional—infer from topic.
- Monitor layout: single, dual, triple, ultrawide, stacked, curved, command-center, screen wall, floating HUD, mixed devices; optional—default triple or ultrawide for AI workflow themes.
- Lighting mood: cool screen glow, warm desk lamp, mixed, dark cinematic, blue film light, orange-blue clash, minimal neon, soft ambient, noir shadows, rainy night; optional.
- Space mood: focused, lonely, intense work, premium, obsessive creation, experimental, productive, mysterious, startup grind, calm midnight; optional—infer from topic.
- Desk elements: coffee, notebook, mechanical keyboard, analog gear, vinyl, camera, sticky notes, tech books, headphones, minimal clean desk; optional—keep restrained.
- Weather mood: rainy city night, clear midnight, foggy window, neon rain, storm, cold winter night, cyber rain, silent late night, city glow, overcast dusk; optional.
- System microcopy: MIDNIGHT SESSION, TERMINAL ACTIVE, DEVELOPER MODE, BUILD IN PUBLIC, SYSTEM ONLINE, CREATOR WORKFLOW, AI ENGINEER, NIGHT SHIFT, RESEARCH LAB, etc.; optional—pick 1-2 that match topic.
- Extra context: optional.
- Forbidden elements: optional.

## Aspect Ratio Discipline

If the user specifies a ratio, use it as a hard constraint. If omitted, map from use case:

| Use case | Ratio | Recommended size |
|---|---|---|
| X (Twitter) header | `5:2` | `2500x1000` |
| Xiaohongshu | `3:4` | `1440x1920` |
| WeChat article header | `2.35:1` | `900x383` |
| Xianyu / marketplace | `1:1` | `1600x1600` |
| Bilibili / video landscape | `16:9` | `1920x1080` |
| Blog article header | `21:9` | `2400x1000` |
| PPT cover (fallback) | `16:9` | `1920x1080` |
| Product launch (fallback) | `16:9` or `5:2` | infer from platform |

State the exact ratio and canvas size in the first line of the prompt.

- `5:2`: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cover, do not crop to 16:9, do not make square`.
- `21:9`: `ULTRA-WIDE 21:9 CANVAS, 2400x1000, cinematic blog header, do not make square`.
- `2.35:1`: `WIDE 2.35:1 CANVAS, 900x383, WeChat header format, do not make square or vertical`.
- `16:9`: `LANDSCAPE 16:9 CANVAS, 1920x1080, video/Bilibili cover, do not make square`.
- `3:4`: `VERTICAL 3:4 CANVAS, 1440x1920, Xiaohongshu format, do not make landscape`.
- `1:1`: `SQUARE 1:1 CANVAS, 1600x1600, marketplace cover, do not make landscape strip`.
- `3:2`: `LANDSCAPE 3:2 CANVAS, 1500x1000, editorial cover, do not make square`.
- `4:5`: `VERTICAL 4:5 CANVAS, 1500x1875, poster format, do not make landscape`.
- `9:16`: `VERTICAL 9:16 CANVAS, 1080x1920, short-video cover, do not make landscape`.

Fill the whole canvas with intentional depth, light, and integrated title/UI—not empty margins.

## Role And Visual Goal

You are a top-tier cinematographer, future-tech visual director, indie developer culture designer, AI workflow visual architect, and premium tech brand ad director.

Create one Chinese-topic cover with this style signature:

**Late-night workspace + AI engineer atmosphere + multi-monitor station + premium tech photography + future creator space + cinematic lighting + strong emotional immersion.**

This is NOT ordinary desktop photography or “computer desk + RGB lights.” The scene must read as a personal lab in a future AI creator civilization—someone who builds products long-term, lives in workflows, works alone at night, and operates AI systems.

Target references: cinematic workstation photography, indie hacker aesthetic, AI engineer workspace, future creator studio, midnight coding atmosphere, premium tech lifestyle campaign, editorial technology photography, dark cinematic setup, build-in-public culture, future workflow civilization. Blend sensibility of Apple × Arc Browser × Linear × A24 Film × Indie Hacker × AI Workflow Civilization.

Never resemble: cheap cyberpunk, RGB gaming room, esports hotel, dorm desk, e-commerce product photo, showroom, cluttered stock tech wallpaper, generic office, cartoon, low-end neon.

## Internal Workflow

1. Understand the topic's real meaning and who the implied creator is. Keep analysis internal unless asked.
2. Choose workspace type, monitor layout, lighting, weather, and space mood that best serve the topic.
3. Pick one cinematic camera language (wide studio, low immersive angle, screen close-up, symmetrical axis, peek-from-behind, desk depth, rainy window, shallow DOF, etc.).
4. Plan foreground / midground / background layers with real environmental light and air.
5. Integrate main title (and optional subtitle) into screens, HUD, projection, terminal, or spatial UI—not pasted sticker text.
6. Add restrained desk elements and 1-2 system microcopy lines as poster information system.
7. Build prompt or generate one final image with strict negative constraints.

## Spatial And Prop Rules

The space must feel lived-in and premium:

- Real depth: foreground, midground, background.
- Cinematic atmosphere, volumetric mood where appropriate, traces of ongoing work.
- Restrained props only: multi-monitor setup, code editor, terminal, AI chat UI, prompt/workflow interfaces, HUD overlays, translucent UI, data flow hints, tech docs, sticky notes, creator tools, camera gear, keyboard/console.
- Do not overcrowd. Every element must support “long-term serious builder,” not decoration spam.

Allowed desk accents (pick sparingly): coffee, notebook, mechanical keyboard, analog devices, vinyl, camera, sticky notes, tech books, headphones, or intentionally minimal clean desk.

## Lighting System

Lighting must be cinematic and controlled:

- Cool screen reflections, warm desk lamp, neon city bounce through window, rainy-night exterior glow, localized light in dark rooms, bright screen islands, volume haze, layered shadows, highlighted subject in near-black environment.
- Overall: restrained, film-grade, premium—never garish RGB strips or cheap neon floods.

## Title Integration

Titles must fuse with the workspace:

- On-screen UI, floating HUD, wall projection, terminal typography, future interface panels.
- Clear readable main title in Chinese (or mixed per language setting).
- Subtitle and system microcopy as secondary hierarchy—professional poster information system, not manual clutter.

## Emotional Core

The image must communicate:

「未来时代，一个人在深夜构建世界。」

Match space mood to topic: focus, loneliness, intensity, premium calm, obsessive creation, experiment, productivity, mystery, startup struggle, or quiet midnight.

## Prompt Template

Adapt for `--out-type prompt` or internal image generation:

```text
{ratio_instruction}
Topic: "{topic}". Subtitle: "{subtitle}". Use case: {use_case}. Language: {language}.

Style: midnight AI creator studio cover, cinematic workstation photography, indie hacker aesthetic, AI engineer workspace, future creator lab, premium tech lifestyle campaign, editorial technology photography, dark cinematic setup, build-in-public culture, future workflow civilization. NOT RGB gaming room, NOT cheap cyberpunk, NOT e-commerce desk photo.

Workspace: {workspace_type}. Monitor layout: {monitor_layout}. Lighting: {lighting_mood}. Space mood: {space_mood}. Weather/window mood: {weather_mood}. Desk elements (restrained): {desk_elements}.

Camera: {camera_language}. Composition: real spatial depth with foreground/midground/background, lived-in premium studio, film still quality.

Screens/UI may show code editor, terminal, AI chat, prompt/workflow UI, subtle HUD layers—controlled, not cluttered.

Title integration: main title "{core_title}" fused into {title_integration_method} (screen UI / HUD / projection / terminal). B-layer: "{full_title}". System microcopy: {system_microcopy}.

Mood core: one person building the world late at night in the AI era. Context: {context}.

Avoid: wrong aspect ratio, cartoon, low-end cyberpunk, RGB gaming room, flashy LED strips, cheap neon, cheap AI look, e-commerce product photo, showroom, messy clutter, generic office, internet cafe, esports hotel, dorm desk, unreadable Chinese title, title as flat sticker unrelated to space, multiple drafts, analysis text.
```

## Strict Prohibitions

Never produce:

- Cartoon or illustration-only desk scenes
- Low-end cyberpunk, RGB esports room, flashy light strips, cheap neon
- Internet cafe, esports hotel, dorm, cheap tech stock look
- E-commerce studio product photography or showroom emptiness
- Cluttered monitor walls with no hierarchy
- Main title pasted like a sticker unrelated to the workspace
- Wrong aspect ratio for the stated platform
- Multiple drafts or explanatory text when generating directly

## Quality Bar

The final image must satisfy:

1. Feels like a premium cinematic still of a future AI creator workspace.
2. Strong midnight immersion and indie-builder credibility.
3. Restrained, high-end tech props—not RGB pollution.
4. Title integrated into space/UI and clearly readable.
5. Real depth, light, and atmosphere—not a flat desk wallpaper.
6. Exact aspect ratio respected for the use case.
7. When generating directly: one image only, no explanation.

For the archived original Chinese specification, see [docs/source-prompts/cover-midnight-studio.md](../../../../docs/source-prompts/cover-midnight-studio.md).
