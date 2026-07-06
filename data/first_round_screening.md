# First-Round Screening Summary

This file summarizes the first-layer screen. The detailed registry is in `source_registry.csv`.

## PASS

These sources explicitly mention `AGENTS.md`, `agents.md`, or `CLAUDE.md` and contain concrete practice, loading, scope, security, concision, or maintenance discussion.

- S001 AGENTS.md official website
- S002 agentsmd/agents.md repository
- S005 OpenAI Codex: Custom instructions with AGENTS.md
- S006 OpenAI Codex: Best practices
- S007 OpenAI Codex: Advanced configuration
- S008 OpenAI Codex: Configuration reference
- S009 OpenAI Codex: Sample configuration
- S010 OpenAI Codex: Customization
- S011 Anthropic Claude Code: Memory
- S012 Anthropic Claude Code: Settings
- S013 Anthropic engineering blog: Claude Code best practices
- S017 Amp owner manual
- S018 Amp: From AGENT.md to AGENTS.md
- S019 Amp: Globs in AGENTS.md
- S021 Amp engineering note: Putting an Agent in an Orb
- S022 Google Jules documentation
- S025 Jules environment setup
- S026 Gemini CLI context file docs
- S027 Google AI Studio agents docs
- S029 GitHub Copilot coding agent best practices
- S031 GitHub changelog: Copilot coding agent supports AGENTS.md
- S032 GitHub Blog: How to write a great agents.md
- S035 Factory AGENTS.md docs
- S037 Factory: Using linters to direct agents
- S038 Factory setup checklist
- S039 Roo Code custom instructions
- S040 Roo Code v3.24 AGENTS.md support
- S042 Kilo Code AGENTS.md docs
- S045 opencode rules
- S046 Augment rules
- S048 Augment: A good AGENTS.md is a model upgrade
- S049 Augment: Agent context is a junk drawer
- S050 Zed agent instructions
- S051 Warp rules for agents
- S052 Windsurf AGENTS.md docs
- S053 Devin Desktop AGENTS.md docs
- S054 Junie guidelines and memory
- S056 Ona AGENTS.md docs
- S068 Hugging Face Spaces agents.md docs

## MAYBE

These sources mention the file or ecosystem support, but the concrete practice evidence is weaker, indirect, or needs manual passage extraction.

- S003 OpenAI AAIF announcement
- S004 Linux Foundation AAIF announcement
- S014 Anthropic: Effective context engineering
- S015 Claude Code hooks guide
- S016 Claude Code subagents
- S020 Amp: Multiple AGENT.md files
- S023 Jules Agent Update
- S024 Jules out of beta
- S028 Google Cloud Mainframe Assessment Tool
- S030 GitHub repository custom instructions
- S033 GitHub Copilot code review AGENTS.md support
- S036 Factory joins AGENTS.md collaboration
- S041 Roo Code v3.38
- S043 Kilo memory bank
- S044 Kilo blog about AGENTS.md and docs
- S047 Augment setup guidelines
- S055 JetBrains joins AAIF
- S057 Ona optimized AGENTS.md template
- S058 Cursor official forum AGENTS.md answer
- S063 Phoenix 1.8 release
- S067 Meta Wearables developer tools repository
- S069 Hugging Face changelog
- S070 Hugging Face blog

## PENDING

These sources likely matter, but direct access or exact passages need additional verification.

- S034 VS Code Copilot customization
- S059 Cursor rules docs
- S060 Aider coding conventions
- S061 Aider YAML configuration
- S062 goose documentation
- S066 Meta AI-assisted development AGENTS.md
- S073 Prompt Security AGENTS.md risk article
- S074 Hacker News AGENTS.md threads
- S075 Hacker News CLAUDE.md threads
- S076 UiPath CLI with Coding Agents
- S077 UiPath Coding Agents product page

## FAIL_BACKGROUND_ONLY

These sources are relevant background but do not currently satisfy the first-round condition of directly discussing `AGENTS.md` or `CLAUDE.md`.

- S064 Semgrep Guardian docs
- S065 Semgrep security skills blog
- S071 OWASP LLM and GenAI security resources
- S072 OWASP Agentic AI threat and mitigation resources

## Immediate Manual Review Priority

Prioritize sources in this order:

1. S005, S011, S029, S035, S042, S046, S052, S054: official semantics for loading and scope.
2. S006, S013, S032, S037, S048, S049: official or product-team practice guidance.
3. S068, S066, S073, S074, S075: secondary ecosystem/security/community evidence.
4. S034, S059, S060, S062: unsupported or underverified supporter tools.

