# Payments Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines official Mercado Pago Pix integration as a future evidence-gated adapter, not an approved capability. References [4] and [5] are documentation snapshots only.

## Normative requirements

- Deposit request creates an internal payment intent and provider request correlation, never an available balance.
- Webhook is untrusted delivery: verify current provider signature contract, store raw/redacted evidence, deduplicate, query canonical provider API, compare amount/currency/reference/customer and apply state transition.
- Authorization/capture, fee, reversal/refund/chargeback, settlement, correction, malformed and conflict are distinct typed facts.

## Component contracts

PaymentIntent, ProviderEvidence, WebhookInbox, PaymentLifecycleEvent, ProviderClaim, ReconciliationCase.

## Invariants and deny conditions

No cross-system atomicity; duplicate/conflicting/malformed evidence is quarantined/audited; no balancing correction repairs unknown provider input; availability changes only through declared ledger accounting event after policy settlement rule.

## State and failure semantics

RECEIVED→AUTHORIZED→CAPTURED→SETTLED with FEE_ASSESSED, REVERSAL, REFUND, CHARGEBACK_OR_DISPUTE, CORRECTION, MALFORMED, CONFLICT and RECONCILIATION_PENDING branches. A dispute/reversal produces protected/reserved/review state only through authorized AccountingCommand and reconciliation case; it never silently reuses a deposit posting.

## Future verification

Sandbox contract tests, signed webhook replay/conflict tests, canonical-query failure tests, ledger separation tests and reconciliation aging tests.

## Queue ownership

Implementation is decomposed in `PR-027..PR-034`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/04-payments.md; .planning/master/SOURCES_EVIDENCE.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
