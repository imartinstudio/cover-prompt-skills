---
name: cover-budapest-poster
description: Generate Budapest-inspired retro Central European cinematic poster/cover image prompts or final images with architectural storytelling, postcard/archive ephemera, theatre/tram/bathhouse/station settings, symmetrical spatial composition, refined pastel color, and film-poster narrative atmosphere. Use when the user asks for a Budapest style cover, retro European cinematic poster, Central European editorial poster, postcard-like concept visual, travel-like cover, theatre poster, archive-ticket visual, or elegant vintage-modern cultural poster.
---

# Budapest Poster Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result should feel like a refined retro Central European film poster, cinematic city postcard, archive-ticket visual, theatre placard, or atmospheric cultural poster.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. If the user explicitly asks for a prompt, output only the final image prompt.

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `3:4`, `16:9`; treat it as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, cultural event poster, travel-style cover, editorial cover, etc.
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
- Fill the entire canvas with deliberate spatial storytelling, period color, title hierarchy, and cinematic scene framing.
- Add negative constraints against `wrong aspect ratio`, `generic 16:9 crop`, `empty accidental margins`, and `centered template poster`.

## Internal Workflow

1. Understand the topic's semantic tension. Do not show this analysis unless asked.
2. Extract the A/B/C title layers.
3. Translate the topic into one retro Central European cinematic setting.
4. Choose one concrete anchor and one spatial frame such as theatre, station, tram stop, bathhouse, archive desk, postcard, riverbank, courtyard, street corner, facade, or interior.
5. Decide how type, signage, windows, tickets, maps, cards, doors, or props interact.
6. Build a prompt with spatial composition, refined period color, retro print polish, and strong title hierarchy.
7. Add negative constraints against generic travel postcards, cheap templates, overbusy collage, and weak typography.

## Style Definition

Budapest style here means:

- Retro Central European cinematic poster mood, more about spatial story than pure graphic impact.
- Theatre foyer, cinema frontage, station hall, street corner, tram stop, bathhouse arches, riverbank, bridge, archive desk, ticket booth, apartment courtyard, old bookshop, cafe window, postcard, luggage tag, map, receipt, or archive card atmosphere.
- Symmetric or near-symmetric composition with precise editorial order.
- Refined vintage color: dusty pink, coral red, burgundy, cream, saffron yellow, mint, teal, sky blue, lavender, chocolate, warm gray. Color can be vivid, but should feel cinematic and period-specific rather than trendy advertising.
- Flat but cinematic depth: architectural layers, windows, doors, curtains, stairs, signs, props, long shadows, clean cutout-like forms.
- Strong typography integrated into architecture, signage, windows, ticket labels, marquee boards, postcards, maps, receipts, or archive panels.

Do not copy any specific film still, named character, logo, or exact branded poster. Capture the broader retro European cinematic editorial language.

Do not default to a hotel facade. Use hotel, lobby, room, corridor, room key, or concierge imagery only when the user's topic, mood, or metaphor specifically benefits from it.

## Semantic Families And Anchors

Choose one theme family and convert it into a Budapest-style setting:

- Knowledge / method / tutorial / route: route map, train timetable, archive cards, station board, folded guide, bookshop shelf, stairway, index cabinet, city map panel.
- AI / technology / system / information: retro switchboard, card catalog, archive drawers, station control room, information windows, ticketing machine, analog dashboard. Avoid robot faces and cyber neon.
- Wealth / finance / trading / risk: ticket counter, exchange booth, locked safe, ledger, receipt desk, price board, red warning stamp, bank window, threshold scene. Avoid coin piles and generic finance icons.
- Growth / learning / cognition: staircase, bridge crossing, train platform, windows opening in an apartment courtyard, small figure entering a lit doorway, reading room, route through a city map.
- Society / emotion / desire / anxiety / conflict: empty theatre seat, late-night tram stop, apartment windows facing each other, shadowed doorway, cinema lobby, small figure isolated in a public space.
- Brand / city / culture / design / travel: tram, bridge, bathhouse arches, river postcard, rooftop, luggage tag, street sign, cafe window, theatre marquee, storefront, archive postcard.
- Hope / restart / future: door, train platform, bridge, morning river, lighted window, open gate, tram arriving, passage through a colored street scene.

Use only 1-3 anchors. They must be specific and legible.

## Title Layering

For long topics, never enlarge the whole sentence. Split into:

- A-layer giant visual text: 2-6 Chinese characters or 1-3 English words; first visual focus.
- B-layer full title: preserve the user's complete original title in a medium title, signboard, postcard headline, timetable, ticket label, map panel, or information bar.
- C-layer system text: subtitle, category, year, issue number, route number, ticket code, label, account name, short note.

Rules:

- Short title: can become the A-layer giant text directly.
- Medium title: extract the strongest phrase for A-layer.
- Long title: mandatory extraction; full title goes to B-layer.
- Functional words such as `教程`, `指南`, `方法论`, `系统`, `手册`, `观察`, `研究` usually belong in B/C layers unless they are the true focus.
- The A-layer must remain readable and semantically faithful.

## Color System

Use refined period color with enough contrast. It should feel cinematic, printed, and memorable, not like a modern high-impact ad poster.

Good palettes:

- Theatre / cinema: burgundy + cream + saffron yellow + warm black.
- Tram / station: teal + cream + chocolate + muted red.
- Bathhouse / arches: mineral blue + dusty pink + warm white + deep green.
- Archive / ticket: cream + burgundy + faded yellow + ink black.
- River / bridge: sky blue + raspberry + cream + warm gray.
- Dreamy travel: sky blue + raspberry + mint + cream.
- Dramatic night: deep plum + warm yellow windows + red accent + black.
- Method / system: teal + cream + black + acid yellow as tiny signal.
- Conflict / risk: burgundy + cream + black + tomato red.

Rules:

- Use 3-5 main colors.
- One dominant period color or scene color must carry the poster.
- One accent color may create the visual hook, but avoid loud contemporary campaign energy.
- Background must be a scene or architectural color field, not a blank white/gray/beige filler.
- Color should be clean, theatrical, and editorial, not ecommerce bright or neon-tech.

## Composition Systems

Choose one:

- Theatre / cinema frontage: title becomes marquee, poster wall, ticket booth, or stage signage.
- Tram stop / station hall: title embedded in timetable, platform sign, route map, ticket window, or departure board.
- Bathhouse / arch interior: title follows arches, tiles, steam, pools, stairs, or wall signage.
- Postcard cover: large title, scenic architectural slice, stamp/label metadata, disciplined margins.
- Archive / ticket desk: title embedded in timetable, ticket, file drawer, receipt, ledger, or map panel.
- Street corner / cafe window: small figure, storefront, window light, signage, and city props create a contained story.
- Bridge / river scene: title integrated with railing, skyline, river postcard, transit sign, or map ribbon.
- Hotel facade or lobby: use only when thematically justified; title becomes signboard or spatial signage.

Maintain three layers:

1. Giant main title, marquee, signboard, ticket headline, map label, or architectural title sign.
2. One to three visual anchors.
3. Full title, subtitle, issue/room/ticket labels, and small editorial metadata.

## Text-Image Fusion

Make type part of the set:

- Title as theatre marquee, station sign, tram route label, facade lettering, ticket headline, map label, archive tab, or wall typography.
- Image embedded in windows, doors, letter counters, sign panels, or postcard frames.
- Object or figure standing in front of huge type to create scale.
- Type casting shadow onto the scene.
- Windows, stairs, doors, or cards cutting into letterforms.
- Title split across architectural levels, signage bands, ticket strips, or map panels.

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
- Repeated small route numbers, issue labels, ticket codes, archive marks, or map labels as a system.

Readability is mandatory. The main word must be understood at first glance.

## Prompt Template

Adapt this template:

```text
Create a Budapest-inspired cinematic editorial cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}.
Main visual title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / C-layer system text: "{subtitle_or_notes}".

Style: retro Central European cinematic poster, Budapest-inspired city postcard and archive-ticket aesthetic, refined vintage editorial cover, symmetrical spatial composition, theatrical architecture, transit/theatre/bathhouse/station visual language, subtle print texture, high-end cultural poster art direction.

Visual metaphor: {selected_metaphor}. Budapest-style setting: {setting}. Use 1-3 precise image anchors: {anchors}. Text-image relationship: {fusion_method}. Compose as {composition}. Typography must be part of the architecture, marquee, station sign, tram label, ticket, postcard, map, archive panel, or window system rather than a generic overlay. Do not default to hotel imagery unless it is clearly justified by the topic.

Typography: readable title as the visual skeleton, refined vintage display type, signboard / marquee / timetable / ticket lettering, strong hierarchy, full original title preserved in a smaller editorial title system, crisp Chinese/English mixing, no spelling errors. Use 2-4 type reconstruction methods: {type_reconstruction_methods}.

Color and background: {palette_and_background}. Refined period palette, clean theatrical contrast, dominant scene color, restrained accent color, architectural or scenic background with mood and story. Not plain white, beige, or gray filler, and not a trendy high-impact advertising palette.

Mood: {mood}. Extra context: {context}.

Avoid: wrong aspect ratio, generic travel postcard, default hotel facade, hotel/lobby/room/corridor unless topic-specific, empty background, default white/beige/gray background, weak dull color, ecommerce cover, ordinary ad page, trendy color-poster look, cheap neon tech, robot face, overbusy collage, low-end 3D, unreadable title, long title enlarged as one block, disconnected image and text, exact film still replication, named character likeness, official logo imitation.
```

## Quality Bar

The final image must satisfy all of these:

- It reads immediately as retro European cinematic / Budapest-style editorial design.
- The viewer is caught by cinematic space, period color, architecture, props, and typography.
- The background is an intentional setting: theatre, tram stop, station, bathhouse, street corner, river, archive desk, postcard, interior, facade, or object scene.
- Typography is integrated into the scene rather than pasted on top.
- The complete title remains understandable through B-layer text.
- The visual metaphor is accurate and concrete.
- The image is refined, charming, theatrical, and high-end, not a generic travel poster and not a modern trendy color poster.
- The requested aspect ratio is respected.
