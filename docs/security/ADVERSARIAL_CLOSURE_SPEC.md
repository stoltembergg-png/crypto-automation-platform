# Adversarial Closure Specification

**Status:** `PROPOSED · PLANNING_ONLY · FAIL_CLOSED`
**Authority:** See `docs/architecture/SPEC_PRECEDENCE.md`. This amendment is the canonical corrective contract for the post-documentation adversarial review. It grants no financial, provider, custody, legal, CI/CD or mainnet capability.

## 1. Universal command boundary

Only a deterministic, authenticated **Accounting Authority** may emit `AccountingCommand.v1`; only the Ledger may apply it. Every command must contain `command_id`, `correlation_id`, `tenant_id`, `environment`, `economic_event_id`, `action_type`, `policy_decision_digest`, `accounting_policy_digest`, issuer identity and expiration. The Ledger must deny an absent/malformed/expired/revoked command, non-enumerated action, caller without the Ledger-write capability, or a command whose tenant/environment differs from every referenced record.

AI, API clients, provider adapters, reconciliation, reports, diagrams, audit projections and human UI requests can create evidence, proposals or review cases only. They have no direct ledger-write or signing capability. `GLOBAL` is server-derived from an immutable contract-classification registry and is permitted only for enumerated public reference data; it is prohibited for authority, ledger, execution, audit, provider, personal, policy-decision or financial objects.

### 1.1 Tenant/account invariant

Accounts, economic events, journal entries, postings, intents, evidence, decisions, audit events, idempotency records and capability grants carry `tenant_id` and `environment`. Postings use composite, tenant/environment-scoped foreign keys to both journal entry and account. A journal entry may not contain postings from more than one tenant or environment. Service-role/migration paths must receive the same database constraints and negative cross-tenant tests as user paths; RLS alone is insufficient.

### 1.2 Signed decision issuer verification

`PolicyDecision.v1`, `ComplianceDecision.v1`, `FraudRiskDecision.v1`, `MainnetAuthorization.v1` and capability grants bind `schema_version`, `decision_id`, canonical payload digest, `issuer_id`, `key_id`, algorithm, issuance/expiry, revocation reference, trust-anchor reference, tenant, environment, operation fingerprint, correlation ID and policy/catalog digests. Verification resolves `issuer_id/key_id` only through a versioned trust registry; unknown key, algorithm, schema, issuer, trust anchor, digest mismatch, scope mismatch, expiry or revocation denies. No payload field can nominate itself as `GLOBAL`, issuer or trusted authority.

## 2. Gate and evidence rules

`Q-001..Q-010` mean exactly the canonical decisions in `.planning/master/GATE_REGISTRY.md`. No bare range or local reinterpretation is valid. A named gate evaluation requires reproducible source/config snapshot, UTC observed-at, canonical/final URL or system path, collector/retrieval method, digest, applicability/scope, effective version/date where available, owner/reviewer, expiry/revalidation trigger, disposition and revocation/conflict state. URL reachability is retrieval proof only.

A `MainnetAuthorization.v1` additionally binds exact action vocabulary, operation/resource fingerprint, amount/asset/network/destination or contract envelope digest, tenant, environment attestation digest, Q-registry digest, exact required Q-IDs, evidence digests, policy/risk/simulation/guard/compliance/fraud decision digests, per-limit reservation IDs, expiry, nonce, issuer quorum and revocation state. Distinct-principal quorum and reset authority must be defined by Q-010; no generic approval, prior paper/testnet result, document or alias deployment can substitute it.

## 3. Payments, withdrawals and reconciliation

### 3.1 Provider evidence and disputes

Provider notifications are untrusted external evidence. Durable inbox/idempotency validation, normalized typed event, provider-side re-query where a future provider contract permits it, evidence correlation, and explicit availability policy precede any ledger command. Deposit, fee, reversal/refund/chargeback/dispute, settlement and correction are distinct events; an event never implies another. A dispute/reversal transitions funds to a defined protected/reserved/review state through authorized AccountingCommand and opens a reconciliation case. It never silently reuses a completed deposit posting.

### 3.2 Withdrawal intent and one economic lock

The canonical flow is:

`INTENT_CREATED → SECURITY_PENDING → RISK_PENDING → COMPLIANCE_PENDING → PREAUTHORIZED → LOCK_POSTED → PROCESSING → SUBMITTED → CONFIRMING → COMPLETED | FAILED | CANCELLED | BROADCAST_AMBIGUOUS`.

`PREAUTHORIZED` creates no accounting posting. `LOCK_POSTED` atomically verifies fresh availability, expected version and all named decisions, then posts one idempotent funding lock. Expiry, denial, revocation or capability loss before `LOCK_POSTED` creates no economic event. Adapter submission requires durable persisted intent, correlation, outbox record, lock ID, valid per-operation authorization and capability grant; a generic adapter `withdraw`/`send` must reject any call without them.

`BROADCAST_AMBIGUOUS` is terminal for the original broadcast attempt except evidence collection: no rebroadcast, retry or compensation transition exists on it. Only verified, correlation-matching external evidence can reconcile it to the original terminal economic outcome. A recovery that needs another broadcast creates a **new linked intent**, new idempotency key, fresh lock/authorization/decisions and new submission evidence after authorized resolution of the original lock. Unknown venue results use provider-negotiated semantics only; absent semantics fail closed to `PENDING/MISSING_EVIDENCE`.

### 3.3 Comparable reconciliation cut

`ReconciliationRun.v1` includes internal-ledger cutoff, tenant/environment, source account/asset scope, observation IDs/digests, retrieval time/cursor, source completeness/pagination state, chain block/finality where applicable, tolerance/policy version and reviewer. `MATCHED` is prohibited unless the run has a complete comparable cut; otherwise status is `PENDING`, `MISSING_EVIDENCE`, `STALE` or `MISMATCH`. Reconciliation produces `CorrectionProposal` only; Accounting Authority must independently authorize any `AccountingCommand` before Ledger accepts it.

## 4. Market, execution and chain safety

### 4.1 Arbitrage and capital reservation

An opportunity is executable only with a serialized `QuoteReservation` containing venue/market path, input snapshot digest, observed-at/expiry, expected cost model/version, amount, exposure/capital reservation IDs and simulation digest. The execution plan expires when quote, reservation, market-data freshness, policy, finality assumption, decision or guard digest changes.

`NetPnL = realised_fill_proceeds - realised_fill_costs - actual_fees - gas - withdrawal/bridge costs - recovery_costs + conservative_residual_liquidation_value`. A partial first leg, unavailable hedge, cancellation, reorg, stale quote or forced residual requires explicit `RECOVERY_REQUIRED` and may not satisfy a profit threshold through theoretical full-cycle spread. Exposure limits include correlation, concentrated-LP impermanent-loss stress, adverse liquidity and cross-position aggregate limits before a strategy can propose activation.

### 4.2 Chain/DEX transaction envelope

The Guard accepts a finite, versioned transaction-envelope grammar. It recursively decodes every supported nested router command; all nested token, spender, recipient, amount/value, deadline, permit, unwrap/sweep, approval and call target must bind to the approved plan. Unknown dynamic subcall, arbitrary calldata, unsupported permit, hidden sweep/recipient or unbound approval denies. Upgradeable targets bind proxy type, beacon/implementation slot, code hashes and pinned block; a change requires resimulation and reauthorization. Chain observations require independently comparable provider observations or explicit equivocation handling, chain-family finality policy, pinned block/hash and reorg transition.

Nonce lifecycle is exclusive: `RESERVED → SUBMITTED → CONFIRMED | REPLACED | EXPIRED | AMBIGUOUS`; only one active submitter owns a nonce reservation, and recovery/replacement requires fresh signed authorization bound to the same account/nonce policy. An LP position becomes `ACTIVE` only after finality threshold; reorg moves it to `RECONCILIATION_REQUIRED`, never silently active.

### 4.3 Submission and MEV

Each plan has a submission policy with exposure class, allowed channels, deadline and fallback rule. Public-channel fallback, protected/private relay use, bundle use or channel change requires fresh simulation and reauthorization. No channel claims guaranteed privacy, ordering or inclusion. Adverse ordering, sandwich/backrun, quote movement and failed-inclusion cost are modeled as deny/recovery scenarios, never as a permission to manipulate markets.

## 5. Compliance, fraud, privacy and audit

`ComplianceDecision.v1` is independent from generic legal disposition and binds subject, payer where applicable, destination, asset/network, transaction fingerprint, provider/list/rule version, screening time, expiry, result (`ALLOW|DENY|HOLD|REVIEW`) and reviewer/appeal reference. `FraudRiskDecision.v1` binds privacy-classified device trust, recovery/security-context changes, account age, payer/destination linkage, velocity aggregates, dispute history, model/rule version and result. Payment credit availability, withdrawal lock and external submission require current ALLOW decisions; HOLD/REVIEW has no spend path. Step-up authorization is invalidated by destination, device, credential, recovery, risk/compliance or security-context change.

Personal data has a purpose, classification, retention owner, deletion trigger and legal-hold/immutable-record exception reference. Immutable audit retention stores minimised/pseudonymous references rather than unrestricted payloads; access/replay uses redaction and purpose checks.

Audit sequence assigns hash-chain order inside the same committed financial transaction or an explicitly linked transaction boundary. It must serialize predecessor assignment, record event/payload canonical digest, correlation/tenant/environment and separately controlled signing-key identity. Internal hash chains are tamper-evidence only. Independently retained periodic anchors, immutable retention controls, key separation and incident response are future prerequisites before any stronger claim.

## 6. Operability and supply chain

Every kill scope (global, user, strategy, protocol, chain, exchange) feeds one scope-matching deny check before signing/submission. The contract defines propagation/max-staleness, in-flight handling, authorized reset/revocation, and per-scope drill evidence. Alerts, incident response and chaos tests have measurable future acceptance thresholds, owners and missing-data behavior; an alert without a tested response path is insufficient.

Q-010 future controls require SHA-pinned third-party Actions, least privilege permissions, protected environments/OIDC claim restrictions, immutable digest promotion with provenance/SBOM verification and a protected evidence-root. The Vercel `/develop` project is static-only: no financial API route, secret, provider credential, capability egress or operation authority; deployment status is not financial readiness.

## 7. Required future negative tests

At minimum: cross-tenant balanced posting; forged GLOBAL classification; invalid issuer/key; stale/expired/conflicting evidence; duplicate/out-of-order provider event; Pix dispute/chargeback; pre-lock denial without posting; ambiguous broadcast no-retry; adapter call without durable intent/outbox; incomplete reconciliation cut; partial fill with unavailable hedge; quote reservation race; nested permit/sweep/proxy change; chain equivocation/reorg; nonce conflict; LP reorg; MEV channel fallback; mule/velocity cash-out; changed step-up context; scoped kill propagation; audit concurrent ordering; supply-chain evidence-root substitution; and exact gate semantic parity.
