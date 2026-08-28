# Hyperplan Insight Bundle: Crypto Automation Platform Planning

## Original User Request

Create, without implementing financial runtime, an implementation-ready SDD for a Brazilian web platform that can eventually receive BRL through Mercado Pago Pix, account through an internal ledger, permit bounded automated crypto strategies, track portfolio/risk/operations in real time, and later support BRL/crypto withdrawals, external wallets, CEX/DEX arbitrage, LP management and constrained AI assistance. The user requires a modular architecture, security/threat/compliance review, ADRs, diagrams, property/adversarial/chaos test design, 20 milestones, a dependency DAG and a traceable executable small-PR queue. No real credentials, money, trades, wallets, testnet/mainnet interaction, or legal conclusion is authorized in this phase.

## Hard Constraints (Survived Review)

- **Capital-flow authority is deterministic.** AI only has proposal-surface access and no route to signing, capital allocation, policy mutation, allowlist mutation, or privileged state mutation. A finite action vocabulary, typed/versioned proposal schema, semantic kernel checks, pinned policy version, independent deterministic gates, and default-deny handling are required. — S5, V2, A1, C1
- **The availability ledger is singular and double-entry.** External provider/chain/exchange observations, inbound deliveries, operational workflows, accounting events, and reconciliation results are separate correlated records. The ledger must not infer settlement or finality, and only declared accounting events change economic balances. — V1, R4, A2, C2 surviving fragment
- **External movement is not cross-system atomic.** Provider contract, source-of-settlement, event provenance, delivery id, accounting state, idempotency key, correlation id, and reconciliation owner must be separately persisted. Transactional inbox/outbox controls local persistence/delivery only. — V1, A2
- **Real capability is denied by default.** Every payment, exchange, wallet, signer, chain, DEX, withdrawal and mainnet integration remains disabled without an owned expiring/revocable claim record, versioned source/config snapshot, contract/boundary test, and non-overridable legal disposition. — R1–R5
- **Privileged execution has a narrow capability boundary.** No tenant-facing path has ambient credentials. Attenuated grants bind service identity, tenant, operation/resource, audience, expiry, rotation and revocation; invalid, unavailable, malicious or conflicting adapter responses are contained and translated to domain-safe errors. — A3, C4
- **Mainnet is an operation-level authorization decision, not a boolean.** It is denied at the privileged spend boundary unless a current signed/versioned authorization artifact binds tenant, operation, environment, legal state, expiry, revocation and replay protection; environment identity attestation mismatches deny signing/broadcast and retain bounded telemetry. — V4, A4, R5
- **Audit log claims are bounded.** PostgreSQL append-only hash-linked events are operational tamper detection only; stronger resistance needs distinct signing keys, external immutable anchoring, periodic verification and incident response. No audit pattern is itself evidence of compliance. — A5
- **Maturity unlocks narrow capabilities by evidence.** Paper, simulation, testnet and limited-mainnet milestones neither imply legal/custody/provider readiness nor unlock broad system access. Each gate has attributable source, reviewer/owner, expiry, revocation/regression rule, measurable acceptance criteria and a single owned capability. — S3, C5
- **Traceability is selective and mechanical.** It links high-risk requirement, state transition, policy, simulation, audit event and PR proof with versioned node semantics, correlation IDs and bypass tests. Card count is not a quality target; every card must independently carry proof value, owner and revalidation trigger. — S6, C6

## Decisions (Converged Through Debate)

1. **Start with a modular monolith but enforce it.** Modules own persistence; cross-module writes are forbidden except through a capability-scoped transaction kernel for explicitly justified atomic workflows. Dependency direction and data ownership must be mechanically tested. — S1, C3
2. **Define broker-neutral events but implement local delivery with PostgreSQL only initially.** Versioned contracts, inbox/idempotency, replay-safe consumers and workload evidence precede Redis, Kafka, NATS or a service split. — S2
3. **First strategy maturity is proposal and simulation only.** A proposal cannot be promoted into funded execution; any future promotion needs suitability/reliance review, model bounds, deterministic policy verdict and separately approved maturity gate. — S3
4. **Withdrawals and MetaMask are specified now but remain formally denied.** Their reservation, authorization, destination-change, recovery and audit invariants exist before the first spend path; no provider semantics is assumed. — S4, V3
5. **Model payment evidence as typed lifecycle events, not one “paid” row.** Authorization/capture, fee, reversal/refund, settlement, correction, malformed delivery and conflict are distinct typed records; duplicate/conflicting evidence is quarantined/audited, never repaired by a balancing correction. — V1
6. **Use a per-operation evidence/claim register.** A single owner manages technical evidence snapshots/tests; legal disposition can block and cannot be overridden by a technical claim. — R3
7. **Do not prescribe implementation languages as established fact.** Preserve a language-neutral safety contract. The user’s Rust/Next preference is recorded as a candidate, and a bounded foundation spike must supply team/tooling/performance evidence before language-specific kernels are committed. — A6 conceded; retained fragment

## Risks & Mitigations

- **Provider webhook ambiguity/replay/out-of-order delivery** — inbox uniqueness on provider evidence identity, state-machine conflict transition, canonical provider re-query, and reconciliation case; test duplicate/conflict/malformed/reversal. — V1, A2
- **LLM prompt or output abuse** — bounded schema, payload redaction/size cap, proposal provenance, finite action vocabulary, default deny, no signer capability. — V2, A1
- **Withdrawal spend/reuse under ambiguity** — idempotent withdrawal intent locks funds once; broadcast tracking performs no economic posting; only verified outcome settles/releases. — V3
- **Cross-tenant data/credential escalation** — tenant operation fingerprint; pseudonymous denial audit; RLS/application tests; attenuated service capability grants. — V6, A3
- **Misconfigured mainnet** — independent environment attestation at privileged spend boundary plus signed authorization artifact; no networking/signing on deny. — V4, A4
- **External market failure** — per-venue capability contract and separate handling for partial fills, reorg/finality, quote expiry, LP drift and exposure limits; no universal adapter lifecycle. — V5
- **Audit rewrite by privileged operator** — external hash anchor and retention independent from production database; periodic verifier and incident response. — A5
- **False product claims** — forbid “capital protection” or suitability promises; use “capital-preservation controls”, risk disclosures and legal review gates. — C1
- **Planning bureaucracy** — admission rule requiring a distinct artifact/proof/owner; no PR-count target. — S6, C6

## Open Questions (Unresolved)

- Q-001 through Q-010 in `.planning/master/OPEN_QUESTIONS.md` remain unresolved; their dependent capability is blocked, not guessed.
- Exact legal/regulatory classification, legal entity, custody/custodian, Mercado Pago contractual product/eligibility, KYC/KYT providers, exchange/asset universe, tax/accounting, approval quorum and LGPD processing model are all decision gates.
- The backend language selection remains a bounded M1 foundation decision pending a reproducible capability/performance/tooling spike; no runtime implementation is authorized regardless.

## Adversarial Provenance

- skeptic: 6 materially refined survivors
- validator: 6 materially refined survivors
- researcher: 1 defended + 4 materially refined survivors
- architect: 5 materially refined survivors; A6 conceded and excluded as a prescribed stack claim
- creative: 5 materially refined survivors; C2 conceded as authoritative-ledger claim, with only its separate operational-workflow fragment retained
- filtered out: 2 original claims conceded; all remaining survivors refined to state explicit boundaries/tests

## Evidence Status

This bundle is planning evidence only. The source ledger in `.planning/master/SOURCES_EVIDENCE.md` establishes at most direct-document reachability/content snapshots. It proves neither contractual eligibility, legal authority, provider capability, credential scope, integration behavior, nor production readiness.
