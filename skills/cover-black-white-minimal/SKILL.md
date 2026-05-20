---
name: cover-black-white-minimal
description: Generate black-and-white minimalist conceptual cover/poster image prompts or final images with portfolio-cover aesthetics, typography-led modern editorial design, deep visual metaphor, strong title extraction, strict grid composition, negative space, subtle print texture, and restrained monochrome art direction. Use when the user asks for a black-white minimal cover, monochrome typography poster, portfolio cover, modernist editorial poster, conceptual title-led cover, X cover, WeChat cover, poster, or high-end visual cover with restrained design.
---

# Black White Minimal Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should look like a high-end portfolio cover, modern editorial poster, Swiss-inspired typography work, or gallery-grade conceptual cover.

If generating the image directly, keep all semantic analysis internal and output only the generated image result. If the user explicitly asks for a prompt, output only the final image prompt.

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `4:5`, `1:1`; treat it as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, WeChat cover, portfolio cover, marketplace cover, etc.
- Extra context: optional.
- Mood: rational, cold, avant-garde, ordered, oppressive, lonely, hopeful, future, restrained, etc.
- Forbidden elements: optional.

Default canvas:

- X cover: `5:2`, recommended `2500x1000`.
- Marketplace cover: `1:1` (`1600x1600`) unless the user specifies another ratio.
- WeChat cover: `3:2`, recommended `1500x1000`.
- Poster / portfolio cover: `4:5` (`1600x2000`) or `1:1` (`1600x1600`).

## Aspect Ratio Discipline

State the exact ratio and canvas size in the first line of the prompt.

- For `5:2`, write: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cover, do not crop to 16:9, do not make square`.
- For `1:1`, write: `SQUARE 1:1 CANVAS, 1600x1600, full square composition, do not make wide banner, do not make vertical poster`.
- For `4:5`, write: `VERTICAL 4:5 CANVAS, 1600x2000, portfolio cover format, do not make square`.
- Design for the full canvas, with deliberate negative space and edge relationships.
- Add negative constraints against `wrong aspect ratio`, `generic 16:9 frame`, `empty accidental margins`, and `template crop`.

## Internal Workflow

1. Understand the real semantic tension of the topic. Do not show this analysis unless asked.
2. Choose one concrete visual anchor that can be composed, not an abstract decoration.
3. Split long titles into A/B/C text layers.
4. Decide the text-image structural relationship.
5. Build a monochrome, typography-led prompt with strict layout hierarchy.
6. Add negative constraints against commercial templates, cheap tech style, and overdecorated design.

## Semantic Families And Visual Anchors

Choose the strongest family, then select 1-3 concrete anchors:

- Knowledge / method / tutorial / path: path lines, maps, folders, cards, manuals, index systems, stairs, navigation marks, micro-person facing a large system.
- Technology / system / order / information: terminal, screen, panel, interface grid, signal path, data filter, file cabinet, machine frame, information channels.
- Wealth / finance / trading / risk: cracked chart, volatility curve, leverage structure, trading terminal, card, chip, threshold, passage, cliff/path contrast, financial city terrain. Avoid coin piles and cheap crypto icons.
- Growth / learning / cognition / upgrade: stairs, light slit, layered strata, window, ladder, archive progression, small figure crossing a structure.
- Society / philosophy / emotion / conflict: crack, shadow, wall, empty space, distant figure, occlusion, confrontation, structural pressure.
- City / brand / design / portfolio: architecture, grid, exhibition label, layout frame, skyline, spatial slicing, geometric order.
- Restart / hope / future: door, portal, key, horizon line, bridge, corridor, light beam, subtle opening in black space.

The anchor must interact with typography. Avoid floating decorative images.

## Title Layering

For long topics, never enlarge the whole sentence. Split into:

- A-layer giant visual text: 2-6 Chinese characters or 1-3 English words; first visual focus.
- B-layer full title: preserve the original topic in a medium title, small headline, or information bar.
- C-layer system text: subtitle, short note, category, year, ID, keywords, author/account, series name.

Extraction rules:

- Short title: the full topic can become the giant text.
- Medium title: extract the most visually and semantically powerful phrase for A-layer.
- Long title: mandatory extraction; the full title must move to B-layer.
- Functional words such as `教程`, `指南`, `方法论`, `入门`, `路线`, `实战`, `分享`, `系统`, `手册`, `观察`, `研究` usually belong in B/C layers unless they are the true conceptual focus.
- Never distort, misspell, or over-abbreviate the user's topic.

## Visual Style

The image should combine:

- Modern editorial poster, typography-led conceptual poster, high-end portfolio cover.
- Swiss-inspired grid layout, black-and-white minimal graphic design, monochrome conceptual design.
- Clean negative space, oversized hero typography, sharp composition, restrained visual metaphor.
- Subtle paper grain, slight print texture, grayscale gradient, soft shadow, mild emboss or ink impression.
- Black, white, and gray as the base. A single tiny accent color is allowed only for semantic emphasis.

Avoid commercial illustration, ecommerce cover language, decorative collage, cheap cyber neon, noisy effects, and overdone 3D.

## Composition Systems

Choose one:

- Giant type as architecture: text becomes a wall, building, port facade, file cabinet, or structural object.
- Micro-figure scale contrast: tiny person stands before enormous type or crosses its shadow.
- Interface/grid system: title aligns with terminal panels, cards, maps, or data channels.
- Crack/light structure: a slit, fracture, or beam cuts through the typography.
- Spatial threshold: door, bridge, corridor, container, key, or window embedded in the title.
- Portfolio grid: strict margins, one dominant title block, one visual anchor, small metadata system.

Maintain three layers:

1. Giant main text as the visual skeleton.
2. One to three restrained metaphor anchors.
3. Full title, subtitle, category, year, ID, and small typographic system.

Negative space must be intentional: it should create pressure, silence, scale, or clarity.

## Text-Image Fusion

Choose a structural relationship:

- Image embedded inside the letterforms.
- Image emerging from the text.
- Image passing through the type.
- Image attached to the type edge.
- Type becomes ground, shadow, wall, container, screen, archive cabinet, port facade, or inner space.
- Small figure or object changes the scale of the giant type.
- Image cuts, supports, erodes, occludes, or reconstructs the text.

The image must complete a visual sentence with the words.

## Prompt Template

Adapt this template:

```text
Create a high-end black-and-white minimalist conceptual cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}.
Main visual title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / C-layer system text: "{subtitle_or_notes}".

Style: black and white minimalist portfolio cover, typography-led modern editorial poster, Swiss-inspired grid layout, monochrome conceptual graphic design, clean negative space, oversized hero typography, restrained visual metaphor, subtle paper grain, slight print texture, sharp composition, gallery poster aesthetic.

Visual metaphor: {selected_metaphor}. Use 1-3 precise image anchors: {anchors}. Text-image relationship: {fusion_method}. Compose as {composition}. The image anchor must grow from, enter, support, cut, shadow, or inhabit the typography rather than floating separately.

Typography: giant readable modern sans-serif title, geometric black type, strong hierarchy, full original title preserved in a smaller editorial title system, minimal category/year/ID labels, precise grid alignment, no spelling errors. The title can be cropped, embedded, shadowed, or structurally interrupted, but must remain readable.

Color: black, white, and gray only, with optional tiny accent color only if semantically necessary. Restrained, rational, crisp, high-end, not decorative.

Mood: {mood}. Extra context: {context}.

Avoid: wrong aspect ratio, generic template crop, long title enlarged as one block, image unrelated to text, floating decoration, ecommerce cover, commercial ad layout, infographic template, cheap blue-purple neon, robot face, low-grade collage, overdone 3D, busy background, large explanatory paragraphs, fancy border, typo, unreadable title, mechanical repeated layout.
```

## Quality Bar

The final image must satisfy all of these:

- The core visual word is immediately visible.
- The complete title remains understandable through B-layer text.
- The image and typography form one integrated concept.
- The design is black-white minimal, modern editorial, and portfolio-cover grade.
- The negative space feels deliberate, not empty.
- Long titles show real design extraction, not mechanical text dumping.
- The requested aspect ratio is respected.
