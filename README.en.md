English | [中文](README.md)

---

# Cover-First Visual Prompt Skills

Reusable visual prompt skills for AI agents and image-generation workflows. Each `cover-X` is an independently installable and callable single-cover skill. Only four confirmed article-friendly styles have an independent `cover-X-with-docs` sibling. `cover-tips` is an optional two-stage selector; it does not own visual-style rules and no longer acts as a universal article planner.

Compatible with Claude Code, Codex, Gemini CLI, Cursor, and any agent that supports `SKILL.md`.

## GitHub Quick Start

![GitHub quick start tutorial](assets/quickstart/github-quickstart.gif)

1. Open this repository on GitHub and copy the install command you prefer.
2. Run it in your terminal or agent workspace.
3. Start rough requests with `$cover-tips`; after confirming a style, use the matching `cover-X` for one cover or one of the four `cover-X-with-docs` skills for an article visual package.

## GitHub Showcases

![GitHub showcases preview](assets/style-showcases/github-showcases.gif)

## Release Model

### Independent single-cover skills

Every `cover-X` is an independent install unit. It accepts a single-cover request directly and does not require another skill to be installed or called first. The current base inventory has 12 skills:

| Skill | Visual style | Best for |
|---|---|---|
| `cover-black-white-minimal` | Black-white minimal, Swiss grid, restrained editorial | Concept covers, serious essays, portfolio covers |
| `cover-trendy-color-poster` | Trendy high-impact color poster | Product covers, launch posters, platform covers |
| `cover-budapest-poster` | Retro Central European cinematic Budapest poster | Theatre, tram, station, archive, postcard concepts |
| `cover-editorial-collage` | Torn-paper editorial collage | Satire, conflict, social commentary, magazine covers |
| `cover-tea-oriental` | Oriental tea aesthetic, Song literati, character-as-image | Cultural posters, invitations, infographics, PPT covers |
| `cover-giant-perspective-poster` | Giant Chinese perspective type, high-contrast cinematic/esports key visual | Movie posters, sports brands, esports visuals, viral covers |
| `cover-cream-orange-knowledge-poster` | Cream-orange knowledge poster and technical infographic | Agents, system architecture, feedback loops, technical explainers |
| `cover-sketch-knowledge-poster` | Hand-drawn knowledge maps and paper sketches | Knowledge maps, tutorials, product education posters |
| `cover-3d-eye` | Black grid, neon terminal green, privacy/offline/local ownership | Local AI tutorials, Ollama, privacy-first posters |
| `cover-midnight-studio` | Cinematic midnight AI creator workspace | Indie hackers, AI workflows, technology headers |
| `cover-light-product` | Light product aesthetic, cream base, warm-cool accents | AI products, SaaS, agent workspaces, launch visuals |
| `cover-mckinsey-briefing-style` | Consulting briefing, strategy frameworks, strict grids | Strategy reports, boardroom briefings, PPT covers |

Base skills support `template | prompt | all`; when `--out-type` is omitted, the default is `template`. Direct image generation requires an explicit image request; ordinary calls return reviewable templates or prompts first.

### Article visual skills: only four with-docs siblings

An article visual package is not a hidden mode inside a base skill. It is an independent skill in the same visual family. The current release contains exactly these four pairs:

| Base style | Independent article visual skill |
|---|---|
| `cover-3d-eye` | `cover-3d-eye-with-docs` |
| `cover-cream-orange-knowledge-poster` | `cover-cream-orange-knowledge-poster-with-docs` |
| `cover-light-product` | `cover-light-product-with-docs` |
| `cover-sketch-knowledge-poster` | `cover-sketch-knowledge-poster-with-docs` |

Each `with-docs` skill can be installed and called independently. It does not invoke its base `cover-X`, a universal planner, or an illustration skill at runtime. A base style without a sibling still supports a single cover, but it is never silently replaced with another article style.

The shared `with-docs` contract is:

- Article sources are limited to pasted content, Markdown files, or plain-text files. DOCX and PDF are not included yet.
- Article sources are read-only. Output is conversational by default and is written to a file only when the user explicitly provides an output path.
- `template | brief | prompt | all` are supported; the default is `brief`.
- The default is 1 cover plus 3 inline visuals. The inline count can be explicitly set to 1–5; the cover is counted separately.
- Every inline visual is bound to a concrete section or paragraph, an insertion position, a reading problem, an aspect ratio, and prompt constraints.
- Existing image references are read to avoid duplicate topics. Missing, empty, or unreadable article input fails clearly and never falls back to a base cover.

## The Two-Stage CoverTips Flow

`cover-tips` is an optional style and asset-scope selector. It does not own concrete visual rules and does not replace the target skill for an article package.

1. **Confirm the visual style first.** If no style is specified, give 1–3 candidates based on the request and wait for confirmation; never guess silently. If the user already named a style, confirm that style.
2. **Confirm the asset scope second.** Choose either “single cover” or “cover + inline visuals.” A single cover routes to the corresponding `cover-X`; an article package shows only the four available `with-docs` styles listed above.

For example:

```text
$cover-tips
Topic: How to run an AI model locally
Asset scope: recommend a style first
```

After the style and scope are confirmed, hand an article package to the concrete sibling:

```text
$cover-3d-eye-with-docs
Article source: /path/to/article.md
Output type: brief
Inline visual count: 3
```

For one cover only, call the base skill directly:

```text
$cover-3d-eye
Output type: template
Topic: local AI
Use case: tutorial cover
```

CoverTips' own cover-organizing mode defaults to a template. Use `--out-type prompt` for a generic image prompt and `--out-type all` for both.

## Article Visual Package Examples

All four article skills use the same asset relationship: one `cover` representing the article thesis, plus `article-inline` visuals bound to sections or paragraphs and concrete reading problems. The normal deliverable is a brief; no image-generation tool is called unless the user explicitly asks for images.

```text
$cover-sketch-knowledge-poster-with-docs
Article source: /path/to/tutorial.md
Output type: brief
Asset scope: cover + inline visuals
```

```text
$cover-light-product-with-docs
Article source: pasted article content
Output type: all
Inline visual count: 4
```

```text
$cover-cream-orange-knowledge-poster-with-docs
Article source: /path/to/architecture.txt
Output type: prompt
```

```text
$cover-3d-eye-with-docs
Article source: /path/to/local-ai.md
Output type: brief
```

## Install

Full and single-skill installs consume the same generated inventory:

- Full installation contains 12 base `cover-X` skills, four `cover-X-with-docs` skills, and `cover-tips`: 17 independent skills total.
- Any one skill can be installed independently. Installing a base skill does not implicitly install its `with-docs` sibling, and vice versa.
- `cover-tips` can also be installed alone, although it needs a concrete style skill to complete a route.

### CLI Plugin Marketplace

Add the marketplace first, then install one skill as needed.

Codex CLI:

```text
codex plugin marketplace add imartinstudio/cover-prompt-skills
codex plugin add cover-3d-eye-with-docs@cover-prompt-skills
```

Claude CLI:

```text
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-3d-eye-with-docs@cover-prompt-skills
```

Marketplace plugins are independent. For a full install, use the installer below or select all 17 skills in the interactive `npx skills add` flow; for a single install, select only the target skill.

After updating an installed plugin, refresh or re-enable it, or restart the agent, so it loads the newest version instead of a cached copy.

### npx

```bash
npx skills add imartinstudio/cover-prompt-skills
```

In the interactive UI, select all skills or only one base skill, one `with-docs` sibling, or `cover-tips`.

### curl

Full installation:

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

Single-skill installation:

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash -s -- cover-3d-eye-with-docs
```

Skills are installed as standalone `SKILL.md` files. The script defaults to `~/.shared-skills`; Codex / Agents users can select another target directory:

```bash
COVER_SKILLS_TARGET=~/.agents/skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### Local development

```bash
cd cover-prompt-skills
./install.sh                              # install all 17 skills
./install.sh cover-3d-eye-with-docs       # install one
```

Local installation creates symlinks from the repository's skill directories into the target directory. The installer does not use the network or generate images.

## Migration Notes

- Migrate old `article-visual-planner` calls to two steps: use `CoverTips` to confirm the style and asset scope, then call an actual `cover-X-with-docs` sibling; a concrete sibling can also be called directly.
- If the old planner targeted a style without a `with-docs` sibling, that style currently supports a single cover only; it is not silently replaced.
- `cover-pixel-avatar` has left the current release scope and no longer appears in the skills table, routes, marketplace, install indexes, or install commands.
- `docs/source-prompts/` contains historical source prompts and requirement evidence only. Names appearing there are not current release entries or installation sources.

## Repository Principles

- Keep each plugin minimal: one `SKILL.md` under `skills/`, plus one manifest for Claude Code and one for Codex.
- Base cover skills and article visual skills are independently installed, called, and versioned; neither is an implicit runtime dependency of the other.
- When a shared visual family changes, maintain both its base and `with-docs` skill; changes limited to article orchestration affect only the relevant `with-docs` skill.
- Do not create a `with-docs` sibling for a style without confirmed article-visual capability, and do not create `cover-tips-with-docs`.
- Article packages must use `cover` and `article-inline` asset types and preserve section binding and the reading problem.
