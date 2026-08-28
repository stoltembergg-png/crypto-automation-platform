# Crypto Automation Platform — SDD Formalization Set

**Status:** planning-only documentation baseline. No source code, deployment, provider integration, legal approval, test execution, environment proof, or operational readiness is asserted by this directory.

## Purpose

This document set turns the reviewed insight bundle into an implementation-ready, evidence-gated Software Design Description (SDD). It constrains future implementation; it does not authorize fund movement, payment processing, custody, signing, broadcasting, trading, or a mainnet release.

## Navigation

| Area | Authoritative document(s) |
|---|---|
| Exact artifact inventory | `SDD-FORMALIZATION-MANIFEST.md` |
| Scope, terminology, data ownership | `specifications/00-charter-scope-and-terminology.md`, `01-domain-data-and-module-boundaries.md` |
| Financial authority and policies | `specifications/02-financial-authority-and-policy-kernel.md`, `adr/ADR-0001-*.md` |
| Ledger, payment and withdrawal semantics | `specifications/03-ledger-and-accounting.md`, `04-payments.md`, `05-withdrawals-and-wallets.md` |
| Markets, venues, chain, DEX, arbitrage and LP | `specifications/06-markets-venues-and-chains.md`, `07-dex-arbitrage-and-lp.md` |
| Strategy, AI, risk and execution | `specifications/08-strategy-ai-risk-and-execution.md` |
| Reconciliation, audit, security, observability | `specifications/09-reconciliation-audit-observability.md`, `10-auth-trust-threat-and-security.md` |
| Environments, CI, release and compliance | `specifications/11-environment-maturity.md`, `12-ci-release-and-compliance.md` |
| ADRs | `adr/ADR-0001-*.md` through `adr/ADR-0012-*.md` |
| Diagrams | `diagrams/*.mmd` |
| Executable formalization plan and gates | `../.planning/` |

## Non-negotiable language

- The product must never promise **capital protection**.
- AI is a proposal surface only. It has no direct financial authority.
- `REQUIRES_LEGAL_REVIEW` is a non-overridable disposition, not a warning that a caller can bypass.
- Mainnet, withdrawal, payment, and MetaMask capabilities are denied by default until all applicable formal gates are evidenced.
- A document that specifies a control is not evidence that the control is implemented, tested, approved, or operating.

## Document governance

Future changes must cite the affected requirement IDs, contract versions, ADRs, owners, proof artifact, and revalidation trigger. Where a claim depends on provider capability, the claim must link to an owned, expiring, revocable claim-register record and boundary test; a vendor page or informal statement is insufficient.
