# Manual Review Queue

## High-Priority Semantics Sources

These should be reviewed first because they can support exact loading, path, scope, precedence, and schema claims.

| Source | What to extract |
|---|---|
| S005 OpenAI Codex AGENTS.md guide | File discovery; global/project/nested loading; precedence; fallback; size behavior |
| S008 OpenAI config reference | `project_doc_max_bytes`; fallback filenames |
| S011 Claude Code memory docs | CLAUDE.md locations; imports; relationship to AGENTS.md; recommended length |
| S012 Claude Code settings | Difference between memory/context and enforceable settings |
| S026 Gemini CLI docs | Configurable context filename; AGENTS.md compatibility |
| S029 GitHub Copilot task best practices | Supported instruction files; root/nested behavior; recommended contents |
| S035 Factory AGENTS.md docs | Recommended sections and agent-facing framing |
| S039 Roo Code custom instructions | Loading and custom instruction semantics |
| S042 Kilo Code AGENTS.md docs | Loading and project-scope semantics |
| S045 opencode rules | Rules and AGENTS.md discovery |
| S046 Augment rules | AGENTS.md / CLAUDE.md compatibility and precedence |
| S050 Zed instructions | How Zed loads instructions and rules |
| S052 Windsurf AGENTS.md docs | Cascade loading behavior and recommended usage |
| S053 Devin AGENTS.md docs | Devin/Cascade loading behavior |
| S054 Junie guidelines and memory | Guideline and memory behavior |
| S056 Ona AGENTS.md docs | Recommended AGENTS.md content and usage |

## High-Priority Practice Sources

These should be reviewed for good/bad practice statements but not used alone as defect rules.

| Source | What to extract |
|---|---|
| S006 OpenAI Codex best practices | Concrete commands; constraints; done criteria |
| S013 Claude Code best practices | CLAUDE.md generation; bash commands; bloat warning |
| S032 GitHub: How to write a great agents.md | Lessons from repositories; recommended sections; anti-patterns |
| S037 Factory linters blog | Natural language instruction versus enforceable checks |
| S048 Augment good AGENTS.md blog | Concision; specificity; examples |
| S049 Augment context junk drawer | Context bloat and stale context motivation |
| S068 Hugging Face Spaces agents.md docs | Related `agents.md` practice for hosted apps |

## Pending Evidence to Resolve

| Source | Action |
|---|---|
| S034 VS Code Copilot customization | Confirm direct AGENTS.md passages and whether it duplicates GitHub docs |
| S059 Cursor rules docs | Confirm official AGENTS.md support and loading behavior |
| S060/S061 Aider docs | Confirm whether Aider officially recommends or loads AGENTS.md directly |
| S062 goose docs | Locate direct AGENTS.md support page |
| S066 Meta Wearables | Access page or find public cached/docs mirror |
| S073 Prompt Security | Locate exact AGENTS.md risk article URL |
| S074/S075 Hacker News | Collect specific item URLs and extract only concrete practice/failure examples |
| S076/S077 UiPath | Confirm whether official pages directly mention AGENTS.md |

