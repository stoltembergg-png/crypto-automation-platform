# Testnet Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines testnet-only wallet/transaction/swap/LP validation after paper gates and provider/chain evidence gates.

## Normative requirements

- Testnet has separate keys/capabilities, allowlists, ledgers, telemetry and environment attestation.
- Testnet failures/reorgs still exercise guard, reconciliation and audit behavior.
- No production endpoint or mainnet chain is reachable from testnet capability.

## Component contracts

TestnetEnvironment, FaucetEvidence, TestnetTransaction, EnvironmentAttestation.

## Invariants and deny conditions

Testnet success does not imply mainnet/legal/custody readiness. Wrong chain, unsigned authorization or missing attestation denies before network call.

## State and failure semantics

OFF→ATTESTED→LIMITED_TESTNET→SUSPENDED|REVOKED.

## Future verification

Network isolation, wrong-chain, reorg, nonce, gas, simulation/receipt and rollback tests.

## Queue ownership

Implementation is decomposed in `PR-112..PR-116`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/11-environment-maturity.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
