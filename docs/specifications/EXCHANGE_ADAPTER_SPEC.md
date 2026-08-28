# Exchange Adapter Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines capability-negotiated CEX adapters; no exchange is selected or enabled in this phase.

## Normative requirements

- Methods: getMarkets, getBalances, getOrderBook, getTicker, getFees, placeOrder, cancelOrder, getOrder, getOpenOrders, getTransfers, withdraw, depositAddress.
- Capabilities include SPOT, LIMIT_ORDER, MARKET_ORDER, WITHDRAW, DEPOSIT, WEBSOCKET, MARGIN, FUTURES. Margin/futures/leverage are deny-by-default.
- Every adapter invocation requires an active ProviderClaim and attenuated capability.

## Component contracts

ExchangeCapability, AdapterRequest, AdapterEvidence, OrderIntent, VenueOrderState, ProviderClaim.

## Invariants and deny conditions

Adapter cannot mutate ledger or policy; malformed/conflicting/unavailable response maps to typed domain error. Order acknowledgment is not fill/settlement.

## State and failure semantics

PROPOSED→RISK_ALLOWED→SUBMITTED→ACKNOWLEDGED→PARTIALLY_FILLED*→FILLED|CANCELLED|REJECTED|UNKNOWN.

## Future verification

Consumer-driven adapter contracts, capability negotiation, partial-fill/cancel race/retry/idempotency tests and simulated provider outage tests.

## Queue ownership

Implementation is decomposed in `PR-048..PR-053`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/06-markets-venues-and-chains.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
