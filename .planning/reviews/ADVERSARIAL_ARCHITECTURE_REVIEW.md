# Adversarial Architecture Review

## Reviewer lenses
Security engineer: privileged-capability, secrets, signing and tenant substitution. Quant researcher: net-profit/latency/slippage/fill assumptions. Exchange engineer: capability, order lifecycle and reconciliation. Blockchain engineer: finality, reorg, nonce, calldata and proxy risk. Backend engineer: state/transaction/module ownership. SRE: outage, lag, recovery and observability. Financial auditor: journal/availability/evidence/correction. Fraud specialist: account takeover, withdrawal and payment abuse. Red team: malicious AI/provider/user input.

## Surviving findings
1. Local transactions are not external settlement; correlate independent evidence.
2. Ledger is financial availability authority; workflow/provider tables are not substitutes.
3. AI is input, not authority; all unknown actions deny.
4. Capability and mainnet authorization must be scoped, expiring, revocable and attested.
5. Hash-linked Postgres audit detects tampering only; stronger integrity needs external anchoring.
6. Venue/chain/LP failure domains stay separate.
7. Documentation/card count is not readiness proof.

## Required adversarial tests
Forged/replayed webhook; conflicting provider evidence; cross-tenant object/key substitution; stale/revoked grant; prompt injection; malformed schema; arbitrary calldata; wrong network; destination mutation; ambiguous broadcast; nonce conflict; stale quote; partial fill; chain reorg; provider/RPC/db/cache outage; audit-chain tamper; policy downgrade; environment attestation mismatch; mainnet feature-flag bypass.
