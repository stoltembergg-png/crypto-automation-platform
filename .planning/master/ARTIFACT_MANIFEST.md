# Planning Artifact Manifest

`PLANNED` means a document is required by the user mandate; it is not a claim that its contents have been reviewed or that its controls exist.

## Architecture and product

- `docs/specifications/PRODUCT_SPEC.md` — product scope, users, automation modes, feature flags, MVP cuts.
- `docs/architecture/SYSTEM_ARCHITECTURE.md` — boundaries, containers, modules, deployment topology, diagrams.
- `docs/architecture/DOMAIN_MODEL.md` — aggregates, events, invariants, state ownership.
- `docs/architecture/DATA_MODEL.md` — tables, tenancy, retention, ownership, migration rules.
- `docs/security/TRUST_BOUNDARIES.md` — actors, data classifications, trust transitions.
- `docs/security/THREAT_MODEL.md` — STRIDE/financial abuse cases and mitigations.
- `docs/architecture/CUSTODY_MODEL.md` — custody comparison, selected phases, signing model.

## Financial and execution specifications

- `docs/specifications/{LEDGER,PAYMENTS,WITHDRAWALS,WALLET,MARKET_DATA,EXCHANGE_ADAPTER,CHAIN_ADAPTER,DEX_ADAPTER,ARBITRAGE_ENGINE,LIQUIDITY_ENGINE,STRATEGY_ENGINE,AI_ORCHESTRATOR,RISK_ENGINE,EXECUTION_ENGINE,TRANSACTION_GUARD,RECONCILIATION,AUDIT,AUTH,SECURITY,OBSERVABILITY,BACKTESTING,PAPER_TRADING,TESTNET,MAINNET_ACTIVATION,CI_CD,RELEASE}_SPEC.md`.
- `docs/compliance/COMPLIANCE_REVIEW.md` — blockers and owner-gated questions.
- `docs/testing/TESTING_STRATEGY.md` — test layers, property/adversarial/chaos/contract evidence.

## Decisions and control artifacts

- `docs/adrs/ADR-001..015-*.md` — technology, boundary, ledger, custody, signing, AI, market-data and adapter decisions.
- `.planning/contracts/` — versioned payload/interface/state-machine contracts.
- `.planning/master/` — decision record, assumptions/questions, risk registers, traceability, mainnet readiness, source evidence.
- `.planning/queue/` — catalog, one-card-per-PR contracts, dependency DAG, milestone plan, critical path.
- `.planning/reviews/` — Hyperplan rounds and adversarial synthesis.

## Validation expectation for this planning phase

All Markdown/YAML/JSON artifacts will be mechanically checked for required paths, stable IDs, non-cyclic DAG edges, references, ownership, and requirement→specification→test→PR traceability. That validates document integrity only; it is **not implementation, security, provider, legal, or mainnet evidence**.
