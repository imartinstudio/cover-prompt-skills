---
name: cover-tips
description: Select a visual style and asset scope, then route a cover request to an installed cover-X or one of four confirmed cover-X-with-docs skills. When the style is missing, propose 1–3 candidates and wait for confirmation; do not generate prompts or silently choose a style.
---

# CoverTips

`cover-tips` is a two-stage selector. It preserves the user's original request,
confirmed style, and confirmed asset scope, then hands the request to the
selected skill. It is a routing boundary only: it does not own visual-style
rules, style defaults, or generic prompt generation.

## Stage 1: Confirm the visual style

1. If the user has named a supported style, identify its route ID and continue
   to Stage 2. Do not generate a cover, template, or prompt at this stage.
2. If the user has not named a style, give 1–3 candidates from the request's
   subject, use case, and explicit constraints. Show each candidate's
   display name, route ID, and a short reason grounded in the request. Ask the
   user to confirm one candidate. Do not silently select a style or call a
   target skill.
3. If the request names an unsupported style, say that no matching route is
   available and ask the user to choose from the supported route IDs. Never
   silently substitute another style.

When the user has already made the asset scope explicit, use that information
to constrain the candidate list: an article package may only propose the four
styles with a published `with-docs` route. Otherwise, keep the style choice
separate from the asset-scope question in Stage 2.

## Supported style route IDs

The following table is an inventory of route IDs, not a copy of any style's
visual rules.

<!-- BEGIN GENERATED COVER-TIPS ROUTES -->
| Display name | Single-cover route | Article-package route |
| --- | --- | --- |
| 3D Eye | `cover-3d-eye` | `cover-3d-eye-with-docs` |
| Black-White Minimal | `cover-black-white-minimal` | — |
| Budapest Poster | `cover-budapest-poster` | — |
| Cream Orange Knowledge Poster | `cover-cream-orange-knowledge-poster` | `cover-cream-orange-knowledge-poster-with-docs` |
| Editorial Collage | `cover-editorial-collage` | — |
| Giant Perspective Poster | `cover-giant-perspective-poster` | — |
| Light Product | `cover-light-product` | `cover-light-product-with-docs` |
| McKinsey Briefing Style | `cover-mckinsey-briefing-style` | — |
| Midnight Studio | `cover-midnight-studio` | — |
| Sketch Knowledge Poster | `cover-sketch-knowledge-poster` | `cover-sketch-knowledge-poster-with-docs` |
| Tea Oriental | `cover-tea-oriental` | — |
| Trendy Color Poster | `cover-trendy-color-poster` | — |
<!-- END GENERATED COVER-TIPS ROUTES -->

## Stage 2: Confirm the asset scope

After the style is confirmed, ask the user to choose one of these targets:

- **单张封面** — route to the selected style's `cover-X` ID.
- **封面 + 正文配图（文章视觉包）** — show and route only to these published
  pairs:
  - `cover-3d-eye` → `cover-3d-eye-with-docs`
  - `cover-cream-orange-knowledge-poster` →
    `cover-cream-orange-knowledge-poster-with-docs`
  - `cover-light-product` → `cover-light-product-with-docs`
  - `cover-sketch-knowledge-poster` → `cover-sketch-knowledge-poster-with-docs`

If the confirmed style has no article-package route, explain that the current
inventory supports that style for a single cover only, then ask the user to
choose one of the four published article-package routes. Do not route an
article request to a base `cover-X` skill and do not silently replace the
confirmed style.

Pass the original request and the two confirmed choices to the target skill.
The target skill owns its own input, output-mode, article-source, count, and
visual rules contract; CoverTips must not restate or reimplement that contract.

## Platform handoff

In Claude Code or Codex, after both choices are confirmed, automatically invoke
the target skill and let it execute its own contract. Do not create an
intermediate CoverTips template or generic image prompt.

For other agents, return a next-call template instead of executing or
generating the target output:

```text
下一步调用：{agent-prefix}{single-cover-route-id}
原始请求：{preserved-user-request}
已确认风格：{display-name}
已确认目标：单张封面
```

For an article package, use the corresponding `with-docs` route ID:

```text
下一步调用：{agent-prefix}{article-package-route-id}
原始文章来源：{preserved-article-source}
已确认风格：{display-name}
已确认目标：封面 + 正文配图
用户指定的正文配图数量：{count-or-未指定}
```

`{agent-prefix}` is the invocation prefix supported by the receiving agent;
the route ID must remain unchanged. Preserve any user-supplied mode or output
constraints for the target skill to interpret.

## Routing guardrails

- Missing style always produces 1–3 candidates and a confirmation request.
- Missing confirmation never triggers a target skill.
- A single-cover request routes only to a base `cover-X` skill.
- An article package routes only to one of the four listed `with-docs` skills.
- CoverTips never invents style defaults, visual constraints, or a universal
  article brief.
