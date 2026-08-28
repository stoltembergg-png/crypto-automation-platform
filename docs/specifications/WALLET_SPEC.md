# Wallet Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines wallet address ownership, allowlists, signer boundaries and MetaMask connectivity without wallet funding or signing.

## Normative requirements

- EVM external wallet integration follows EIP-1193 provider and ERC-4361 sign-in compatibility references [6][7], plus backend nonce/domain/URI/chain/expiry/one-time-use validation.
- Handle account/chain changes as invalidating session-bound wallet proof.
- Network, token, contract, amount and destination are independently validated.

## Component contracts

WalletAddress, WalletProofChallenge, SIWEMessage, AllowlistEntry, ChainContext, SignerRequest.

## Invariants and deny conditions

Wallet proof grants identity evidence only; it never grants custody. Address display includes checksum/chain context; no clipboard-derived address is trusted. Unknown chain/token/contract/function/default deny.

## State and failure semantics

UNVERIFIED→CHALLENGED→VERIFIED→STALE|REVOKED. Allowlist PENDING→CONFIRMED→COOLDOWN→ACTIVE→REVOKED.

## Future verification

EIP/provider compatibility tests, nonce replay tests, chain/account-change tests, address poisoning fixtures, allowlist cooldown tests and decoded-signer-request equivalence tests.

## Queue ownership

Implementation is decomposed in `PR-053..PR-068`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/05-withdrawals-and-wallets.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
