---
name: cover-tips
description: Convert a user's rough cover idea, product description, article topic, or design brief into a standardized template or generic image prompt for a user-specified cover style. Use when the user asks for cover tips, cover prompt formatting, style-specific cover templates, or wants to transform unstructured content into inputs for cover-black-white-minimal, cover-trendy-color-poster, cover-budapest-poster, cover-editorial-collage, or cover-tea-oriental. The user should specify a style such as black-white minimal, trendy color, Budapest, editorial collage, or tea oriental.
---

# Cover Tips

Use this skill as a style-specific cover prompt organizer. It does not choose a style by guessing unless the user explicitly asks for a recommendation. The normal workflow is:

```text
$cover-tips + style + output intent + user content
```

Default output is a standardized template. Only output a full generic image prompt when the user clearly asks for prompt output.

## Supported Styles

Map user style names and aliases to these cover skills:

- Black-white minimal: `cover-black-white-minimal`
  - Aliases: `黑白极简`, `黑白`, `极简`, `minimal`, `bw`, `black white`, `black-white`.
  - Use for rational, restrained, premium, monochrome, Swiss-grid, portfolio-grade covers.
- Trendy color poster: `cover-trendy-color-poster`
  - Aliases: `潮流彩色`, `彩色`, `高冲击`, `trendy`, `color`, `color poster`, `高饱和`.
  - Use for product covers, promotional posters, marketplace covers, launch visuals, bright high-impact graphics.
- Budapest poster: `cover-budapest-poster`
  - Aliases: `布达佩斯`, `budapest`, `复古欧洲`, `电影感`, `明信片`, `酒店感`.
  - Use for retro European cinematic, boutique hotel, postcard, facade, theatrical pastel-pop covers.
- Editorial collage: `cover-editorial-collage`
  - Aliases: `撕纸剪贴`, `剪贴`, `拼贴`, `collage`, `editorial collage`, `torn paper`, `杂志拼贴`.
  - Use for torn-paper collage, magazine collage, satire, social commentary, conflict, handmade editorial covers.
- Tea oriental: `cover-tea-oriental`
  - Aliases: `茶风格`, `茶`, `东方美学`, `宋代美学`, `宋风`, `文人气`, `国风编辑设计`, `汉字成像`, `字中有画`, `tea`, `oriental tea`, `song literati`.
  - Use for high-end oriental cultural posters, tea-aesthetic invitations, character-as-image covers, refined infographics, PPT covers, and exhibition-style visuals with rice-paper texture and Song literati mood.

If no style is specified, ask the user to choose one of: `黑白极简`, `潮流彩色`, `布达佩斯`, `撕纸剪贴`, `茶风格`. Do not silently pick a style unless the user asks for a recommendation.

## Output Intent Detection

Do not require exact syntax. Detect the user's intent from natural language.

- Default: template only.
- Template only: `模版`, `模板`, `整理成格式`, `标准格式`, `调用格式`, `使用格式`.
- Prompt only: `提示词`, `prompt`, `image prompt`, `完整提示词`, `生图提示词`, `直接给 prompt`, `只要提示词`.
- Both: any request that clearly asks for both template and prompt, such as `模版和提示词`, `模板和 prompt`, `模版+提示词`, `两个都要`, `都输出`, `先给模版再给提示词`, `既要标准格式也要完整 prompt`.

When both are requested, output the template first, then the generic image prompt.

## Field Extraction

Extract or infer these fields from the user's content:

- `主题词`: the core title. Preserve product names, regions, denominations, or exact conceptual titles.
- `副标题`: a concise supporting line: benefits, promise, context, or secondary idea.
- `画幅比例`: respect explicit user input. If omitted, infer from use case.
- `语言`: Chinese, English, or mixed Chinese-English.
- `用途`: X cover, marketplace cover, WeChat cover, poster, product poster, knowledge card, portfolio cover, etc.
- `情绪倾向`: infer from content and selected style.
- `禁用元素`: combine user-forbidden items with style defaults.

Ratio defaults:

- X cover: `5:2`.
- Xianyu / marketplace cover: `5:2` unless the user explicitly asks for square marketplace format.
- WeChat cover: `3:2`.
- Poster / event poster: `3:4`.
- Portfolio cover: `4:5`.
- Knowledge card: `1:1` or `4:5`; use `1:1` when no platform is specified.

Language defaults:

- Mostly Chinese input: `中文`.
- Mixed Chinese and English product/platform words: `中英混排`.
- Mostly English input: `英文`.

## Style Defaults

Use these default moods and forbidden elements when the user does not specify them.

Black-white minimal:

- Mood: `理性 / 克制 / 可信 / 冷静 / 精密`.
- Forbidden: `彩色 Apple logo、购物车图标、金币堆、蓝紫霓虹、机器人脸、廉价模板、过度 3D、大段说明文字`.

Trendy color poster:

- Mood: `明亮 / 快速 / 可信 / 高冲击 / 活跃`.
- Forbidden: `廉价电商模板、购物车图标、金币堆、蓝紫霓虹、机器人脸、低端 3D、PPT 风、过度堆字`.

Budapest poster:

- Mood: `复古 / 戏剧感 / 精致 / 轻微荒诞 / 电影感`.
- Forbidden: `机器人脸、蓝紫霓虹、廉价科技感、普通旅行明信片、官方品牌标志、过度 3D、杂乱拼贴`.

Editorial collage:

- Mood: `讽刺 / 冲突 / 街头 / 复古 / 观点感`.
- Forbidden: `机器人脸、蓝紫霓虹、廉价科技感、PPT 布局、干净矩形堆叠、低质脏乱朋克、不可读文字`.

Tea oriental:

- Mood: `安静 / 雅致 / 书卷气 / 东方哲思 / 展览感`.
- Forbidden: `廉价国风模板、俗气红金配色、随机书法背景、过度装饰边框、网红茶室风、杂乱信息、不可读核心字、蓝紫霓虹、低端 3D`.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-{selected-style} 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
情绪倾向：{mood}
禁用元素：{forbidden_elements}
```

### Skill invocation prefix

Detect the current platform and use the matching prefix in the template:

- Claude Code → `/cover-{style}`
- Codex → `$cover-{style}`
- Cursor → `/cover-{style}`
- Gemini CLI → `/cover-{style}`
- Default (unknown platform) → `/cover-{style}`

## Generic Prompt Output

For prompt-only mode, output a generic image-generation prompt. Do not include provider-specific syntax, model names, API names, or agent-specific parameters. Do not mention OpenAI, Claude, Midjourney, Flux, Stable Diffusion, or ComfyUI unless the user explicitly asks.

Build the prompt in the style of the selected cover skill, using its visual language and aspect-ratio discipline. The prompt should include:

1. Exact canvas ratio and canvas size in the first line.
2. Topic, use case, language, A/B/C title layers.
3. Style description.
4. Visual metaphor and 1-3 concrete anchors.
5. Text-image relationship.
6. Typography hierarchy.
7. Color/background system.
8. Mood and extra context.
9. Avoid list.

Do not hard-code one provider's prompt syntax. Use plain English image-prompt language that any image-generation agent can adapt.

## Both Output

When both template and prompt are requested, output:

```text
【模版】
{template}

【提示词】
{generic image prompt}
```

## Error Handling

- If style is missing: ask the user to choose one style and list the four supported styles.
- If user content is missing: ask for at least a title, topic, product description, or article idea.
- If output intent is missing or unclear: default to template only.
- If the user asks for automatic style recommendation, provide one recommended style and then output the requested mode.
