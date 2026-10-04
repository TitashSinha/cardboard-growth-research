# Cardboard growth research — interim work sample

Independent application project by Titash Sinha, with disclosed AI assistance. Zero new spending; no Cardboard account or internal access. Private repository: https://github.com/TitashSinha/cardboard-growth-research. **Research and one test are prepared; buyer feedback, experiment results and buyer-driven revision are not complete.**

## Verified observation → buyer evidence

October 2–4, 2026: three specifically checked official articles contain price claims that differ from the inspected pricing display. Trial claims also disagree between articles; the current correct trial remains unverified. This establishes information inconsistency, not lost revenue or a conversion problem. [Exact comparison](research/product-audit.md), [October 4 refresh](research/offer-refresh-2026-10-04.md), [prioritized hygiene audit](research/website-hygiene.md), [sources](research/sources.csv).

Public buyer-language research includes a historical self-reported Cardboard-use account, real-interface concerns, correction sequences and adequate-incumbent counterevidence. Roles, payment, outputs and exact dates are not independently verified. Vendor promotion is separated. [Buyer evidence review](research/buyer-evidence-review.md).

The retained baseline has **20 Google observations, 12 completed ChatGPT observations and 57 source records**. The review base 929c0d5 had 9 AI observations and 36 sources; later observations and source rereads are now retained. Additional records include rereads, role/contact routes and seven community-rule pages; they are not new buyers. The Google location is unknown and full result lists were not preserved. AI dates/efforts differ; two prompts are branded controls and one repeats an earlier prompt with different effort. These are scoped field observations, not market-wide visibility or demand. [Method](research/collection-method.md), [derived counts](research/evidence-summary.json).

## Chosen intervention → experiment

Provisional research cohort: people doing marketing in a small SaaS team who personally produced/edited a recent feature/launch video and influence workflow choice. This is not validated positioning. [Segment comparison](strategy/positioning.md), [competing hypotheses](assumptions.md).

Titash challenged incumbent adequacy first: clearer pricing/proof may not justify switching if the current method already meets the need. That actual decision changed the test priority. [Contribution and bounded ownership](strategy/contribution-log.md).

**EX01, prepared and unrun:** a neutral recent-project workflow test, followed by a prototype decision-aid task. It records concrete correction/handoff problems, incumbent strengths and reasons to keep or investigate the workflow. Offer comprehension is a conditional next test. No Cardboard output is generated or evaluated. [Preregistered protocol](experiments/workflow-fit/protocol.md), [research guide](research/buyer-research-guide.md), [uncontacted lead sourcing and unsent invitation](research/participant-sourcing.md).

## Result → revision → next action

Actual participant responses: **0**. Result: not available. Buyer-driven revision: not performed. [Empty result template](experiments/workflow-fit/results.csv), [case template](experiments/workflow-fit/case-template.md), [revision record](experiments/workflow-fit/revision-log.md).

Before version: [decision aid v1](experiments/workflow-fit/materials/decision-aid-v1.md). A small [v1.1 internal revision](experiments/workflow-fit/materials/decision-aid-v1.1.md) explicitly allows “none” as a correction answer; it is the prepared test material, not a buyer-driven after version. First content asset: [initial article](content/blogs/01-workflow-switch.md) and [brief](content/briefs/01-workflow-switch.md). Remaining four briefs/drafts await feedback; five distinct articles remain the deliverable. Internal/AI review is not buyer feedback.

Next action: Monday October 5, 10:00 Asia/Kolkata, review all six [tracked public questions](research/reddit-tracker-update-2026-10-04.md) using the [preregistered observation method](research/reddit-response-plan.md). Count spontaneous Cardboard mentions separately from firsthand recommendations; public replies cannot settle H03 alone. The [L03 invitation](outreach/participant-invitation-L03.md) remains unsent. [Route checks](research/lead-route-check.md) found that r/SaaS restricts cold DMs; L04/L01 share that constraint. A permitted opt-in route and exact authorization are needed before screening volunteers or collecting responses. Titash can demonstrate moderation and result interpretation; update the hypotheses and revise v1 before developing remaining articles. Until then, source/editorial checks and a truthful interim package can proceed.

## Scope and supporting artifacts

- [AAARRR map](strategy/funnel.md): public research/testable questions separated from company-dependent activation, retention, revenue and referral metrics. Detailed event implementation remains future work.
- [Product audit](research/product-audit.md), [technical evidence](research/technical-audit.md), [competitors](research/competitors.csv), [content coverage](research/coverage-matrix.md).
- [Verified founder route](research/founder-route.md), [interim unsent message](outreach/founder-message.md). Two Codex-operated questions and four additional Titash-reported manual posts are tracked; two additional posts currently show removal notices. No private recruitment, founder messages, applications or company changes have occurred.
- [Plan](plan.md), [status](status.md), [decisions](decisions.md), [acceptance gates](quality/acceptance-checklist.md), [critical review](quality/review-log.md).

Product quality/time savings, keyword volume, analytics, conversion, retention and business results are unavailable. No claim of independent growth-program ownership is made. Final packaging and presentation remain pending.

## Reproduce the inventory and capture checks

Run with existing Python; standard library only:

    python analysis/summarize_evidence.py --output research/evidence-summary.json
    python analysis/check_collector.py

The collector reads public pages only. A new run saves a UTC timestamped capture; an explicit new destination is also supported:

    python analysis/collect_public.py --output research/captures/my-new-capture.json

Existing destinations are refused. Original captures and Google field notes are retained; missing result lists cannot be reconstructed by the summary script. No dashboard or paid tooling is needed for this work unit.
