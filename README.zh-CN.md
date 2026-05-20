[English](README.md) | [中文](README.zh-CN.md)

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
| `cover-budapest-poster` | 复古中欧电影感、布达佩斯海报风 | 剧院、电车、车站、浴场、档案、明信片概念图 |
| `cover-editorial-collage` | 撕纸编辑拼贴 | 讽刺、冲突、社会评论、杂志拼贴封面 |
| `cover-tea-oriental` | 茶风格东方美学、宋代文人气、汉字成像 | 文化海报、邀请函、信息图、PPT封面 |

## 风格展示

### `cover-black-white-minimal`

![黑白极简风格展示](assets/style-showcases/cover-black-white-minimal.png)

### `cover-trendy-color-poster`

![潮流高冲击彩色海报风格展示](assets/style-showcases/cover-trendy-color-poster.png)

### `cover-editorial-collage`

![撕纸编辑拼贴风格展示](assets/style-showcases/cover-editorial-collage.png)

### `cover-tea-oriental`

![茶风格东方美学展示](assets/style-showcases/cover-tea-oriental.png)

## 推荐使用方式

以 `cover-tips` 为入口：

```text
$cover-tips 撕纸剪贴

生成一个模版
主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
```

默认输出为模板：

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

需要生成提示词时：

```text
$cover-tips 潮流彩色 提示词

主题：提示词 副主题：好的提示，不只是命令，更是设计 其他的你定就好 画幅比例：5:2 用途：x封面
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
