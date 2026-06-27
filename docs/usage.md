# Usage

## The Main Entry Point

Use `cover-tips` as the daily entry point when you have rough content and a rough style direction. It cleans up the brief, extracts fields, chooses the matching concrete style skill, and returns a ready-to-use invocation template by default.

Install it with the full package; by itself it is only a navigator and is not useful without the concrete cover style skills.

Formula:

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

## Supported Styles

| User style input | Routed skill |
|---|---|
| `黑白极简` / `黑白` / `极简` / `minimal` / `bw` | `$cover-black-white-minimal` |
| `潮流彩色` / `彩色` / `高冲击` / `trendy` / `color` | `$cover-trendy-color-poster` |
| `巨型透视` / `透视标题` / `电影海报风` / `电竞主视觉` / `perspective` | `$cover-giant-perspective-poster` |
| `手绘知识图谱` / `知识图谱` / `知识地图` / `白板框架` / `sketch knowledge` | `$cover-sketch-knowledge-poster` |
| `本地AI` / `3D Eye` / `黑绿终端` / `local AI` / `terminal poster` | `$cover-3d-eye` |
| `深夜工作室` / `深夜工作室风` / `AI工程师空间` / `indie hacker` / `midnight studio` | `$cover-midnight-studio` |
| `像素头像` / `像素` / `8-bit头像` / `pixel avatar` / `Q版像素头像` | `$cover-pixel-avatar` |
| `布达佩斯` / `Budapest` / `复古欧洲` / `电影感` / `明信片` | `$cover-budapest-poster` |
| `撕纸剪贴` / `剪贴` / `拼贴` / `collage` / `editorial collage` | `$cover-editorial-collage` |
| `茶风格` / `茶` / `东方美学` / `宋代美学` / `汉字成像` | `$cover-tea-oriental` |
| `浅色产品` / `浅色产品风` / `SaaS产品` / `light product` / `奶油白` | `$cover-light-product` |
| `麦肯锡简报风` / `麦肯锡风` / `咨询简报` / `strategy report` / `mckinsey style` | `$cover-mckinsey-briefing-style` |

## Output Type

If `--out-type` is omitted, `cover-tips` outputs the template only.

Template only:

```text
--out-type template
```

Prompt only:

```text
--out-type prompt
```

Both:

```text
--out-type all
```

For backward compatibility, Chinese natural-language output requests still work, but `--out-type` is the preferred control parameter.

## Direct Style Skills

Call a concrete style skill directly when you already know the exact style and do not need `cover-tips` to reorganize the brief:

```text
$cover-black-white-minimal ...
$cover-trendy-color-poster ...
$cover-giant-perspective-poster ...
$cover-sketch-knowledge-poster ...
$cover-3d-eye ...
$cover-midnight-studio ...
$cover-pixel-avatar ...
$cover-budapest-poster ...
$cover-editorial-collage ...
$cover-tea-oriental ...
$cover-light-product ...
$cover-mckinsey-briefing-style ...
```

Direct style skills also support `--out-type`.

```text
$cover-black-white-minimal --out-type prompt
主题：长期主义 副标题：在即时反馈时代重新理解耐心 画幅比例：4:3 用途：文章封面
```

Omit `--out-type` or use `--out-type template` when you only want the invocation template:

```text
$cover-budapest-poster --out-type template
主题：提示词 副主题：好的提示，不只是命令，更是设计 画幅比例：5:2 用途：X封面
```

In this case, `主题：提示词` is treated as the topic value, not as a request to output a full image prompt.

Use `cover-tips` when the user needs content cleanup, field extraction, or standard formatting first.

## Illustration Skills

Use `illustration-*` skills for inline images, tutorial illustrations, product explanation graphics, and feature walkthrough visuals. They are separate from `cover-*` because they solve a different output job.

```text
$illustration-sketch-ui --out-type prompt
主题：Claude Projects 入口说明
说明：解释用户从侧边栏进入 Projects 并创建第一个项目
画幅比例：16:9
用途：教程配图
界面来源/产品场景：Claude Projects
重点区域：Projects 入口和 Create Project 按钮
```

```text
$illustration-light-product --out-type prompt
主题：Codex 自动化工作流
说明：解释 Agent 如何创建任务、调用工具并验证结果
画幅比例：16:9
用途：教程配图
产品/场景：Codex Agent 工作区
重点模块：任务状态面板和工具调用流程
```

```text
$illustration-3d-eye --out-type prompt
主题：量化模型怎么选
说明：解释 Q2_K、Q4_K_M、Q8_0、F16 在体积和质量之间的取舍
画幅比例：16:9
用途：教程配图
图解类型：量化柱状图
重点区域：Q4_K_M 作为 sweet spot
连续角色：蓝白手绘 3D Eye 指引姿态指向高亮柱
```

## Cover + Illustration Kits

Use `sketch-knowledge-kit` when one article, tutorial, or product explanation needs a coordinated cover plus several matching illustrations.

```text
$sketch-knowledge-kit
主题：Claude Projects 使用教程
封面用途：X文章封面
插图用途：教程配图
插图数量：3
语言：中文
内容结构：入口位置、创建项目、添加上下文
```

The kit output should contain:

- `封面 brief`: calls `$cover-sketch-knowledge-poster`.
- `插图 brief[]`: calls `$illustration-sketch-ui`.
- `一致性约束`: title tone, black/orange ratio, paper texture, icon linework, terminology.
- `差异化约束`: cover for overview/shareability, illustrations for feature explanation.

Use `light-product-kit` when an AI product article, SaaS tutorial, or Agent workflow explanation needs one light product cover plus several matching product illustrations.

```text
$light-product-kit
主题：Codex 自动化工作流
封面用途：X文章封面
插图用途：教程配图
插图数量：3
语言：中文
产品/场景：Codex Agent 工作区
内容结构：创建任务、调用工具、验证结果
```

The light product kit output should contain:

- `封面 brief`: calls `$cover-light-product`.
- `插图 brief[]`: calls `$illustration-light-product`.
- `一致性约束`: cream-white base, warm/cool color balance, SaaS UI modules, product terminology.
- `差异化约束`: cover for product story and shareability, illustrations for feature/workflow explanation.

Use `3d-eye-kit` when a local AI, Ollama, offline model, privacy, hardware, or quantization tutorial needs one 3D Eye cover plus several matching tutorial illustrations.

```text
$3d-eye-kit
主题：14 步搭建自己的本地 AI
封面用途：X文章封面
配图用途：教程配图
配图数量：5
语言：中英混排
核心钩子：No cloud, no filters, no one watching
内容结构：全流程、Local vs Cloud、硬件匹配、量化选择、常见错误
连续角色：蓝白手绘 3D Eye 吉祥物贯穿全套，按内容切换挥手、奔跑、指引、技能卡、点赞等姿态
```

The 3D Eye kit output should contain:

- `封面 brief`: calls `$cover-3d-eye`.
- `配图 brief[]`: calls `$illustration-3d-eye`.
- `一致性约束`: black grid board, neon green terminal glow, blue-white hand-drawn 3D Eye mascot continuity, terminal UI labels.
- `差异化约束`: cover for thesis/shareability, illustrations for specific tutorial explanations.

## Direct Image Generation

You can skip template generation entirely and ask a concrete skill to generate the final cover from a natural-language brief:

```text
$cover-editorial-collage 直接生成一张 5:2 的 X 封面，主题是“提示词”，副标题是“好的提示，不只是命令，更是设计”。整体要撕纸剪贴、杂志感、讽刺一点，不要机器人脸和蓝紫霓虹。
```

Use this path when the style is clear and you do not need to inspect intermediate fields. The concrete skill should keep analysis internal and either call the available image-generation tool directly or produce the final cover result according to the host agent's capabilities.

## Recommended Workflow

1. Start with `$cover-tips <style>` for rough ideas.
2. Use the returned template to confirm title, subtitle, ratio, language, use case, mood, and banned elements.
3. Switch to `--out-type prompt` or `--out-type all` when you need reusable prompt text.
4. Use `$cover-*` followed by natural-language instructions when you want to skip the template and generate the final cover immediately.
5. Directly call `$cover-*` for repeated workflows where the style and fields are already stable.
