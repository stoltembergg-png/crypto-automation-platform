# Withdrawals Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines future BRL Pix and crypto withdrawal intent state machines. Both remain denied until legal, provider, custody, signing and environment gates pass.

## Normative requirements

- Request binds tenant, asset/BRL, amount, destination, network, fee quote, allowlist version, security challenge and operation fingerprint.
- Destination or security-context change invalidates authorization.
- A withdrawal intent posts one economic lock; broadcast tracking does not perform a second economic mutation.
- BRL provider results and crypto confirmations/reorgs are evidence requiring reconciliation.

## Component contracts

WithdrawalIntent, DestinationApproval, FundingLock, PayoutEvidence, BroadcastEvidence, ConfirmationEvidence.

## Invariants and deny conditions

Idempotency scope is tenant+operation fingerprint+lifecycle/TTL; only same-fingerprint retry is duplicate; conflicting reuse denied generically and pseudonymously audited. No automatic retry of ambiguous broadcast.

## State and failure semantics

`INTENT_CREATED→SECURITY_PENDING→RISK_PENDING→COMPLIANCE_PENDING→PREAUTHORIZED→LOCK_POSTED→PROCESSING→SUBMITTED→CONFIRMING→COMPLETED|FAILED|CANCELLED|BROADCAST_AMBIGUOUS`.

`PREAUTHORIZED` has no ledger effect. `LOCK_POSTED` atomically verifies fresh availability and all named decisions then posts one idempotent funding lock. Timeouts/unknown provider results stay non-terminal until reconciliation. `BROADCAST_AMBIGUOUS` prohibits retry/rebroadcast on the original attempt; only correlation-matching external evidence can settle it. A new broadcast must use a linked new intent, fresh idempotency key, authorization, lock and evidence. See `docs/security/ADVERSARIAL_CLOSURE_SPEC.md` §3.2.

## Future verification

Model/property tests for one lock, mutation invalidation, duplicate request, ambiguous broadcast, wrong network, reorg and operator-resolution evidence.

## Queue ownership

Implementation is decomposed in `PR-053..PR-068`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/05-withdrawals-and-wallets.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
