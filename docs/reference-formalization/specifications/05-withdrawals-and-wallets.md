# SDD-05 — Withdrawals, Wallets and MetaMask Boundary

**Status:** `DENIED_BY_DEFAULT`. This document does not enable withdrawal, wallet custody, wallet connection, signing or MetaMask support.

## Preconditions
No withdrawal path may leave documentation-only status without Q-001 legal/custody disposition, Q-002 verified provider/wallet claim, Q-003 signing/recovery model, Q-004 accounting policy, approved asset/chain scope, authority-kernel implementation evidence, and per-environment release approval. Any absent/expired/revoked condition returns `BLOCKED`, `NO_PROOF`, `DENIED`, or `REQUIRES_LEGAL_REVIEW` as applicable.

## Intent and lock protocol
1. A tenant-authenticated actor creates a versioned `WithdrawalIntent` with destination reference classification, asset/amount, parameters hash, environment, expiry and idempotency key.
2. Policy, legal, risk, available balance, capability and per-operation authorization independently evaluate it.
3. Exactly once, the Ledger posts the approved economic availability lock, linked to intent and accounting policy.
4. A capability-scoped adapter may request broadcast only after a valid signed authorization and environment attestation.
5. Provider/chain observations are correlated as evidence; they do not create a second lock/debit/credit.

## Ambiguous broadcast rule
`BROADCAST_AMBIGUOUS` is a first-class terminal-pending condition when request delivery/acceptance cannot be proven. It MUST freeze automatic retry and prohibit a second economic mutation. Resolution requires evidence correlation, reconciliation and an explicitly authorized compensating/retry path under a new, linked intent/version. Human/operator intervention cannot bypass legal, policy, accounting or audit requirements.

## Wallet and MetaMask
A wallet integration is an untrusted client boundary. MetaMask is specified only as a future browser-wallet adapter candidate and is formally unavailable until provider claim, security/threat, user-consent, chain scope, signing, legal and test evidence pass. No browser message, account address, signature or network identifier is authoritative without tenant binding, nonce/replay checks, audience/environment validation and explicit user interaction evidence.

## Tests
State-model tests prove one lock, duplicate/conflict denial, insufficient availability, expired/revoked/replayed authorization, wrong tenant/destination/environment, adapter timeout, rejected broadcast, ambiguous broadcast, reorg and correction. All assertions include “no second accounting mutation.”
