# Data Model

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines relational schema boundaries and migrations for immutable financial records, tenant isolation and PII separation. It is a logical design only; migrations are future work.

## Normative requirements

- Tables include users, sessions, auth_methods, wallets, wallet_addresses, exchange_accounts, deposits, withdrawals, ledger_accounts, ledger_entries, ledger_postings, assets, chains, protocols, pools, positions, lp_positions, orders, trades, strategies, strategy_runs, strategy_proposals, risk_decisions, transactions, blockchain_transactions, market_snapshots, audit_events and api_credentials_metadata.
- Secrets are references to a secret manager, never values.
- PII, financial records, credentials metadata and trading data have separate classification/retention rules.

## Component contracts

TenantScopedRow, ImmutableJournalEntry, Posting, ProviderEvidence, OutboxMessage, InboxRecord, ReconciliationCase.

## Invariants and deny conditions

Row-level policy and application authorization must agree; every financial mutation has correlation/idempotency keys; posted journal rows are immutable; corrections are compensating entries. Accounts, events, journal entries and postings carry tenant/environment and use composite scoped foreign keys. A balanced entry spanning tenants/environments is denied even for service roles/migrations. The Ledger accepts only an Accounting Authority-issued `AccountingCommand.v1`; direct reconciliation/adapter/AI writes are denied. `GLOBAL` classification is server-derived and permitted only for enumerated immutable public reference data, never authority, ledger, execution, audit, provider, personal or financial data.

## State and failure semantics

Migrations are expand→backfill→contract; destructive migration needs restore rehearsal and accounting sign-off.

## Future verification

Migration replay, RLS negative tests, unique/idempotency constraints, schema contract tests and retention/deletion policy tests.

## Queue ownership

Implementation is decomposed in `PR-017..PR-026`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/01-domain-data-and-module-boundaries.md; docs/reference-formalization/specifications/03-ledger-and-accounting.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
