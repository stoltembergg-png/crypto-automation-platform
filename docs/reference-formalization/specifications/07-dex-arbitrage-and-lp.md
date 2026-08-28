# SDD-07 — DEX, Arbitrage and Liquidity Provision

**Status:** future-risk specification only. It does not authorize DEX use, arbitrage, LP mint/burn, bridge, swap or any profitability claim.

## DEX contract
A DEX operation is a policy/risk-authorized proposal with chain/network, protocol/version claim, pool/token identifiers, route/calldata hash, spender/allowance scope, slippage/gas/deadline constraints, expected state reference and signed authorization reference. Adapter execution must verify environment, audience, capability, expiry, nonce/replay and approved resource bounds. Quote/route data is an untrusted observation.

## Arbitrage semantics
An arbitrage proposal contains comparable quote sources/timestamps, units/decimals, executable-size assumptions, explicit fee/gas/slippage/latency bounds, liquidity and finality assumptions, and risk decision. It MUST be rejected when inputs are stale, incomparable, outside scope, unverified or exceed policy. It cannot state or imply profit certainty, capital protection or provider/settlement assurance.

## LP lifecycle and drift
An LP position models `PROPOSED → AUTHORIZED → MINT_REQUESTED → ACTIVE → REBALANCE_REQUESTED|EXIT_REQUESTED → CLOSED|UNKNOWN`. Separate observations track price/range drift, accrued-fee estimate, liquidity change, impermanent-loss estimate, oracle discrepancy, gas and reorg status. None is a settled economic balance until the ledger receives an authorized accounting event backed by reconciliation evidence.

## Tests
Per approved protocol/chain: route/calldata substitution, unknown spender, deadline expiry, slippage/gas overflow, stale/oracle-disagreeing quote, pool token/decimal mismatch, chain reorg, duplicate log, partial execution, failed cancellation, LP range crossing, liquidity removal and fee drift. The denial suite asserts no signing/network/broadcast or ledger change on rejected input.
