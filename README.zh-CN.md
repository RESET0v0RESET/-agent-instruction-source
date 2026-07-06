# Agent Instruction Source Corpus

这个仓库用于整理 `AGENTS.md`、`agents.md` 和 `CLAUDE.md` 相关的公开来源，后续可直接上传到 GitHub。

## 研究定位

官方文档和产品团队文章可以说明 instruction files 的设计语义、加载规则、scope、precedence 和推荐实践。但是，推荐实践本身不是 defect。论文中不能把“不遵守 best practice”直接写成缺陷。真正的 defect 应该有更强证据，例如 instruction claim 与仓库事实不一致、与工具官方加载语义冲突，或 GitHub discussion / issue / PR 中出现真实负面现象。

## 语料范围

我们收集了 **440 个 source-level candidate URLs**，来源包括官方、准官方、权威和社区文档，主题围绕 `AGENTS.md` 和 `CLAUDE.md`。

来源范围包括：

- Claude Code 官方文档、engineering blog 和产品团队实践文章；
- AGENTS.md 官方来源，以及 AGENTS.md 官网列出的支持 AGENTS.md 的工具；
- GitHub、Hugging Face、OWASP、Meta、Hacker News、安全公司博客等权威或社区来源。

Hacker News 在这里作为社区来源通道纳入 440 个候选来源中，不把每一条 Hacker News comment/story 单独计入论文主统计。

## 文件结构

- `data/candidate_sources_440.csv`：最终用于上传和人工筛选的 440 个候选来源。
- `data/source_site_counts.csv`：440 个候选来源按站点的分布。
- `data/source_registry.csv`：人工整理的种子来源登记表。
- `data/first_round_screening.md`：种子来源的第一轮 PASS / MAYBE / PENDING / FAIL 汇总。
- `data/raw_collection_summary.md`：统计口径和原始采集计数说明。
- `docs/collection_scope.md`：收集范围和来源层级。
- `docs/paper_counting_protocol.md`：论文中使用的计数口径。
- `docs/screening_protocol.md`：第一轮和第二轮筛选规则。
- `docs/search_log.md`：搜索关键词和采集过程。
- `docs/manual_screening_guide.md`：人工二筛指南。
- `notes/manual_review_queue.md`：建议优先人工审核的来源。
- `notes/source_gaps.md`：目前仍缺少直接官方证据的工具或网站。
- `scripts/`：用于复现候选链接采集和合并的脚本。

## 第一层检索方法

第一层检索使用精确关键词：

- `AGENTS.md`
- `agents.md`
- `CLAUDE.md`

对于官方和权威网站，我们从 sitemap、官方文档入口、官方 blog/changelog、产品团队文章和人工种子 URL 中收集候选链接。为了减少无关页面，使用了路径过滤，例如 `/docs/`、`/blog/`、`/changelog/`、`agent`、`rules`、`memory`、`guidelines`、`copilot`、`claude-code` 和 `codex`。

## 第一轮筛选规则

一篇来源通过第一轮筛选需要同时满足：

1. 明确包含 `AGENTS.md`、`agents.md` 或 `CLAUDE.md`。
2. 不只是提到文件名，而是包含具体实践讨论，例如加载规则、scope、precedence、具体命令、context bloat、安全风险、维护问题、agent 忽略/冲突/读错等。

只提到生态支持的来源标为 `MAYBE`。对 agent security 有用但没有直接讨论 instruction file 的来源保留为 background-only。

## 论文建议表述

> We collected 440 source-level candidate URLs from official, quasi-official, authoritative, and community sources related to `AGENTS.md` and `CLAUDE.md`. We then applied a first-round screening step to retain sources that explicitly discuss concrete good or bad practices, loading semantics, scoping rules, security risks, context-size concerns, or maintenance issues.

