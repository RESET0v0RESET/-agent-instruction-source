# Agent Instruction Source Corpus

This repository records the source collection and first-layer screening protocol for public documents about repository-level instruction files for coding agents, especially `AGENTS.md`, `agents.md`, and `CLAUDE.md`.

## Research Position

Official documentation and product-team articles describe how instruction files are intended to be written, loaded, scoped, and maintained. These materials are useful for understanding tool semantics and best practices, but a recommended practice is not automatically a defect rule. In the paper, a defect should require stronger evidence, such as mismatch with repository facts, tool loading semantics, or real developer-reported failure cases.

## Corpus Scope

We collected **440 source-level candidate URLs** from official, quasi-official, authoritative, and community sources related to `AGENTS.md` and `CLAUDE.md`.

The source pool covers:

- Claude Code official documentation, engineering blogs, and product-team practice articles about `CLAUDE.md`;
- AGENTS.md official sources and tools listed as supporting AGENTS.md;
- authoritative/community sources such as GitHub, Hugging Face, OWASP, Meta, Hacker News, and selected security-company posts.

Hacker News is treated as a community source channel in the 440-source corpus, rather than expanding every individual Hacker News story/comment into a separate counted source.

## Repository Layout

- `data/candidate_sources_440.csv`: canonical 440-source candidate pool for upload and manual screening.
- `data/source_site_counts.csv`: source-site distribution for the 440 candidates.
- `data/source_registry.csv`: manually curated seed registry used during collection.
- `data/first_round_screening.md`: first-round PASS / MAYBE / PENDING / FAIL summary for seed sources.
- `data/raw_collection_summary.md`: counting protocol and raw/audit count explanation.
- `docs/collection_scope.md`: collection scope and source hierarchy.
- `docs/paper_counting_protocol.md`: paper-facing counting protocol.
- `docs/screening_protocol.md`: first-round and second-round screening rules.
- `docs/search_log.md`: search terms and collection process.
- `docs/manual_screening_guide.md`: guide for manual second-round screening.
- `notes/manual_review_queue.md`: recommended manual review queue.
- `notes/source_gaps.md`: tools or domains where stronger direct evidence is still needed.
- `scripts/`: reproducibility scripts for collecting and merging candidate links.

## First-Layer Retrieval

The retrieval process used exact keyword matching for:

- `AGENTS.md`
- `agents.md`
- `CLAUDE.md`

For official and authoritative sites, candidate URLs were collected from sitemaps, known documentation roots, official blog/changelog indexes, and manually seeded official pages. Path filters were used to focus on documentation and agent-related pages, such as `/docs/`, `/blog/`, `/changelog/`, `agent`, `rules`, `memory`, `guidelines`, `copilot`, `claude-code`, and `codex`.

## First-Round Screening Rule

A source passes the first round only if it satisfies both conditions:

1. It explicitly contains `AGENTS.md`, `agents.md`, or `CLAUDE.md`.
2. It discusses a concrete good/bad practice, loading behavior, scoping behavior, priority rule, context-size risk, security risk, or maintenance concern.

Sources that only mention ecosystem adoption are marked `MAYBE`. Sources relevant to agent security but not directly about instruction files are retained as background only.

## Recommended Paper Wording

> We collected 440 source-level candidate URLs from official, quasi-official, authoritative, and community sources related to `AGENTS.md` and `CLAUDE.md`. We then applied a first-round screening step to retain sources that explicitly discuss concrete good or bad practices, loading semantics, scoping rules, security risks, context-size concerns, or maintenance issues.

