---
name: cover-editorial-collage
description: Generate high-end editorial collage cover/poster image prompts or final images with torn-paper collage, visual magazine layout, retro print grain, mixed media, bold typography, visual metaphor, and balanced handmade disorder. Use when the user asks for a cover, X cover, poster, WeChat public account cover, knowledge card, event poster, magazine-style visual, collage poster, torn-paper artwork, or wants to turn a topic/title into a strong conceptual cover image.
---

# Editorial Collage Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The output should feel like an independent magazine cover, street poster, youth culture zine, retro film poster, or art exhibition poster.

If generating the image directly, keep all theme analysis internal and output only the generated image result. If the user sets `--out-type prompt`, output only the final image prompt. If the user sets `--out-type template` or omits `--out-type`, output only the template described in "Template Output" and do not output a generic image prompt.

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
使用 $cover-editorial-collage 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
情绪倾向：{mood}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer these fields from the user request:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `4:5`, `1:1`, `3:4`; infer from use case if omitted. Treat the requested aspect ratio as a hard layout constraint, not a style hint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, WeChat cover, knowledge card, event poster, etc.
- Extra context: optional.
- Mood: optional; examples include warm, rebellious, retro, youthful, satirical, street, psychedelic, growing, conflict.
- Forbidden elements: optional.

Default ratios:

- X cover: `5:2`, recommended working canvas `2500x1000`.
- Xianyu / marketplace cover: `5:2`, recommended working canvas `2500x1000`.
- WeChat public account cover: `3:2`, recommended working canvas `1500x1000`.
- Poster / event poster: `4:5` (`1600x2000`) or `3:4` (`1500x2000`).
- Knowledge card: `1:1` (`1600x1600`) or `4:5` (`1600x2000`).

## Aspect Ratio Discipline

Image models often drift toward common square or 16:9 outputs. Prevent this by making the ratio explicit, early, and repeated:

- Put the exact ratio and canvas size in the first line of the prompt.
- For `5:2`, write: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide banner, do not crop to 16:9, do not make square`.
- Design for the full canvas, not a centered poster placed inside a wider frame.
- Keep important text inside the central safe area, but fill the left and right edges with intentional collage material.
- Do not use words like `poster` alone for `5:2` outputs; pair it with `wide horizontal cover banner`.
- Add negative constraints against `square composition`, `vertical poster`, `16:9 frame`, `centered poster with empty side margins`, and `wrong aspect ratio`.

## Internal Workflow

1. Understand the topic and choose a visual metaphor. Do not show this analysis unless the user asks.
2. Split long titles into three text layers.
3. Pick one composition system and one color strategy.
4. Build a concise but complete image-generation prompt.
5. Enforce readability, texture, material layering, and visual hierarchy.
6. Add negative constraints to avoid common failures.

## Theme Metaphors

Choose visual anchors from the closest theme family:

- AI / knowledge / writing / methods: manuscripts, computer screens, sticky notes, search box, index cards, typewriter, folders, eyes, magnifier, brain texture, prompt slips, editorial marks, clipped sentences. Avoid robot faces and cheap blue-purple neon.
- Growth / self / cognition / flow: plants, stairs, old photos, back view of a person, diary fragments, mirror, window, light beams, torn paper layers revealing an image.
- Women / community / being seen: female illustration, gauze, eyes, flowers, group photo fragments, hands, curtains, soft fabric, stickers, handwriting, warm daily-life scenes.
- Web3 / finance / trading / risk: charts, torn graphs, receipts, chips, trading UI fragments, red/blue signals, warning labels, city fragments, financial newspaper, risk marks.
- Social phenomenon / conflict / satire: old newspapers, portraits, red warning notes, torn slogans, question marks, black-and-white photos, judgment labels, damaged edges.
- City / travel / culture: architecture, maps, tickets, postcards, road signs, vintage photos, landmarks, handwritten place names, postmarks, travel stickers.
- Visual beats plain text / attention: giant eye, magnifier, torn text layers, image fragments bursting through text, picture-over-text contrast.
- "Can rewrite, but do not be brainwashed": split "洗脑", brain texture paper, washed-out words, warning annotations, torn opinion slips.
- HerName / female AI community: female illustration, gauze, eyes, flowers, life scenes, group images, warm paper scraps, handwritten stickers; keywords: seen, needed, witnessed, female creativity, naming oneself in the AI era.
- Tutorial / methodology: manuals, step cards, path diagrams, tool screenshot cutouts, arrows, numbered stickers, index cards; keep it editorial, not a flat infographic.

## Title Layering

For long topics, never enlarge the entire sentence. Split into:

- A-layer giant visual title: 2-6 Chinese characters or 1-3 English words. This is the first visual focus.
- B-layer full title: preserve the original topic in a medium-size title, paper strip, newspaper headline, label, or poster information bar.
- C-layer microcopy: subtitle, keywords, issue number, date, column name, English notes, handwritten annotations, sticker text.

Rules:

- Main title must be bold, readable, and visually dominant.
- Full title must preserve the original meaning.
- Microcopy must look like a real magazine system, not random explanation.
- Use mixed Chinese-English naturally when it improves editorial tension.
- Do not introduce typos, fake brand spellings, or unreadable title distortion.

## Visual Style

The image should combine:

- Torn-paper collage, analog handmade magazine layout, punk zine energy, vintage print texture, mixed-media poster design.
- Ripped irregular paper edges; avoid clean rectangular paper for every element.
- Old newspapers, magazine photos, handwritten notes, printed labels, receipts, tape, stickers, photocopy paper, color paper, photo scraps, doodle lines.
- Paper grain, uneven ink, halftone dots, slight registration offset, scan marks, folds, stains, risograph or offset texture.
- Strong contrast colors with a refined editorial balance.

Good palette directions:

- Red / black / white for satire, conflict, opinions, risk, warning, reflection.
- Orange / yellow / blue for growth, knowledge, tutorials, lifestyle, city, travel.
- Pink / yellow / blue for women, AI life, creativity, growth, youthful energy.
- Black / white / gray plus one saturated accent for serious essays, social observation, X long-form covers.
- Vintage beige paper plus bright stickers for manuals, methods, guides, knowledge cards.

Avoid all-low-saturation grayness. Use at least one memorable high-impact color.

## Composition Systems

Choose one:

- Central explosion collage: giant title centered, paper scraps radiating outward.
- Magazine cover collage: big title, main image, structured information bars.
- Horizontal tear band: one ripped paper band cuts across the frame.
- Profile/archive collage: one person or object in the center, surrounded by labels and annotations.
- Street poster wall: layered pasted posters, rips, overprints, exposed older layers.
- Ticket/manual scrapbook: opened manual, file folder, receipt book, or scrapbook.
- Retro event poster: strong title, date/numbering, image fragments, offset print texture.

Maintain four layers:

1. Giant main title as the visual skeleton.
2. One to three theme image anchors.
3. Paper strips, tape, labels, numbering, dates, English microcopy, handwriting, arrows, stamp marks.
4. Textured paper or photocopy background, not plain blank space.

## Text-Image Fusion

Make image and type interact:

- Text can be split by torn paper.
- Images can emerge from behind letters.
- Figures or objects may cover part of the title, but never enough to harm readability.
- Main title can be printed on a torn band.
- Microcopy can sit like handwritten margin notes around the image.
- Images can look like newspaper silhouettes or magazine cutouts.
- Titles can be photocopied, offset, repeated, stamped, or slightly misregistered.
- Use tape, clips, stickers, and layered paper to create physical depth.

## Prompt Template

When generating, adapt this template:

```text
Create a high-end editorial collage cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}.
Main visual title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / microcopy C-layer: "{subtitle_or_notes}".

Style: torn paper collage, handmade magazine cover layout, punk zine aesthetic, vintage print texture, mixed media poster, ripped irregular paper edges, bold readable typography, retro offset printing, risograph grain, photocopy grain, halftone dots, scanned magazine cutouts, analog collage, street poster design.

Visual metaphor: {selected_metaphor}. Use 1-3 strong image anchors: {anchors}. Compose as {composition}. Background: textured paper / old newspaper / photocopy surface with folds, stains, scan marks, and layered paper fibers.

Typography: giant bold readable title, strong editorial hierarchy, Chinese/English magazine microcopy, issue number, date, field report labels, handwritten annotations, stickers. The main title may be torn, offset, overprinted, partially covered, or cut by paper layers, but it must remain legible and correctly spelled.

Color: {palette}. Strong contrast, one memorable saturated accent, refined magazine art direction, not cheap commercial poster colors.

Mood: {mood}. Extra context: {context}.

Avoid: wrong aspect ratio, square composition, vertical poster, 16:9 frame, centered poster with empty side margins, clutter without focus, unreadable title, fake typos, cheap ecommerce template, PPT layout, robot face, cheap cyber neon, unrelated door scenes, clean rectangles only, all-gray low contrast, excessive explanatory text, low-grade dirty punk chaos, flat infographic.
```

## Quality Bar

The final image must satisfy all of these:

- The core title is visible at first glance.
- The delivered image respects the requested aspect ratio; for `5:2`, it must be a true extra-wide horizontal banner, not a 16:9 or square poster.
- The image strongly reads as torn-paper collage and visual magazine design.
- Typography, image anchors, paper scraps, and labels form a story rather than competing randomly.
- The handmade disorder is deliberate and balanced.
- The theme metaphor is accurate and emotionally legible.
- Paper grain, print texture, halftone, scan marks, or offset ink texture are visible.
- The color has enough impact to stop a feed scroll.
- The result looks like an independent magazine cover, street art poster, or refined visual collage artwork.
