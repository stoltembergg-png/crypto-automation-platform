# SDD-01 — Domain, Data and Module Boundaries

**Status:** Proposed; modular-monolith design only.

## Modules and owned persistence
| Module | Owns | May publish / consume |
|---|---|---|
| Identity & Tenant | tenant, principal, role, consent, tenant-scoped idempotency namespace | auth assertions; consumes no financial writes |
| Policy & Authority | policy version/hash, proposal evaluation, authorization disposition, capability verification | authority decisions; consumes proposals/risk/legal inputs |
| Ledger | account, availability, accounting event, posting, hold, correction | immutable accounting facts; consumes validated accounting commands only |
| Payments | payment intent/lifecycle/evidence correlation | payment facts and accounting commands; consumes provider evidence |
| Wallet & Withdrawal | wallet reference, withdrawal intent, authorization/broadcast evidence | withdrawal facts/accounting commands; consumes capability decisions |
| Market & Venue | instruments, quotes, orders, fills, capability claims | market/venue facts; consumes approved scopes |
| Chain & DEX | chain observations, finality/reorg state, DEX/LP observations | evidence facts; never ledger writes directly |
| Strategy & Risk | strategy version, backtest/paper evidence, risk decision, proposal | proposals/risk decisions; consumes market projections |
| Execution & Reconciliation | dispatch attempts, guard decisions, reconciliation cases | correlated evidence; consumes authorized commands |
| Audit & Observability | audit entries, telemetry, alerts, incident packages | append-only records; consumes redacted facts |
| Compliance & Release | legal disposition, retention, release approval, evidence register | gate decisions; consumes artifacts |

## Boundary rules
- Each module owns tables/collections/schema and migration namespace. Direct writes to another module’s persistence are forbidden.
- A module consumes another module only through a versioned command/event/read-model contract. Read projections must disclose freshness and source version.
- The initial topology is a modular monolith with a single Postgres transaction kernel and inbox/outbox. A separate broker/service requires workload and failure-isolation evidence recorded in an ADR.
- Tenant key is mandatory in all tenant-scoped entities, idempotency, correlation and access control. Global reference data is explicitly classified `GLOBAL`.

## Data classes and trust zones
`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `SENSITIVE_FINANCIAL`, `SECURITY_SECRET`, `LEGAL_RESTRICTED` govern collection, log redaction, retention, access and export. Provider payloads, browser/wallet input, AI output and chain/venue events begin untrusted; trusted state changes occur only after validation and authority checks.

## Required architecture tests
Static dependency tests reject forbidden imports/writes; contract tests reject cross-tenant keys; migration review validates ownership; outbox/inbox test proves a ledger command and its local event share one local transaction but makes no external atomicity claim.
