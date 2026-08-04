# Task 4 报告：文档迁移与质量验证

## 状态

**DONE_WITH_CONCERNS**

Task 4 实现提交：`5effe19e58ef5fd51d58718c7657bc72c752be76`。

本报告只记录该提交中的文档、marketplace 描述源、派生产物和迁移清单变更。报告文件在后续收尾提交中单独提交；最终交付消息会给出该报告提交的真实 SHA。

## 完成内容

- 更新 `README.md`、`README.en.md`、`docs/usage.md` 和 `docs/naming.md`，明确 `cover-X` 是独立单张封面技能，文章视觉包只有四个独立 `cover-X-with-docs` sibling。
- 记录 CoverTips 两阶段流程：先确认风格，再确认单张封面或封面 + 正文配图；没有 sibling 的风格只支持单张封面，不静默替换。
- 记录 `with-docs` 输入边界：用户粘贴内容、Markdown 文件或纯文本文件；默认 `brief`；默认 1 张封面 + 3 张正文图；正文图数量 1–5；DOCX/PDF 暂不纳入。
- 更新四个 with-docs 和 `cover-tips` 的 Claude marketplace 描述源，并用现有生成器生成 Claude marketplace 及派生 registry 描述。Codex marketplace 没有逐插件 description 字段，生成后 17 个插件库存保持一致，没有内容 diff。
- 为 `docs/source-prompts/` 增加历史档案边界说明；历史记录没有被伪造删除。
- 更新迁移清单中有真实命令证据支持的复选框；人工抽样验收和未执行项保持未勾选。
- 没有修改四个 with-docs `SKILL.md`、基础技能提示词、registry 实现、安装器、测试、`CONTEXT.md` 或 `docs/adr/0001-independent-cover-and-with-docs-skills.md`。

## 质量门命令与结果

### 生成器与索引

命令：

```bash
python3 scripts/skill_registry.py generate
```

第一次运行在写 `.agents/plugins/marketplace.json` 时被沙箱只读权限拦截；使用同一现有命令获得受控写权限后成功生成 7 个产物，包括两个 marketplace。没有联网。

命令：

```bash
python3 scripts/skill_registry.py check
```

结果：`registry check passed: 17 plugins`。

### Frontmatter

使用只读 Python inline validator 检查 `plugins/*/skills/*/SKILL.md` 的 frontmatter 起止标记、`name`、`description` 以及 name 与技能目录名一致性。

结果：`frontmatter-ok 17 skills`。

### Markdown

提交 `5effe19` 时的 pre-commit hook 实际运行了仓库 `scripts/lint.sh`，结果为：

```text
Markdown: all OK
Summary: 0 issues in 0 files
Linting: 33 files
```

为遵守不联网边界，另行执行：

```bash
npx --offline --yes markdownlint-cli2 README.md README.en.md docs/naming.md docs/usage.md docs/skill-repository-migration-checklist.md docs/source-prompts/README.md docs/source-prompts/3d-eye.md docs/source-prompts/cream-orange-knowledge.md
```

该命令返回 `ENOTCACHED`，本机没有可供 offline 模式使用的 npm 缓存，未联网重试。补充执行了本地 Markdown 结构检查：fenced block 平衡、heading 非空、Markdown 文件非空。

结果：`markdown-structure-ok 46 files; fenced blocks balanced; headings non-empty`。

因此本报告区分记录了提交钩子的实际 Markdown lint 通过、offline 独立探测不可用，以及本地结构检查通过。

### JSON

命令：

```bash
while IFS= read -r -d "" file; do python3 -m json.tool "$file" >/dev/null; done < <(find . -name "*.json" -not -path "./.git/*" -print0)
```

结果：`json-ok 41 files`；提交钩子报告 `JSON: 41 ok, 0 failed`。

### Shell

命令：

```bash
while IFS= read -r -d "" file; do bash -n "$file"; done < <(find . -name "*.sh" -not -path "./.git/*" -print0)
```

结果：`shell-ok 5 files`；提交钩子报告 `Shell: 5 ok, 0 failed`。

### 测试

命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p "test_*.py" -v
```

结果：`Ran 17 tests ... OK`。测试覆盖实际库存、四个 with-docs 配对、废弃入口排除、生成器重复性、style spec 漂移、安全 shell 名称、全量安装和单个安装。

### 安装 smoke

在 `/private/tmp/cover-prompt-task4.ZoslvG` 临时目标执行本地安装器，没有访问网络：

```bash
COVER_SKILLS_TARGET="$tmpdir/all" COVER_SKILLS_BACKUP_DIR="$tmpdir/all-backup" bash scripts/install.sh
COVER_SKILLS_TARGET="$tmpdir/single" COVER_SKILLS_BACKUP_DIR="$tmpdir/single-backup" bash scripts/install.sh cover-3d-eye-with-docs
COVER_SKILLS_TARGET="$tmpdir/single" COVER_SKILLS_BACKUP_DIR="$tmpdir/single-backup" bash scripts/install.sh cover-tips
```

结果：全量目标创建 17 个 symlink；单个目标最终只有 `cover-3d-eye-with-docs` 和 `cover-tips`：

```text
install-smoke-ok all=17 single=cover-3d-eye-with-docs cover-tips
```

### Diff

命令：

```bash
git diff --check
```

结果：退出码 `0`。实现提交前已通过；报告提交前会再次执行。

## 残留引用分类

### 当前发布库存：已清理

实际发布残留检查结果：

```text
published-residue-ok marketplaces=2 install-index=4 registry=1
deprecated-published-files-ok 0; empty historical directories retained
```

`article-visual-planner` 和 `cover-pixel-avatar` 不在两个 marketplace 插件名、安装索引、CoverTips 风格列表或 registry 有效插件列表中。`generated/skill-registry.json` 的 `excluded_skills` 字段仍保留两个名称，这是弃用入口审计字段，不是发布库存。两个旧 plugin 目录只剩空目录结构，没有 manifest 或技能文件。

### 当前用户文档：仅保留迁移说明

README、usage 和 source-prompts 说明中的两个旧名称只用于迁移指导或历史档案边界说明，没有出现在当前技能表、路由示例、安装命令或 marketplace 插件列表中。

### 受保护运行时文件中的非入口残留

- `plugins/cover-tips/skills/cover-tips/SKILL.md:168-172` 仍有未被当前 Supported Styles 使用的 `Pixel avatar` style-default 段落。它不形成 `cover-pixel-avatar` 安装入口；由于用户明确禁止修改基础提示词，本 Task 4 未改动它。
- 四个受保护的 with-docs `SKILL.md` 仍有显式的“不路由到”旧 planner、kit 或 illustration 名称。这些是负向运行时边界，不是当前发布入口；由于用户明确禁止修改四个技能正文，本 Task 4 未改动它们。
- source prompt 中的 `Illustration` 等词是历史参考图角色描述，不是独立技能名；source-prompt README 已明确标成历史档案。

## 未解决疑问

1. 四个 with-docs 尚未进行发布前人工抽样验收。本次按要求不联网、不实际生图，因此没有真实视觉结果可做风格、章节绑定、重复图片规避和提示词质量验收；迁移清单对应项保持未勾选。
2. CoverTips 当前受保护基础提示词在未指定风格时要求用户从支持列表中选择，尚未验证它已经实现“给出 1–3 个推荐并等待确认”的精确行为。文档按已确认产品契约记录；若要收紧运行时行为，需要后续授权修改基础提示词。
3. 独立 `npx --offline` markdownlint 探测因 npm 缓存缺失返回 `ENOTCACHED`；提交钩子的实际 lint 输出全通过，另有本地 Markdown 结构检查通过。若发布门要求独立 offline markdownlint 命令，需要提供本地缓存或 vendored 工具。
4. 未执行网络安装、`npx skills add`、curl 远程安装、provider 调用或实际生图；安装验证仅覆盖本地临时目标的全量和单个 symlink smoke。
