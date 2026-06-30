# Source Prompts

This directory archives the original Chinese prompts used to create the visual prompt skills.

These files are source/design records only. Runtime behavior is defined by each plugin's `SKILL.md`.

## Files

| File | Skill |
|---|---|
| `cover-editorial-collage.md` | `cover-editorial-collage` |
| `cover-black-white-minimal.md` | `cover-black-white-minimal` |
| `cover-trendy-color-poster.md` | `cover-trendy-color-poster` |
| `cover-budapest-poster.md` | `cover-budapest-poster` |
| `cover-tea-oriental.md` | `cover-tea-oriental` |
| `cover-giant-perspective-poster.md` | `cover-giant-perspective-poster` |
| `cover-midnight-studio.md` | `cover-midnight-studio` |
| `cover-light-product.md` | `cover-light-product` |
| `cover-mckinsey-briefing-style.md` | `cover-mckinsey-briefing-style` |
| `cover-sketch-knowledge-poster.md` | `cover-sketch-knowledge-poster` |
| `cream-orange-knowledge.md` | `cover-cream-orange-knowledge-poster`, usable through `article-visual-planner` |
| `3d-eye.md` | `cover-3d-eye`, usable through `article-visual-planner` |

`article-visual-planner` has no standalone source prompt. It is the unified planner that reads article content and chains planned visual assets to a selected `cover-*` style.

`3d-eye.md` tracks the original case images in `assets/cases/`. Runtime behavior is owned by `cover-3d-eye`; article-level visual packages are planned by `article-visual-planner`.

`cream-orange-knowledge.md` tracks the original reference-image set and requirement dialogue for the cream-orange technical knowledge family. Runtime style behavior is owned by `cover-cream-orange-knowledge-poster`; article-level visual packages are planned by `article-visual-planner`.

## Source

- `cover-editorial-collage`, `cover-black-white-minimal`, `cover-trendy-color-poster`, and `cover-budapest-poster` were extracted from Codex session `019e42b6-037e-7160-8df6-9d2d81a9e903`.
- `cover-tea-oriental` was extracted from a later Codex session on the same date.
