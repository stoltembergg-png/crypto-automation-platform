# Product Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines a capital-preservation-control platform, not a promise of profit or loss protection. User modes are MANUAL, AI_ADVISORY, AI_PROPOSE, and AI_AUTO_WITH_LIMITS; only the first three may be planned before evidence gates admit the last.

## Normative requirements

- Account, strong authentication, balances, activity, deposits and future withdrawals are tenant-scoped views of authoritative domain records.
- Feature flags default OFF for `ARBITRAGE`, `DEX`, `LP`, `AUTO_LP`, `WITHDRAW_PIX`, `WITHDRAW_CRYPTO`, `METAMASK`, `AI_AUTOPILOT`, and `MAINNET`.
- MVP-A is identity + ledger + payment sandbox specification + market-data paper view + risk dashboard; later MVPs remain gated.

## Component contracts

ProductMode, FeatureFlag, UserDisclosureVersion, PortfolioView, ActivityFeed, ReadModelProjection.

## Invariants and deny conditions

No UI or mode may manufacture availability, execute an external action, or hide a denied/risk/reconciliation status. Customer language MUST NOT imply guaranteed capital protection, suitability, licensing, custody, or return.

## State and failure semantics

Mode transition: MANUAL→AI_ADVISORY→AI_PROPOSE→AI_AUTO_WITH_LIMITS is monotonic only after product, legal, risk, security and mainnet gates; any gate regression returns the affected capability to DENIED.

## Future verification

UX contract tests for feature-flag denial, tenant visibility, disclosure rendering and capability regression; E2E tests later prove an off flag has no API side effect.

## Queue ownership

Implementation is decomposed in `PR-001..PR-010`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/00-charter-scope-and-terminology.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
