# SDD-03 — Singular Double-Entry Availability Ledger

**Status:** Proposed accounting semantics; requires Q-004 approval before implementation.

## Principle
The Ledger module is the sole authoritative economic availability record. It contains balanced, immutable postings produced by declared accounting events. Provider statuses, chain logs, UI workflow state, dispatch success and reconciliation findings are separate correlated facts and MUST NOT mutate balances directly.

## Core model
An `AccountingEvent` has immutable ID/version, tenant, asset, event type, effective/recorded timestamps, idempotency scope/key, correlation/causation IDs, policy/authorization references, source evidence references, and a non-empty balanced set of postings. Each posting names ledger account, debit/credit direction, asset quantity, availability classification and metadata classification. For each asset and event: total debits equal total credits. Multi-asset conversions require explicitly linked balanced legs and approved valuation/fee treatment; no implicit netting.

## Availability and correction
Available, reserved/locked, pending, settled and unavailable are ledger-defined account classes, not booleans inferred from external systems. A lock is one posted accounting event with tenant/action/intent idempotency. A posted event never changes; error correction uses a separately authorized compensating accounting event with causal reference. Reconciliation may propose a correction but cannot post it without all normal authority/accounting gates.

## No cross-system atomicity
A local posting plus local outbox entry may be atomic inside the transaction kernel. Dispatch, provider acceptance, chain broadcast, settlement and observation are eventually correlated and may be unknown/conflicting. The SDD prohibits a claim of atomicity across those systems.

## Required properties
Balanced postings; per-tenant/asset conservation; no duplicate mutation; rejected/malformed/conflicting input changes nothing; ambiguous external delivery produces no second economic event; corrections are traceable; all posting consumers validate event version and tenant.
