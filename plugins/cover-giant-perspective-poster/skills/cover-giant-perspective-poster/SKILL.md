---
name: cover-giant-perspective-poster
description: Generate giant Chinese perspective typography poster/cover image prompts or final images with high-contrast color clashes, theme narrative illustration, strong spatial depth, cinematic composition, sports/esports/movie-poster aesthetics, and typography-as-architecture. Use when the user asks for giant perspective Chinese title, 巨型透视标题, 高冲突撞色封面, cinematic Chinese poster, esports key visual, sports brand visual, perspective text architecture, movie poster composition, or high-impact Chinese typography cover with text as spatial structure.
---

# Giant Perspective Poster Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result must feel like a top-tier movie poster, sports campaign, esports key visual, or high-impact Chinese advertising poster where giant perspective Chinese typography is the spatial structure—not pasted text.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. Do not output analysis, explanations, reference collages, or multiple layout drafts. Generate exactly one complete poster.

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
使用 $cover-giant-perspective-poster 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
插图方向：{illustration_style}
配色倾向：{color_direction}
补充语境：{context}
情绪倾向：{mood}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Aspect ratio: one of `5:2`, `3:2`, `4:5`, `1:1`, `16:9`, `9:16`; treat as a hard layout constraint.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, poster, video cover, WeChat cover, Xiaohongshu cover, movie poster, event key visual, etc.
- Illustration direction: manga, realistic, semi-realistic, 3D, sporty, cinematic, esports, retro ad, etc.; optional—infer from topic if omitted.
- Color direction: high-contrast clash, red-black, purple-green, blue-pink, orange-blue, yellow-green, cyan-red, or free; default to high-contrast clash.
- Extra context: optional.
- Mood: passionate, oppressive, rebellious, crazy, speed, victory, crisis, lonely, futuristic, dramatic, etc.; optional.
- Forbidden elements: optional.

Default canvas:

- X cover: `5:2`, recommended `2500x1000`.
- WeChat / article cover: `3:2`, recommended `1500x1000`.
- Poster / Xiaohongshu: `4:5`, recommended `1500x1875`.
- Square social: `1:1`, recommended `1500x1500`.
- Video / cinematic landscape: `16:9`, recommended `1920x1080`.
- Short video / vertical poster: `9:16`, recommended `1080x1920`.

## Aspect Ratio Discipline

State the exact ratio and canvas size in the first line of the prompt.

- `5:2`: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cover, do not crop to 16:9, do not make square`.
- `3:2`: `LANDSCAPE 3:2 CANVAS, 1500x1000, editorial cover format, do not make square`.
- `4:5`: `VERTICAL 4:5 CANVAS, 1500x1875, poster format, do not make landscape`.
- `1:1`: `SQUARE 1:1 CANVAS, 1500x1500, centered burst composition, do not make landscape or vertical strip`.
- `16:9`: `LANDSCAPE 16:9 CANVAS, 1920x1080, cinematic widescreen poster, do not make square`.
- `9:16`: `VERTICAL 9:16 CANVAS, 1080x1920, short-video cover, strong vertical depth, do not make landscape`.

Fill the whole canvas with intentional color, typography-as-space, and integrated illustration.

## Role And Visual Goal

You are a top-tier movie poster designer, trendy visual director, Chinese type designer, advertising creative director, sports brand visual designer, and esports key visual designer.

Create one high-impact Chinese cover around the user's topic. Style signature:

**Giant Chinese perspective title + high-contrast color clash + theme narrative illustration + strong spatial depth + cinematic composition + trendy advertising visual + high-shareability cover design.**

This is NOT a ordinary poster or simply enlarged title. Chinese text must be part of space—like architecture, wall, road, track, giant sign, stage, projection, ground structure, tunnel, or oppressive visual device.

The Chinese title must be the first visual, occupying roughly 50%–80% of visual area, with strong perspective, angle, depth, and pressure. Figures/objects must relate to the text spatially—not sit beside it as decoration.

Target references: high-impact typography poster, cinematic Chinese title design, giant perspective typography, bold color contrast, editorial sports poster, esports key visual, movie poster composition, dramatic advertising poster, fashion campaign poster, perspective text architecture, visual storytelling poster.

Never resemble: ordinary WeChat cover, knowledge card, e-commerce promo, template poster, flat giant characters, cheap neon tech, simple text plus illustration, flat title without perspective.

## Internal Workflow

1. Understand the topic's real meaning. Keep analysis internal unless asked.
2. Extract A/B/C title layers (see below).
3. Choose the best perspective typography mode for the theme.
4. Select theme metaphor and 1–3 concrete illustration anchors.
5. Define text–image spatial relationship (standing on text, bursting from text, crushed by text, etc.).
6. Build high-contrast palette where color shapes text and space.
7. Compose for the exact aspect ratio.
8. Write prompt or generate one final image with strict negative constraints.

## Title Layering

- **A-layer**: 2–8 Chinese characters with maximum impact; giant perspective main visual; first read.
- **B-layer**: full user topic as medium title, subtitle, info bar, header, or footer.
- **C-layer**: small professional poster system text—year, issue, Guide, Method, Action, Field Notes, Campaign, Manifesto, keywords, edition numbers.

Short topics: use full topic as A-layer but still apply giant perspective. Long topics: never enlarge the whole sentence equally.

## Perspective Typography Modes

Choose the best mode for the theme:

1. **Ground perspective** — title as road, track, landmark, red carpet receding to horizon; figure on/running along text. Growth, route, sprint, victory, journey.
2. **Wall perspective** — title as building facade, billboard, wall vanishing to distance; figure at wall, running from edge, crushed by scale. Business, conflict, city, brand KV.
3. **Ceiling pressure** — title pressing from above like ceiling, sign, beam, stage rig; figure small below. Pressure, crisis, power, fate.
4. **Diagonal slash** — aggressive斜切 title across frame with speed; running, boxing, racing, flight. Passion, rebellion, speed, sports.
5. **Depth tunnel** — repeating/recursive title layers forming tunnel, corridor, track; figure at center bursting out. AI, tech, system, training, games, future.
6. **Giant projection** — title as projected shadow on ground/wall/behind figure; long dramatic shadow. Film, suspense, loneliness, fate.
7. **Top-down** — title as city ground, map, plaza, rooftop sign; tiny figure anchor. Strategy, map, business, city, plan.
8. **Low-angle monument** — title as giant building, monument, sign; heroic oppression. Champion, victory, brand manifesto.
9. **Surround enclosure** — title wraps figure like stage, vortex, orbit. Emotion, controversy, traffic, AI, community.
10. **Fracture burst** — title torn/opened but readable; figure/object breaks through. Breakthrough, rebellion, change, crisis, rebirth.

Requirements for all modes: heavy powerful type with spatial thickness; may stretch, compress, offset, rotate, crop, extend, exit frame; must stay readable; type is entity not sticker.

## Theme Metaphor Families

Metaphor must enter composition, perspective, action, or space—not sit as side icons.

- Tutorial / guide / method: road, stairs, arrows, map, trajectory, entrance, navigation, coordinates, signs; title as path to distance.
- AI / prompts / tools: input box, code UI, robot, cursor, data tunnel, info flow, nodes, screens, CLI; title as digital tunnel, giant interface, channel.
- Growth / comeback / transformation: runner, mountain road, stairs, door, broken wall, sunrise, shadow, old vs new self; title as sprint track or giant stairs.
- Business / money / traffic: funnel, channel, crowd, currency, growth arrows, city ads, traffic path, giant sign tower.
- Trading / risk / finance: volatility, K-line, cliff, protection line, red-green signals, capital flow, dashboard, fault line; title as danger edge or trading battlefield.
- Emotion / attitude / opinion: giant shadow, crack, wall, isolated figure, confrontation, red field, oppressive type as wall or falling stone.
- Community / character / persona: group portrait, stage, flag, spotlight, cards, queue, magazine cover; title as stage or manifesto wall.

## Illustration And Text Integration

Illustration must participate in narrative and connect to title in at least one way: stand on text, burst from text, covered by projection, run along text direction, object hits text, text becomes road/wall/tunnel/stage, partial occlusion, text oppresses figure, figure/object as perspective vanishing point, title as story space.

Allowed: manga/realistic/semi-realistic/3D/cinematic characters, athletes, vehicles, robots, products, city, animals, roads, planes, cars, fists, flags, architecture, maps, stages, signals, screens, tools, devices.

Illustration and text are one integrated composition—not separate layers.

## High-Contrast Color

Must be vivid, conflicting, memorable. Avoid default B/W gray, soft low saturation, bland gradients, cheap cyber blue-purple, safe dull palettes.

Example pairs (also invent others):

- `#80001E` + `#FED6B8`
- `#690DAD` + `#39FF16`
- `#01008A` + `#FF0086`
- `#0236FE` + `#B7F800`
- `#F0FF0C` + deep green
- `#00413C` + `#EB4743`
- `#FB821C` + `#000035`
- scarlet + off-white + charcoal; acid green + deep purple + black; electric blue + hot pink + white

Color must shape text and space: solid fields, contrasting title colors, strong shadows, perspective side darker for thickness, distant text fading for depth, warm/cool fight between figure and type, B/W background with saturated title punch-through.

Keep premium—never muddy, chaotic, or cheap.

## Composition Hierarchy

1. Giant perspective Chinese title (may crop off canvas).
2. Theme figure/object.
3. Subtitle.
4. Small system text.

Use asymmetric, non-centered, non-template layouts. Small text must feel like professional poster information system—not manual copy.

## Aspect Ratio Layout Notes

- **5:2**: horizontal giant title with strong tilt or recession; figure left/center/right in run/burst/pressure/cross relation. X cover, horizontal video, WeChat banner.
- **4:5**: title surging up from bottom or pressing from top; figure in foreground. Xiaohongshu, poster.
- **1:1**: center burst; huge title + focal figure/object.
- **16:9**: cinematic widescreen; title as distant building, ground road, or giant projection.
- **9:16**: strong vertical depth; title rising from bottom; figure foreground/midground. Short video cover.

## Texture And Quality

Include where appropriate: cinematic poster light, print grain, paper texture, strong projection, light noise, motion blur, spatial depth, premium illustration, semi-realistic ad finish, magazine cover quality, thick type shadow, dramatic light, large pure color fields, extreme contrast.

Avoid: cheap AI look, clutter, low resolution, blurred unreadable text, illustration stealing title focus.

## Strict Prohibitions

Never produce: tiny flat Chinese title; no perspective or depth; illustration unrelated to text; decorative side illustration; bland palette; only B/W gray; knowledge-card or e-commerce promo look; unreadable or over-distorted type; figure overshadowing title; flat centered template; no pressure or speed; dirty colors; cheap neon; generic tech blue-purple gradient; over-stacked elements; too much small text; no ad/poster premium; wrong Chinese characters; separated text and image; PPT cover; cheap template feel.

## Prompt Template

Adapt this template for `--out-type prompt` or internal image generation:

```text
Create a giant Chinese perspective typography cinematic poster cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}". Use case: {use_case}. Language: {language}.
A-layer giant perspective title: "{core_title}". B-layer full title: "{full_title}". Subtitle / C-layer: "{subtitle_and_system_text}".

Style: giant perspective Chinese typography poster, high-impact typography poster, cinematic Chinese title design, bold high-contrast color clash, editorial sports poster, esports key visual, movie poster composition, dramatic advertising poster, perspective text architecture, trendy campaign poster, visual storytelling poster. Illustration direction: {illustration_style}.

Perspective mode: {perspective_mode}. The Chinese title occupies 50-80% of visual area, with strong angle, depth, and pressure, acting as {spatial_role} (architecture, wall, road, track, stage, projection, tunnel, sign, ground structure). Typography: ultra-bold Chinese display type, 3D thickness, compressed/stretched/tilted forms, cropped at edges, readable at first glance.

Visual metaphor: {metaphor}. Anchors: {anchors}. Text-image relationship: {fusion_method}. Figure/object must {spatial_action}, integrated with the title space, not floating as decoration.

Color: {palette}. High-contrast clash, premium clean saturation, color participates in text depth and spatial shaping. Mood: {mood}. Context: {context}.

Composition hierarchy: 1 giant perspective title, 2 narrative illustration, 3 subtitle, 4 small poster system text. Cinematic light, print grain optional, strong shadows, dramatic depth.

Avoid: wrong aspect ratio, small flat title, no perspective, disconnected illustration, bland gray palette, cheap neon cyber gradient, e-commerce promo, knowledge card, PPT layout, unreadable Chinese, wrong characters, template centering, illustration overpowering title, muddy colors, multiple drafts, analysis text, reference collage.
```

## Quality Bar

The final image must satisfy:

1. First glance: enormous readable Chinese perspective title.
2. Strong angle, space, pressure on the title.
3. Illustration clearly tied to topic and fused with text space.
4. High-contrast memorable palette with premium finish.
5. Movie poster / sports / esports / fashion campaign level—not template cover.
6. Stops the scroll on social platforms.
7. Exact aspect ratio respected.
8. When generating directly: one image only, no explanation.

For the archived original Chinese specification, see [docs/source-prompts/cover-giant-perspective-poster.md](../../../../docs/source-prompts/cover-giant-perspective-poster.md).
