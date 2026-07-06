# Collection Scope

## Research Framing

We collect sources about repository-level instruction files used by coding agents. The focus is on `AGENTS.md` and `CLAUDE.md`, but related instruction surfaces are recorded when they clarify loading, precedence, context budget, security boundary, or portability.

The paper should not claim that every recommended practice is a defect rule. Recommended practices are background evidence. Defects require evidence that a file can mislead an agent, contradict repository facts, violate tool loading semantics, create security risk, or appear in real developer-reported failures.

## Primary Official Sources

The strongest sources are:

1. AGENTS.md official website and official repository.
2. Claude Code official documentation and engineering blogs about `CLAUDE.md`.
3. Official documentation, official blog, changelog, engineering blog, or product-team article from tools listed as AGENTS.md supporters.

The AGENTS.md supporters currently tracked are:

- Codex
- Amp
- Jules
- Cursor
- Factory
- RooCode
- Aider
- Gemini CLI
- goose
- Kilo Code
- opencode
- Phoenix
- Zed
- Semgrep
- Warp
- GitHub Copilot Coding Agent
- VS Code
- Ona
- Devin
- Windsurf
- UiPath Autopilot and Coded Agents
- Augment Code
- Junie

## Secondary Authoritative and Community Sources

We also collect sources from:

- GitHub official docs, blog, and changelog.
- Hugging Face docs, changelog, official/blog-hosted technical posts.
- OWASP pages about agentic skills, trust boundaries, and prompt/context risk.
- Meta developer docs and official Meta GitHub repositories.
- Hacker News discussion threads with concrete practitioner experience.
- Security-company posts when they provide concrete AGENTS.md or CLAUDE.md risk scenarios.

## Exclusion Criteria

Exclude or mark as background-only:

- Generic AI agent posts with no `AGENTS.md` or `CLAUDE.md` mention.
- Pure product marketing pages that only say a tool supports agents.
- Repository files that are only examples, unless they are from official product repositories and show concrete practices.
- Blog posts that discuss prompt engineering generally but not repository-level instruction files.

