---
name: cover-pixel-avatar
description: Generate abstract retro 8-bit pixel art avatar image prompts or final images from a user-uploaded reference photo. Extracts 3-5 memorable visual traits, redesigns (not copies) the subject into a bold high-saturation clash-color square avatar on a solid background. Use when the user uploads an image and asks for pixel avatar, 8-bit avatar, retro game avatar, NFT-style avatar, abstract pixel portrait, Q版像素头像, or social profile picture from a photo.
---

# Pixel Avatar Cover

Use this skill to turn a user-uploaded reference image into one abstract retro pixel art avatar. The result must feel like a redesigned commercial pixel avatar IP—not a pixelated copy of the photo.

If generating the image directly, keep feature extraction and design decisions internal and output only the generated image result. Do not output analysis, multiple drafts, or reference collages. Generate exactly one `1:1` avatar.

If the user sets `--out-type prompt`, output only the final image prompt. If the user sets `--out-type template` or omits `--out-type`, output only the template described in "Template Output" and do not output a generic image prompt.

## Output Type

Use the explicit `--out-type` parameter to decide what to output. Read `--out-type` only as a control parameter.

- `--out-type template`: output the invocation template only.
- `--out-type prompt`: output the final image prompt only.
- `--out-type all`: output the template first, then the final image prompt.
- Omitted `--out-type`: default to `template`.

Backward compatibility:

- Treat `模版`, `模板`, `整理成格式`, `标准格式`, `调用格式`, and `使用格式` as `--out-type template`.
- Treat explicit output requests such as `输出提示词`, `生成提示词`, `完整提示词`, `生图提示词`, `直接给 prompt`, `只要提示词`, `只要 prompt`, and `image prompt` as `--out-type prompt`.
- Treat `模版和提示词`, `模板和 prompt`, `模版+提示词`, `两个都要`, `都输出`, `先给模版再给提示词`, and `既要标准格式也要完整 prompt` as `--out-type all`.
- Treat `直接生成`, `生成头像`, `出图`, `生成像素头像` as direct image generation when an image tool is available.

If `--out-type` has any value other than `template`, `prompt`, or `all`, ask the user to choose one of those three values.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-pixel-avatar 根据上传图片生成像素头像
参考图片：{uploaded_or_pending}
主体类型：{subject_type}
表情倾向：{expression_mood}
背景配色倾向：{background_color_direction}
主体配色倾向：{subject_color_direction}
补充说明：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

- Reference image: required. If missing, ask the user to upload one before continuing.
- Subject type: optional—infer from the image (person, pet, toy, food, object, vehicle, plant, animal, etc.).
- Expression mood: optional for people/animals—infer from the photo if omitted.
- Background color direction: optional—randomize per run if omitted.
- Subject color direction: optional—creative high-saturation recolor allowed.
- Extra context: optional.
- Forbidden elements: optional.

Fixed canvas:

- Always `1:1`, recommended `1024x1024` or `1500x1500`.
- First line of any prompt must state: `SQUARE 1:1 AVATAR CANVAS, {canvas_size}, centered subject, solid flat background only, do not make landscape or portrait strip`.

## Core Specification

请根据我上传的图片，生成一张抽象像素风头像。

核心目标：
不要做写实复制，不要做 1:1 像素化还原，也不要保留原图场景。
请提取主体最有识别度、最有记忆点的 3-5 个特征，并将它们重新设计成一个独立的复古像素头像。

适用对象：
不限人物、宠物、玩具、食物、物品、交通工具、植物、动物或任何主体。
只要图片里有明确主体，都可以转成像素头像。

识别特征提取：
请优先抓取最有辨识度的特征，例如：
- 发型、脸型、眼镜、帽子、表情、配饰
- 毛发、耳朵、尾巴、花纹、身体轮廓
- 服装图案、道具、姿态、动作
- 物体的形状、颜色分区、结构特征
- 任何一眼能记住的视觉符号

设计方式：
请主动进行抽象、夸张、Q版化、符号化、像素化重构。
不要把原图翻译成像素照片，而是基于原图特征重新设计一个头像角色。

画面要求：
- 1:1 正方形头像
- 主体居中或偏中心
- 主体占画面主要面积
- 背景必须是纯色背景
- 不要保留真实场景
- 不要风景、街道、建筑、房间、桌面、草地、天空等原图环境
- 只保留主体和极少量必要符号

像素风格：
- retro 8-bit pixel art
- 清晰像素块
- 黑色或深色像素描边
- 大色块概括
- 强轮廓
- 极简五官
- 图标化头像感
- 像复古游戏角色 / NFT头像 / 社交媒体头像

颜色规则：
颜色可以大胆、有创意，不必真实。
请自动根据主体特征随机选择高饱和撞色方案。

背景颜色必须随机变化，可以从以下方向中自由选择：
亮粉、湖蓝、电光绿、荧光黄、紫色、橘红、天蓝、薄荷绿、珊瑚粉、深蓝、亮橙、酸性绿、玫红、青绿色。

主体颜色也可以创意强化：
头发、毛色、衣服、配饰、道具都可以进行高饱和改色或局部强调。
但要保留主体最核心的识别感。

配色逻辑：
- 主体和背景必须形成明显撞色
- 如果主体偏深色，背景用明亮高饱和色
- 如果主体偏暖色，背景可用冷色
- 如果主体偏冷色，背景可用暖色
- 避免主体和背景颜色太接近
- 不要每次都黄底
- 不要每次都橙发
- 不要固定同一套配色模板

表情与气质：
如果主体是人物或动物，可以根据原图气质自动设计表情：
呆萌、酷脸、震惊、坏笑、害羞、无语、开心、高冷、调皮。
不要每次都用同一种表情。

如果主体是物品：
不要强行加人脸。
优先保留物体轮廓和结构，只在不破坏识别度的前提下轻微拟人化。

禁止：
- 不要写实
- 不要3D
- 不要厚涂
- 不要普通动漫插画
- 不要真实照片质感
- 不要复杂背景
- 不要保留原图真实环境
- 不要过度追求相似度
- 不要让不同图片生成同一个模板

最终效果：
生成一张高度抽象、颜色大胆、纯色背景、像素感强、适合做头像的 1:1 图片。
它应该像一个被重新设计过的商业像素头像IP，而不是原图的像素翻版。

## Internal Workflow

1. Inspect the uploaded reference image. Identify the clearest subject. If no clear subject exists, ask the user to provide a clearer image.
2. Extract exactly 3–5 most memorable traits. Keep this list internal unless asked.
3. Decide subject category (person, animal, pet, object, etc.) and whether expression or light anthropomorphism applies.
4. Choose one fresh high-saturation clash palette for this run. Vary background and accent colors from the approved list; avoid repeating the same template across runs.
5. Redesign the subject as abstract, exaggerated, chibi-like, symbolic pixel art—not a photo translation.
6. Compose a centered `1:1` avatar with solid flat background only.
7. Write the prompt or generate one final image with strict negative constraints.

When an image tool accepts a reference image, pass the user's upload as the visual reference while the prompt enforces redesign rules above. Never ask the model to reproduce the original scene, lighting, or environment.

## Trait Extraction Rules

- Pick traits a viewer would recognize at a glance: silhouette, hair/hat/glasses, color blocks, signature accessory, pose, species markers, product shape zones.
- Drop background clutter, scenery, furniture, sky, street, room, desk, grass, and photographic texture.
- Translate traits into pixel symbols: fewer pixels, stronger outline, simplified face, iconic props only.
- For objects: preserve shape and structural color zones; do not add a face unless it helps recognition without breaking object identity.

## Color System

Background pool (pick one per generation, vary across sessions):

亮粉、湖蓝、电光绿、荧光黄、紫色、橘红、天蓝、薄荷绿、珊瑚粉、深蓝、亮橙、酸性绿、玫红、青绿色.

Clash rules:

- Subject vs background must contrast strongly.
- Dark subject → bright saturated background.
- Warm subject → cool background (or inverse).
- Never default to yellow background every time.
- Never default to orange hair every time.
- Never reuse one fixed palette template.

Subject recolor is allowed for hair, fur, clothing, accessories, and props if core recognition remains.

## Expression Rules

For people and animals only:

- Match vibe from the reference when possible, then stylize: 呆萌、酷脸、震惊、坏笑、害羞、无语、开心、高冷、调皮.
- Rotate expression choices across generations; do not reuse one default face every time.

For objects:

- No forced human face.
- Light anthropomorphism only when it improves recognition.

## Prompt Template

Adapt for `--out-type prompt` or internal image generation:

```text
SQUARE 1:1 AVATAR CANVAS, {canvas_size}. Centered subject occupying most of the frame. Solid flat single-color background only. No scenery, no room, no street, no sky, no desk, no grass.

Create an abstract retro 8-bit pixel art avatar redesigned from the reference subject. Do NOT photorealistically copy the photo. Do NOT do 1:1 photo pixelation. Do NOT keep the original scene or environment.

Subject type: {subject_type}. Memorable traits to preserve and stylize (3-5): {trait_list}. Design approach: abstract, exaggerated, chibi, symbolic pixel reconstruction—commercial pixel avatar IP, retro game character, NFT-style social avatar.

Pixel style: crisp pixel blocks, dark pixel outline, large flat color areas, strong silhouette, minimal facial features, icon-like profile picture.

Palette: background {background_color}, subject accents {subject_colors}. High-saturation clash between subject and background. Creative recolor allowed while keeping core recognition.

Expression / mood: {expression_mood}. Context: {context}.

Avoid: photorealism, 3D render, thick paint, generic anime illustration, photo texture, complex background, original environment, excessive likeness to source photo, same template across different inputs, wrong aspect ratio, landscape or vertical strip, yellow-background default every time, orange-hair default every time, muddy low-contrast palette, analysis text, multiple drafts.
```

## Strict Prohibitions

Never produce:

- Realistic portrait or photo-like pixel filter
- 3D, thick paint, or standard anime illustration
- Original scene, landscape, architecture, interior, or environmental context
- Complex or textured backgrounds
- Over-similarity to the uploaded photo layout
- The same color template and expression for every request
- Multiple layout drafts or explanatory text when generating directly

## Quality Bar

The final image must satisfy:

1. Clearly pixel art with retro 8-bit avatar energy.
2. Recognizable subject rebuilt from 3–5 traits, not copied scene.
3. Bold clash colors on a solid background.
4. Square `1:1` avatar composition ready for profile use.
5. Feels like a new pixel IP character, not a pixelated photograph.
6. When generating directly: one image only, no explanation.

For the archived original Chinese specification, see [docs/source-prompts/cover-pixel-avatar.md](../../../../docs/source-prompts/cover-pixel-avatar.md).
