# Screening Protocol

## First-Round Screening

The first-round screening is mechanical and source-level. Each source is labeled with:

- `PASS`: contains `AGENTS.md`, `agents.md`, or `CLAUDE.md` and discusses a concrete practice, risk, loading rule, scope rule, precedence rule, context-size issue, or maintenance concern.
- `MAYBE`: mentions the file or ecosystem support, but the practice evidence is thin or indirect.
- `FAIL_BACKGROUND_ONLY`: relevant to agent security or agent tooling, but does not directly discuss `AGENTS.md` or `CLAUDE.md`.
- `PENDING`: source likely relevant but needs login, manual access, or additional verification.

## Practice Signal Tags

Each source can receive one or more practice tags:

- `GOOD_COMMANDS`: recommends concrete build/test/lint/run commands.
- `GOOD_SCOPE`: explains root, nested, per-directory, global, or project-level scoping.
- `GOOD_PRECEDENCE`: explains conflict resolution or loading priority.
- `GOOD_CONCISION`: recommends short or concise instruction files.
- `GOOD_STRUCTURE`: recommends structured sections, examples, or project-specific guidance.
- `GOOD_SECURITY`: recommends secrets handling, sensitive-file rules, permissions, hooks, or security checks.
- `BAD_BLOAT`: describes too much context, bloated files, or context-window degradation.
- `BAD_STALE`: describes outdated, wrong, or misleading instructions.
- `BAD_CONFLICT`: describes inconsistent instruction sources.
- `BAD_IGNORED`: describes agents ignoring or failing to follow instructions.
- `BAD_HIJACK`: describes malicious or poisoned instruction files.
- `LOADING_SEMANTICS`: gives exact file discovery, path, casing, or fallback behavior.
- `PORTABILITY`: discusses cross-tool AGENTS.md compatibility.

## Second-Round Manual Screening

The second round should be manual. For each `PASS` or high-value `MAYBE` source, record:

1. Whether the source is accepted for the paper.
2. Which claim it supports.
3. Whether it supports motivation, tool semantics, defect scenario, or repair strategy.
4. Whether the source should be cited in the paper or only used internally.

Manual labels:

- `ACCEPT_SEMANTICS`: cite for official loading/scope/precedence semantics.
- `ACCEPT_MOTIVATION`: cite for why instruction quality matters.
- `ACCEPT_DEFECT_EVIDENCE`: cite as evidence of concrete bad practice or risk.
- `ACCEPT_REPAIR`: cite for repair or best-practice recommendations.
- `REJECT_WEAK`: do not cite because evidence is weak.
- `REJECT_DUPLICATE`: covered by a stronger source.

## Key Discipline

Do not convert best practices into defect labels by themselves. For example, a source saying "keep AGENTS.md concise" motivates D8 Context Bloat, but the defect rule should still rely on concrete thresholds, tool context behavior, or observed failures.

