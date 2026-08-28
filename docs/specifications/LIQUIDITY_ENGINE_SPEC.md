# Liquidity Management Engine Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines LP analysis/position lifecycle and concentrated-liquidity risk without active pool management.

## Normative requirements

- Pool analysis includes TVL, volume, fee APR, volatility, depth, range/tick, concentration, impermanent loss, earned fees, gas and rebalance cost.
- Range proposal is untrusted AI/strategy input; risk policy validates pool/protocol, exposure, range, expected benefit/cost and execution simulation.
- Rebalance compares benefit against removal/collection/swap/mint costs and finality risk.

## Component contracts

PoolRiskAssessment, LPProposal, RangePolicy, ILModel, RebalanceDecision, LPPositionEvidence.

## Invariants and deny conditions

LP position, fees and valuations are evidence/reconciliation records; no raw on-chain event directly changes user availability. Out-of-range does not force a transaction; it opens a decision.

## State and failure semantics

PROPOSED→RISK_ALLOWED→MINT_REQUESTED→ACTIVE→REBALANCE_REQUESTED|EXIT_REQUESTED→CLOSED|UNKNOWN.

## Future verification

IL/fee/range property tests, out-of-range/reorg/revert/gas-spike fixtures, exposure-cap tests and no-autorebalance-without-gate test.

## Queue ownership

Implementation is decomposed in `PR-094..PR-099`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/07-dex-arbitrage-and-lp.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
