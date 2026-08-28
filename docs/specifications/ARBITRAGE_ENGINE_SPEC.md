# Arbitrage Engine Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines opportunity detection and simulation; it does not permit funded arbitrage until a separately authorized maturity capability.

## Normative requirements

- Pipeline: normalized market data→opportunity detection→fees→slippage/impact→latency/finality→liquidity→risk→simulation→decision.
- Expected net profit includes spread minus maker/taker, gas, bridge/withdrawal, slippage, impact, latency and expected failed-transaction cost.
- `NetPnL = realised_fill_proceeds - realised_fill_costs - actual_fees - gas - withdrawal/bridge costs - recovery_costs + conservative_residual_liquidation_value`. Partial fill, unavailable hedge, cancellation, reorg or residual requires RECOVERY_REQUIRED and cannot pass a theoretical full-cycle profit threshold.
- QuoteReservation serializes venue/market path, snapshot digest, observed-at/expiry, cost-model version, amount, exposure/capital reservation IDs and simulation digest. Any change/expiry denies before execution.
- Triangular detection is directed graph/cycle analysis with per-edge executable quantity/cost constraints.

## Component contracts

Opportunity, OpportunityLeg, NetProfitModel, QuoteReservation, VenueAssumption, SimulationResult.

## Invariants and deny conditions

Positive gross spread alone is never profitable. Any stale/missing/contradictory input, unsupported atomicity assumption, bridge requirement or reserve/limit breach denies proposal.

## State and failure semantics

DETECTED→NORMALIZED→SIMULATED→RISK_EVALUATED→PROPOSED|DENIED|EXPIRED.

## Future verification

Property tests for fee arithmetic/monotonic slippage, graph-cycle tests, stale quote tests, partial-fill/reorg fixtures and no-funded-transition test.

## Queue ownership

Implementation is decomposed in `PR-074..PR-079`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/07-dex-arbitrage-and-lp.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
