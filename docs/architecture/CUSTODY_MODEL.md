# Custody Model

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Compares custodial, non-custodial, hybrid, exchange-managed, MPC, multisig and smart-account models without declaring a legally permissible selection.

## Normative requirements

- Initial recommendation is a future hybrid model only if counsel/provider/custody gates pass: segregated internal liabilities, qualified/capable provider evidence, low-limit automated hot capability, warm controls and cold/offline no-autopilot.
- MPC/HSM/KMS/multisig evaluation is vendor and threat-model dependent.
- MetaMask starts as external wallet/destination/identity proof, never assumed custodial signer.

## Component contracts

CustodyPolicy, SignerPolicy, KeyReference, WalletAllowlist, WithdrawalAuthorization, KeyCeremonyRecord.

## Invariants and deny conditions

Private key material is never held by application database or common environment variable. Signing request must bind exact decoded action, value, destination, chain, nonce and authorization hash.

## State and failure semantics

Custody mode can regress to deny; key compromise/revocation stops withdrawal and mainnet capabilities before attempting recovery.

## Future verification

Key-ceremony drills, signer-policy tests, destination mutation tests, HSM/MPC contract tests and break-glass non-spend rehearsal.

## Queue ownership

Implementation is decomposed in `PR-035..PR-040`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/05-withdrawals-and-wallets.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
