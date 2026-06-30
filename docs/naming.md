# Naming

This repository is cover-first but now supports multiple visual output types. Preserve existing `cover-*` names for backward compatibility.

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

Illustration skills should use the `illustration-` prefix:

```text
illustration-{style-or-visual-system}
```

Example:

```text
illustration-sketch-ui
illustration-3d-eye
illustration-cream-orange-diagram
```

Multi-asset coordination skills should use the `kit-` prefix instead of `cover-`, because they do not produce only one cover:

```text
kit-{style-or-visual-system}
```

Example:

```text
kit-cream-orange-knowledge
```

Older kit names such as `sketch-knowledge-kit`, `light-product-kit`, and `3d-eye-kit` are preserved for backward compatibility. New kit skills should prefer the `kit-*` prefix.

Use a shared visual-family name when a cover skill and an illustration skill are designed to work together. For example, `cover-cream-orange-knowledge-poster`, `illustration-cream-orange-diagram`, and `kit-cream-orange-knowledge` belong to the same `cream-orange-knowledge` visual family.

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
