---
name: cover-anthropic-research
description: Use when a user asks for an Anthropic Research, research-editorial, AI lab report, quiet serif minimal, solid-color abstract-line-art, or low-saturation premium cover.
---

# Anthropic Research Editorial Cover

Create one restrained research-editorial cover prompt or one final cover image. Treat “Anthropic Research” as a visual shorthand for a research report, design manual, or AI laboratory archive; do not imply official Anthropic affiliation and do not use Anthropic logos or protected brand marks.

## Output Contract

Read `--out-type` as a control parameter:

- `template`: output only the invocation template below.
- `prompt`: output only one complete image prompt.
- `all`: output the template, then the complete image prompt.
- Omitted: default to `template`.
- `模板`, `模版`, `调用格式` map to `template`; `提示词`, `prompt`, `完整提示词`, `生成提示词` map to `prompt`; `模板和提示词`, `两个都要`, `all` map to `all`.
- `直接生成`, `出图`, `生成封面图` means generate exactly one final image when an image tool is available.

For `template`, output exactly:

```text
使用 $cover-anthropic-research 生成一张封面
主题词：{topic}
主标题：{title}
副标题：{subtitle_or_blank}
核心表达：{one_sentence_thesis}
画幅比例：{ratio}
用途：{use_case}
背景方案：{palette_choice}
视觉隐喻：{abstract_metaphor}
字体：{title_and_supporting_type}
禁用元素：{forbidden_elements}
```

Do not output internal analysis, multiple drafts, or an unrelated generic prompt.

## Required Inputs and Ratio Rules

Extract or infer the topic, main title, optional subtitle, one-sentence thesis, use case, language, palette choice, abstract metaphor, and forbidden elements. Keep one readable main title; leave the subtitle blank when it adds no real information.

When the user specifies a ratio, treat it as hard. Otherwise use:

| Use case | Ratio | Canvas hint |
| --- | --- | --- |
| X / LinkedIn header or article header | `5:2` | `2500x1000`, wide editorial cover |
| X post, tutorial, product introduction | `16:9` | `1920x1080`, landscape cover |
| Report title page or poster | `4:5` | `1600x2000`, vertical editorial page |
| Article or knowledge portrait | `3:4` | `1500x2000`, vertical editorial cover |
| Short-video cover | `9:16` | `1080x1920`, vertical cover |

State the ratio and canvas size in the first line of a prompt. Do not silently crop a requested ratio or make a wide cover square.

## Visual System

### Fixed background palette

Choose one scheme deliberately; never randomize the background or mix schemes without a stated reason:

| Scheme | Background | Primary text | Feeling |
| --- | --- | --- | --- |
| Terracotta | `#D97757` | `#1A1A1A` | warm, creative, experimental |
| Deep black | `#1A1A1A` | `#EFEAE0` | technical research, premium, serious |
| Warm gray | `#D8D5CF` | `#1A1A1A` | report, manual, archival |
| Sage green | `#B8C9B8` | `#1A1A1A` | knowledge, education, long-term thinking |
| Haze blue | `#8FA9C7` | `#1A1A1A` | calm systems thinking, reflection |

Keep the background as a large, mostly flat color field. Use low-saturation supporting colors only: paper `#EFEAE0`, muted terracotta `#CD6F47`, sage `#6B8A6F`, haze blue `#8FA9C7`, and charcoal `#1A1A1A`. Avoid gradients, glow, metallic effects, and loud texture.

### Composition

Use a calm editorial layout with generous negative space. On wide covers, place the main title in a strong left or central text block and one abstract visual field on the opposite side. On vertical covers, preserve the same hierarchy with one title block and one visual metaphor rather than adding more panels.

- The main title is the absolute visual center; keep it to one title only.
- A subtitle is optional and subordinate. Do not add a label row, page number, date, logo, brand signature, or filler English text.
- Use clear margins and a stable reading path. Leave quiet space around the title and linework.
- Add only 2–4 irregular accent shapes, together no more than 5% of the canvas.

### Typography

Use an elegant serif for the main title: Source Han Serif or Georgia, with a New York Times Magazine-like editorial character and visible thick-thin contrast. Use a clean sans serif such as Inter for a short subtitle or supporting line. Use JetBrains Mono or another monospace face only for a small technical token when it has semantic value.

### Abstract visual metaphor

Translate the topic into a conceptual structure instead of drawing the literal object. Use black hand-drawn linework, a restrained off-white paper form, and one simple relationship such as a human profile with thought paths, a modular system becoming architecture, or information nodes converging into a structure. Keep the linework sparse, legible, and slightly irregular; it should feel observed and designed, not like a generic icon set.

## Prompt Construction

1. Lock the requested ratio and canvas size.
2. Select one fixed background scheme that supports the topic.
3. Reduce the topic to one thesis and one abstract metaphor.
4. Compose one title block, one visual metaphor, and 2-4 small irregular shapes.
5. Specify serif-led typography and the exact text language.
6. Add the negative constraints below, then output one prompt only.

Use this prompt shape for `--out-type prompt`:

```text
{ratio_instruction}
Create one premium research-editorial cover for “{topic}”. Main title: “{title}”. Optional subtitle: “{subtitle}”. Use case: {use_case}. Language: {language}.

Visual direction: quiet, rational, restrained, intelligent, archival, and high-end; like an AI research report, design research manual, or thoughtful laboratory publication. Use {palette_choice} as a mostly flat solid-color background with generous negative space and strong visual stability.

Composition: one readable main title as the visual center, {title_position}; one abstract conceptual line-art metaphor for {abstract_metaphor}; 2-4 irregular organic or paper-like accent shapes occupying no more than 5% of the canvas. Keep the visual path simple and the empty space intentional.

Typography: {title_font}, with pronounced serif contrast and a bookish editorial character; supporting text in a clean sans serif; monospace only when semantically necessary. Render the supplied title accurately in {language}; do not invent extra copy.

Linework and color: sparse charcoal hand-drawn lines, restrained off-white paper form, low-saturation accents, no more than one emphasis color beyond the selected background system. Do not depict the topic literally; express its structure or idea through metaphor.

Avoid marketing-poster energy, launch-event graphics, cyberpunk, neon, blue glow, gradients, glossy 3D, photorealism, stock illustration, complex infographic panels, dense paragraphs, UI buttons, repeated cards, decorative labels, page numbers, dates, logos, brand signatures, meaningless English, unreadable text, multiple title blocks, and wrong aspect ratio.
```

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Turning the style into a corporate or product launch banner | Reduce elements to one title, one metaphor, and a flat color field. |
| Drawing a literal robot, book, laptop, or dashboard | Replace the object with an abstract structure or relationship. |
| Adding many labels to make the cover feel “designed” | Remove labels; the title and metaphor carry the cover. |
| Using random colors or saturated gradients | Select one palette row and preserve its text contrast. |
| Treating “minimal” as an empty blank canvas | Keep one meaningful line-art metaphor and a small, deliberate accent system. |
| Reproducing an official logo or implying affiliation | Use the style name only as a visual reference; create an original composition. |

The original prompt is preserved in [docs/source-prompts/cover-anthropic-research.md](../../../../docs/source-prompts/cover-anthropic-research.md).
