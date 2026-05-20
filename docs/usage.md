# Usage

## The Main Entry Point

Use `cover-tips` when the user knows the desired style but has not formatted the content. Install it with the full package; by itself it is only a navigator and is not useful without the concrete cover style skills.

Formula:

```text
$cover-tips + style + output intent + user content
```

Examples:

```text
$cover-tips 撕纸剪贴
```

```text
$cover-tips 潮流彩色 提示词
```

```text
$cover-tips 布达佩斯 模版和提示词
```

If output intent is omitted, `cover-tips` outputs the template only.

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
```

## Output Intent

Template only:

```text
模版
模板
整理成格式
标准格式
调用格式
```

Prompt only:

```text
提示词
prompt
image prompt
完整提示词
生图提示词
```

Both:

```text
模版和提示词
模板和 prompt
模版+提示词
两个都要
都输出
先给模版再给提示词
```

## Direct Style Skills

Use a direct style skill when the user already knows the exact style and wants that skill's final behavior:

```text
$cover-black-white-minimal ...
$cover-trendy-color-poster ...
$cover-budapest-poster ...
$cover-editorial-collage ...
```

Use `cover-tips` when the user needs content cleanup, field extraction, or standard formatting first.
