# Collection Summary

Collection date: 2026-07-06.

## Paper-Facing Count

For the paper, use the source-level normalized count:

> We collected 440 source-level candidate URLs from official, quasi-official, authoritative, and community sources related to `AGENTS.md` and `CLAUDE.md`.

This is the main corpus count to use in the manuscript.

## Counting Rationale

Hacker News search can return thousands of story/comment hits for `AGENTS.md` and `CLAUDE.md`. Counting each Hacker News hit as an independent source would make the corpus look community-heavy and would obscure the primary evidence base: official documentation, official blogs, changelogs, engineering blogs, and product-team practice notes.

Therefore, the uploaded corpus uses source-level normalization:

1. Official and authoritative pages are counted as candidate source URLs.
2. Hacker News is included as a community source channel.
3. Individual Hacker News comments/stories are used for qualitative exploration, not as thousands of independent paper sources.

## Canonical Data File

The canonical candidate-source file is:

```text
data/candidate_sources_440.csv
```

It contains exactly 440 source-level candidate records.

## Site Distribution

The source-site distribution is stored in:

```text
data/source_site_counts.csv
```

The largest source groups include Windsurf, Devin, Augment, Ona, Factory, Kilo, opencode, Roo Code, Hugging Face, Anthropic Claude Code, OpenAI Codex, GitHub Copilot, Amp, and Hacker News.

## Audit Note

During collection, we also expanded Hacker News story/comment hits and per-site sitemap hits for audit purposes. Those intermediate files are not included as main corpus files because they are not the paper-facing source-level unit. The scripts under `scripts/` can regenerate them if needed.

