# Backtesting Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines future reproducible historical replay, walk-forward, Monte Carlo and stress testing without claiming predictive validity.

## Normative requirements

- Dataset provenance, version/hash, corporate/token events, fees, liquidity, latency and survivorship assumptions are explicit.
- Strategy replay cannot reuse live provider credentials or mutate live ledger.
- Results present confidence/limitations and cannot bypass risk/policy or become suitability advice.

## Component contracts

HistoricalDataset, BacktestRun, AssumptionSet, WalkForwardRun, StressScenario.

## Invariants and deny conditions

No overfitting claim, no future-leakage, deterministic seed/replay required; missing data marks result invalid/not comparable.

## State and failure semantics

REGISTERED→VALIDATED→REPLAYED→REVIEWED→REJECTED|EVIDENCED (not approved for capital).

## Future verification

Leakage, seed determinism, fee/slippage assumptions, dataset hash, walk-forward and stress scenario tests.

## Queue ownership

Implementation is decomposed in `PR-106..PR-111`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/11-environment-maturity.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
