# Task 3 报告：库存索引、生成和一致性校验

- 状态：DONE
- commit：Task 3 主实现为 `ca1f0a22641ddf6c46e7e50b1db084a1084a9fd2`；本报告为后续收尾提交

## 实现摘要

- 新增 `scripts/skill_registry.py`，只使用 Python 标准库，提供三个离线命令：
  - `python3 scripts/skill_registry.py discover`
  - `python3 scripts/skill_registry.py generate`
  - `python3 scripts/skill_registry.py check`
- 新增共享 source spec `style-specs/with-docs.json`，把四个已确认风格的基础视觉
  系统、文章封面/正文图职责、默认数量/边界、文章来源、绑定字段和避用规则纳入
  结构化来源；现有四个 `with-docs/SKILL.md` 正文没有重写。
- `generate` 从 source spec 和实际 `SKILL.md` 生成
  `generated/with-docs-style-index.json`；`check` 重新计算 source spec、基础版和
  `with-docs` 版 `SKILL.md` 的 SHA-256，并把 `visual_system`、
  `article_visual_system`、base/with-docs rule markers 写入 style index；任何产物
  漂移或配对/路径变化都会失败。
- 库存从 `plugins/<name>` 下真实存在的 `.claude-plugin/plugin.json`、
  `.codex-plugin/plugin.json` 和 `skills/<name>/SKILL.md` 发现；校验目录名、两份
  manifest 的 `name`、skill 目录名和 frontmatter `name` 一致，并校验 Codex
  `skills` 路径和两份 manifest 的 display name。
- 当前有效库存为 17 个：12 个基础技能、4 个实际存在且已确认的 `with-docs`
  技能、`cover-tips`。文章配图风格只生成四个实际配对：
  `cover-3d-eye`、`cover-cream-orange-knowledge-poster`、
  `cover-light-product`、`cover-sketch-knowledge-poster`。
- `article-visual-planner` 和 `cover-pixel-avatar` 被列为废弃入口，空的遗留目录
  不会进入库存、marketplace、安装列表或 CoverTips 生成列表。
- 生成产物包含两套 marketplace、JSON 安装索引、可被两个 shell 安装器共同消费的
  shell 安装索引、CoverTips 风格列表、with-docs style index 和完整 registry；输出
  排序、格式和内容稳定。
- 本地 `scripts/install.sh` 与远程根 `install.sh` 都消费生成的
  `generated/install-index.sh`；全量安装包含全部 17 个技能，单个技能（包括
  `with-docs` 和 `cover-tips`）可独立安装。

## 命令与结果

### TDD RED

命令：

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

结果：`7` 个测试全部失败。失败原因均为目标 `scripts/skill_registry.py` 尚不存在
或安装器尚未引用生成库存，确认测试确实捕获了缺失功能。

补充 style spec RED：在已有 registry 实现上先要求
`with-docs-style-index.json` 投影 `visual_system` 和 `article_visual_system`；测试按预期
因生成条目缺少这两项而失败。补齐最小生成逻辑并重新生成 style index 后，再加入缺失
spec、错误配对和 SKILL 漂移三个临时 fixture 检查，最终共 `11` 个测试全部通过。

### 生成与一致性检查

```bash
python3 scripts/skill_registry.py generate
# generated 7 files, including both marketplace indexes and the with-docs style index

python3 scripts/skill_registry.py check
# registry check passed: 17 plugins
```

### 定向验证

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
# Ran 11 tests ... OK

bash -n scripts/install.sh install.sh
# exit 0

python3 -m json.tool style-specs/with-docs.json >/dev/null
python3 -m json.tool generated/with-docs-style-index.json >/dev/null
python3 -m json.tool generated/skill-registry.json >/dev/null
python3 -m json.tool generated/install-index.json >/dev/null
python3 -m json.tool generated/cover-tips-styles.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
# all exit 0

git diff --check -- scripts/skill_registry.py scripts/install.sh install.sh \
  tests/test_skill_registry.py generated .claude-plugin/marketplace.json \
  .agents/plugins/marketplace.json
# exit 0
```

本地安装 smoke test 使用临时目标目录：全量安装创建 `17` 个 symlink；
`cover-3d-eye-with-docs` 和 `cover-tips` 单个安装均返回 `0`。

## 改动文件

新增：

- `scripts/skill_registry.py`
- `tests/test_skill_registry.py`
- `style-specs/with-docs.json`
- `generated/skill-registry.json`
- `generated/install-index.json`
- `generated/install-index.sh`
- `generated/cover-tips-styles.json`
- `generated/with-docs-style-index.json`
- `.superpowers/sdd/skill-repository-migration-checklist/task-3-report.md`

生成/更新：

- `.claude-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`

安装器接入：

- `scripts/install.sh`
- `install.sh`

本 Task 3 未修改、未暂存、未重复提交 Task 2 的四个 `with-docs` `SKILL.md` 和
`task-2-report.md`；它们已由现有 HEAD `70b4a76` 的前序 Task 2 加强提交纳入历史。
用户未跟踪的 `CONTEXT.md`、`docs/adr/`、`docs/skill-repository-migration-checklist.md`
也未修改、未暂存；README 和详细迁移文档同样未修改。

## 未解决疑问

无。废弃插件目录仍可能保留空的子目录结构，但 registry 将其视为未发布入口；
不删除这些前序任务留下的目录，也不会把它们写入任何生成产物。四个现有
`with-docs/SKILL.md` 的内容保持原样，由 source spec 的规则 marker 和固定 SHA
负责后续漂移检测。
