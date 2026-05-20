# Cover Prompt Skills

Reusable cover prompt skills for AI agents and image-generation workflows.

This repository contains plain Markdown instruction files. They are not tied to a specific model provider, agent runtime, or image tool.

## Skills

| Skill | Style | Best For |
|---|---|---|
| `cover-tips` | Style-specific prompt organizer | Turn rough user content into a template or generic image prompt |
| `cover-black-white-minimal` | Black-white minimal, Swiss grid, restrained editorial | Premium concepts, serious essays, portfolio covers |
| `cover-trendy-color-poster` | Trendy high-impact color poster | Product covers, marketplace covers, launch posters |
| `cover-budapest-poster` | Retro European cinematic, Budapest-style poster | Elegant cinematic covers, postcard-like concepts, facade compositions |
| `cover-editorial-collage` | Torn-paper editorial collage | Satire, conflict, social commentary, magazine collage covers |

## Recommended Daily Use

Use `cover-tips` as the entry point:

```text
$cover-tips 撕纸剪贴

主题：可以洗稿，但不能被洗脑
副标题：AI 时代的内容判断力
用途：X封面
情绪：讽刺、冲突
```

Default output is a template:

```text
使用 $cover-editorial-collage 生成一张封面
主题词：可以洗稿，但不能被洗脑
副标题：AI 时代的内容判断力
画幅比例：5:2
语言：中文
用途：X封面
情绪倾向：讽刺 / 冲突
禁用元素：机器人脸、蓝紫霓虹
```

Ask for a prompt when needed:

```text
$cover-tips 潮流彩色 提示词

美区苹果 App Store 礼品卡，2-100 面值，现货秒发，库存充足。
```

Ask for both when you want to inspect the structured template and the final prompt:

```text
$cover-tips 黑白极简 模版和提示词

苹果土耳其礼品卡 + Apple 苹果礼品卡 500 里拉，24小时自动发货，一次性卡密。
```

## Install

Fast install:

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

Install one concrete style skill:

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash -s -- cover-editorial-collage
```

`cover-tips` is a navigator skill. It is installed with the full package, but should not be installed by itself because it needs the concrete cover style skills to be useful.

By default, skills are linked into `~/.shared-skills`, and the repository is cloned or updated at `~/.cover-prompt-skills`.

If an old non-symlink skill directory already exists, the installer moves it to:

```text
~/.shared-skills/.cover-prompt-skills-backup/
```

Override the install target when your agent uses another skills directory:

```bash
COVER_SKILLS_TARGET=~/your-agent-skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

Use a custom repository URL or local clone path:

```bash
COVER_PROMPT_SKILLS_REPO=https://github.com/your-name/cover-prompt-skills.git \
COVER_PROMPT_SKILLS_HOME=~/.cover-prompt-skills \
curl -fsSL https://raw.githubusercontent.com/your-name/cover-prompt-skills/main/install.sh | bash
```

Manual install:

```bash
git clone https://github.com/imartinstudio/cover-prompt-skills.git
cd cover-prompt-skills
scripts/install.sh
```

Install one concrete style skill manually:

```bash
scripts/install.sh cover-editorial-collage
```

## Repository Principles

- Keep each skill directory minimal: `SKILL.md` only unless extra bundled resources are genuinely required.
- Do not include provider-specific agent metadata by default.
- Keep prompts generic unless a user explicitly asks for a provider-specific variant.
- Use `cover-` as the naming prefix for cover-generation skills.

## License

MIT
