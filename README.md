[English](README.en.md) | 中文

---

# 封面优先的视觉提示词技能

面向 AI agent 和图像生成工作流的可复用视觉提示词技能。`cover-X` 是可独立安装、可独立调用的单张封面技能；只有四个已确认适合文章配图的风格另有独立的 `cover-X-with-docs` sibling。`cover-tips` 是可选的两阶段选择器，不拥有具体视觉风格规则，也不再由通用 planner 统筹所有文章配图。

兼容 Claude Code、Codex、Gemini CLI、Cursor，以及任何支持 `SKILL.md` 的 agent。

## GitHub 快速上手

![GitHub 快速上手教程](assets/quickstart/github-quickstart.gif)

1. 在 GitHub 打开本仓库，复制你偏好的安装命令。
2. 在终端或 agent 工作区执行安装命令。
3. 粗略需求先调用 `$cover-tips`；确定风格后，单张封面调用对应 `cover-X`，文章视觉包调用对应的四个 `cover-X-with-docs` 之一。

## GitHub 展示

![GitHub showcases 展示](assets/style-showcases/github-showcases.gif)

## 发布模型

### 独立基础封面技能

每个 `cover-X` 都是独立安装单元，可以直接接收单张封面需求，不要求先安装或调用其他技能。当前基础库存为 13 个：

| 技能 | 视觉风格 | 适用场景 |
|---|---|---|
| `cover-black-white-minimal` | 黑白极简、瑞士网格、克制编辑风 | 概念封面、严肃文章、作品集封面 |
| `cover-trendy-color-poster` | 潮流高冲击彩色海报 | 产品封面、发布海报、平台封面 |
| `cover-budapest-poster` | 复古中欧电影感、布达佩斯海报风 | 剧院、电车、车站、档案、明信片概念 |
| `cover-editorial-collage` | 撕纸编辑拼贴 | 讽刺、冲突、社会评论、杂志拼贴封面 |
| `cover-tea-oriental` | 茶风格东方美学、宋代文人气、汉字成像 | 文化海报、邀请函、信息图、PPT 封面 |
| `cover-giant-perspective-poster` | 巨型中文透视标题、强对比撞色、电影/电竞主视觉 | 电影海报、运动品牌、电竞视觉、传播封面 |
| `cover-cream-orange-knowledge-poster` | 奶油橙知识海报、技术信息图、AI 工程图解 | Agent、系统架构、反馈循环、技术解释封面 |
| `cover-sketch-knowledge-poster` | 手绘知识图谱、白板框架、黑橙纸张素描 | 知识地图、教程封面、产品教育海报 |
| `cover-3d-eye` | 黑网格、霓虹绿终端、隐私/离线/本地掌控 | 本地 AI 教程、Ollama、隐私优先海报 |
| `cover-midnight-studio` | 深夜 AI 创作者工作室、电影感工作站 | 独立开发、AI 工作流、科技头图 |
| `cover-light-product` | 浅色产品、奶油底、暖冷双强调色 | AI 产品、SaaS、Agent workspace、发布视觉 |
| `cover-anthropic-research` | 研究编辑极简、纯色留白、衬线标题、抽象线稿 | AI 研究报告、工具教程、知识封面、产品概念 |
| `cover-mckinsey-briefing-style` | 咨询简报、战略框架、留白和严格网格 | 战略报告、董事会简报、PPT 封面 |

基础技能支持 `template | prompt | all`，省略 `--out-type` 时默认输出 `template`。需要直接生成图片时，必须明确提出生图请求；普通调用先返回可审阅的模板或提示词。

### 文章配图技能：只有四个 with-docs sibling

文章视觉包不是基础技能的隐藏模式，而是同风格的独立技能。当前发布库存严格只有以下四个：

| 基础风格 | 独立文章配图技能 |
|---|---|
| `cover-3d-eye` | `cover-3d-eye-with-docs` |
| `cover-cream-orange-knowledge-poster` | `cover-cream-orange-knowledge-poster-with-docs` |
| `cover-light-product` | `cover-light-product-with-docs` |
| `cover-sketch-knowledge-poster` | `cover-sketch-knowledge-poster-with-docs` |

每个 `with-docs` 都可以独立安装和调用，运行时不依赖基础 `cover-X`、通用 planner 或 illustration 技能。没有对应 sibling 的基础风格仍然可以做单张封面，但不会被静默替换成另一种文章风格。

`with-docs` 的共同契约：

- 文章源只接受用户粘贴的文章内容、Markdown 文件或纯文本文件；DOCX 和 PDF 暂不纳入。
- 文章源只读；默认在对话中输出，只有用户明确提供输出路径时才写文件。
- 支持 `template | brief | prompt | all`，默认 `brief`。
- 默认输出 1 张封面 + 3 张正文配图；正文图数量可明确指定为 1–5 张，封面另计。
- 每张正文图必须绑定具体章节或段落、建议插入位置、要解决的阅读问题、画幅比例和提示词约束。
- 会读取已有图片引用以避免重复主题；缺少文章、文章为空或无法读取时明确失败，不自动降级到基础封面。

## CoverTips 两阶段流程

`cover-tips` 是可选的风格与资产范围选择器。它不拥有具体风格规则，也不直接替代目标技能完成文章视觉包。

1. **先确认视觉风格。** 用户未指定风格时，先根据需求给出 1–3 个候选并等待确认；不能静默猜测。用户已明确风格时直接确认该风格。
2. **再确认资产范围。** 选择“单张封面”或“封面 + 正文配图”。单张封面路由到对应的 `cover-X`；文章视觉包只显示上表中的四个可用 `with-docs` 风格。

例如：

```text
$cover-tips
主题：如何在本地运行一个 AI 模型
资产范围：先推荐风格
```

确认风格和范围后，文章视觉包应转交给具体 sibling：

```text
$cover-3d-eye-with-docs
文章来源：/path/to/article.md
输出类型：brief
正文配图数量：3
```

如果用户只要一张封面，则直接调用基础技能：

```text
$cover-3d-eye
输出类型：template
主题词：本地 AI
用途：教程封面
```

CoverTips 没有自己的输出模式，也不生成通用提示词或中间模板；完成两项确认后，它会把原始请求和确认结果交给目标 `cover-X` 或 `cover-X-with-docs` 技能，由目标技能负责输出。

## 文章视觉包示例

四个文章技能的目标都是同一组资产关系：一张代表整篇文章论点的 `cover`，以及绑定章节或段落、解释具体阅读问题的 `article-inline` 正文图。常规输出是 brief，不会在没有明确生图请求时调用生图工具。

```text
$cover-sketch-knowledge-poster-with-docs
文章来源：/path/to/tutorial.md
输出类型：brief
资产范围：封面 + 正文配图
```

```text
$cover-light-product-with-docs
文章来源：用户粘贴的文章正文
输出类型：all
正文配图数量：4
```

```text
$cover-cream-orange-knowledge-poster-with-docs
文章来源：/path/to/architecture.txt
输出类型：prompt
```

```text
$cover-3d-eye-with-docs
文章来源：/path/to/local-ai.md
输出类型：brief
```

## 安装

全量安装和单个安装都使用同一份生成库存：

- 全量安装包含 13 个基础 `cover-X`、四个 `cover-X-with-docs` 和 `cover-tips`，共 18 个独立技能。
- 单个技能可以独立安装；安装基础版不会隐式安装对应的 `with-docs`，反之亦然。
- `cover-tips` 也是可单独安装的技能，只是没有具体风格技能时不能完成目标路由。

### CLI Plugin Marketplace

先添加 marketplace，再按需安装一个技能：

Codex CLI：

```text
codex plugin marketplace add imartinstudio/cover-prompt-skills
codex plugin add cover-3d-eye-with-docs@cover-prompt-skills
```

Claude CLI：

```text
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-3d-eye-with-docs@cover-prompt-skills
```

marketplace 的插件彼此独立。需要全量安装时，可使用下面的安装器或在 `npx skills add` 的交互选择中选中全部 18 个技能；需要单个安装时选择目标技能即可。

更新已安装插件后，需要刷新/重新启用插件，或重启对应 agent，让它加载最新版本而不是旧缓存。

### npx

```bash
npx skills add imartinstudio/cover-prompt-skills
```

在交互界面中选择全部技能，或只选择一个基础技能、一个 `with-docs` sibling 或 `cover-tips`。

### curl

全量安装：

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

单个安装：

```bash
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash -s -- cover-3d-eye-with-docs
```

技能会以独立 `SKILL.md` 文件安装到目标目录。脚本默认使用 `~/.shared-skills`；Codex / Agents 用户可指定目标目录：

```bash
COVER_SKILLS_TARGET=~/.agents/skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### 本地开发安装

```bash
cd cover-prompt-skills
./install.sh                              # 全量安装 18 个技能
./install.sh cover-3d-eye-with-docs       # 单个安装
```

本地安装会把仓库中的技能目录软链到目标目录，适合修改仓库并在 agent 中测试。安装器不会联网，也不会执行实际生图。

## 迁移说明

- 旧的 `article-visual-planner` 调用应迁移为两步：先用 `CoverTips` 确认风格和资产范围，再调用实际存在的 `cover-X-with-docs`；也可以直接调用具体 sibling。
- 如果旧 planner 指向的风格没有 `with-docs` sibling，当前只支持该风格的单张封面，不自动替换风格。
- `cover-pixel-avatar` 已退出本仓库当前发布范围，不再出现在技能表、路由、marketplace、安装索引或安装命令中。
- `docs/source-prompts/` 只保存历史源提示词和需求证据；其中出现的旧名称不是当前发布入口或安装库存。

## 仓库原则

- 每个插件保持精简：一个 `SKILL.md` 置于 `skills/` 下，Claude Code 和 Codex 各一个 manifest。
- 基础封面技能与文章配图技能独立安装、独立调用、独立版本化；两者不构成运行时隐式依赖。
- 共享视觉风格变更时同步维护对应的基础版和 `with-docs` 版；文章编排变化只影响对应的 `with-docs` 版。
- 不为没有确认文章配图能力的风格创建 `with-docs` sibling，也不创建 `cover-tips-with-docs`。
- 文章视觉包必须使用 `cover` 与 `article-inline` 资产类型，并保留章节绑定和阅读问题。
