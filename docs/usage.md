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
| `布达佩斯` / `Budapest` / `复古欧洲` / `电影感` / `明信片` | `$cover-budapest-poster` |
| `撕纸剪贴` / `剪贴` / `拼贴` / `collage` / `editorial collage` | `$cover-editorial-collage` |
| `茶风格` / `茶` / `东方美学` / `宋代美学` / `汉字成像` | `$cover-tea-oriental` |

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
$cover-budapest-poster ...
$cover-editorial-collage ...
$cover-tea-oriental ...
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
