# Crypto Automation SDD — Hyperplan Executable Formalization Plan

> **Delivery type:** documentation-only. This plan defines future work; it neither creates runtime code nor asserts a provider, legal, custody, security, test, deployment, payment, withdrawal, wallet, market, trade, or mainnet capability.

## 1. Scope boundaries and required outputs

### Goal
Produce a reviewable, internally consistent SDD baseline that makes every future privileged financial action explicitly authorized, policy-bound, ledger-accounted, evidence-gated, testable, auditable, and deny-by-default.

### In scope
1. Formal domain/data boundaries; trust and threat model; module ownership; typed contracts; state machines; audit and reconciliation semantics.
2. Specifications for ledger, payments, withdrawals, wallet/MetaMask, market/exchange/chain/DEX, arbitrage/LP, strategy/AI/risk/execution/guards, auth/security, observability, backtest/paper/testnet/mainnet, CI/release/compliance.
3. A decision record sequence, critical-path DAG, high-risk traceability, Q-001–Q-010 input gates, adversarial review, architecture/contract test catalog, PR queue, and readiness matrix.
4. A language-selection evidence gate that records the preference for **Next.js + TypeScript frontend** and **Rust critical backend** without selecting either until the required evidence exists.

### Out of scope and expressly prohibited in this phase
- Runtime code, infrastructure, database migrations, accounts, secrets, CI execution, a Vercel deployment change, a provider connection, wallet linkage, signing key, payment capture, fund lock, withdrawal, blockchain transaction, trade, quote, liquidity position, or user-facing financial promise.
- Any conclusion that a provider supports a workflow, that a jurisdiction permits it, that the platform is licensed/custodial, or that a control is effective.
- A cross-system atomicity claim. Ledger mutation and external/provider delivery/reconciliation remain separate correlated facts.

### Authoritative output inventory
| Path | Purpose |
|---|---|
| `docs/specifications/00-charter-scope-and-terminology.md` | Scope, terms, non-goals, approval vocabulary. |
| `docs/specifications/01-domain-data-and-module-boundaries.md` | Bounded contexts, module-owned data and read contracts. |
| `docs/specifications/02-financial-authority-and-policy-kernel.md` | Deterministic authority kernel, finite actions, policy pinning and proposals. |
| `docs/specifications/03-ledger-and-accounting.md` | Singular double-entry availability ledger and accounting events. |
| `docs/specifications/04-payments.md` | Payment lifecycle, conflicts, fees, settlement and correction. |
| `docs/specifications/05-withdrawals-and-wallets.md` | Withdrawal intent, economic locks, ambiguity, wallets and MetaMask denial. |
| `docs/specifications/06-markets-venues-and-chains.md` | Market/exchange/chain contracts and provider-claim rules. |
| `docs/specifications/07-dex-arbitrage-and-lp.md` | DEX, arbitrage and LP-specific risk/state semantics. |
| `docs/specifications/08-strategy-ai-risk-and-execution.md` | Strategy/AI proposals, risk decisions, guarded execution. |
| `docs/specifications/09-reconciliation-audit-observability.md` | Correlation, reconciliation, audit integrity limits and telemetry. |
| `docs/specifications/10-auth-trust-threat-and-security.md` | Tenant auth, trust boundaries, capabilities and threats. |
| `docs/specifications/11-environment-maturity.md` | Backtest/paper/testnet/mainnet maturity and attestation gates. |
| `docs/specifications/12-ci-release-and-compliance.md` | CI, release control and non-overridable compliance disposition. |
| `docs/contracts/*.md` | Contract catalogue, event envelopes and state-machine invariants. |
| `docs/adr/ADR-0001-*.md` through `ADR-0012-*.md` | Ordered decision records. |
| `docs/diagrams/*.mmd` | Architecture/trust/authority/ledger Mermaid diagrams. |
| `.planning/*.md` and `.planning/formalization-dag.mmd` | Formal task plan, input gates, readiness, queue, traceability, verification, review and dependency graph. |

## 2. Architecture decisions and ADR order

All ADRs begin `Proposed`, name owner and decision input, and may become `Accepted` only after their gate/approval record is attached. Later work must not quietly override an earlier ADR.

| Order | ADR | Decision | Non-negotiable consequence |
|---|---|---|---|
| 1 | ADR-0001 | Deterministic financial authority | AI can only emit typed/versioned proposals; only finite kernel actions under a pinned policy may be requested. |
| 2 | ADR-0002 | Singular double-entry availability ledger | Economic balance changes happen only through declared accounting events; no “provider status” directly changes balances. |
| 3 | ADR-0003 | Modular monolith with module-owned persistence | No cross-module write; integration uses explicitly versioned contracts. |
| 4 | ADR-0004 | Postgres inbox/outbox and broker-neutral events first | No broker or microservice split absent documented workload evidence. |
| 5 | ADR-0005 | Privileged adapter capability attenuation | Identities bind tenant, operation/resource, audience, expiry, rotation, revocation and environment. |
| 6 | ADR-0006 | Provider capability claim register | Capability claims are owned, sourced/snapshotted, expiring/revocable, boundary-tested and legally constrained. |
| 7 | ADR-0007 | Signed per-operation mainnet authorization | Spend boundary verifies signed/versioned authorization plus environment attestation, legal, expiry, revocation and replay constraints. |
| 8 | ADR-0008 | Audit integrity claim boundary | Postgres hash-links are tamper detection only; external anchor, separate keys, immutable retention and incident procedure are preconditions for stronger claims. |
| 9 | ADR-0009 | Maturity gates are narrow | Backtest/paper/testnet/mainnet unlock capability scope only; they never infer legal, custody or provider readiness. |
| 10 | ADR-0010 | Evidence-gated language selection | Next.js/TypeScript and Rust are preferences, not selected architecture, until evaluation criteria and evidence pass. |
| 11 | ADR-0011 | Withdrawal and wallet denial by default | Withdrawal/MetaMask remain unavailable until all authority, legal, provider, custody, signing and environment gates pass. |
| 12 | ADR-0012 | High-risk-only traceability | Trace only high-risk requirements/flows; every card needs an owner, proof value and revalidation trigger; no count target. |

## 3. Contracts, state machines and test families

### Contract rules
- Every contract has `contract_name`, semantic version, schema digest, tenant/environment, correlation/causation IDs, idempotency key scope, producer identity, timestamp, and sensitivity classification.
- Breaking change requires a new major version, migration/replay policy, consumer compatibility evidence and explicit security review. Unknown fields may be ignored only where a contract says so; unknown action, environment, policy, legal disposition, capability or authority values deny.
- Every command returns one typed disposition: `ACCEPTED`, `DENIED`, `DUPLICATE`, `CONFLICT`, `PENDING_EXTERNAL_EVIDENCE`, `REQUIRES_LEGAL_REVIEW`, or `INVALID`. A denial cannot produce an external privileged side effect.

### Required state machines
1. **Proposal:** `DRAFT → VALIDATED → POLICY_EVALUATED → (DENIED | REQUIRES_LEGAL_REVIEW | AWAITING_AUTHORIZATION → AUTHORIZED → EXPIRED|REVOKED|CONSUMED)`.
2. **Accounting event:** `PROPOSED → VALIDATED → POSTED | REJECTED`; a posted event is immutable and corrected only by a compensating accounting event.
3. **Payment:** `RECEIVED → AUTHORIZED → CAPTURED → SETTLED`, with explicit `FEE_ASSESSED`, `REVERSAL`, `REFUND`, `CORRECTION`, `MALFORMED`, `CONFLICT` and `RECONCILIATION_PENDING` branches.
4. **Withdrawal:** `INTENT_CREATED → ECONOMIC_LOCK_POSTED → AUTHORIZED → BROADCAST_REQUESTED → (BROADCAST_EVIDENCED | BROADCAST_AMBIGUOUS | BROADCAST_REJECTED) → CONFIRMED|FAILED|REORGED`; ambiguity forbids a second economic mutation or automatic retry.
5. **External delivery/reconciliation:** `REQUESTED → DISPATCHED → EVIDENCE_OBSERVED → RECONCILED | DISPUTED | EXPIRED`; never equate this with an accounting post.
6. **Venue order/fill:** `PROPOSED → RISK_ALLOWED → SUBMITTED → ACKNOWLEDGED → PARTIALLY_FILLED* → FILLED|CANCELLED|REJECTED|UNKNOWN`; venue-specific reorg/finality rules attach to settlement evidence.
7. **LP position:** `PROPOSED → RISK_ALLOWED → MINT_REQUESTED → ACTIVE → REBALANCE_REQUESTED|EXIT_REQUESTED → CLOSED|UNKNOWN`; price/range/fee drift have independent evidence events.

### Required test families (specified; not executed)
- **Architecture:** module import/dependency graph; forbidden cross-module write; ownership assertions; no privileged adapter bypass; Postgres inbox/outbox atomicity boundary test; no unsupported atomicity wording.
- **Contract:** schema/semantic-version compatibility; event-envelope parsing; unknown/duplicate/conflicting input; tenant-scoped idempotency; correlation and causation preservation; consumer-driven examples.
- **Ledger/accounting property tests:** balanced postings; conservation by asset/tenant; availability locks exactly once; immutable post/compensating correction; rejected/malformed/duplicate input changes nothing.
- **State-machine/model tests:** generated legal transitions; every illegal transition denies; replay/expiry/revocation; payment reversal/refund/fee/correction; ambiguous broadcast no double mutation.
- **Security/adversarial:** cross-tenant substitution, stale/revoked capability, audience mismatch, policy downgrade, forged proposal, replay, malformed provider payload, provider timeout, partial provider response, tampered audit chain, environment-attestation mismatch.
- **Market/chain/DEX:** partial fills, cancel races, stale market data, rate-limit/timeout, venue-specific confirmation/reorg/finality, oracle discrepancy, gas variance, slippage, LP price/range/fee drift, duplicate chain logs, reorg rollback correlation.
- **Readiness/release:** environment isolation, policy pin, signed authorization verification, release provenance/SBOM/scan, rollback, incident drill and retained proof revalidation.

## 4. Ordered milestones M0–M20 and gates

Each milestone produces documentation/approval/proof requirements only. “Complete” requires its named acceptance checks, not a calendar date. A failed or missing input blocks dependent milestones.

| Milestone | Deliverable / exit criteria | Depends on |
|---|---|---|
| M0 | Boundary charter, evidence vocabulary, non-runtime attestation; planning-only Vercel `develop` content constraint recorded. | — |
| M1 | Q-001–Q-010 input register with owner, due evidence and dependent work. | M0 |
| M2 | Domain glossary, module map, data classification and trust-boundary diagram. | M0 |
| M3 | ADR-0001..0004 accepted/proposed with no contradictions; contracts governance. | M1, M2 |
| M4 | Ledger/accounting spec and balance/availability invariants. | M2, M3, Q-004 |
| M5 | Payment lifecycle spec and negative-path/accounting correlation contract. | M4, Q-002, Q-004, Q-001 |
| M6 | Withdrawal/wallet/MetaMask denial spec and ambiguous-broadcast rule. | M4, Q-001, Q-002, Q-003 |
| M7 | Market/exchange capability-claim and order/fill contract specs. | M2, Q-002, Q-005 |
| M8 | Chain/DEX finality/reorg/DEX-adapter specs. | M7, Q-002, Q-005 |
| M9 | Arbitrage and LP risk/state specs including drift evidence. | M8, Q-005, Q-007 |
| M10 | AI proposal, strategy, risk and policy-kernel specifications. | M3, M4, Q-007 |
| M11 | Execution guard, signing, adapter, reconciliation and compensation specifications. | M5–M10, Q-003, Q-007 |
| M12 | Auth, capability, trust/threat and secure-data specifications. | M2, M3, Q-006, Q-007 |
| M13 | Audit integrity boundary, observability and incident-evidence specs. | M11, M12, Q-008 |
| M14 | Backtest/paper/testnet maturity matrices and test strategy. | M9–M13, Q-005, Q-007, Q-008 |
| M15 | Mainnet signed authorization, environment-attestation and denial test specification. | M6, M11–M14, Q-001–Q-008 |
| M16 | CI architecture, static quality, contract/security test gate and provenance specs. | M3–M15, Q-009, Q-010 |
| M17 | Release/rollback, change control and planning-only Vercel `develop` deployment specification. | M16, Q-010 |
| M18 | Compliance disposition, records retention and legal-review handoff specifications. | M5, M6, M15, Q-001, Q-008 |
| M19 | Independent adversarial review, high-risk traceability review and defect disposition. | M0–M18 |
| M20 | Formalization baseline freeze: integrity check, DAG/critical-path validation, overall readiness `BLOCKED`, and handoff packet. | M19 |

## 5. PR queue composition rules

The queue is **recommended exactly 21 review cards**, allowable range **20–24** only when a card has independent acceptance evidence and reviewer value. This is a queue-sizing heuristic, not a productivity target. High-risk traceability cards have **no target count**; each exists only if its proof value, owner and revalidation trigger justify it.

- One card changes a coherent document set and its cross-links; it must not mix unrelated legal, ledger and UI decisions.
- Every card declares upstream contract/ADR versions, evidence required, negative tests affected, approval role, rollback/rejection action and revalidation trigger.
- No card may mark a capability ready based only on documentation. No merge order can bypass an input gate.
- No card can change policy semantics, ledger events, privileged authority, signing requirements, withdrawal handling or provider claims without explicit security, accounting and legal-review dispositions.
- See `.planning/pr-queue.md` for IDs P01–P21, phase grouping, dependencies, and merge conditions.

## 6. DAG, critical path and parallelization

The authoritative Mermaid DAG is `.planning/formalization-dag.mmd`.

**Critical path:** `M0 → M1 → M3 → M4 → M6 → M11 → M13 → M14 → M15 → M16 → M18 → M19 → M20`. It includes the most constrained high-risk decisions (legal/provider/custody/ledger/signing/audit/environment). A missing Q gate halts its dependent edge rather than being treated as an assumption.

**Safe parallelization:** after M2/M3, M5 (payment), M7 (markets), M10 (strategy/AI), and M12 (auth/threat) may be authored in parallel; M8 follows M7; M9 follows M8; M6 never outruns ledger or legal/custody/provider gates; M13 waits on reconciliation and security semantics. Parallel workers must use distinct files and resolve all conflicting ADR/contract versions through the owner of the upstream contract.

## 7. Success criteria, verification gates and mitigations

### Completion criteria for the planning phase
1. Every inventory path exists and links resolve conceptually from `docs/README.md` or `.planning/README.md`.
2. Every privileged-flow spec names explicit deny conditions, authority source, tenant/environment binding, idempotency semantics, accounting relationship, evidence correlation, audit event and test families.
3. Each of M0–M20 has dependencies, outputs, acceptance criteria and a blocker outcome.
4. Q-001–Q-010 have owner role, evidence threshold, expiry/revalidation, decision disposition and dependent work.
5. ADRs do not contradict scope: modular monolith, module ownership, Postgres inbox/outbox first, no cross-system atomicity, AI proposal-only, ledger singularity, capability attenuation, audit claim boundary, and maturity-gate limits.
6. The mainnet matrix uses only `PASS`, `FAIL`, `BLOCKED`, `NO_PROOF`; overall status remains `BLOCKED` absent actual evidence.
7. The adversarial review rejects unsupported claims rather than converting them to assumptions.

### High-risk mitigations
| Risk | Required mitigation and verification gate |
|---|---|
| AI bypasses financial control | Finite action grammar + typed/versioned proposal + deterministic kernel + pinned policy + independent risk/legal/auth checks. Test forged/unknown/policy-downgraded proposals deny. |
| Double-spend / duplicate lock | Ledger idempotency key is tenant/action/intent scoped; post lock once; property/model tests prove duplicate and ambiguous broadcast do not create second mutation. |
| Provider assumption is false | Claim register with owner/source snapshot/boundary test/expiry/revocation/legal disposition; absent proof yields `NO_PROOF` or `BLOCKED`. |
| Cross-tenant privilege escalation | Attenuated capability binds tenant/operation/resource/audience/expiry/revocation; substitution tests deny. |
| Audit overclaim | Use “tamper detection” for hash-link only; stronger tamper-resistance blocked on external anchor, separate key, immutable retention and incident procedure evidence. |
| Reorg/partial fill/LP drift is treated as settled | Model independent venue facts and reconciliation; per-venue finality, partial-fill and LP drift tests; no balance update from a raw observation. |
| Mainnet executed under wrong environment | Signed/versioned per-operation authorization and environment attestation both required at sign/network/broadcast boundaries; mismatch denies with bounded telemetry. |
| Legal/custody release by technical maturity | `REQUIRES_LEGAL_REVIEW` non-overridable; maturity documents state no implied legal/provider/custody readiness; overall mainnet gate remains blocked. |

## 8. Input gates Q-001–Q-010

The gate register in `input-gates-q001-q010.md` is authoritative. An unresolved gate means dependent work may produce only a `BLOCKED` placeholder/disposition and may not select a provider, authorize a flow, or claim support. The exact gates cover: legal/jurisdiction/custody; provider capabilities; signing/custody; accounting policy; assets/chains/venues; identity/privacy; risk appetite; operational retention/incident responsibilities; language evaluation; and CI/release/environment authority.

## Planning-phase attestation
No code or runtime was requested or produced by this formalization plan. No acceptance criterion above is claimed as executed. The immediate deliverable is a coherent specification package for later, separately authorized work.
