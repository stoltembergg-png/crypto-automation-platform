# Evidence and Planning Boundary

**Observed at:** 2026-08-28T18:29:40-03:00
**Status:** planning baseline; not implementation or production evidence.

## Authorized outcome

This repository is for a specification-first plan for a Brazilian crypto-investment automation platform. The authorized work in this phase is architecture, threat modeling, regulatory/operational analysis, test design, ADRs, traceability, milestones, and an executable PR queue. It is not authorization to create financial runtime behavior.

## Explicitly out of scope

- No payment, exchange, custody, KMS, blockchain, DEX, wallet, or AI-provider credential.
- No Mercado Pago account linkage, API call, webhook registration, Pix, withdrawal, wallet funded, testnet transaction, mainnet transaction, trade, bridge, or signing operation.
- No deployment of a financial product, public deposit endpoint, or real-money feature.
- No legal conclusion, legal opinion, or assertion of regulatory approval.

## Local baseline (observed)

| Item | Observation | Evidence class |
|---|---|---|
| Workspace | `E:\BOT` was empty before planning materialization. | observed |
| Git | No repository existed; a new local `main` repository was initialized for planning artifacts. | observed |
| GitHub | Private repository `stoltembergg-png/crypto-automation-platform` exists and is configured as `origin`. Its remote has no default branch until the first planning commit. | authenticated external observation |
| Vercel | CLI is present and authenticated as `stoltembergg-png`; no Vercel project or deployment has been created yet. | authenticated external observation |
| Financial providers | No credentials, accounts, access tokens, or live capability checks were supplied or performed. | observed absence / NO_PROOF |

## Source boundary

The external-search and extraction providers returned billing/quota errors during this run. Direct URL reachability was verified for Mercado Pago documentation, Banco Central do Brasil, EIP-1193, EIP-4361, and WebAuthn; content-level verification of the referenced Planalto laws timed out. Therefore:

1. Sources `[1]` through `[8]` in `.planning/master/sources.json` are authoritative-reference candidates, not proof that an integration is approved or active.
2. Legal and compliance statements use `REQUIRES_LEGAL_REVIEW` unless a retained document identifies a narrow factual requirement and cites an authoritative source.
3. Provider capabilities, fee behavior, webhook signature behavior, exchange support, chain status, and account eligibility must be re-queried against official documentation and authenticated sandbox accounts in the owning future PR.
4. A missing or unavailable provider response is `NO_PROOF`, never a negative or positive capability assertion.

## Planning invariants

1. `AI proposal → deterministic gates → signer` is one-way; an LLM can never authorize, sign, mutate policy, register allowlist targets, or move funds.
2. The internal double-entry ledger is the accounting authority; caches and UI aggregates are derived views.
3. Real capital remains technically unavailable until every critical item in `MAINNET_READINESS_MATRIX.md` is `PASS` with current evidence.
4. Legal, compliance, security, custody, and operational blockers are release gates, not backlog notes.
5. Documentation describes intended controls only; it never represents a control as implemented or tested in this phase.
