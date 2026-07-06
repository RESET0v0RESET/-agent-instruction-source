# Agent Instruction Source Corpus

This repository is a working corpus for collecting and screening public sources about repository-level instruction files for coding agents, especially `AGENTS.md` and `CLAUDE.md`.

## Purpose

The research position is:

1. Official documentation and engineering blogs tell us what `AGENTS.md` and `CLAUDE.md` are intended to do.
2. Good practices are useful background, but failing to follow a good practice is not automatically a defect.
3. A defect should require stronger evidence, such as mismatch with repository facts, tool loading semantics, or developer-reported failure cases.

## Collection Scope

We first collect official and quasi-official sources from:

- Claude Code official documentation, official blog, engineering blog, and product-team practice articles.
- AGENTS.md official sources and all tools listed as supporting AGENTS.md on the official AGENTS.md site.
- Common authoritative or community evidence sources, including GitHub, Hugging Face, OWASP, Meta, Hacker News, and security-company analyses.

## Repository Layout

- `data/source_registry.csv`: main source registry with first-round screening result.
- `data/first_round_screening.md`: grouped summary of PASS / MAYBE / FAIL / PENDING sources.
- `docs/collection_scope.md`: exact collection scope and source hierarchy.
- `docs/screening_protocol.md`: first-round and second-round screening rules.
- `docs/search_log.md`: search queries, search dates, and known gaps.
- `docs/manual_screening_guide.md`: how to perform the second manual screening.
- `notes/manual_review_queue.md`: sources that should be manually reviewed next.
- `notes/source_gaps.md`: tools or domains where direct official evidence is still missing or weak.

## First-Round Screening Rule

A source passes the first round if it satisfies both conditions:

1. It explicitly contains `AGENTS.md`, `agents.md`, or `CLAUDE.md`.
2. It discusses a concrete good or bad practice, loading behavior, scoping behavior, priority rule, size/context risk, security risk, or maintenance concern.

Sources that only mention tool support or ecosystem adoption are marked `MAYBE`. Sources that are relevant to agent security but do not mention `AGENTS.md` or `CLAUDE.md` are marked `FAIL_BACKGROUND_ONLY`. Sources that require login or need later verification are marked `PENDING`.

## Current Status

The current corpus is a first-layer screening dataset. The next step is manual second-round screening by the researcher: mark which PASS/MAYBE sources are suitable for the paper's evidence base, and tag each accepted source with the specific defect or motivation it supports.

