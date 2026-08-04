# 技能仓库重构迁移清单

状态：部分完成；文档、静态索引和本地安装验证已完成，CoverTips 的真实路由执行、自动执行行为和人工视觉验收仍未完成。

本清单把已确认的产品模型转换为后续实现任务。每一项只有在有对应的静态检查、安装命令或其他明确证据时才勾选；未勾选项不得被表述为已生效。

## Task 1: 清理旧入口并落实 CoverTips 选择器

- 删除 `plugins/article-visual-planner` 和 `plugins/cover-pixel-avatar` 的发布实现。
- 将 `cover-tips` 改成两阶段选择器：确认风格，再确认单张封面或封面加正文配图；不拥有具体风格规则。
- 保留基础 `cover-X` 的直接调用路径；文章配图只允许路由到实际存在的 `cover-X-with-docs`。
- 先完成运行时 skill 与对应 manifest 的清理，README 和迁移说明留给 Task 4。

## Task 2: 创建四个自包含 with-docs 技能

- 创建 `cover-sketch-knowledge-poster-with-docs`、`cover-light-product-with-docs`、`cover-cream-orange-knowledge-poster-with-docs` 和 `cover-3d-eye-with-docs`。
- 每个技能独立拥有 Claude/Codex manifest 和 `SKILL.md`，不在运行时调用基础 skill、planner 或 illustration skill。
- 每个 `with-docs` 统一支持 `template | brief | prompt | all`，缺省为 `brief`，读取粘贴内容、Markdown 或纯文本，默认输出 1 张封面和 3 张正文图，最多 5 张。
- 复用对应基础风格的视觉规则，并为封面和 `article-inline` 正文图提供风格一致性与章节绑定规则。

## Task 3: 建立库存索引、生成和一致性校验

- 以实际插件目录和 plugin manifest 发现库存，生成安装索引、marketplace 索引和 CoverTips 可用风格列表；不要要求所有基础风格都有 `with-docs`。
- 为四个文章配图风格维护共享 style spec，并生成已提交的 `SKILL.md` 产物；基础版与 `with-docs` 版发布时彼此独立。
- 为 registry、manifest、生成产物和弃用入口添加先失败后通过的自动化检查。
- 全量安装包含基础技能、四个 `with-docs` 和 `CoverTips`；单个技能仍可独立安装。

## Task 4: 更新文档并完成质量验证

- [x] 更新 README、命名/使用文档、marketplace 描述和迁移说明，反映选择性 `with-docs` 模型。
- [x] 验证 frontmatter、Markdown、JSON、Shell、索引一致性和安装 smoke test。
- 常规 CI 不联网、不实际生图；发布前对四个 `with-docs` 进行抽样人工验收。

## 目标技能库存

- [x] 保留所有适用的基础 `cover-X` 技能，并确保每个基础技能可独立安装、独立调用。
- [x] 新增 `cover-sketch-knowledge-poster-with-docs`。
- [x] 新增 `cover-light-product-with-docs`。
- [x] 新增 `cover-cream-orange-knowledge-poster-with-docs`。
- [x] 新增 `cover-3d-eye-with-docs`。
- [x] 不为其他基础风格创建 `with-docs` 兄弟技能，除非未来重新确认其适合文章配图。
- [x] 移除 `cover-pixel-avatar` 的发布库存、文档入口和安装入口。
- [x] 移除通用 `article-visual-planner` 的发布库存、文档入口和安装入口。
- [x] 不创建 `cover-tips-with-docs`。

## 内容源与生成产物

- [x] 为每个视觉风格建立一份维护用 style spec，包含基础封面规则，以及适用风格的文章封面/正文图规则。
- [ ] 从共享 style spec 生成基础版和 `with-docs` 版 `SKILL.md`；两者发布时彼此独立，不依赖运行时链式调用。
- [ ] 将生成后的 `SKILL.md` 提交到仓库，供 marketplace、`npx skills add` 和 `curl` 直接使用。
- [x] 增加生成一致性检查，阻止 style spec 与已提交 `SKILL.md` 漂移。

## 技能契约

- [x] 基础 `cover-X` 统一支持 `template | prompt | all`，缺省为 `template`。
- [x] `cover-X-with-docs` 统一支持 `template | brief | prompt | all`，缺省为 `brief`。
- [x] `with-docs` 首版只接受用户粘贴内容、Markdown 文件和纯文本文件；DOCX/PDF 暂不纳入。
- [x] `with-docs` 默认生成 1 张封面和 3 张正文图，自动选择最多 5 张；用户明确指定时允许覆盖数量。
- [x] 读取文章已有图片引用，避免规划重复主题。
- [x] 每张正文图必须绑定具体章节或段落，并输出插入位置、阅读问题、画幅比例和提示词。
- [ ] 文章源只读；默认在对话中输出，只有用户明确提供输出路径时才写文件。
- [x] 缺少文章、文章为空或无法读取时明确失败，不自动降级到基础 `cover-X`。
- [x] 直接生图仅在用户明确提出时执行；常规默认输出 brief/提示词。

## CoverTips 路由

- [x] `CoverTips` 保留为可选选择器，不持有具体视觉风格规则（已完成静态检查）。
- [ ] 用户未指定风格时，先给出 1–3 个推荐并要求确认，不静默猜测。
- [ ] 用户确认风格后，再选择“单张封面”或“封面 + 正文配图”。
- [ ] 单张封面路由到 `cover-X`。
- [x] 文章视觉包的静态可用列表只包含实际存在的 `cover-X-with-docs`。
- [x] 文章视觉包的静态列表隐藏没有 `with-docs` 版本的风格。
- [ ] Claude/Codex 支持时自动执行目标 skill；其他 Agent 输出明确的下一步调用模板。

## 注册、安装与版本

- [x] 以插件目录和 plugin manifest 作为技能库存事实来源。
- [x] marketplace、安装索引、CoverTips 风格列表和 README 技能表改为派生索引或可校验产物。
- [x] 全量安装包含基础技能、四个 `with-docs` 技能和 `CoverTips`。
- [x] 单个技能可独立安装；安装基础版不隐式安装 `with-docs`。
- [ ] 基础技能和 `with-docs` 技能独立版本化。
- [ ] 共享视觉风格变更时同步升级对应的两个技能；仅文章编排变化时只升级 `with-docs`。
- [ ] `CoverTips` 路由规则独立版本化。

## 质量门

- [x] 校验每个已发布 `with-docs` 都有对应基础技能，且不存在未确认的 `with-docs` 入口。
- [x] 校验 marketplace、安装索引、四个文章技能配对和生成产物一致。
- [ ] 通过实际 CoverTips 调用验证候选确认顺序、资产范围确认和目标技能执行。
- [x] 校验 `article-visual-planner` 和 `cover-pixel-avatar` 不再出现在发布库存或新文档入口中。
- [x] 运行 frontmatter、Markdown、JSON 和 Shell 校验。
- [ ] 常规 CI 不依赖网络，也不执行实际生图。
- [ ] 发布前对四个 `with-docs` 做抽样人工验收，检查风格一致性、章节绑定、重复图片规避和真实提示词质量。

## 迁移说明

- [x] 在文档中说明：旧的 `article-visual-planner` 调用应改为 `CoverTips` 选择器或具体的 `cover-X-with-docs`。
- [x] 对没有对应 `with-docs` 的旧 planner 风格调用，明确提示该风格当前只支持单张封面，不自动替换风格。
- [x] 说明 `cover-pixel-avatar` 已退出本仓库的当前发布范围。
- [x] 在实现完成后重新运行本地安装和 manifest 静态检查。
- [ ] 通过 CoverTips 路由的端到端 smoke check。
