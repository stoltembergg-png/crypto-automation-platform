# Reconciliation Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines periodic and event-driven comparison of ledger with payment, exchange, wallet, on-chain and position evidence.

## Normative requirements

- Reconcile internal ledger, exchange balances, wallet balances, on-chain positions, protocol positions and Mercado Pago transaction evidence.
- Difference creates immutable case with severity, evidence, owner, aging SLA and capability-block scope.
- Reconciliation cannot silently mutate balance; any correction follows accounting authority.

## Component contracts

ReconciliationRun, ReconciliationItem, MismatchCase, EvidenceSet, CorrectionProposal.

## Invariants and deny conditions

Unexplained/mature mismatch blocks affected strategy/provider/withdrawal/mainnet scope. A missing provider response is NO_PROOF, not zero balance.

## State and failure semantics

SCHEDULED→COLLECTING→COMPARING→MATCHED|MISMATCH→INVESTIGATING→RESOLVED|ESCALATED.

## Future verification

Fixture comparisons, tolerance policy tests, missing/duplicate evidence, aged mismatch kill-switch and correction authorization tests.

## Queue ownership

Implementation is decomposed in `PR-061..PR-067`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/09-reconciliation-audit-observability.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
