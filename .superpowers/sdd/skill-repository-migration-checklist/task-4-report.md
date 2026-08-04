# Task 4 报告：文档迁移与质量验证

## 状态

**DONE_WITH_CONCERNS**

Task 4 实现提交：`5effe19e58ef5fd51d58718c7657bc72c752be76`。

本报告保留首轮 Task 4 和前两轮 NEEDS_FIX 的历史证据；当前最终审查修复回合基于 HEAD `4c41aad`，最终交付 commit 的真实 SHA 以本次交付消息为准。

## 本次 NEEDS_FIX 修复回合

本回合仍为 **DONE_WITH_CONCERNS**。已修复：

- 将 `plugins/cover-tips/skills/cover-tips/SKILL.md` 重写为纯选择器：无风格时给出 1–3 个候选并等待确认；确认风格后再确认单张封面或封面 + 正文配图；单张路由到 `cover-X`，文章包只展示并路由到四个真实 `with-docs`，其中包含 `cover-cream-orange-knowledge-poster-with-docs`。
- 删除 CoverTips 运行时中的具体视觉规则、风格默认值、通用 prompt 生成和 Pixel avatar 入口；补充 Claude/Codex 自动调用边界及其他 Agent 的下一步调用模板。
- 同步两个 CoverTips manifest 描述；运行生成器更新 `.claude-plugin/marketplace.json` 和 `generated/skill-registry.json`。Codex marketplace 保持未修改。
- 将命名契约改为默认 1 cover + 3 inline，显式 inline 数量为 1–5；迁移清单改为只勾静态/安装证据，保留真实 CoverTips 路由、自动执行和人工验收未勾选。

本回合没有修改四个 with-docs `SKILL.md`、基础风格技能、registry 实现、安装器、测试、`CONTEXT.md` 或 ADR。

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

## 本修复回合验证记录

### 针对性静态边界检查

命令检查了 CoverTips 的 1–3 候选契约、四个文章路由 ID、两个 manifest 的旧入口残留、具体风格规则标题/条目，以及迁移清单中已勾选的路由 smoke 项。

结果：`targeted CoverTips static check passed`。

### 生成器与 registry

```bash
python3 scripts/skill_registry.py generate
python3 scripts/skill_registry.py check
```

`generate` 已写入 `generated/skill-registry.json`、`.claude-plugin/marketplace.json` 和其他可写生成物，随后在写 `.agents/plugins/marketplace.json` 时因仓库只读保护返回 `PermissionError`（退出码 1）。Codex marketplace 未被修改；`check` 结果为 `registry check passed: 17 plugins`（退出码 0）。

### Frontmatter、Markdown、JSON、Shell

```bash
python3 -c 'from pathlib import Path; paths=sorted(Path("plugins").glob("*/skills/*/SKILL.md")); assert len(paths)==17; assert all((lambda text: text.startswith("---\n") and "\n---\n" in text and f"name: {p.parent.name}\n" in text and "description:" in text)(p.read_text(encoding="utf-8")) for p in paths); print(f"frontmatter-ok {len(paths)} skills")'
find . -name '*.md' -not -path './.git/*' -not -path './node_modules/*' -print0 | xargs -0 npx --offline --yes markdownlint-cli2
python3 -c 'from pathlib import Path; paths=sorted(Path(".").rglob("*.md")); assert paths; assert all(sum(1 for line in p.read_text(encoding="utf-8").splitlines() if line.strip().startswith(chr(96)*3)) % 2 == 0 for p in paths); assert all(all(not line.lstrip().startswith("#") or line.lstrip("#").strip() for line in p.read_text(encoding="utf-8").splitlines()) for p in paths); print(f"markdown-structure-ok {len(paths)} files; fenced blocks balanced; headings non-empty")'
find . -name '*.json' -not -path './.git/*' -not -path './node_modules/*' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null
find . -name '*.sh' -not -path './.git/*' -not -path './node_modules/*' -print0 | xargs -0 -n1 bash -n
```

结果：`frontmatter-ok 17 skills`、`markdown-structure-ok 47 files; fenced blocks balanced; headings non-empty`、`json-ok 41 files`、`shell-ok 5 files`。离线 markdownlint 因本机没有缓存返回 `ENOTCACHED`，未联网重试。

### unittest

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p "test_*.py" -v
```

结果：`Ran 17 tests ... OK`。

### 离线临时安装 smoke

```bash
COVER_SKILLS_TARGET="$tmpdir/all" COVER_SKILLS_BACKUP_DIR="$tmpdir/all-backup" bash scripts/install.sh
COVER_SKILLS_TARGET="$tmpdir/single" COVER_SKILLS_BACKUP_DIR="$tmpdir/single-backup" bash scripts/install.sh cover-3d-eye-with-docs
COVER_SKILLS_TARGET="$tmpdir/single" COVER_SKILLS_BACKUP_DIR="$tmpdir/single-backup" bash scripts/install.sh cover-tips
```

结果：`install-smoke-ok all=17 single=cover-3d-eye-with-docs cover-tips`。临时目标为 `/private/tmp/cover-prompt-task4-repair.CN2ZGs`，未联网。

### 本回合 Diff

```bash
git diff --check
```

结果：退出码 `0`。

## 本次最终审查修复回合（基于 HEAD `4c41aad`）

本回合状态仍为 **DONE_WITH_CONCERNS**；最终交付 commit 的真实 SHA 以本次交付消息为准。

已实际修复：

- README、README.en 和 usage 不再把 CoverTips 描述成输出模板、通用 prompt 或中间结果；现在明确 CoverTips 只确认风格与资产范围，输出由目标 `cover-X` 或 `cover-X-with-docs` 技能负责。基础技能和 `with-docs` 自己的输出模式说明保留。
- CoverTips 路由表增加 `BEGIN/END GENERATED COVER-TIPS ROUTES` 标记。现有 `scripts/skill_registry.py generate` 从真实 registry 的 base 与 with-docs 配对生成表，`check` 解析并比较区块；隔离测试篡改为 `cover-fake-with-docs` 时会失败。CoverTips 仍只负责选择和转交，不包含视觉规则。
- `style-specs/with-docs.json` 的 `visual_system` 投影到四个 base 技能，`visual_system` 与 `article_visual_system` 投影到四个 with-docs 技能，均为稳定、可审阅的 JSON fenced generated block。生成块被规范化排除在 artifact SHA 之外，避免自引用循环；只改 spec 的 palette、background 或 inline contract 而不更新 SKILL.md 时，`check` 会失败。
- 四个 with-docs 的 Hard Boundaries 明确：默认在对话中输出；只有用户明确给出输出路径才写文件；输出路径只作用于该路径；文章源始终只读。
- 迁移清单 line 58 改为“未指定=3，显式 inline 数量=1–5”，未验证的真实 Agent 路由、自动执行和人工视觉验收仍未勾选。

本回合没有修改用户现有的未跟踪 `CONTEXT.md` 或 `docs/adr/`。

### 本回合 TDD 与质量门结果

- RED：`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p "test_*.py" -v`；新增行为接入后为 `Ran 20 tests ... FAILED (failures=16)`。
- GREEN：同一命令最终为 `Ran 20 tests ... OK`，覆盖真实路由表篡改、三类 style spec 语义漂移、生成稳定性和四个 Hard Boundaries。
- `python3 scripts/skill_registry.py generate`：使用现有 generator 完整成功，写入 7 个产物，包括两个 marketplace；未联网。
- `python3 scripts/skill_registry.py check`：`registry check passed: 17 plugins`。
- frontmatter：`frontmatter-ok 17 skills`；本地 Markdown 结构检查：`markdown-structure-ok 47 files; fenced blocks balanced; headings non-empty`。
- JSON：`json-ok 41 files`；Shell：`shell-ok 5 files`。
- 离线 `npx --offline --yes markdownlint-cli2` 返回 `ENOTCACHED`，未联网重试；本地结构检查通过。
- 离线临时安装 smoke：`install-smoke-ok all=17 single=cover-3d-eye-with-docs cover-tips`。
- `git diff --check`：退出码 `0`。

### 本回合剩余 concerns

仍未执行真实 Agent 调用、网络安装、provider 调用、实际生图或四个 with-docs 的发布前人工视觉抽样；这些是本回合明确禁止或未授权的外部验证。独立 offline markdownlint 仍因本机没有 npm 缓存不可用；现有提交钩子的历史 lint 证据与本地 Markdown 结构检查已分别保留记录。

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

- CoverTips 当前选择器已不再包含 `Pixel avatar` 规则或入口。`generated/skill-registry.json` 的 `excluded_skills` 仍保留 `cover-pixel-avatar`，这是弃用入口审计字段，不是当前发布或 CoverTips 路由。
- 四个受保护的 with-docs `SKILL.md` 仍有显式的“不路由到”旧 planner、kit 或 illustration 名称。这些是负向运行时边界，不是当前发布入口；由于用户明确禁止修改四个技能正文，本 Task 4 未改动它们。
- source prompt 中的 `Illustration` 等词是历史参考图角色描述，不是独立技能名；source-prompt README 已明确标成历史档案。

## 未解决疑问

1. 四个 with-docs 尚未进行发布前人工抽样验收。本次按要求不联网、不实际生图，因此没有真实视觉结果可做风格、章节绑定、重复图片规避和提示词质量验收；迁移清单对应项保持未勾选。
2. 本回合已把 CoverTips 选择器正文收紧为“给出 1–3 个候选并等待确认”的契约，但未执行真实 Agent 调用，因此尚未验证候选质量、确认顺序、目标 skill 自动执行或其他 Agent 模板的实际行为。
3. 独立 `npx --offline` markdownlint 探测因 npm 缓存缺失返回 `ENOTCACHED`；提交钩子的实际 lint 输出全通过，另有本地 Markdown 结构检查通过。若发布门要求独立 offline markdownlint 命令，需要提供本地缓存或 vendored 工具。
4. 未执行网络安装、`npx skills add`、curl 远程安装、provider 调用或实际生图；安装验证仅覆盖本地临时目标的全量和单个 symlink smoke。两个 marketplace 均已由现有 generator 成功生成并由 registry check 校验。
