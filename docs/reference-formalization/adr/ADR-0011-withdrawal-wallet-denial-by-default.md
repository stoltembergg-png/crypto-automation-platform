# ADR-0011: Withdrawal and Wallet Denial by Default

**Status:** Proposed — Q-001/Q-002/Q-003/Q-004 required.

## Decision
Withdrawals, wallet connections and MetaMask integrations remain unavailable until all legal, provider, custody/signing, accounting, authority, security, chain-scope, environment and release gates pass. An ambiguous broadcast has no automatic retry or second economic mutation.

## Consequences
Future wallet support requires explicit user/tenant/nonce/audience/environment verification. Withdrawal lock is singular and independently reconciled; no technical maturity gate waives external readiness.
