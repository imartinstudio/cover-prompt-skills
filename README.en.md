[English](README.en.md) | [中文](README.md)

---

# Cover-First Visual Prompt Skills

Reusable visual prompt skills for AI agents and image-generation workflows. The project keeps the existing `cover-*` cover line backward compatible while adding `illustration-*` illustration skills and optional coordinated visual kits.

Compatible with Claude Code, Codex, Gemini CLI, Cursor, and any agent that supports SKILL.md.

## GitHub Quick Start

![GitHub quick start tutorial](assets/quickstart/github-quickstart.gif)

1. Open this repository on GitHub and copy the install command you prefer.
2. Run the command in your terminal or agent workspace.
3. Use `$cover-tips` as the daily cover entry point, or call a specific `cover-*`, `illustration-*`, or `*-kit` skill directly.

## GitHub Showcases

![GitHub showcases preview](assets/style-showcases/github-showcases.gif)

## Skills

| Skill | Style | Best For |
|---|---|---|
| `cover-tips` | Style-specific prompt organizer | Turn rough user content into a template or generic image prompt |
| `cover-black-white-minimal` | Black-white minimal, Swiss grid, restrained editorial | Premium concepts, serious essays, portfolio covers |
| `cover-trendy-color-poster` | Trendy high-impact color poster | Product covers, marketplace covers, launch posters |
| `cover-budapest-poster` | Retro Central European cinematic, Budapest-style poster | Theatre, tram, station, bathhouse, archive, postcard concepts |
| `cover-editorial-collage` | Torn-paper editorial collage | Satire, conflict, social commentary, magazine collage covers |
| `cover-tea-oriental` | Oriental tea aesthetic, Song literati, character-as-image | Cultural posters, invitations, infographics, PPT covers |
| `cover-giant-perspective-poster` | Giant Chinese perspective type, high-contrast clash, cinematic/esports KV | Movie posters, sports brand, esports key visuals, viral covers |
| `cover-sketch-knowledge-poster` | Hand-drawn knowledge maps, whiteboard frameworks, black/orange paper sketch | Knowledge map covers, tutorial covers, product education posters, X/WeChat covers |
| `cover-3d-eye` | 3D Eye style, black grid, neon green, privacy/offline/ownership mood | Local AI tutorial covers, Ollama/local model covers, privacy-first AI posters, black-green terminal covers |
| `cover-midnight-studio` | Midnight AI creator studio, cinematic workstation, multi-monitor workflow | Indie hackers, build-in-public, AI workflow, premium tech headers |
| `cover-pixel-avatar` | Retro 8-bit pixel avatars, high-saturation clash colors, solid backgrounds | Uploaded image to abstract pixel avatar, social profile picture, chibi pixel IP |
| `cover-light-product` | Light product aesthetic, cream base, warm-cool dual color, SaaS Hero look | AI product covers, SaaS brand headers, product launch visuals, Agent workspace covers |
| `cover-mckinsey-briefing-style` | McKinsey-style executive briefing, consulting report, strategy frameworks | Strategy briefing covers, consulting reports, PPT covers, business analysis visuals |
| `illustration-light-product` | Light product illustrations, refined UI modules, Agent workflow diagrams | AI product feature explanations, SaaS tutorial images, workflow diagrams, product docs illustrations |
| `illustration-sketch-ui` | Hand-drawn UI product education illustrations, black/orange arrows and callouts | Tutorial images, product explanation graphics, feature walkthroughs, X article illustrations |
| `illustration-3d-eye` | 3D Eye illustrations, black grid boards, neon green diagrams, terminal UI cards | Local AI tutorial images, hardware maps, quantization charts, privacy flows, local vs cloud comparisons |
| `light-product-kit` | Light product visual kit | Organize one light product cover brief plus multiple product illustration briefs in the same visual system |
| `sketch-knowledge-kit` | Sketch knowledge visual kit | Organize one cover brief plus multiple illustration briefs in the same visual system |
| `3d-eye-kit` | 3D Eye visual kit | Organize one 3D Eye cover brief plus multiple tutorial illustration briefs in the same visual system |

## Style Preview

### `cover-black-white-minimal`

![Black-White Minimal style showcase](assets/style-showcases/cover-black-white-minimal.png)

### `cover-trendy-color-poster`

![Trendy Color Poster style showcase](assets/style-showcases/cover-trendy-color-poster.png)

### `cover-giant-perspective-poster`

![Giant Perspective Poster style showcase](assets/style-showcases/cover-giant-perspective-poster.png)

### `cover-midnight-studio`

![Midnight Studio style showcase](assets/style-showcases/cover-midnight-studio.png)

### `cover-light-product`

![Light Product style showcase](assets/style-showcases/cover-light-product.png)

### `cover-editorial-collage`

![Editorial Collage style showcase](assets/style-showcases/cover-editorial-collage.png)

### `cover-tea-oriental`

![Tea Oriental style showcase](assets/style-showcases/cover-tea-oriental.png)

## Recommended Daily Use

Use `cover-tips` as the daily entry point when you have rough content and a rough style direction. It cleans up the brief, extracts fields, chooses the matching concrete style skill, and returns a ready-to-use invocation template by default.

Basic formula:

```text
$cover-tips + style + --out-type template|prompt|all + user content
```

Example:

```text
$cover-tips 撕纸剪贴

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

Default output is a template. This is the same as `--out-type template`, and is recommended when you want to review or edit structured fields before generating the final image:

```text
使用 $cover-editorial-collage 生成一张封面
主题词：提示词
副标题：好的提示，不只是命令，更是设计
画幅比例：5:2
语言：中文
用途：X 封面
情绪倾向：讽刺 / 冲突 / 街头 / 复古 / 观点感
禁用元素：机器人脸、蓝紫霓虹、廉价科技感、PPT 布局、干净矩形堆叠、低质脏乱朋克、不可读文字
```

Ask for a final image prompt when the brief is already clear:

```text
$cover-tips 潮流彩色 --out-type prompt

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

Use `--out-type all` when you need both the structured template and the final image prompt.

Supported style aliases:

| User style input | Routed skill |
|---|---|
| `黑白极简` / `黑白` / `极简` / `minimal` / `bw` | `$cover-black-white-minimal` |
| `潮流彩色` / `彩色` / `高冲击` / `trendy` / `color` | `$cover-trendy-color-poster` |
| `巨型透视` / `透视标题` / `电影海报风` / `电竞主视觉` / `perspective` | `$cover-giant-perspective-poster` |
| `手绘知识图谱` / `知识图谱` / `知识地图` / `白板框架` / `sketch knowledge` | `$cover-sketch-knowledge-poster` |
| `本地AI` / `3D Eye` / `黑绿终端` / `local AI` / `terminal poster` | `$cover-3d-eye` |
| `深夜工作室` / `深夜工作室风` / `AI工程师空间` / `indie hacker` / `midnight studio` | `$cover-midnight-studio` |
| `像素头像` / `像素` / `8-bit头像` / `pixel avatar` / `Q版像素头像` | `$cover-pixel-avatar` |
| `浅色产品` / `浅色产品风` / `SaaS产品` / `light product` / `奶油白` | `$cover-light-product` |
| `麦肯锡简报风` / `麦肯锡风` / `咨询简报` / `战略报告` / `consulting briefing` | `$cover-mckinsey-briefing-style` |
| `布达佩斯` / `Budapest` / `复古欧洲` / `电影感` / `明信片` | `$cover-budapest-poster` |
| `撕纸剪贴` / `剪贴` / `拼贴` / `collage` / `editorial collage` | `$cover-editorial-collage` |
| `茶风格` / `茶` / `东方美学` / `宋代美学` / `汉字成像` | `$cover-tea-oriental` |

Call a concrete style skill directly when you already know the exact style and do not need `cover-tips` to reorganize the brief:

```text
$cover-black-white-minimal --out-type prompt
主题：长期主义 副标题：在即时反馈时代重新理解耐心 画幅比例：4:3 用途：文章封面
```

You can also skip template generation entirely and ask a concrete skill to generate the final cover from a natural-language brief:

```text
$cover-editorial-collage 直接生成一张 5:2 的 X 封面，主题是“提示词”，副标题是“好的提示，不只是命令，更是设计”。整体要撕纸剪贴、杂志感、讽刺一点，不要机器人脸和蓝紫霓虹。
```

Use this direct generation path when the style is clear and you do not need to inspect intermediate fields.

## Cover + Illustration Kits

`cover-*` names are for cover/poster outputs. `illustration-*` names are for inline illustrations, tutorial images, and product explanation graphics. They can share the same visual family while keeping separate invocation surfaces.

The sketch knowledge visual family includes:

```text
$cover-sketch-knowledge-poster     # Overview cover / knowledge map poster
$illustration-sketch-ui            # Product UI tutorial illustration / feature explanation image
$sketch-knowledge-kit              # Coordinated brief organizer
```

The light product visual family includes:

```text
$cover-light-product               # AI product cover / SaaS Hero / Agent workspace header
$illustration-light-product        # Product feature explanation illustration / Agent workflow diagram
$light-product-kit                 # Coordinated light product cover + illustration brief organizer
```

The 3D Eye visual family includes:

```text
$cover-3d-eye           # Local AI tutorial cover / black-green terminal poster
$illustration-3d-eye    # Local AI tutorial illustration / hardware, quantization, privacy, flow diagram
$3d-eye-kit             # Coordinated 3D Eye cover + illustration brief organizer
```

When you need one article or tutorial to have a cover and several matching illustrations, use:

```text
$sketch-knowledge-kit
主题：Claude Projects tutorial
封面用途：X article cover
插图用途：tutorial illustrations
插图数量：3
语言：中文
内容结构：entry point, create project, add context
```

When you need a light product visual package for an AI product article, SaaS tutorial, or Agent workflow explanation, use:

```text
$light-product-kit
主题：Codex automation workflow
封面用途：X article cover
插图用途：tutorial illustrations
插图数量：3
语言：中文
产品/场景：Codex Agent workspace
内容结构：create task, call tools, verify result
```

When you need a black-green terminal visual package for local AI, Ollama, offline models, privacy, hardware, or quantization tutorials, use:

```text
$3d-eye-kit
主题：14 steps to run your own local AI
封面用途：X article cover
配图用途：tutorial illustrations
配图数量：5
语言：mixed Chinese-English
核心钩子：No cloud, no filters, no one watching
内容结构：whole flow, local vs cloud, hardware match, quantization choice, common mistakes
连续角色：blue-white hand-drawn 3D Eye mascot across the series, switching between waving, running, pointing, skill-card, and thumbs-up poses
```

Recommended workflow:

1. Start with `$cover-tips <style>` for rough ideas.
2. Use the returned template to confirm title, subtitle, ratio, language, use case, mood, and banned elements.
3. Switch to `--out-type prompt` or `--out-type all` when you need reusable prompt text.
4. Use `$cover-*` followed by natural-language instructions when you want to skip the template and generate the final cover immediately.
5. Call `$illustration-*` directly when you need inline/tutorial illustrations.
6. Call `$sketch-knowledge-kit` when you need coordinated hand-drawn knowledge cover + illustration briefs.
7. Call `$light-product-kit` when you need coordinated light product cover + product illustration briefs.
8. Call `$3d-eye-kit` when you need coordinated 3D Eye cover + tutorial illustration briefs.

## Install

Four ways to install.

### CLI Plugin Marketplace

Codex CLI:

```
codex plugin marketplace add imartinstudio/cover-prompt-skills
codex plugin add cover-editorial-collage@cover-prompt-skills
```

Claude CLI:

```
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-editorial-collage@cover-prompt-skills
```

Use the command variant for your CLI. In Codex CLI, add the plugin marketplace repository, then install the skill/plugin you need. In Claude CLI, use the `/plugin` slash commands.

After updating an already-installed plugin, refresh/re-enable the plugin or restart the agent so it loads the newest plugin version instead of the cached version.

### npx

```
npx skills add imartinstudio/cover-prompt-skills
```

Pick the skills you want interactively. Works in Claude Code, Codex, Cursor, Gemini CLI, Windsurf, and 40+ other agents.

### curl

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

Install a single skill:

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash -s -- cover-editorial-collage
```

Skills are downloaded as standalone `SKILL.md` files to the target directory. The script defaults to `~/.shared-skills`; different agents may use different skill directories, and Codex / Agents users can usually set `~/.agents/skills` or `~/.codex/skills`:

```bash
COVER_SKILLS_TARGET=~/.agents/skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### Local development

```bash
cd cover-prompt-skills
./install.sh                              # install all (symlinks)
./install.sh cover-editorial-collage      # install one
```

Local development install creates symlinks from this repository's skill directories into the target directory, which is useful when editing the repository and testing in an agent.

`cover-tips` is a navigator skill. It is installed with the full package, but cannot be installed alone — it depends on concrete cover style skills.

## Repository Principles

- Keep each plugin minimal: one `SKILL.md` under `skills/`, one manifest each for Claude Code and Codex.
- Do not include provider-specific agent metadata by default.
- Keep prompts generic unless a user explicitly asks for a provider-specific variant.
- Use `cover-` as the naming prefix for cover/poster skills.
- Use `illustration-` as the naming prefix for illustration skills.
- Use a neutral `*-kit` name for multi-asset coordination skills that are not themselves a single cover.

## License

MIT
