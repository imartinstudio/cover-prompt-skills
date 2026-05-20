---
name: cover-trendy-color-poster
description: Generate trendy high-impact color poster/cover image prompts or final images with bold contrast palettes, typography-led composition, visual metaphor, oversized reconstructed type, contextual backgrounds, magazine-cover energy, and modern editorial art direction. Use when the user asks for a trendy poster, colorful concept cover, bold magazine cover, type-led promotional poster, X cover, product launch cover, event poster, or high-saturation editorial visual with strong graphic impact.
---

# Trendy Color Poster Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should feel like a high-end trendy magazine cover, modern type poster, bold editorial campaign visual, or concept poster with strong color memory.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. If the user explicitly asks for a prompt, output only the final image prompt.

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `3:4`, `16:9`; treat it as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, product launch, marketplace cover, etc.
- Extra context: optional.
- Mood: hot, light, retro, bouncy, playful, restrained, avant-garde, dreamy, dramatic, calm, strong, loud, high-pressure, etc.
- Forbidden elements: optional.

Default canvas:

- X cover: `5:2`, recommended `2500x1000`.
- Product launch / landscape poster: `16:9`, recommended `1920x1080`.
- WeChat / article cover: `3:2`, recommended `1500x1000`.
- Poster: `3:4`, recommended `1500x2000`.
- Marketplace cover: use the user's requested ratio; if omitted, use `1:1` only if the platform requires it, otherwise ask or infer from platform norms.

## Aspect Ratio Discipline

State the exact ratio and canvas size in the first line of the prompt.

- For `5:2`, write: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cover, do not crop to 16:9, do not make square`.
- For `16:9`, write: `LANDSCAPE 16:9 CANVAS, 1920x1080, cinematic poster cover, do not make square or vertical`.
- For `3:2`, write: `LANDSCAPE 3:2 CANVAS, 1500x1000, editorial cover format, do not make square`.
- For `3:4`, write: `VERTICAL 3:4 CANVAS, 1500x2000, poster format, do not make square`.
- Fill the whole canvas with intentional color, typography, and background relationships.
- Add negative constraints against `wrong aspect ratio`, `template crop`, `empty accidental margins`, and `generic centered poster`.

## Internal Workflow

1. Understand the topic's real semantic tension. Do not show this analysis unless asked.
2. Extract the A/B/C title layers.
3. Choose a color system and contextual background based on theme and mood.
4. Select 1-3 concrete visual anchors.
5. Decide how image and type structurally interact.
6. Build a bold, color-forward prompt with strong typography reconstruction.
7. Add negative constraints against flat templates, weak color, unreadable type, and disconnected imagery.

## Semantic Families And Visual Anchors

Choose the strongest theme family, then pick 1-3 precise anchors:

- Knowledge / method / tutorial / route / prompt: paths, maps, index cards, interface panels, terminals, screens, arrows, notebooks, route signs.
- AI / tech / system / information / decision: screen, terminal, dashboard, signal path, data channels, panel grid, decision switch, structured interface. Avoid robot faces and cheap blue-purple cyber neon.
- Wealth / finance / risk / trading: volatility curve, card, receipt, chip, trading panel, threshold, cliff/path contrast, lever, city financial facade. Avoid coin piles and low-end crypto icons.
- Growth / learning / cognition / upgrade: stairs, hill, bridge, road, window, light passage, small figure facing large type.
- Society / emotion / desire / anxiety / expression: wall, room, shadow, doorway, conflict scene, phone, chair, spotlight, crowded fragment.
- Brand / city / culture / design / travel: building facade, street scene, doorway, window, corridor, small house, hill, seaside, pier, island, car, boat, phone, lighthouse, city color wall.
- Philosophy / conflict / pressure / hope / restart: crack, gate, key, tunnel, bridge, portal, strong shadow, horizon line.

The anchor must be concrete and composable, not a vague symbol.

## Title Layering

For long topics, never enlarge the whole sentence. Split into:

- A-layer giant visual text: 2-6 Chinese characters or 1-3 English words; first visual focus.
- B-layer full title: preserve the user's complete original title in a medium title, subtitle, column title, or information bar.
- C-layer system text: subtitle, category label, year, issue number, keywords, account name, series name, short notes.

Rules:

- Short title: can become the A-layer giant text directly.
- Medium title: extract the strongest word/phrase for A-layer.
- Long title: mandatory design extraction; full title goes to B-layer.
- The A-layer must optimize for recognition, semantic density, layout stability, metaphor potential, and memory.
- Never distort, misspell, or over-abbreviate the topic.

## Color And Background System

Color must be active, memorable, and theme-specific. Do not default to white, beige, pale gray, or safe light backgrounds.

Use 2-5 dominant colors:

- One absolute main color.
- One conflict/accent color.
- Optional secondary color blocks.
- Optional tiny bright "pin color" for emphasis.

Background must be a designed situation, not blank filler. Choose one:

- High-saturation solid color field.
- Large contrast color blocks.
- Retro cinematic sky color.
- Pink-orange sunset gradient.
- Retro green / blue / red / yellow wall scene.
- Strong warm-cool conflict field.
- Building facade background.
- Landscape slice or travel-poster scene.
- Candy-color city background.
- Emotional room or space.
- Dramatic dark or neon-color field, but not cheap cyberpunk.

Theme palettes:

- Light / playful / lifestyle / travel: coral red, tomato red, lemon yellow, lake blue, sky blue, mint green, pink, cream white, bright orange.
- Rational / AI / system / method: electric blue, royal blue, cold white, black, acid yellow, tiny fluorescent green, high-contrast gray-blue, structural color blocks.
- Pressure / conflict / philosophy / social observation: deep red, black-red, burnt orange, cold gray, dark blue, sharp white, high-pressure black or dark field.
- Retro / cinematic / lifestyle / magazine: cream pink, vintage yellow, sage green, lake blue, orange-red, dusty pink, cream white, saturated candy blocks.

Avoid dull, gray, average, conservative, or muddy colors.

## Visual Impact Rules

Use at least 4-6 impact devices:

- Oversized title filling the frame.
- Extreme crop of large type.
- High-saturation background.
- Large contrast color blocks.
- Strong image/type occlusion.
- Strong foreground/background depth.
- Extreme close-up framing.
- Asymmetric composition.
- Diagonal or horizontal rushing type rhythm.
- Condensed vertical type or extended horizontal type.
- Type crossing the canvas edge.
- Image touching or pressing against edges.
- Dramatic scale contrast.
- Strong main type + strong background + one small precise image anchor.

The image must be both high-end and memorable.

## Typography Reconstruction

Typography is the main visual structure. Use 3-5 reconstruction methods:

- Aggressively oversized type.
- Cropped letters with only partial forms visible.
- Offset word blocks.
- Horizontally stretched or vertically compressed letterforms.
- Image embedded inside type.
- Type edges occluded by image.
- Word split into two or three blocks.
- Structural gaps between letters.
- Part of a letter replaced by an image element.
- Solid type mixed with outlined/hollow type.
- Repeated type layers for rhythm.
- Type as wall, facade, frame, passage, or structure.
- Image inserted between strokes.
- Limited rotation, inversion, or interlock while preserving readability.

The A-layer title must remain readable at first glance. Reconstruction must serve the theme, not show off.

## Composition Systems

Choose one:

- Giant text covers most of the frame, image embedded in the lower/middle zone.
- Large color-block background + oversized type + one core image.
- Text presses over the edge of a scene image.
- Background split into contrast zones, type crosses zones.
- Type as building facade, image becomes a window/door/interior space.
- Left/right split color composition.
- Top/bottom cut color composition.
- Image slightly below center, title pressing from top or bottom.

Maintain three layers:

1. Giant main visual text.
2. One to three metaphor image anchors.
3. Full title, subtitle, tags, issue number, and small editorial system.

Negative space is allowed only when it increases tension, clarity, or scale.

## Text-Image Fusion

Choose a structural relationship:

- Image embedded inside text.
- Image revealed behind giant type.
- Image pressed under type.
- Image appears from gaps in letterforms.
- Image becomes type's base, ground, shadow, window, or inner space.
- Giant type acts like a wall, building, facade, or structural device.
- Small figure stands before huge type for scale contrast.
- Image cuts, penetrates, supports, occludes, or erodes the text.

Do not let the image float independently as decoration.

## Prompt Template

Adapt this template:

```text
Create a trendy high-impact color editorial poster cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}.
Main visual title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / C-layer system text: "{subtitle_or_notes}".

Style: trendy editorial poster, color-block typography poster, bold magazine cover aesthetic, retro-modern poster, conceptual type-led design, vibrant contrast color system, high-impact graphic poster, image and typography fusion, strong modern editorial art direction.

Visual metaphor: {selected_metaphor}. Use 1-3 concrete image anchors: {anchors}. Text-image relationship: {fusion_method}. Compose as {composition}. The image must be structurally integrated with the typography, not placed as a separate background.

Typography: huge readable title as the visual skeleton, aggressive scale, cropped and reconstructed letterforms, strong hierarchy, full original title preserved in smaller editorial title system, crisp Chinese/English mixing, no spelling errors. Use 3-5 type reconstruction methods: {type_reconstruction_methods}.

Color and background: {palette_and_background}. Strong saturation, clear dominant color, clear conflict/accent color, contextual background with mood and scene, not default white/beige/gray. Use bold color blocks or dramatic color field to create immediate visual memory.

Impact devices: {impact_devices}. The first impression must be color + text + structure.

Mood: {mood}. Extra context: {context}.

Avoid: wrong aspect ratio, default white/beige/gray background, weak dull color, average safe palette, long title enlarged as one block, only big text with no visual metaphor, only color with no structure, disconnected image and text, too many small words, conservative flat design, cheap internet-trend look, cheap cyber neon, ordinary ad page, PPT cover, overfilled elements, low-end 3D, unreadable title, blank filler background, mechanical repeated template.
```

## Quality Bar

The final image must satisfy all of these:

- The viewer is caught immediately by color and type.
- The background has context, mood, and design judgment; it is not a safe blank backdrop.
- Typography has strong structure and reconstruction while staying readable.
- Image and type are deeply fused, not stacked.
- Color is bold, bright, clean, and contrast-driven.
- The result feels like a high-end magazine cover, trendy editorial poster, or type concept poster.
- It has both portfolio-grade design taste and feed-stopping impact.
- Different themes produce different backgrounds, palettes, and compositions rather than one repeated template.
- The requested aspect ratio is respected.
