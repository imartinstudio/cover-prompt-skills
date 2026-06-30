# Naming

This repository is cover-first. Preserve existing `cover-*` names as the stable visual style surface.

All cover/poster-generation skills should use the `cover-` prefix.

Recommended pattern:

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
cover-pixel-avatar
cover-light-product
cover-3d-eye
cover-mckinsey-briefing-style
cover-sketch-knowledge-poster
cover-cream-orange-knowledge-poster
```

The general organizer uses:

```text
cover-tips
```

Article visual planning uses one explicit planner name:

```text
article-visual-planner
```

Use `article-visual-planner` when one article needs a cover plus coordinated inline visuals. It should read the article, plan the visual set, then chain every planned asset to a selected `cover-*` style.

Preferred Claude CLI chaining syntax:

```text
/article-visual-planner:cover-cream-orange-knowledge-poster
```

Portable field syntax:

```text
$article-visual-planner
视觉风格：cover-sketch-knowledge-poster
```

Do not add new `illustration-*` skills or per-style `*-kit` / `kit-*` coordination skills. Inline visuals, workflow diagrams, comparison graphics, long infographics, and social cards should be planned by `article-visual-planner` and rendered through the selected `cover-*` visual style.

Use a shared visual-family name inside the selected cover skill and planner brief when a style supports multiple asset types. For example, `cover-cream-orange-knowledge-poster` owns the `cream-orange-knowledge` style, while `article-visual-planner` decides whether a planned asset is a cover, article-inline diagram, workflow diagram, comparison panel, architecture map, or long infographic.

Use `3d-eye` for the black-grid, neon-green, terminal-native local AI tutorial family. The name should be preferred over generic names such as `cyber`, `hacker`, or `black-green`, because the core usage is local/offline/private AI education rather than decorative cyberpunk.

Avoid names tied to a provider or runtime:

```text
provider-cover-skills
vendor-cover-prompts
runtime-specific-cover-skills
```

Use neutral project naming:

```text
cover-prompt-skills
```
