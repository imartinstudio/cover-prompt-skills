[English](README.en.md) | [中文](README.md)

---

# 封面优先的视觉提示词技能

面向 AI agent 和图像生成工作流的可复用视觉提示词技能。项目保持 `cover-*` 封面主线向后兼容，同时开始支持 `illustration-*` 插图能力和可选的配套视觉套件。

兼容 Claude Code、Codex、Gemini CLI、Cursor，以及任何支持 SKILL.md 的 agent。

## GitHub 快速上手

![GitHub 快速上手教程](assets/quickstart/github-quickstart.gif)

1. 在 GitHub 打开本仓库，复制你偏好的安装命令。
2. 在终端或 agent 工作区执行安装命令。
3. 日常封面使用以 `$cover-tips` 为入口，也可以直接调用具体的 `cover-*`、`illustration-*` 或 `*-kit` 技能。

## GitHub 展示

![GitHub showcases 展示](assets/style-showcases/github-showcases.gif)

## 技能列表

| 技能 | 风格 | 适用场景 |
|---|---|---|
| `cover-tips` | 风格化提示词组织器 | 将用户粗糙的封面想法转化为模板或通用图像提示词 |
| `cover-black-white-minimal` | 黑白极简、瑞士网格、克制编辑风 | 高级概念封面、严肃文章、作品集封面 |
| `cover-trendy-color-poster` | 潮流高冲击彩色海报 | 产品封面、电商封面、发布海报 |
| `cover-budapest-poster` | 复古中欧电影感、布达佩斯海报风 | 剧院、电车、车站、浴场、档案、明信片概念图 |
| `cover-editorial-collage` | 撕纸编辑拼贴 | 讽刺、冲突、社会评论、杂志拼贴封面 |
| `cover-tea-oriental` | 茶风格东方美学、宋代文人气、汉字成像 | 文化海报、邀请函、信息图、PPT封面 |
| `cover-giant-perspective-poster` | 巨型中文透视标题、高冲突撞色、电影/电竞主视觉 | 电影海报、运动品牌、电竞 KV、强传播封面 |
| `cover-sketch-knowledge-poster` | 手绘知识图谱、白板框架、黑橙双色、纸张质感 | 知识图谱封面、教程封面、产品教育海报、X/公众号封面 |
| `cover-midnight-studio` | 深夜工作室、AI 工程师空间、电影级多屏工作站 | 独立开发者、Build in Public、AI 工作流、科技品牌头图 |
| `cover-pixel-avatar` | 复古 8-bit 像素头像、高饱和撞色、纯色背景 | 上传图片转抽象像素头像、社交头像、Q版像素 IP |
| `cover-light-product` | 浅色产品风、奶油白基底、冷暖双色融合、SaaS Hero 美学 | AI 产品封面、SaaS 品牌头图、产品发布会视觉、Agent 工作区封面 |
| `cover-mckinsey-briefing-style` | 麦肯锡简报风、咨询报告、战略框架、董事会级版式 | 战略简报封面、咨询报告、PPT 封面、商业分析视觉 |
| `illustration-sketch-ui` | 手绘 UI 产品教育插图、黑橙双色、箭头讲解 | 教程配图、产品说明图、功能讲解图、X文章配图 |
| `sketch-knowledge-kit` | 手绘知识图谱视觉套件 | 一次组织封面 brief + 多张插图 brief，保持同一视觉系统 |

## 风格展示

### `cover-black-white-minimal`

![黑白极简风格展示](assets/style-showcases/cover-black-white-minimal.png)

### `cover-trendy-color-poster`

![潮流高冲击彩色海报风格展示](assets/style-showcases/cover-trendy-color-poster.png)

### `cover-giant-perspective-poster`

![巨型中文透视海报风格展示](assets/style-showcases/cover-giant-perspective-poster.png)

### `cover-midnight-studio`

![深夜工作室风格展示](assets/style-showcases/cover-midnight-studio.png)

### `cover-light-product`

![浅色产品风格展示](assets/style-showcases/cover-light-product.png)

### `cover-editorial-collage`

![撕纸编辑拼贴风格展示](assets/style-showcases/cover-editorial-collage.png)

### `cover-tea-oriental`

![茶风格东方美学展示](assets/style-showcases/cover-tea-oriental.png)

## 推荐使用方式

日常建议以 `cover-tips` 为入口，适合只有粗略主题、粗略风格方向、但还没有整理成标准字段的情况。它会先清理需求、提取字段、匹配具体封面风格技能，并默认输出可直接调用的模板。

基本公式：

```text
$cover-tips + 风格 + --out-type template|prompt|all + 用户内容
```

示例：

```text
$cover-tips 撕纸剪贴

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

默认输出为模板，等同于 `--out-type template`。当你希望先检查或修改结构化字段，再进入最终出图提示词时，推荐使用默认模式：

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

需求已经清楚、希望直接得到完整图像提示词时，使用 `--out-type prompt`：

```text
$cover-tips 潮流彩色 --out-type prompt

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

需要同时输出模板和完整提示词时，使用 `--out-type all`。

支持的风格别名：

| 用户输入风格 | 路由到的技能 |
|---|---|
| `黑白极简` / `黑白` / `极简` / `minimal` / `bw` | `$cover-black-white-minimal` |
| `潮流彩色` / `彩色` / `高冲击` / `trendy` / `color` | `$cover-trendy-color-poster` |
| `巨型透视` / `透视标题` / `电影海报风` / `电竞主视觉` / `perspective` | `$cover-giant-perspective-poster` |
| `手绘知识图谱` / `知识图谱` / `知识地图` / `白板框架` / `sketch knowledge` | `$cover-sketch-knowledge-poster` |
| `深夜工作室` / `深夜工作室风` / `AI工程师空间` / `indie hacker` / `midnight studio` | `$cover-midnight-studio` |
| `像素头像` / `像素` / `8-bit头像` / `pixel avatar` / `Q版像素头像` | `$cover-pixel-avatar` |
| `浅色产品` / `浅色产品风` / `SaaS产品` / `light product` / `奶油白` | `$cover-light-product` |
| `麦肯锡简报风` / `麦肯锡风` / `咨询简报` / `战略报告` / `consulting briefing` | `$cover-mckinsey-briefing-style` |
| `布达佩斯` / `Budapest` / `复古欧洲` / `电影感` / `明信片` | `$cover-budapest-poster` |
| `撕纸剪贴` / `剪贴` / `拼贴` / `collage` / `editorial collage` | `$cover-editorial-collage` |
| `茶风格` / `茶` / `东方美学` / `宋代美学` / `汉字成像` | `$cover-tea-oriental` |

如果你已经确定具体风格，并且不需要 `cover-tips` 帮你重组内容，可以直接调用具体技能：

```text
$cover-black-white-minimal --out-type prompt
主题：长期主义 副标题：在即时反馈时代重新理解耐心 画幅比例：4:3 用途：文章封面
```

也可以完全跳过模板生成，直接用具体技能加用户说明生成最终封面：

```text
$cover-editorial-collage 直接生成一张 5:2 的 X 封面，主题是“提示词”，副标题是“好的提示，不只是命令，更是设计”。整体要撕纸剪贴、杂志感、讽刺一点，不要机器人脸和蓝紫霓虹。
```

当风格已经明确、且不需要检查中间字段时，推荐使用这种直接生成方式。

## 封面 + 插图配套

`cover-*` 只表示封面或海报类产物，`illustration-*` 表示正文插图、教程配图、产品说明图。二者可以共享同一个视觉家族，但调用面保持分离。

手绘知识图谱视觉家族包含：

```text
$cover-sketch-knowledge-poster     # 总览封面 / 知识图谱海报
$illustration-sketch-ui            # 产品 UI 教程插图 / 功能讲解图
$sketch-knowledge-kit              # 配套 brief 编排入口
```

当你要为一篇文章或教程同时准备封面和多张配图时，使用：

```text
$sketch-knowledge-kit
主题：Claude Projects 使用教程
封面用途：X文章封面
插图用途：教程配图
插图数量：3
语言：中文
内容结构：入口位置、创建项目、添加上下文
```

推荐工作流：

1. 粗略想法先用 `$cover-tips <风格>`。
2. 根据返回模板确认标题、副标题、画幅比例、语言、用途、情绪和禁用元素。
3. 需要可复用提示词文本时，再切到 `--out-type prompt` 或 `--out-type all`。
4. 希望跳过模板、马上生成最终封面时，在 `$cover-*` 后面直接接自然语言说明。
5. 需要正文教程配图时，直接调用 `$illustration-*`。
6. 需要封面和插图配套时，调用 `$sketch-knowledge-kit`。

## 安装

四种方式任选。

### CLI Plugin Marketplace

Codex CLI：

```
codex plugin marketplace add imartinstudio/cover-prompt-skills
codex plugin add cover-editorial-collage@cover-prompt-skills
```

Claude CLI：

```
/plugin marketplace add imartinstudio/cover-prompt-skills
/plugin install cover-editorial-collage@cover-prompt-skills
```

根据你使用的 CLI 选择对应命令。Codex CLI 中先添加插件市场仓库，再安装需要的 skill/plugin。Claude CLI 中使用 `/plugin` slash commands。

更新已安装的插件后，需要刷新/重新启用插件，或重启对应 agent，让它加载最新插件版本，而不是继续使用旧缓存版本。

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

技能会以独立 `SKILL.md` 文件下载到目标目录。脚本默认使用 `~/.shared-skills`；不同 agent 的技能目录可能不同，Codex / Agents 用户通常可以指定 `~/.agents/skills` 或 `~/.codex/skills`：

```bash
COVER_SKILLS_TARGET=~/.agents/skills \
curl -fsSL https://raw.githubusercontent.com/imartinstudio/cover-prompt-skills/main/install.sh | bash
```

### 本地开发安装

```bash
cd cover-prompt-skills
./install.sh                              # 安装全部（symlink）
./install.sh cover-editorial-collage      # 安装单个
```

本地开发安装会把仓库里的技能目录软链到目标目录，适合一边修改仓库内容、一边在 agent 中测试。

`cover-tips` 是导航技能，随完整包安装，不可单独安装 —— 它依赖具体的封面风格技能。

## 仓库原则

- 每个插件保持精简：一个 `SKILL.md` 置于 `skills/` 下，Claude Code 和 Codex 各一个 manifest。
- 默认不包含特定平台的 agent 元数据。
- 保持提示词通用，除非用户明确要求特定平台的变体。
- 使用 `cover-` 作为封面/海报技能的命名前缀。
- 使用 `illustration-` 作为插图技能的命名前缀。
- 使用中性的 `*-kit` 命名多资产编排技能，避免把非封面能力塞进 `cover-`。

## 许可证

MIT
