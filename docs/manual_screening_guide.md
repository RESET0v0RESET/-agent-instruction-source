# Manual Screening Guide

Use `data/candidate_sources_440.csv` as the source of truth for the paper-facing corpus. `data/source_registry.csv` is the manually curated seed table and should not be treated as the full corpus.

## Recommended Workflow

1. Open all rows with `first_round_status=PASS`.
2. For each source, inspect the page directly.
3. Highlight concrete statements about:
   - where files are loaded from;
   - file naming and casing;
   - root/nested/global/project scope;
   - fallback or precedence behavior;
   - concrete commands, tests, or verification;
   - context size, concision, or bloat;
   - secrets, sensitive files, permissions, hooks, and enforcement;
   - real failure or bad-practice examples.
4. Fill `second_round_status` and `manual_notes`.
5. Only move a source into the paper's citation set when it supports a specific claim.

## Suggested Paper Mapping

- Tool loading semantics: D6 Invalid Path / Schema, D7 Context Files Conflict.
- Commands and verification: D2 Stale Commands, D3 Verification Gap.
- Path and scope: D1 Stale References.
- Security and high-risk operations: D4 High-Risk Operation, D5 Credential Exposure.
- Context budget and concision: D8 Context Bloat.
- Ecosystem adoption only: Introduction/background, not defect taxonomy.

## Manual Review Output

For each accepted source, record:

```text
source_id:
accepted_claim:
evidence_type: semantics | motivation | defect | repair
linked_defects:
quote_or_paraphrase:
paper_location:
```
