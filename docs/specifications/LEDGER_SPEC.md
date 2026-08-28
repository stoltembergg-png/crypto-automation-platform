# Ledger Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines the singular double-entry availability ledger as financial authority.

## Normative requirements

- Every AccountingEvent has immutable ID/version, tenant, asset, type, effective/recorded time, idempotency scope/key, correlation/causation, policy/evidence references and balanced postings.
- Accounts distinguish pending, available, reserved, exchange custody, chain custody, protocol position, receivable, liability, revenue/fee and equity as applicable.
- Multi-asset conversion uses linked balanced legs; PnL/valuation are explicit records, never balance mutation by UI.

## Component contracts

AccountingEvent, JournalEntry, Posting, LedgerAccount, ValuationSnapshot, CompensatingEntry.

## Invariants and deny conditions

For each asset/event debits equal credits; posted entries immutable; lock exactly once; provider state cannot post directly; corrections compensate, never edit; asset=liabilities+equity where applicable.

## State and failure semantics

PROPOSED→VALIDATED→POSTED|REJECTED. Reconciliation may open a case/propose correction but cannot post without normal authority.

## Future verification

Property tests for balance/conservation/idempotency/reversal; model tests for locks; mutation tests prove forbidden direct-balance update is rejected.

## Queue ownership

Implementation is decomposed in `PR-017..PR-026`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/03-ledger-and-accounting.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
