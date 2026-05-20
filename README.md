[English](README.md) | [中文](README.zh-CN.md)

---

# Cover Prompt Skills

Reusable cover prompt skills for AI agents and image-generation workflows.

Compatible with Claude Code, Codex, Gemini CLI, Cursor, and any agent that supports SKILL.md.

## Skills

| Skill | Style | Best For |
|---|---|---|
| `cover-tips` | Style-specific prompt organizer | Turn rough user content into a template or generic image prompt |
| `cover-black-white-minimal` | Black-white minimal, Swiss grid, restrained editorial | Premium concepts, serious essays, portfolio covers |
| `cover-trendy-color-poster` | Trendy high-impact color poster | Product covers, marketplace covers, launch posters |
| `cover-budapest-poster` | Retro Central European cinematic, Budapest-style poster | Theatre, tram, station, bathhouse, archive, postcard concepts |
| `cover-editorial-collage` | Torn-paper editorial collage | Satire, conflict, social commentary, magazine collage covers |
| `cover-tea-oriental` | Oriental tea aesthetic, Song literati, character-as-image | Cultural posters, invitations, infographics, PPT covers |

## Style Preview

### `cover-black-white-minimal`

![Black-White Minimal style showcase](assets/style-showcases/cover-black-white-minimal.png)

### `cover-trendy-color-poster`

![Trendy Color Poster style showcase](assets/style-showcases/cover-trendy-color-poster.png)

### `cover-editorial-collage`

![Editorial Collage style showcase](assets/style-showcases/cover-editorial-collage.png)

### `cover-tea-oriental`

![Tea Oriental style showcase](assets/style-showcases/cover-tea-oriental.png)

## Recommended Daily Use

Use `cover-tips` as the entry point:

```text
$cover-tips 撕纸剪贴

生成一个模版
主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

Default output is a template:

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

Ask for a prompt when needed:

```text
$cover-tips 潮流彩色 提示词

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

## Install

Four ways to install.

### Plugin Marketplace

```
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-editorial-collage@cover-prompt-skills
```

Works in Claude Code and Codex.

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

Skills are downloaded as standalone `SKILL.md` files to `~/.shared-skills`. Override the target directory:

```bash
COVER_SKILLS_TARGET=~/your-agent-skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### Local development

```bash
cd cover-prompt-skills
./install.sh                              # install all (symlinks)
./install.sh cover-editorial-collage      # install one
```

`cover-tips` is a navigator skill. It is installed with the full package, but cannot be installed alone — it depends on concrete cover style skills.

## Repository Principles

- Keep each plugin minimal: one `SKILL.md` under `skills/`, one manifest each for Claude Code and Codex.
- Do not include provider-specific agent metadata by default.
- Keep prompts generic unless a user explicitly asks for a provider-specific variant.
- Use `cover-` as the naming prefix for cover-generation skills.

## License

MIT
