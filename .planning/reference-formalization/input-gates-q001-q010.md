# Required Input Gates Q-001–Q-010

**Rule:** A gate is open only when its accountable owner records a decision, the stated evidence is independently reviewable, scope/tenant/environment is explicit, legal disposition is recorded where relevant, expiry/revalidation is set, and the decision is linked to its dependent contract/ADR. A verbal answer, provider marketing page, or implementation preference is not evidence.

| ID | Required decision / accountable owner | Minimum acceptable input | Disposition if absent or adverse | Blocks |
|---|---|---|---|---|
| Q-001 | Jurisdiction, regulated activity, custody, payment/withdrawal permissions; Legal/Compliance owner | Written jurisdictional analysis scoped to customer, entity, assets, flow and date; explicit `ALLOWED`, `PROHIBITED`, or `REQUIRES_LEGAL_REVIEW` | `REQUIRES_LEGAL_REVIEW`; no override | M5, M6, M15, M18; payment, withdrawal, custody, customer claims |
| Q-002 | Provider/venue/wallet capability claims; Provider owner plus Legal review | Owned claim-register record: source/config snapshot, exact capability/version/region, boundary test plan/result when later available, expiry/revocation and legal disposition | `NO_PROOF`/`BLOCKED`; no adapter selection or support claim | M5–M9, M15 |
| Q-003 | Signing, key custody, authorization issuer and recovery/revocation model; Security/Custody owner | Threat-reviewed key/custody design; issuer identities; authorization format; rotation/revocation/replay and incident recovery responsibilities | `BLOCKED`; sign/network/broadcast remain denied | M6, M11, M15 |
| Q-004 | Chart of accounts, asset treatment, availability/hold/revenue/fee/refund/reversal/correction policy; Finance/Accounting owner | Approved accounting policy plus illustrative balanced postings and correction policy | `BLOCKED`; no economic event semantics finalized | M4–M6, M10–M11 |
| Q-005 | Initial asset, chain, network, venue, confirmation/finality, oracle and LP scope; Product/Risk owner | Versioned supported-scope inventory and venue/chain risk analysis, including reorg/finality/partial-fill/LP drift expectations | `NO_PROOF`/`BLOCKED`; no asset/venue/chain support claim | M7–M9, M14–M15 |
| Q-006 | Authentication, tenancy, roles, data classification, privacy/residency and retention requirements; Security/Privacy owner | Identity/tenant model, data map, role matrix and privacy disposition per jurisdiction | `BLOCKED`; no user/auth/data design is approved | M12–M16 |
| Q-007 | Risk appetite, limits, kill-switch authority, loss/incident thresholds and prohibited strategy classes; Risk owner | Signed risk taxonomy and limit/exception hierarchy; named independent approvers | `BLOCKED`; risk allow decisions and strategy execution remain denied | M9–M16 |
| Q-008 | Operations ownership, evidence retention/immutability, audit anchoring, alert/incident handling and recovery objectives; Operations/Security owner | Retention schedule, immutable-storage/anchor design decision, separate key plan, on-call and incident procedure | `NO_PROOF`/`BLOCKED`; no strong audit or operational-resilience claim | M13–M18 |
| Q-009 | Technology-language selection for frontend and critical backend; Architecture owner | Recorded evaluation against threat-safe performance, determinism, library maturity, hiring/operability, build/reproducibility, test/toolchain and interoperability criteria | `BLOCKED`; preference stays non-binding | M16 |
| Q-010 | CI, release, deployment environment, Vercel `develop` planning-only policy, attestation authority and rollback responsibility; Release owner | Environment matrix, protected-branch/release policy, provenance/rollback plan, attestation identity, Vercel scope confirmation | `BLOCKED`; no deployment/release claim | M16–M20 |

## Q-009 technology evaluation rubric

Next.js + TypeScript for the frontend and Rust for critical backend paths are the user’s preferences. They may be selected only after the Architecture owner records weighted criteria, alternatives considered, threat-model compatibility, build/reproducibility evidence, long-term operability, interoperability boundary, and an approval/revalidation date. No language selection is proven by this document.

## Gate record template

```text
Gate ID:
Owner / independent reviewer:
Decision and scope:
Evidence locator and digest:
Source/config/version snapshot:
Legal disposition (where applicable):
Environment / tenant boundary:
Expiry and revalidation trigger:
Affected ADRs/contracts/milestones:
Decision: PASS | FAIL | BLOCKED | NO_PROOF
```
