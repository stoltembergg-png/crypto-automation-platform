# Paper Trading Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines real market data with virtual capital and simulated execution as first strategy evidence environment.

## Normative requirements

- Paper wallet/ledger is physically/environmentally isolated from any real-fund ledger.
- Simulated fills use declared model/latency/slippage/fee assumptions and report divergence.
- Paper success is neither legal, custody, provider nor mainnet readiness.

## Component contracts

PaperAccount, PaperOrder, FillModel, SimulationAssumption, PaperPosition.

## Invariants and deny conditions

No paper entity can reach signer/provider credential; environment identity mismatch denies. Virtual capital is clearly labelled and cannot be withdrawn.

## State and failure semantics

CREATED→SIMULATED→SETTLED_VIRTUAL→RECONCILED_VIRTUAL→ARCHIVED.

## Future verification

Isolation, deterministic replay, stale data, partial fill, fee/slippage and no-network-signing tests.

## Queue ownership

Implementation is decomposed in `PR-068..PR-073`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/11-environment-maturity.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
