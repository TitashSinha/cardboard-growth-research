# AAARRR: independent work and later company measurements

2026-10-03; measurement clarification added October 4 (D019). Design map only; no internal baselines or implemented events. H06 is unvalidated.

| Stage | Buyer handoff / next decision | Externally testable now | Company-dependent metric proposal |
|---|---|---|---|
| Awareness | Recognize a relevant product-video problem | Retained scoped Google/ChatGPT observations; buyer language about task | Relevant search impressions/clicks by page/query, with geography/device and reporting window |
| Acquisition | Visit a useful explanation/proof route | Review unpublished article/decision-aid clarity with consented people | Eligible landing sessions → next-action clicks, deduplicated by consented session/account; attribution limits explicit |
| Activation | Obtain a result judged usable for the actual task | Ask recent-project acceptance criteria; storyboard requirements only | New eligible accounts → user-confirmed useful first export/share within a validated window; exclude failed/empty outputs |
| Retention | Repeat the workflow when another need occurs | Research recent release/update cadence; no usage measurement | Activated accounts with mature observation window → second distinct useful project; choose window from actual cadence |
| Revenue | Pay for access/value; payment may precede activation | Record past task spending and real selection behavior; no hypothetical WTP | Mature eligible unpaid-at-account-creation cohort → first settled paid-access purchase; billing truth, test exclusions and refunds separate |
| Referral | Introduce a relevant person who gets value | Ask actual past collaboration/handoff behavior | Referred eligible accounts → attributable useful activation; separate invitations/shares from successful referrals |

Anonymous visitors, individual users and paying organizations are different denominators. The prepared specification defines proposed identity linkage, consent, duplicate handling, cohort eligibility/windows, attribution and failure events; actual semantics still require company confirmation. Do not calculate rates from mismatched counts or treat a public share as referral success.

The selected independent workflow test challenges the assumed reason to enter this funnel. It does not measure any live AAARRR outcome. The [detailed measurement specification](measurement-plan.md) and [event dictionary](measurement-events.csv) are now prepared; actual instrumentation and company baselines remain unavailable. The later experiment backlog is still pending.

October 4 / D019 clarification: AAARRR need not occur in sequence; paid access may precede a useful result. The primary proposed revenue measure in the specification uses eligible unpaid-at-account-creation cohorts, not an activation prerequisite. The earlier activated-to-paid concept is a possible secondary diagnostic only, preserved in Git history. Proposed seven-/30-day windows and analysis identity need company approval before collection, not retroactive optimization. This is a measurement design, not an observed product flow.
