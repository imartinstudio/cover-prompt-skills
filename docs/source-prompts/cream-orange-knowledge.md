# 奶油橙知识视觉系统（Cream Orange Knowledge）

这套视觉系统来自一组 AI 工程、Agent 系统、反馈循环、架构演进类信息图参考图。运行时由一个 `cover-*` 风格技能承载；整篇文章的封面和正文配图由统一 planner 编排：

- `cover-cream-orange-knowledge-poster`
- `article-visual-planner`

## 核心定位

用于 AI 工程解释型视觉系统：封面、正文配图、长图/信息图、文章视觉编排。

适合主题：

- AI Agent
- AI 工程
- 系统架构
- 工作流
- 反馈循环
- 产品技术解释
- 从 prompt-first 到 loop-first 的范式转移

## 视觉关键词

- 奶油色纸感背景
- burnt orange / terracotta 强调色
- charcoal black 标题与线稿
- warm gray 辅助线
- 编辑信息图构图
- 手绘但克制的技术图解
- 模块卡片、流程箭头、闭环、阶梯、架构栈、对比框架
- 中高信息密度，但层级必须清楚

## 画面结构母题

- Stage progression：阶段演进、路线图、成熟度模型
- Before/after comparison：prompt-first vs loop-first、旧范式 vs 新范式
- System architecture：模型、RAG、工具调用、记忆、评估、观测、人类升级
- Feedback loop：Observe、Decide、Act、Evaluate、Refine
- Maturity ladder：能力阶梯、组织采用路径
- Decision framework：团队落地判断框架
- Bounded vs unbounded contrast：安全边界、权限、guardrails、人类审核

## 默认输出关系

封面 skill：

```text
$cover-cream-orange-knowledge-poster
```

负责总览论点、主视觉隐喻、传播性和收藏价值。

文章视觉 planner：

```text
/article-visual-planner:cover-cream-orange-knowledge-poster
```

根据文章内容编排一张封面和多张正文配图 brief。每个资产继续交给 `cover-cream-orange-knowledge-poster` 承载风格，但通过 `资产类型` 区分 `cover`、`article-inline`、`workflow-diagram`、`comparison`、`architecture`、`long-infographic` 等用途。

## 禁用方向

- 深色赛博背景
- 蓝紫 AI 渐变
- 真实产品截图
- 真实品牌 logo
- 高光 3D 渲染
- 随机电路板填充
- 过密不可读的小字
- 无逻辑的装饰箭头
- 廉价 SaaS banner
- 与奶油橙黑灰体系无关的高饱和彩色
