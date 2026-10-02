# Decisions and blockers

## D001 — 2026-10-02 — Phase 0 — Execution scope
- Evidence: user instruction; original cardoboard-growth-plan.md (copied as plan.md).
- Decision: preserve parent learning notes and original plan; work in a separate cardboard-growth repository. Complete Phases 0–6; Phase 7 is excluded.
- Alternatives: edit parent workspace (rejected: unrelated learning materials); wait for internal access (rejected: public-only scope).
- Constraints: zero spend; no internal access; no messages, applications, social publishing, or company-site edits.
- Workaround: public evidence, explicit manual worksheets where direct observation is unavailable.
- Validation: original files inspected; parent is not a Git repository.
- Status: resolved. Remaining uncertainty: account/tool access being checked.
- Next action: verify free tools and GitHub authentication; push each coherent work unit if available.

## D002 — 2026-10-02 — Phase 0 — Repository and goal support
- Evidence: E000; successful Git push; GitHub private visibility readback; CLI help and goal tools.
- Choice: new private TitashSinha/cardboard-growth-research; native goal tool per phase. Use existing Git credential helper; no CLI installation.
- Alternatives: connector-only writes or public repository rejected as unnecessary or outside plan.
- Workaround: gh unavailable; authenticated browser creates repository and Git pushes.
- Validation: initial 58f1559 pushed to origin/main successfully.
- Status: resolved. Uncertainty: future network availability only. Next: research.
