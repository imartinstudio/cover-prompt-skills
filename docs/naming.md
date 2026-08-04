# Naming

This repository is cover-first. A name should expose whether a skill creates a single cover or an article visual package, and it should not imply a hidden runtime dependency.

## Visual style surface

All single-cover and poster-generation skills use the `cover-` prefix:

```text
cover-{style-or-visual-system}
```

Examples:

```text
cover-black-white-minimal
cover-trendy-color-poster
cover-budapest-poster
cover-editorial-collage
cover-tea-oriental
cover-giant-perspective-poster
cover-midnight-studio
cover-light-product
cover-3d-eye
cover-mckinsey-briefing-style
cover-sketch-knowledge-poster
cover-cream-orange-knowledge-poster
```

Every base `cover-X` is an independent skill for one cover. It supports `template | prompt | all` and defaults to `template`.

## Article visual skills

An article visual skill uses the sibling suffix:

```text
cover-{style-or-visual-system}-with-docs
```

The suffix means that the skill reads a user-provided article source and returns one article cover plus section-bound `article-inline` visuals in the same visual family. It does not mean an optional mode inside the base skill.

Only these four sibling names are currently published:

```text
cover-3d-eye-with-docs
cover-cream-orange-knowledge-poster-with-docs
cover-light-product-with-docs
cover-sketch-knowledge-poster-with-docs
```

They are independently installable and versioned. The article source contract is deliberately narrow: pasted content, Markdown files, and plain-text files. DOCX and PDF are not included. Each skill supports `template | brief | prompt | all`, defaults to `brief`, defaults to 1 cover plus 3 inline visuals, and accepts 1–5 inline visuals when a count is explicitly supplied.

Every `article-inline` asset must be bound to a concrete section or paragraph, a suggested insertion position, a reading problem, an aspect ratio, and style-specific prompt constraints. The article source is read-only, and the normal output is a conversational brief or prompt rather than an image.

Do not create a sibling merely because a base style exists. Add one only after the style is confirmed as suitable for article cover and inline visual work.

## CoverTips

The selector is named:

```text
cover-tips
```

`CoverTips` first confirms the visual style and then confirms the asset scope: single cover or cover plus inline visuals. If the style is missing, it proposes 1–3 candidates and waits for confirmation. The single-cover route calls `cover-X`; the article route shows only styles with one of the four published siblings.

`CoverTips` does not own visual-style rules and does not write a universal article package. It is a routing boundary, not a substitute name for a concrete visual style.

## Shared vocabulary

Use the following terms consistently:

- **Visual style**: a stable, recognizable, reusable set of composition, color, typography, material, and visual-tone rules.
- **Base cover skill**: an independent `cover-X` skill for a single cover.
- **Article visual skill**: an independent `cover-X-with-docs` skill for an article cover and section-bound inline visuals.
- **Visual family**: the shared identity between a base skill and its optional sibling; the two remain separate install and runtime units.
- **Article source**: pasted content, a Markdown file, or a plain-text file accepted by a `with-docs` skill.
- **Article visual package**: 1 `cover` plus 3 `article-inline` assets by default; when an inline count is explicitly supplied, it must be 1–5.
- **Asset scope**: the user's confirmed choice between a single cover and a cover plus inline visuals.
- **Section binding**: the requirement that every inline asset names its source section or paragraph, insertion position, and reading problem.
- **Brief**: an executable plan for an asset, including its purpose, placement or use case, visual task, aspect ratio, and prompt constraints.

## Names to avoid

Do not introduce names that imply an unconfirmed universal article mode, hidden base-skill dependency, or an article package for every style. Do not add a `cover-tips-with-docs` sibling. Keep new article capability attached to a confirmed visual family through the explicit `-with-docs` suffix.

Historical source-prompt records may contain names from earlier designs. Those records are evidence, not current skill names, marketplace entries, or installation routes.
