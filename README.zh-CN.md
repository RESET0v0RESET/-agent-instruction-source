# Agent Instruction Source Corpus

用于整理 `AGENTS.md` 和 `CLAUDE.md` 相关的官方/权威来源。

## 文件说明

- `data/source_registry.csv`：完整来源登记表，包含链接、来源类型、证据强度、命中关键词、实践标签和第一轮筛选结论。
- `data/first_round_screening.md`：按 PASS / MAYBE / FAIL / PENDING 汇总的第一轮筛选结果。
- `docs/collection_scope.md`：收集范围和来源层级。
- `docs/screening_protocol.md`：第一轮筛选和第二轮人工筛选规则。
- `docs/search_log.md`：搜索关键词、时间和当前缺口。
- `docs/manual_screening_guide.md`：人工二筛时如何记录证据。
- `notes/manual_review_queue.md`：建议优先人工审核的来源。
- `notes/source_gaps.md`：目前缺少直接官方证据的工具或网站。

## 第一轮筛选标准

一篇文档通过第一轮筛选需要同时满足：

1. 明确包含 `AGENTS.md`、`agents.md` 或 `CLAUDE.md`。
2. 不只是提到文件名，而是包含具体实践讨论，例如：
   - 如何写 build/test/lint/run 命令；
   - 文件放在哪里、如何被加载；
   - root/nested/global/project scope；
   - precedence 或 fallback 行为；
   - 文件过长、上下文膨胀、过时内容；
   - secret、安全边界、hook、settings、enforcement；
   - agent 忽略、冲突、读错、被污染等负面现象。

## 筛选标签

- `PASS`：明确命中文件名，并包含具体实践或风险讨论。
- `MAYBE`：提到了文件或生态支持，但具体实践证据较弱。
- `FAIL_BACKGROUND_ONLY`：对 agent security 或上下文风险有用，但没有直接讨论 `AGENTS.md` / `CLAUDE.md`。
- `PENDING`：可能相关，但需要登录、进一步访问或人工确认。

## 下一步

人工二筛时建议先看：

1. OpenAI Codex、Anthropic Claude Code、GitHub Copilot、Factory、Kilo、Augment、Windsurf、Junie、Ona 这类官方文档。
2. GitHub Blog、Anthropic engineering blog、Augment blog、Factory blog 这类实践文章。
3. Hugging Face、Meta、OWASP、Hacker News、安全公司博客作为 motivation 或风险补充来源。

