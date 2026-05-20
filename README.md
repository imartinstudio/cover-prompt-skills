[English](#cover-prompt-skills) | [中文](#封面提示词技能)

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

---

# 封面提示词技能

面向 AI agent 和图像生成工作流的可复用封面提示词技能。

兼容 Claude Code、Codex、Gemini CLI、Cursor，以及任何支持 SKILL.md 的 agent。

## 技能列表

| 技能 | 风格 | 适用场景 |
|---|---|---|
| `cover-tips` | 风格化提示词组织器 | 将用户粗糙的封面想法转化为模板或通用图像提示词 |
| `cover-black-white-minimal` | 黑白极简、瑞士网格、克制编辑风 | 高级概念封面、严肃文章、作品集封面 |
| `cover-trendy-color-poster` | 潮流高冲击彩色海报 | 产品封面、电商封面、发布海报 |
| `cover-budapest-poster` | 复古欧洲电影感、布达佩斯海报风 | 优雅电影感封面、明信片式概念图、建筑立面构图 |
| `cover-editorial-collage` | 撕纸编辑拼贴 | 讽刺、冲突、社会评论、杂志拼贴封面 |

## 推荐使用方式

以 `cover-tips` 为入口：

```text
$cover-tips 撕纸剪贴

主题：可以洗稿，但不能被洗脑
副标题：AI 时代的内容判断力
用途：X封面
情绪：讽刺、冲突
```

默认输出为模板：

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

需要生成提示词时：

```text
$cover-tips 潮流彩色 提示词

美区苹果 App Store 礼品卡，2-100 面值，现货秒发，库存充足。
```

## 安装

四种方式任选。

### Plugin Marketplace

```
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-editorial-collage@cover-prompt-skills
```

适用于 Claude Code 和 Codex。

### npx

```
npx skills add imartinstudio/cover-prompt-skills
```

交互式选择要安装的技能。支持 Claude Code、Codex、Cursor、Gemini CLI、Windsurf 等 40+ 个 agent。

### curl

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

安装单个技能：

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash -s -- cover-editorial-collage
```

技能以独立 `SKILL.md` 文件下载到 `~/.shared-skills`。自定义目标目录：

```bash
COVER_SKILLS_TARGET=~/your-agent-skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### 本地开发安装

```bash
cd cover-prompt-skills
./install.sh                              # 安装全部（symlink）
./install.sh cover-editorial-collage      # 安装单个
```

`cover-tips` 是导航技能，随完整包安装，不可单独安装 —— 它依赖具体的封面风格技能。

## 仓库原则

- 每个插件保持精简：一个 `SKILL.md` 置于 `skills/` 下，Claude Code 和 Codex 各一个 manifest。
- 默认不包含特定平台的 agent 元数据。
- 保持提示词通用，除非用户明确要求特定平台的变体。
- 使用 `cover-` 作为封面生成技能的命名前缀。

## 许可证

MIT
