# SDD-09 — Reconciliation, Audit and Observability

**Status:** proposed evidence and detection design. Hash links alone provide tamper detection, not a strong immutability guarantee.

## Reconciliation
Reconciliation correlates: authorization/proposal, execution request, local outbox/inbox, provider/venue/chain evidence, accounting event and external settlement/finality observation. It classifies `MATCHED`, `PENDING`, `MISSING_EVIDENCE`, `CONFLICT`, `STALE`, `REORGED`, `DISPUTED`, `CORRECTION_PROPOSED` and `CLOSED`. It cannot mutate a balance; correction flows back through normal authority and Ledger accounting-event rules.

## Audit
Each audit entry is append-only and includes UTC time, actor/service identity, tenant/environment, action/resource hash, policy/contract version, correlation/causation, prior-entry hash, current hash and redacted disposition. A Postgres hash-linked sequence detects alteration in the stored sequence but is not by itself immutable, independently witnessed or resistant to privileged database/key compromise.

Stronger audit claims are prohibited until Q-008 evidence covers: external anchoring cadence/location, signing keys separate from operational database control, immutable/WORM retention with access boundaries, legal retention/hold requirements, verified restore and a tested incident procedure for chain/key/anchor failure.

## Observability
Telemetry is bounded, structured, tenant-safe and classified. Required signals: authority denial reason; policy/authorization/revocation mismatch; environment mismatch; provider claim expiry; outbox/inbox lag; unreconciled age; ledger invariant breach; reorg/partial-fill/LP drift observation; audit-chain verification failure; release-gate block. Secrets, full wallet data and sensitive financial data are redacted or tokenized according to classification.

## Tests
Injected late/duplicate/conflicting/no evidence; reconciliation aging; hash-chain deletion/substitution; unauthorized audit read; anchor/key/retention absence; telemetry payload overcollection; alert suppression/overload. Assertions distinguish detect, alert, contain and correct—none may be conflated.
