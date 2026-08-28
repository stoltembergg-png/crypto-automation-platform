# Market Data Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines collectors, normalizer, snapshots, freshness, quality and publication for CEX/DEX/on-chain market data.

## Normative requirements

- Sources are untrusted and capability-gated; each snapshot records source, market, timestamp, sequence/block, latency, quality, confidence and staleness.
- Collectors→Normalizer→PostgreSQL/derived cache→Opportunity engines. Cache never becomes ledger or execution authority.
- Redis/streaming broker is deferred until measured workload evidence.

## Component contracts

MarketSnapshot, OrderBookSnapshot, QuoteReservation, SourceHealth, DataQualityDecision.

## Invariants and deny conditions

Stale, crossed, inconsistent, insufficient-depth or unverified data denies strategy/execution use. Price/fee/gas/finality assumptions must be per venue/chain and versioned.

## State and failure semantics

OBSERVED→NORMALIZED→QUALITY_VALIDATED→PUBLISHED|STALE|REJECTED. Publication is idempotent by source/market/sequence.

## Future verification

Sequence-gap, stale-price, source divergence, rate-limit, timeout and normalizer property tests; deterministic replay fixture suite.

## Queue ownership

Implementation is decomposed in `PR-041..PR-047`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/06-markets-venues-and-chains.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
