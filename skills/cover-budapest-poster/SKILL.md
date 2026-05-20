---
name: cover-budapest-poster
description: Generate Budapest-inspired cinematic editorial cover/poster image prompts or final images with pastel-pop European film-poster aesthetics, symmetrical composition, retro hotel/postcard atmosphere, architectural facades, theatrical color blocking, typography-led layout, visual metaphor, and refined magazine-cover design. Use when the user asks for a Budapest style cover, pastel cinematic poster, retro European editorial cover, symmetrical hotel facade poster, postcard-like concept visual, X cover, product poster, travel-like cover, or high-end colorful vintage-modern poster.
---

# Budapest Poster Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should feel like a refined retro European film poster, boutique hotel postcard, high-end magazine cover, or theatrical editorial concept poster.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. If the user explicitly asks for a prompt, output only the final image prompt.

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `3:4`, `16:9`; treat it as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, product launch, travel-style cover, magazine cover, etc.
- Extra context: optional.
- Mood: warm, light, retro, playful, dreamy, theatrical, romantic, calm, restrained, ironic, elegant, dramatic, etc.
- Forbidden elements: optional.

Default canvas:

- X cover: `5:2`, recommended `2500x1000`.
- Product launch / landscape poster: `16:9`, recommended `1920x1080`.
- WeChat / article cover: `3:2`, recommended `1500x1000`.
- Poster / portfolio cover: `3:4`, recommended `1500x2000`.

## Aspect Ratio Discipline

State the exact ratio and canvas size in the first line of the prompt.

- For `5:2`, write: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cinematic cover, do not crop to 16:9, do not make square`.
- For `16:9`, write: `LANDSCAPE 16:9 CANVAS, 1920x1080, cinematic poster cover, do not make square or vertical`.
- For `3:2`, write: `LANDSCAPE 3:2 CANVAS, 1500x1000, editorial cover format, do not make square`.
- For `3:4`, write: `VERTICAL 3:4 CANVAS, 1500x2000, vintage poster format, do not make square`.
- Fill the entire canvas with deliberate architecture, color, title hierarchy, and scene framing.
- Add negative constraints against `wrong aspect ratio`, `generic 16:9 crop`, `empty accidental margins`, and `centered template poster`.

## Internal Workflow

1. Understand the topic's semantic tension. Do not show this analysis unless asked.
2. Extract the A/B/C title layers.
3. Translate the topic into one theatrical Budapest-style visual setting.
4. Choose one concrete anchor and one architectural/spatial frame.
5. Decide how type, facade, windows, doors, cards, or props interact.
6. Build a prompt with symmetric composition, pastel-pop color, retro print polish, and strong title hierarchy.
7. Add negative constraints against generic travel postcards, cheap templates, overbusy collage, and weak typography.

## Style Definition

Budapest style here means:

- Retro European cinematic poster mood.
- Boutique hotel facade, station hall, street corner, room, corridor, elevator, ticket desk, bathhouse, tram stop, postcard, luggage tag, or archive card atmosphere.
- Symmetric or near-symmetric composition with precise editorial order.
- Pastel-pop but saturated color: dusty pink, coral red, raspberry, burgundy, cream, saffron yellow, mint, teal, sky blue, lavender, chocolate, warm gray.
- Flat but cinematic depth: facade layers, windows, doors, curtains, stairs, signs, props, long shadows, clean cutout-like forms.
- Strong typography integrated into architecture, signage, windows, ticket labels, marquee boards, hotel keys, postcards, or map panels.

Do not copy any specific film still, named character, logo, or exact branded poster. Capture the broader retro European cinematic editorial language.

## Semantic Families And Anchors

Choose one theme family and convert it into a Budapest-style setting:

- Knowledge / method / tutorial / route: hotel directory, concierge desk, route map, train timetable, archive cards, staircase, room-number system, folded guide.
- AI / technology / system / information: retro terminal inside a hotel office, switchboard, card catalog, control panel behind a reception desk, information windows, archive drawers. Avoid robot faces and cyber neon.
- Wealth / finance / trading / risk: ticket counter, exchange booth, locked safe, ledger, receipt desk, elevator threshold, cliff-like staircase, price board, red warning stamp. Avoid coin piles and generic finance icons.
- Growth / learning / cognition: staircase, corridor, room keys, windows opening in a facade, small figure crossing a lobby, light from a door.
- Society / emotion / desire / anxiety / conflict: empty hotel room, long corridor, two windows facing each other, red lobby, shadowed doorway, small figure isolated in a grand facade.
- Brand / city / culture / design / travel: hotel facade, tram, bridge, bathhouse arches, rooftop, river postcard, luggage, room tag, street sign, theatrical storefront.
- Hope / restart / future: door, key, train platform, elevator opening, morning sky, bridge, lighted window, passage through a colored facade.

Use only 1-3 anchors. They must be specific and legible.

## Title Layering

For long topics, never enlarge the whole sentence. Split into:

- A-layer giant visual text: 2-6 Chinese characters or 1-3 English words; first visual focus.
- B-layer full title: preserve the user's complete original title in a medium title, signboard, postcard headline, hotel directory, ticket label, or information bar.
- C-layer system text: subtitle, category, year, issue number, room number, route number, label, account name, short note.

Rules:

- Short title: can become the A-layer giant text directly.
- Medium title: extract the strongest phrase for A-layer.
- Long title: mandatory extraction; full title goes to B-layer.
- Functional words such as `教程`, `指南`, `方法论`, `系统`, `手册`, `观察`, `研究` usually belong in B/C layers unless they are the true focus.
- The A-layer must remain readable and semantically faithful.

## Color System

Use bold pastel-pop, not timid pale colors.

Good palettes:

- Hotel facade: dusty pink + burgundy + cream + teal.
- Retro lobby: coral red + saffron yellow + chocolate + warm white.
- Dreamy travel: sky blue + raspberry + mint + cream.
- Dramatic night: deep plum + warm yellow windows + red accent + black.
- Method / system: teal + cream + black + acid yellow as tiny signal.
- Conflict / risk: burgundy + cream + black + tomato red.

Rules:

- Use 3-5 main colors.
- One dominant background color must carry the poster.
- One accent color must create the visual hook.
- Background must be a scene or architectural color field, not a blank white/gray/beige filler.
- Color should be clean, theatrical, and editorial, not ecommerce bright or neon-tech.

## Composition Systems

Choose one:

- Symmetric hotel facade: giant title becomes the signboard or facade structure; windows/doors hold visual clues.
- Postcard cover: large title, scenic architectural slice, stamp/label metadata, disciplined margins.
- Lobby stage: central object or small figure in a colored interior, title as wall signage.
- Ticket desk / archive: title embedded in timetable, ticket, file drawer, or room-number board.
- Split facade: left/right or top/bottom color architecture, title crosses the division.
- Corridor / threshold: title frames a door, elevator, staircase, or passage.
- Travel-object still life: luggage, key, ticket, card, map, or receipt arranged as a theatrical editorial scene.

Maintain three layers:

1. Giant main title or architectural title sign.
2. One to three visual anchors.
3. Full title, subtitle, issue/room/ticket labels, and small editorial metadata.

## Text-Image Fusion

Make type part of the set:

- Title as hotel sign, facade lettering, room-number board, marquee, ticket headline, map label, or wall typography.
- Image embedded in windows, doors, letter counters, sign panels, or postcard frames.
- Object or figure standing in front of huge type to create scale.
- Type casting shadow onto the scene.
- Windows, stairs, doors, or cards cutting into letterforms.
- Title split across facade levels or architectural bands.

Do not place typography as a generic overlay on top of a background.

## Typography Reconstruction

Use 2-4 methods, not too many:

- Oversized title with clean editorial weight.
- Cropped title touching canvas edges.
- Condensed or extended geometric type.
- Signboard-style title.
- Solid and outlined type mix.
- Type split into architectural bands.
- Letter counters used as windows, doors, or frames.
- Repeated small room numbers, issue labels, or ticket codes as a system.

Readability is mandatory. The main word must be understood at first glance.

## Prompt Template

Adapt this template:

```text
Create a Budapest-inspired cinematic editorial cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}.
Main visual title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / C-layer system text: "{subtitle_or_notes}".

Style: retro European cinematic poster, boutique hotel postcard aesthetic, pastel-pop editorial cover, symmetric modern magazine layout, theatrical architectural facade, typography-led concept poster, refined color-block composition, subtle print texture, high-end visual art direction.

Visual metaphor: {selected_metaphor}. Budapest-style setting: {setting}. Use 1-3 precise image anchors: {anchors}. Text-image relationship: {fusion_method}. Compose as {composition}. Typography must be part of the architecture, signboard, window system, ticket, postcard, or room-number layout rather than a generic overlay.

Typography: giant readable title as the visual skeleton, refined modern display type, signboard or facade lettering, strong hierarchy, full original title preserved in a smaller editorial title system, crisp Chinese/English mixing, no spelling errors. Use 2-4 type reconstruction methods: {type_reconstruction_methods}.

Color and background: {palette_and_background}. Bold pastel-pop palette, clean theatrical contrast, dominant background color, strong accent color, architectural or scenic background with mood and story. Not plain white, beige, or gray filler.

Mood: {mood}. Extra context: {context}.

Avoid: wrong aspect ratio, generic travel postcard, empty background, default white/beige/gray background, weak dull color, ecommerce cover, ordinary ad page, PPT cover, cheap neon tech, robot face, overbusy collage, low-end 3D, unreadable title, long title enlarged as one block, disconnected image and text, exact film still replication, named character likeness, official logo imitation.
```

## Quality Bar

The final image must satisfy all of these:

- It reads immediately as retro European cinematic / Budapest-style editorial design.
- The viewer is caught by color, architecture, and typography.
- The background is an intentional setting, facade, interior, postcard, or object scene.
- Typography is integrated into the scene rather than pasted on top.
- The complete title remains understandable through B-layer text.
- The visual metaphor is accurate and concrete.
- The image is refined, charming, theatrical, and high-end, not a generic travel poster.
- The requested aspect ratio is respected.
