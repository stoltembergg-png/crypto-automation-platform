# Chain Adapter Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines EVM-family chain adapter requirements; Solana is deferred to a separate adapter family and cannot be forced into EVM semantics.

## Normative requirements

- Methods: getBalance, getTokenBalance, estimateGas, simulateTransaction, sendTransaction, getReceipt, getBlock, getNonce, getAllowance, approve, swap.
- Each operation is bound to approved chain, environment attestation, token registry, contract allowlist, nonce/fee policy and transaction authorization.
- Ethereum, Base, Arbitrum, Optimism and Polygon remain candidate inventories, not enabled networks.

## Component contracts

ChainCapability, TransactionSimulation, NonceReservation, ReceiptEvidence, FinalityPolicy, ChainObservation.

## Invariants and deny conditions

No arbitrary calldata; no unapproved RPC; wrong chain/environment denies before network call. Receipt is evidence, not finality until per-chain policy passes.

## State and failure semantics

BUILT→SIMULATED→GUARDED→AUTHORIZED→SUBMITTED→OBSERVED→FINALIZED|REORGED|UNKNOWN.

## Future verification

Fork/testnet simulation contract tests later, nonce conflict, gas spike, RPC outage, duplicate log, reorg and finality tests.

## Queue ownership

Implementation is decomposed in `PR-080..PR-086`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/06-markets-venues-and-chains.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
