---
name: cover-light-product
description: Generate light-theme AI-native SaaS product cover image prompts or final images with cream-white base, Claude-Codex dual-brand fusion, Agent workspace narrative, premium hero-banner aesthetics, refined typography, and magazine-editorial composition. Use when the user asks for 浅色产品风, 浅色产品, light product cover, SaaS产品封面, AI产品封面, 奶油白封面, AI-native product visual, agent workspace cover, SaaS hero banner, product launch visual, or light-theme professional tech cover.
---

# Light Product Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result must feel like a premium SaaS website hero banner from a $10B AI company—not an ad banner, not a stock illustration, not a tutorial cover.

If generating the image directly, keep all semantic and design analysis internal and output only the generated image result. Do not output analysis, explanations, reference collages, or multiple layout drafts. Generate exactly one complete cover.

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
使用 $cover-light-product 生成一张封面
主题词：{topic}
副标题：{subtitle}
用途：{use_case}
画幅比例：{ratio}
语言：{language}
视觉主体：{visual_subject}
构图模式：{composition_mode}
暖色比例：{warm_color_ratio}
冷色比例：{cool_color_ratio}
基底色调：{base_tone}
强调色倾向：{accent_leaning}
UI元素：{ui_elements}
系统微文案：{system_microcopy}
补充语境：{context}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional.
- Use case: X header, Xiaohongshu, WeChat header, WeChat article, Bilibili, Zhihu, Xianyu, LinkedIn, PPT cover, product launch, SaaS landing hero, blog header, etc.
- Aspect ratio: optional—if omitted, infer from use case (see defaults below).
- Language: Chinese, English, or mixed Chinese-English.
- Visual subject: Agent workspace, multi-agent collaboration, workflow graph, dashboard, task system, knowledge graph, research pipeline, browser automation, AI coding workflow, design workspace, automation flow, memory system, knowledge base, execution status, etc.; optional—infer from topic.
- Composition mode: left-text-right-visual, top-visual-bottom-text, center-focus, full-canvas-workspace; optional—infer from topic and use case.
- Warm color ratio: how much Claude warm palette (orange/brown/gold) vs cool palette; optional—default balanced.
- Cool color ratio: how much Codex cool palette (indigo/purple-blue); optional—default balanced.
- Base tone: cream white, rice white, warm gray white, cool gray white; optional—default cream white.
- Accent leaning: Claude warm, Codex cool, neutral fusion; optional—infer from topic.
- UI elements: agent nodes/cards, workflow lines, floating info cards, task panels, browser windows, document panels, terminal windows, dashboards, search panels, status indicators, timeline, knowledge graph nodes, tree structures, grid systems, progress rings, tag systems, automation pipes; optional—auto-select from element library.
- System microcopy: AGENT, WORKFLOW, AUTOMATION, AI NATIVE, TASK SYSTEM, MULTI-AGENT, RESEARCH, DEPLOY, BUILD, ANALYZE, IN PROGRESS, COMPLETED, 3 agents running, Task completed, etc.; optional—pick 1-3 that match topic.
- Extra context: optional.
- Forbidden elements: optional.

## Aspect Ratio Discipline

If the user specifies a ratio, use it as a hard constraint. If omitted, map from use case:

| Use case | Ratio | Recommended size |
|---|---|---|
| X (Twitter) header | `5:2` | `2500x1000` |
| X (Twitter) post | `16:9` | `1920x1080` |
| Xiaohongshu | `3:4` | `1440x1920` |
| WeChat article header | `2.35:1` | `900x383` |
| WeChat post image | `16:9` | `1920x1080` |
| Bilibili cover | `16:10` | `1920x1200` |
| Zhihu cover | `16:9` | `1920x1080` |
| Xianyu / marketplace | `1:1` | `1600x1600` |
| LinkedIn cover | `5:2` | `2500x1000` |
| PPT cover (fallback) | `16:9` | `1920x1080` |
| Product launch (fallback) | `16:9` or `5:2` | infer from platform |

State the exact ratio and canvas size in the first line of the prompt.

- `5:2`: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, extra-wide cover, do not crop to 16:9, do not make square`.
- `21:9`: `ULTRA-WIDE 21:9 CANVAS, 2400x1000, cinematic blog header, do not make square`.
- `2.35:1`: `WIDE 2.35:1 CANVAS, 900x383, WeChat header format, do not make square or vertical`.
- `16:9`: `LANDSCAPE 16:9 CANVAS, 1920x1080, video/Bilibili cover, do not make square`.
- `16:10`: `LANDSCAPE 16:10 CANVAS, 1920x1200, Bilibili cover, do not make square`.
- `3:4`: `VERTICAL 3:4 CANVAS, 1440x1920, Xiaohongshu format, do not make landscape`.
- `1:1`: `SQUARE 1:1 CANVAS, 1600x1600, marketplace cover, do not make landscape strip`.
- `3:2`: `LANDSCAPE 3:2 CANVAS, 1500x1000, editorial cover, do not make square`.
- `4:5`: `VERTICAL 4:5 CANVAS, 1500x1875, poster format, do not make landscape`.
- `9:16`: `VERTICAL 9:16 CANVAS, 1080x1920, short-video cover, do not make landscape`.

Fill the whole canvas with intentional depth, information hierarchy, and integrated title/UI—not empty margins.

## Role And Visual Goal

You are a world-class visual design director, brand designer, SaaS product design consultant, and AI cover design expert.

Create one cover with this style signature:

**Light product feel + cream-white base + Claude-Codex dual-brand fusion + Agent workspace narrative + SaaS hero-banner quality + magazine-editorial typography + refined information hierarchy.**

This is a new visual category: **AI Native Product Visual Style**. It is neither cold corporate tech nor candy-colored consumer internet illustration. It is the visual language of AI-era professional tools and workflows—warm without being childish, tech without being cold, professional without being dull.

Brand sensibility references: Claude (warm restraint, humanistic, soft orange, conversational interface, thinking feel) × Codex (precision efficiency, indigo-purple, terminal texture, agent orchestration, task systems) × Linear (minimal task management, keyboard-driven, pixel-level UI) × Stripe (developer tool aesthetics, gradient and glassmorphism, commercial-grade refinement) × Notion (block-based information organization, cream-white base, knowledge system feel) × Arc Browser (spatial tab system, soft rounded corners, transparency layers) × Apple Keynote (keynote-level typography, oversized type, minimal slide composition).

Never resemble: cheap AI poster art, stock business illustration, e-commerce banner, infographic template, dark mode (this style is light-first), overdone 3D, candy colors, fluorescent gradients.

## Internal Workflow

1. Understand the topic's real meaning and what it implies about the AI product or workflow. Keep analysis internal unless asked.
2. Choose visual subject, composition mode, warm/cool ratio, and base tone that best serve the topic.
3. Pick one composition mode (left-text-right-visual, top-visual-bottom-text, center-focus, full-canvas-workspace) based on use case aspect ratio.
4. Plan the three-layer structure: foreground subject (60-70%), midground title area (15-25%), background label zone (5-10%).
5. Select 3-5 UI elements from the element library that support the narrative—agent nodes, workflow lines, dashboards, etc.
6. Integrate main title with refined typography—large sans-serif with strong contrast against the visual subject.
7. Add system microcopy as professional label/tag information—like a real product UI, not decoration.
8. Build prompt or generate one final image with strict negative constraints.
9. Ensure warm and cool colors coexist (4:6 or 6:4 ratio), with color covering only 10-20% of the canvas.

## Color System

### Base tones (background, 80-90% of canvas)
- Cream white `#FAF7F2`
- Rice white `#F8F6F0`
- Warm gray white `#F5F4F0`
- Cool gray white `#F4F5F7`

### Claude palette (warm, ~40-60% of colored area)
- Soft orange `#D9794A`
- Light brown `#C4956A`
- Warm gold `#D4A853`
- Terracotta `#C47A5A`
- Warm beige `#E8D5C0`

### Codex palette (cool, ~40-60% of colored area)
- Indigo blue `#4A5FD9`
- Purple blue `#6B5FD9`
- Cool gray blue `#7A8FAF`
- Deep blue gray `#5A6A8A`
- Light purple gray `#C5C5E0`

### Neutral system
- Deep gray black (text) `#1A1A1A`
- Mid gray (secondary text) `#6A6A6A`
- Light gray (dividers) `#E0E0E0`
- Ultra light gray (card backgrounds) `#F0F0F0`

### Color rules (strict)
1. Overall low saturation—no harsh, fluorescent, or candy colors.
2. Claude warm and Codex cool must coexist in every image, balanced 4:6 or 6:4.
3. Color covers only 10-20% of canvas area (accents, nodes, links).
4. 80-90% of canvas stays neutral (white, gray, cream).
5. Subtle gradients (Claude warm → Codex cool) allowed for backgrounds or key elements.

## Composition System

### Three-layer structure
- **Layer 1: Main visual area (60-70%)** — core visual narrative: agent workspace, dashboard, workflow graph, etc. This is what the viewer sees first.
- **Layer 2: Title area (15-25%)** — main title + subtitle, refined typography in dialogue with the visual.
- **Layer 3: Info label area (5-10%)** — platform identifier, category tags, date, small supporting text, reinforcing the editorial feel.

### Composition modes (auto-select the best fit)
- **Mode A: Left text, right visual** — large title area on left, agent workspace visual on right. Best for X header, LinkedIn, and other wide horizontal canvases.
- **Mode B: Top visual, bottom text** — large agent workspace above, title system below. Best for WeChat header, Bilibili cover.
- **Mode C: Center focus** — large central agent dashboard, title overlaid or placed at bottom. Best for Xiaohongshu, Xianyu, and other vertical canvases.
- **Mode D: Full-canvas workspace** — the entire image is a refined agent workspace, with the title embedded as part of the UI (e.g., dashboard title bar). Best for immersive scenarios.

### Composition requirements
1. Abundant whitespace—30-40% of canvas should be breathing room.
2. Information density high in the subject zone, zero in whitespace zones.
3. Magazine-editorial feel—strong size contrast (large type very large, small type very small, 3:1 to 5:1 ratio).
4. Product keynote visual quality—like a Keynote slide, not a banner ad.
5. SaaS website hero quality—like the first screen of a landing page.

## Visual Element Library

### UI elements (auto-select 3-5)
- Agent nodes / cards
- Workflow connection lines / data flow arrows
- Floating info cards
- Task panels / Kanban columns
- Browser windows (showing automation in action)
- Document windows / editor panels
- Terminal windows (refined, not raw)
- Data dashboards
- Search interfaces / query panels
- Notifications / status indicators

### Structural elements
- Timelines / Gantt bars
- Knowledge graph node networks
- Tree structures / hierarchy diagrams
- Grid / table systems
- Progress bars / status rings
- Tags / classification systems
- Automation flow pipes

### Brand-feel elements
- Subtle gradient backgrounds
- Glassmorphism cards
- Refined rounded-corner containers
- Soft shadows
- Thin line dividers
- Icon system (clean linear icons)

### Element usage principles
1. Rich but not cluttered—every element has a position and function.
2. Maintain order and hierarchy—like a real product interface, not a collage of assets.
3. Elements must have visual relationships (lines, alignment, grouping)—no isolated floating elements.
4. Prioritize "system actively running" state, not static empty interfaces.

## Typography

### Title strategy
1. Main title must be prominent, using large sans-serif type.
2. If title is long (>8 Chinese characters), consider extracting a keyword as the hero type and using the full title as subtitle.
3. Title and visual subject must have breathing space between them.
4. Title may overlay the visual subject but must maintain readability.

### Type personality
- Chinese: modern geometric sans-serif, clean and crisp.
- English: SF Pro / Inter / Untitled Sans style, modern tech feel.
- Numbers/data: monospace feel to reinforce tool/product identity.

### Supporting text
- Subtitle uses small type, 3:1 to 5:1 size contrast with main title.
- May include tiny category labels: AGENT · WORKFLOW · AUTOMATION · AI NATIVE.
- May include product-UI-like status text: "3 agents running", "Task completed".

## Title Integration

Titles must feel like part of the product design:
- On UI panels, floating HUD labels, dashboard headers, or spatial typography.
- Clear readable main title in the specified language.
- Subtitle and system microcopy as secondary hierarchy—professional poster information system, not manual clutter.
- Never paste title as a flat sticker unrelated to the visual system.

## Prompt Template

Adapt for `--out-type prompt` or internal image generation:

```text
{ratio_instruction}
Topic: "{topic}". Subtitle: "{subtitle}". Use case: {use_case}. Language: {language}.

Style: light product cover, AI-native product visual, cream-white base, SaaS hero-banner quality, Claude-Codex dual-brand fusion, agent workspace aesthetics, magazine-editorial typography, refined information hierarchy, premium tech brand campaign. NOT dark mode, NOT cheap AI poster, NOT e-commerce banner, NOT candy-colored illustration, NOT infographic template, NOT overdone 3D.

Base tone: {base_tone}. Warm palette (Claude): {warm_colors_specified}. Cool palette (Codex): {cool_colors_specified}. Warm-to-cool ratio: {warm_cool_ratio}. Color covers only 10-20% of canvas; 80-90% stays neutral white/gray/cream.

Visual subject: {visual_subject}. Composition mode: {composition_mode}. Three-layer structure: foreground subject zone (60-70%), midground title zone (15-25%), background label zone (5-10%). 30-40% whitespace.

UI elements from library: {ui_elements}. Brand-feel elements: glassmorphism cards, subtle gradients, refined rounded corners, soft shadows, thin dividers, linear icons. Elements must have visual relationships—lines, alignment, grouping. Prioritize "system actively running" state.

Title integration: main title "{core_title}" rendered as {title_integration_method} (UI panel / dashboard header / spatial typography). Subtitle: "{subtitle}" in small type with 3:1 to 5:1 contrast. System microcopy: {system_microcopy} as professional label/tag system.

Typography: large modern geometric sans-serif for Chinese, SF Pro / Inter style for English, monospace feel for numbers. Strong size contrast, magazine-editorial feel, Keynote-slide quality.

Mood: AI is working, not humans in an office. This is the future of work—agent workspace, multi-agent collaboration, intelligent systems. Context: {context}.

Avoid: coffee cups, notebooks, pencils, desk lamps, plants, human hands, office scenes, meeting rooms, circuit boards, robots, glowing brains, cyberpunk cities, outer space, locks, shields, handshakes, lightbulbs, dark mode, fluorescent gradients, candy colors, cluttered compositions, unreadable titles, titles pasted as flat stickers, wrong aspect ratio, stock illustration feel, multiple drafts, analysis text.
```

## Core Narrative

One sentence: **AI is working, not humans in an office.**

The image shows an Agent Workspace—multiple AI agents simultaneously collaborating on complex tasks. This is the future of work, not the past of office scenes.

The image should make people think:
- "This is the next generation of work."
- "AI agents are doing things for me."
- "Complex tasks are being automatically orchestrated and executed."
- "I define the goal; agents handle execution."
- "This is an intelligent system, not a tool."

## Strict Prohibitions

### Forbidden office elements (no traditional office)
- Coffee cups, notebooks, pencils, rulers
- Desk lamps, plants, desk ornaments
- Human hands, typing hands, hands holding pens
- Offices, workstations, meeting rooms

### Forbidden cliché tech
- Chips, circuit boards, PCB traces
- Robots, robotic arms
- Glowing brains, neural network spheres
- Cyberpunk cities, neon rain nights
- Outer space, Earth, particle universes
- Locks, shields (security icons)
- Handshakes (collaboration icons)
- Lightbulbs (creativity icons)

### Forbidden design styles
- Cheap AI poster look (Midjourney default aesthetic)
- Generic business illustration
- E-commerce cover feel
- Infographic template feel
- Overdone 3D showmanship
- Decorative borders and ornaments
- Fluorescent gradients
- Dark mode (this style is light-first)

### Forbidden design mistakes
- Text-background contrast too low
- Floating unrelated elements
- Overcrowded canvas, no breathing room
- Color covering more than 30% of canvas
- Only warm or only cool colors (both must coexist)
- Title unreadable or over-deformed

## Quality Bar

The final image must satisfy:

1. Commercial-grade design—like a top AI company's website hero.
2. Tech media cover quality—worthy of TechCrunch / The Verge feature images.
3. High click-through rate—visually competitive in information feeds.
4. High shareability—makes people want to save, share, and bookmark.
5. Dual-brand fusion—both Claude warmth and Codex precision are felt.
6. Ultra-clear 8K—crisp details usable at enlargement.
7. Professional brand visual—could serve as a product website design reference.
8. Modern UI design—interface elements look like real, usable products.
9. Pixel-level refinement.
10. Premium product marketing poster—not a tutorial cover, but a product launch.

First impression targets:
- "This is professional."
- "This is premium."
- "This is the next generation of work."
- "I want to click and learn more."
- "I want to use this product."
- "This could be my wallpaper."

For the archived original Chinese specification, see [docs/source-prompts/cover-light-product.md](../../../../docs/source-prompts/cover-light-product.md).
