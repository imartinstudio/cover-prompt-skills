---
name: cover-mckinsey-briefing-style
description: Generate McKinsey-style executive briefing cover image prompts or final images with consulting-grade report aesthetics, crisp white space, blue-black-red accent discipline, strategy frameworks, issue trees, quadrant matrices, data charts, boardroom-ready typography, and rigorous business insight hierarchy. Use when the user asks for 麦肯锡简报风, 咨询简报封面, consulting briefing cover, strategy report cover, boardroom deck cover, executive briefing visual, management consulting style, business report cover, strategy presentation cover, or PPT consulting cover.
---

# McKinsey Briefing Style Cover

Use this skill to create a finished image prompt, or call an image generation tool directly when the user asks to generate the final cover. The result must feel like a top-tier strategy consulting executive briefing or boardroom-ready report cover: rigorous, restrained, analytical, and premium.

Do not use McKinsey logos, official brand marks, or claim official affiliation. Treat "McKinsey-style" as a visual shorthand for high-end management consulting report aesthetics.

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
- Treat `直接生成`, `生成海报`, `出图`, `生成封面图`, `生成简报封面`, and `生成PPT封面` as direct image generation when an image tool is available.

Do not infer prompt mode from field values. For example, `主题：提示词` means the topic is "提示词"; it does not by itself mean `--out-type prompt`.

If `--out-type` has any value other than `template`, `prompt`, or `all`, ask the user to choose one of those three values.

## Template Output

For template-only mode, output exactly this structure and fill every field:

```text
使用 $cover-mckinsey-briefing-style 生成一张封面
主题词：{topic}
副标题：{subtitle}
画幅比例：{ratio}
语言：{language}
用途：{use_case}
行业语境：{industry_context}
分析框架：{analysis_framework}
视觉主体：{visual_subject}
情绪倾向：{mood}
禁用元素：{forbidden_elements}
```

## Required Inputs

Extract or infer:

- Topic / main title: required.
- Subtitle: optional; use a concise executive promise, insight, or scope statement.
- Aspect ratio: optional; if omitted, infer from use case.
- Language: Chinese, English, or mixed Chinese-English.
- Use case: X cover, LinkedIn cover, PPT cover, strategy deck cover, executive briefing, board report, WeChat cover, report title page, knowledge card, etc.
- Industry context: AI, SaaS, consumer, healthcare, finance, manufacturing, energy, retail, education, strategy, operations, growth, risk, transformation, etc.; optional, infer from topic.
- Analysis framework: issue tree, 2x2 matrix, value chain, market map, waterfall chart, benchmark table, scenario grid, roadmap, operating model, portfolio matrix, risk heatmap; optional, infer from topic.
- Visual subject: strategic map, executive memo sheet, report spread, chart system, boardroom table abstraction, industry landscape, decision matrix, data dashboard, transformation roadmap, etc.; optional, infer from topic.
- Mood: rational, authoritative, precise, calm, strategic, executive, sober, urgent, premium, etc.
- Forbidden elements: optional.

## Aspect Ratio Discipline

If the user specifies a ratio, use it as a hard constraint. If omitted, map from use case:

| Use case | Ratio | Recommended size |
|---|---|---|
| X / LinkedIn cover | `5:2` | `2500x1000` |
| PPT cover / strategy deck | `16:9` | `1920x1080` |
| WeChat article header | `2.35:1` | `900x383` |
| WeChat cover | `3:2` | `1500x1000` |
| Report title page | `4:5` | `1600x2000` |
| Knowledge card | `1:1` | `1600x1600` |
| Poster / vertical briefing | `4:5` | `1600x2000` |

State the exact ratio and canvas size in the first line of the prompt.

- `5:2`: `WIDE HORIZONTAL 5:2 CANVAS, 2500x1000, executive briefing header, do not crop to 16:9, do not make square`.
- `16:9`: `LANDSCAPE 16:9 CANVAS, 1920x1080, strategy deck cover, do not make square`.
- `2.35:1`: `WIDE 2.35:1 CANVAS, 900x383, WeChat header format, do not make square or vertical`.
- `3:2`: `LANDSCAPE 3:2 CANVAS, 1500x1000, consulting report cover, do not make square`.
- `4:5`: `VERTICAL 4:5 CANVAS, 1600x2000, report title page format, do not make landscape`.
- `1:1`: `SQUARE 1:1 CANVAS, 1600x1600, executive knowledge card, do not make landscape strip`.

Design for the full canvas with rigorous margins, proportional whitespace, and a visible information hierarchy.

## Internal Workflow

1. Understand the topic's real business question: growth, risk, market entry, transformation, cost, operating model, AI adoption, customer behavior, competitive dynamics, or investment thesis. Keep analysis internal unless asked.
2. Convert the topic into a boardroom-level visual thesis, not a decorative poster concept.
3. Split long titles into A/B/C layers: a strong executive title, the full original title, and small metadata labels.
4. Choose one consulting framework that clarifies the topic: issue tree, 2x2 matrix, market landscape, roadmap, benchmark chart, value chain, or risk heatmap.
5. Compose the cover with a strict grid, large white space, crisp typography, one analytical visual system, and limited blue/black/red accents.
6. Add negative constraints against generic corporate stock art, startup gradient banners, decorative dashboards, and fake logo usage.

## Title Layering

For long topics, never enlarge the whole sentence. Split into:

- A-layer executive title: 2-8 Chinese characters, 1-4 English words, or a concise business phrase. This is the first visual focus.
- B-layer full title: preserve the original topic in a medium title, subtitle row, or report header.
- C-layer consulting metadata: industry, date, "Executive Briefing", "Strategy Note", "Market Map", "Confidential Draft", section number, region, KPI labels, or 1-3 framework tags.

Extraction rules:

- Short title: the full topic can become the A-layer title.
- Medium title: extract the most decision-relevant business phrase for A-layer.
- Long title: mandatory extraction; full title moves to B-layer.
- Functional words such as `教程`, `指南`, `方法论`, `入门`, `路线`, `实战`, `分享`, `观察`, `研究`, `报告`, `简报`, and `复盘` usually belong in B/C layers unless they are the true concept.
- Preserve product names, industry terms, company names, regions, numbers, and exact strategic claims.

## Visual Style

The image should combine:

- Top-tier management consulting report cover, executive briefing title page, boardroom strategy deck, business review note.
- Crisp white or off-white background, strict modular grid, fine rules, footnote-scale metadata, precise chart alignment.
- Large confident title, restrained analytical visual, high information clarity, not decorative complexity.
- Consulting-grade frameworks: issue tree, 2x2 matrix, strategic roadmap, market map, benchmark bars, waterfall, value chain, risk heatmap, scenario matrix, operating model diagram.
- Subtle paper texture or print grain only when it improves report realism.

Color discipline:

- Base: white, off-white, light gray, deep charcoal.
- Accent: deep consulting blue, muted red, cool gray. Use red only for risk, tension, or important deltas.
- Keep color accents to 5-15% of the canvas.
- Avoid one-note blue gradients; use blue as a disciplined executive accent, not a tech glow.

Typography:

- Use readable modern sans-serif typography with strong executive hierarchy.
- Prefer left-aligned or grid-aligned title systems.
- Use small caps / thin metadata labels sparingly.
- All visible text must be clean, spelled correctly, and aligned like a real consulting deck.

## Semantic Families And Framework Choices

Choose the strongest family and select one dominant visual system:

- Strategy / competition / market entry: 2x2 matrix, market landscape, competitor map, strategic options table.
- Growth / customer / product: growth flywheel, funnel chart, customer journey, segmentation grid, KPI dashboard.
- AI / technology / transformation: operating model, capability maturity map, workflow architecture, adoption roadmap. Avoid robot faces and neon cyberpunk.
- Finance / investment / risk: waterfall chart, risk heatmap, scenario matrix, portfolio map, valuation bridge. Avoid coin piles and crypto icon cliches.
- Operations / supply chain / manufacturing: value chain, process map, bottleneck diagram, cost curve, capacity roadmap.
- Organization / talent / management: org model, decision rights map, leadership system, capability matrix.
- Policy / economy / macro: regional map, scenario grid, trendline chart, briefing memo layout.
- Learning / methodology / playbook: issue tree, checklist grid, roadmap, executive memo page, decision framework.

The framework must support the topic's meaning. It should look like part of the cover, not pasted as a random infographic.

## Composition Systems

Choose one:

- Executive memo cover: large title on left/top, small metadata block, one analytical figure on right/bottom.
- Report spread: title page and chart page overlap as refined paper layers, with clean shadows and grid alignment.
- Strategy matrix hero: a large 2x2 or scenario grid becomes the main visual structure behind or beside the title.
- Market map: minimal node/region map with labeled clusters, restrained dots and connecting lines.
- Roadmap / value chain: horizontal strategic flow across the canvas with title anchored to the grid.
- Data chart title page: one precise chart, table, or benchmark panel supporting the title.
- Boardroom abstraction: subtle report pages, table edge, or projection surface, but no generic business people posing.

Maintain three layers:

1. Executive title and core message.
2. Analytical framework visual.
3. Small metadata system: subtitle, industry, date, section, KPI labels, region, source line.

## Text-Visual Relationship

The analytical visual must clarify the title:

- A matrix can frame the title or sit behind it as the logic structure.
- A roadmap can run under the title as a strategic timeline.
- An issue tree can branch out from the core phrase.
- A market map can occupy the whitespace next to the title.
- A chart can expose the tension, delta, or opportunity implied by the topic.
- Report pages can layer under the title as a physical briefing object.

Avoid floating charts that have no relationship to the title.

## Prompt Template

Adapt this template:

```text
Create a McKinsey-style executive briefing cover for a {ratio} canvas, {canvas_size}. {ratio_instruction}
Topic: "{topic}".
Use case: {use_case}. Language: {language}. Industry context: {industry_context}.
Executive title A-layer: "{core_title}". Full title B-layer: "{full_title}". Subtitle / C-layer metadata: "{subtitle_or_notes}".

Style: top-tier management consulting report cover, executive briefing title page, boardroom strategy deck aesthetic, crisp white space, strict modular grid, precise business typography, restrained analytical visual system, premium strategy report design, clean editorial hierarchy, subtle paper texture, high information clarity.

Analytical framework: {analysis_framework}. Visual subject: {visual_subject}. Use 1 dominant framework and 1-3 supporting micro-elements: {supporting_elements}. The framework must clarify the business question and interact with the title, not float as decoration.

Composition: {composition}. Large readable executive title, full original title preserved in a smaller report-header system, small metadata labels such as industry/date/region/KPI/source line, rigorous margins, clear alignment, boardroom-ready polish.

Color: white/off-white/light gray base, deep charcoal text, disciplined consulting blue accent, optional muted red only for risk or delta emphasis, color accents limited to 5-15% of the canvas, no neon, no decorative gradient overload.

Mood: {mood}. Extra context: {context}.

Avoid: official McKinsey logo or brand marks, fake affiliation, wrong aspect ratio, generic corporate stock photos, smiling business people, handshake imagery, skyscraper stock photo, startup gradient banner, cheap blue-purple tech neon, robot face, coin pile, decorative dashboard clutter, infographic template feel, crowded slide, long title enlarged as one block, typo, unreadable text, overdone 3D, random floating charts, bland PowerPoint template.
```

## Direct Generation

When the user asks to generate the final image, create exactly one complete cover. Keep all reasoning internal and output only the generated image. The final image should look like a credible executive briefing cover that a consulting partner could put in front of a board, while remaining generic and unaffiliated with any real consulting firm's official identity.
