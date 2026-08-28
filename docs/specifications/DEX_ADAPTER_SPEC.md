# DEX Adapter Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines DEX adapter and protocol registry boundary for quotes, swaps and liquidity actions.

## Normative requirements

- Methods: getQuote, getPool, getLiquidity, getPriceImpact, buildSwap, simulateSwap, getLPPosition, addLiquidity, removeLiquidity, collectFees.
- Protocol is admitted only through registry record: address/chain, bytecode/proxy/implementation, audit/age/TVL/permissions/upgrade/pause/exploit history/risk score.
- BuildSwap returns a candidate decoded action; Transaction Guard constructs or validates a finite template, never arbitrary AI calldata.

## Component contracts

ProtocolRegistry, PoolSnapshot, Quote, SwapCandidate, LPActionCandidate, DecodedAction.

## Invariants and deny conditions

Unknown token, router, implementation, function selector, price impact, slippage, gas ratio or protocol status denies. Approvals use exact scope/minimum and require separate policy.

## State and failure semantics

QUOTED→SIMULATED→GUARDED→AUTHORIZED→SUBMITTED→OBSERVED→FINALIZED|REVERTED|REORGED|UNKNOWN.

## Future verification

Quote/simulation drift, malicious calldata, proxy upgrade, unexpected token, slippage, approval and revert contract tests.

## Queue ownership

Implementation is decomposed in `PR-087..PR-093`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/07-dex-arbitrage-and-lp.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
