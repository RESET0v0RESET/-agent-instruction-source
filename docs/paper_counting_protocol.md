# Paper Counting Protocol

## Main Count

Use the following count in the paper:

> We collected 440 source-level candidate URLs from official, quasi-official, authoritative, and community sources related to `AGENTS.md` and `CLAUDE.md`.

This count includes Hacker News as a community source channel, but does not count every Hacker News story/comment as an independent source.

## Why Source-Level Normalization?

The study uses official and authoritative documents to understand the semantics and practices of repository-level instruction files. Hacker News is useful for finding practitioner discussions, but counting every comment would distort the corpus. Therefore, the main unit is a source-level URL or source channel rather than every individual comment.

## Retrieval Keywords

The first-layer retrieval used exact keyword matching for:

- `AGENTS.md`
- `agents.md`
- `CLAUDE.md`

The search is case-insensitive for page text, while snippets and URLs preserve the original spelling.

## Retrieval Process

For official and authoritative sites, the retrieval process was:

1. Start from the AGENTS.md supporter list and Claude Code official sources.
2. Add common authoritative/community domains: GitHub, Hugging Face, OWASP, Meta, selected security-company posts, and Hacker News.
3. For each domain, collect candidate URLs from official sitemap files, documentation roots, blog/changelog indexes, and manually seeded official URLs.
4. Apply path filters to reduce unrelated pages, such as `/docs/`, `/blog/`, `/changelog/`, `/news/`, `/engineering/`, `agent`, `agents`, `rules`, `memory`, `guidelines`, `copilot`, `claude-code`, and `codex`.
5. Fetch page text and search for exact keyword hits.
6. Deduplicate and normalize to a source-level candidate list.

## Canonical Data

The final candidate list is:

```text
data/candidate_sources_440.csv
```

The site-level distribution is:

```text
data/source_site_counts.csv
```

## First-Round Screening

The 440 candidate sources are not final evidence. A source passes first-round screening only if it:

1. explicitly contains `AGENTS.md`, `agents.md`, or `CLAUDE.md`; and
2. discusses a concrete good/bad practice, loading rule, scope rule, precedence rule, size/context risk, security concern, or maintenance concern.

Sources that only mention ecosystem adoption are marked `MAYBE`. Sources relevant to agent security but not directly about instruction files are retained as background-only.

