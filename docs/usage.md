# Usage

## The Main Entry Point

Use `cover-tips` when the user knows the desired style but has not formatted the content. Install it with the full package; by itself it is only a navigator and is not useful without the concrete cover style skills.

Formula:

```text
$cover-tips + style + --out-type template|prompt|all + user content
```

Examples:

```text
$cover-tips 撕纸剪贴
```

```text
$cover-tips 潮流彩色 --out-type prompt
```

```text
$cover-tips 布达佩斯 --out-type all
```

If `--out-type` is omitted, `cover-tips` outputs the template only.

## Supported Styles

```text
黑白极简 / 黑白 / 极简 / minimal / bw
→ $cover-black-white-minimal

潮流彩色 / 彩色 / 高冲击 / trendy / color
→ $cover-trendy-color-poster

布达佩斯 / Budapest / 复古欧洲 / 电影感 / 明信片
→ $cover-budapest-poster

撕纸剪贴 / 剪贴 / 拼贴 / collage / editorial collage
→ $cover-editorial-collage

茶风格 / 茶 / 东方美学 / 宋代美学 / 汉字成像
→ $cover-tea-oriental
```

## Output Type

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

Use a direct style skill when the user already knows the exact style and wants that skill's final behavior:

```text
$cover-black-white-minimal ...
$cover-trendy-color-poster ...
$cover-budapest-poster ...
$cover-editorial-collage ...
$cover-tea-oriental ...
```

Direct style skills also support `--out-type`. Omit it or use `--out-type template` when you only want the invocation template:

```text
$cover-budapest-poster --out-type template
主题：提示词 副主题：好的提示，不只是命令，更是设计 画幅比例：5:2 用途：X封面
```

In this case, `主题：提示词` is treated as the topic value, not as a request to output a full image prompt.

Use `cover-tips` when the user needs content cleanup, field extraction, or standard formatting first.
