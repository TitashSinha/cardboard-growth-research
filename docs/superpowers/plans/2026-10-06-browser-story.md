# Browser Story Implementation Plan

> **Execution:** Inline local artifact work with checkpoint verification; preserve the existing main checkout under Titash's explicit commit/push authorization.

**Goal:** A simple browser presentation with five editable article-review Docs.

**Architecture:** One self-contained static HTML file. Native Google Docs hold separate review drafts; the file opens their canonical links. Repository records retain source versions and traceable findings.

**Tech stack:** HTML, inline CSS, small vanilla JavaScript; Google Drive/Docs connector; existing bundled runtimes for QA.

## Global constraints

- No sending, hosting, spending, app access, analytics or sharing changes.
- Preserve all source articles and PPT/PDF versions.
- Keep identities and exact replies outside Git.
- Follow the approved [design](../specs/2026-10-06-browser-story-design.md); dated facts and proposed changes stay distinct.

## Task 1 — Article review copies

- [ ] Import all five existing drafts into private native Docs; verify complete body text, tables, lists, source links, metadata and editorial notes. Repair conversion omissions using fresh document indexes.
- [ ] Save canonical URLs and source versions in `presentation/article-review-links.json`; expose the links through a readable `presentation/article-review-links.md`.
- [ ] Check metadata for native MIME type and private state; commit/push this checkpoint with decision/status records.

## Task 2 — Standalone story

- [ ] Write `presentation/cardboard-growth-story.html` to the approved question-based outline; embed the existing conversion-copy sample with clear illustrative status.
- [ ] Add anchor navigation, native disclosures, optional active-section/progress enhancement, responsive styles, visible focus, reduced-motion and print rules. Core content must not depend on JavaScript.
- [ ] Save `presentation/html-story-source-map.md` mapping findings and proposals to existing dated project sources. Add the HTML entry to the repository/presentation navigation.

## Task 3 — Verification and delivery

- [ ] Inspect desktop/mobile and exercise menu links, disclosures, focus and print styling. Load the actual file without networking; confirm no external resource request or JavaScript error. Recheck with JavaScript disabled.
- [ ] Run `git diff --check`; check the five canonical Doc links against the manifest; review simple language and unsupported-claim boundaries.
- [ ] Record results in `quality/browser-story-review-2026-10-06.md`, commit/push explicit paths and confirm `git status --short` is empty and `git rev-parse HEAD origin/main` matches.
