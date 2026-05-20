---
name: cover-tea-oriental
description: Generate high-end oriental tea-aesthetic poster/cover image prompts or final images with Chinese character-as-image structure, Song dynasty literati aesthetics, rice paper texture, gongbi ink-wash collage, refined information hierarchy, exhibition poster quality, and restrained cultural atmosphere. Use when the user asks for 茶风格, 东方美学, 宋代美学, 国风编辑设计, 汉字成像, 字中有画, high-end cultural poster, invitation, infographic, PPT cover, knowledge poster, or collectible oriental visual cover.
---

# Tea Oriental Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should feel like a collectible oriental aesthetic poster, cultural exhibition visual, high-end invitation, refined infographic, or art-book cover rather than a generic guofeng template.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. If the user sets `--out-type prompt`, output only the final image prompt. If the user sets `--out-type template` or omits `--out-type`, output only the template described in "Template Output" and do not output a generic image prompt.

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

Do not infer prompt mode from field values. For example, `主题：提示词` means the topic is "提示词"; it does not by itself mean `--out-type prompt`.

If `--out-type` has any value other than `template`, `prompt`, or `all`, ask the user to choose one of those three values.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-tea-oriental 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
情绪倾向：{mood}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Use case: PPT cover, infographic, invitation, knowledge poster, cultural poster, exhibition visual, brand cover.
- Topic / main title: required.
- Core character / core word: optional; if missing, extract the most visual and spiritually accurate Chinese character or short phrase from the topic.
- Required information: title, subtitle, time, place, organizer, notes, knowledge points, slogan, etc.
- Aspect ratio: one of `16:9`, `3:4`, `3:2`, `4:5`, `5:2`; treat it as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Mood: more poetic, rational, academic, elegant, modern, exhibition-like, bookish, quiet, etc.
- Forbidden elements: optional.

Default canvas:

- PPT cover / landscape presentation: `16:9`, recommended `1920x1080`.
- Poster / invitation / exhibition poster: `3:4`, recommended `1500x2000`.
- Article / WeChat cover: `3:2`, recommended `1500x1000`.
- Knowledge card: `4:5`, recommended `1600x2000`.
- X cover: `5:2`, recommended `2500x1000`.

## Aspect Ratio Discipline

State the exact ratio and canvas size in the first line of the prompt.

- For `16:9`, write: `LANDSCAPE 16:9 CANVAS, 1920x1080, premium oriental PPT cover, do not make square or vertical`.
- For `3:4`, write: `VERTICAL 3:4 CANVAS, 1500x2000, collectible oriental exhibition poster, do not make square`.
- For `3:2`, write: `LANDSCAPE 3:2 CANVAS, 1500x1000, refined editorial cover format, do not make square`.
- For `4:5`, write: `VERTICAL 4:5 CANVAS, 1600x2000, high-end knowledge card or cultural poster, do not make square`.
- For `5:2`, write: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide oriental cover, do not crop to 16:9, do not make square`.
- Fill the whole canvas with deliberate character structure, paper texture, image-in-character detail, and refined information hierarchy.
- Add negative constraints against `wrong aspect ratio`, `generic guofeng template`, `cheap decorative border`, `random calligraphy background`, and `unreadable character`.

## Internal Workflow

1. Understand the topic's cultural meaning, information purpose, and use case. Do not show this analysis unless asked.
2. Extract the core character or core word. Prefer one Chinese character when it can carry the topic; use a short word only when one character would distort the meaning.
3. Split text into title layers: core character/word, full title, subtitle, required information, poetic lead, and small closing notes.
4. Choose the image content embedded inside the core character based on the topic family.
5. Decide how the core character works simultaneously as text, image container, and metaphor.
6. Build a prompt with character-as-structure composition, gongbi / ink-wash / old-paper image language, disciplined editorial information design, and restrained color.
7. Add negative constraints against cheap national-style templates, overdecorated borders, stock tea imagery, messy text, vulgar gold-red palettes, and pasted illustration.

## Core Visual Principle

The main visual must follow:

```text
Chinese character structure + illustration underlay/mask + information design + oriental negative space
```

The core character or core word is not ordinary typography. It must become the poster's visual skeleton:

- Use oversized Chinese character structure as the central symbol.
- Treat the character as an image container through masking, underlay, silhouette, paper-cut-like insertion, or image-inside-strokes.
- Let the embedded image form a miniature narrative: people, objects, mountains, tea room, courtyard, books, diagrams, vessels, knowledge symbols, event scene, or theme-specific fragments.
- Keep the character readable at first glance even when image content is embedded.
- Avoid making the character a generic calligraphy sticker placed on top of a background.

## Topic Families And Embedded Content

Choose the strongest theme family and embed content accordingly:

- Tea / culture / art / history / philosophy: classical gongbi figures, tea utensils, mountain water, courtyard, literati gathering, scrolls, bamboo, stone, books, incense, old paintings, quiet tea-room scenes.
- Knowledge / academic / science / theory: orientalized diagrams, symbolic vessels, structured scenes, annotated tea-table logic, scroll-like flow, minimal nodes, conceptual objects, restrained labels.
- Invitation / event / salon / exhibition: people and space interaction, tea table, entrance, hanging scroll, venue atmosphere, lamps, garden, formal information blocks.
- PPT cover / report / lecture: simpler character silhouette, stronger recognition, fewer objects, cleaner negative space, conceptual image-in-character metaphor.
- Brand / product / publication: vessel, paper, bookbinding, seal mark, label, package texture, refined editorial still life.

Use only precise, inspectable details. The image should reward close viewing, but the whole poster must remain calm and readable.

## Visual Language

Preferred image language:

- Chinese classical gongbi painting, ink-wash light color, old-painting collage, paper-based print texture.
- Rice paper, aged paper, fine paper fibers, pale water stains, faint flower shadows, old book traces, subtle time marks.
- Scroll fragments, antique painting scraps, tea vessel texture, courtyard, rocks, book desk, bamboo grove, cloud mist, lamp shadow, paper-color mineral pigments.
- Slight bleeding, worn edges, multiply-print feel, art microprint texture; image should look printed into paper, not pasted on top.

If the topic is modern, combine modern infographic language with oriental restraint. Keep the design cultural, quiet, and professional.

## Layout And Information Hierarchy

The poster must include a mature hierarchy like an exhibition poster, cultural invitation, art-book cover, or editorial infographic:

1. Main title: prominent topic title, often vertical on the right or near the core character; elegant, slender, stable Chinese serif / Ming style.
2. Subtitle / English auxiliary title: low-key fine serif publication style.
3. Basic information zone: time, place, organizer, audience, series name, event theme, or issue number, typeset neatly.
4. Poetic lead: one concise oriental line that strengthens mood without becoming empty.
5. Bottom notes / slogan / remark: small text closure for completeness.
6. For infographics or knowledge posters: include logical sections, subheads, key takeaways, and structured information, but integrate them with the paper, scroll, label, or annotation system.

Do not crowd the layout. Use negative space as a structural element. Text must be accurate, tidy, and readable.

## Typography

- Chinese: Songti, Ming-style, classical serif, bookish, narrow, elegant, stable.
- English: fine serif, classic publication style, quiet and non-decorative.
- Main title can be vertical.
- Auxiliary information can live in upper-left small text, right-side vertical notes, bottom editorial metadata, or scroll-label blocks.
- Use small seal marks, title slips, and stamp-like elements only as restrained accents.
- Avoid random brush-calligraphy chaos, fake ancient fonts, heavy decorative borders, and illegible text.

## Color System

Use low-saturation colors:

- Base: warm rice white, old paper, light gray, parchment, faint ink.
- Tea / wood: tea brown, deep tea, quiet wood, light ochre, warm gray.
- Green / ink: gray green, bamboo green, pale ink, moss, mineral green.
- Accent: a tiny cinnabar seal, muted indigo, old gold, or pale mineral blue only when needed.

Rules:

- Use 3-5 colors, mostly soft and restrained.
- Avoid vulgar red-gold, saturated neon, ecommerce orange, cyber blue-purple, and one-note beige monotony.
- The palette must feel like Song dynasty literati aesthetics, high-end publication design, and cultural exhibition identity.

## Prompt Template

Adapt this template:

```text
Create a high-end oriental tea-aesthetic poster for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Use case: {use_case}. Language: {language}.
Topic: "{topic}".
Core character / core word: "{core_character}". Required information: "{required_information}".
Main title: "{main_title}". Subtitle / English auxiliary title: "{subtitle}". Poetic lead: "{poetic_lead}".

Style: premium oriental aesthetic poster, Song dynasty literati mood, Chinese character-as-image structure, "字中有画, 画中有意, 意中有信息", rice paper texture, old paper fibers, pale water stains, faint flower shadows, refined art-book cover, exhibition poster quality, restrained cultural visual identity, elegant editorial information design.

Main visual structure: use the oversized core Chinese character "{core_character}" as the central visual skeleton. The character must be readable at first glance and also act as an image container through masking, illustration underlay, silhouette insertion, or image-inside-strokes. Embed {embedded_content} inside the character, forming a miniature narrative that matches the topic. The relationship between character and image must be natural, not a pasted calligraphy overlay.

Composition: {composition}. Use deliberate negative space, strict information hierarchy, right-side vertical title or nearby title block, upper-left small metadata, bottom small notes, and optional restrained seal mark or title slip. If this is an infographic, include {knowledge_sections} as elegant scroll-like labels, small annotations, or structured editorial blocks.

Typography: refined Chinese Songti / Ming-style serif, slender and bookish; fine English serif for auxiliary text; clean vertical and horizontal mixing; accurate readable text; mature art-publication layout; no crowded text.

Image language: Chinese classical gongbi painting mixed with ink-wash light color and old-painting collage, small but exquisite figures or objects, tea vessels, mountains, courtyard, desk, bamboo, books, mist, lamp shadow, paper-color mineral pigments, subtle bleeding and printed-into-paper texture.

Color and material: {palette}. Low-saturation rice white, tea brown, gray green, pale ink, light ochre, warm gray, quiet wood tones, with at most one tiny restrained accent such as cinnabar seal. Background should be fine rice paper or old book paper with subtle water marks and age traces.

Mood: {mood}. Extra requirements: {extra_requirements}.

Avoid: wrong aspect ratio, generic guofeng template, cheap Chinese style, vulgar red-gold palette, random calligraphy background, overdecorated border, stock tea photo, ecommerce design, web celebrity template, messy information, overbusy illustration, empty fake elegance, unreadable core character, pasted illustration, low-end 3D, neon cyberpunk, robot face, spelling errors, distorted Chinese text.
```

## Quality Bar

The final image must satisfy all of these:

- It reads immediately as a refined oriental cultural poster with tea-aesthetic restraint.
- The core character or word is both legible and visually meaningful.
- The embedded scene is theme-specific, detailed, and naturally integrated into the character.
- The information hierarchy is complete: title, subtitle, metadata, poetic lead, and closure notes when applicable.
- The design feels like a high-end exhibition poster, art-book cover, invitation, infographic, or PPT cover.
- Paper texture, color, typography, and illustration style are unified.
- It avoids cheap guofeng decoration, generic templates, clutter, and unreadable typography.
