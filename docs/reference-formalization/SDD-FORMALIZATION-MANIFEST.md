# SDD Formalization Manifest

**Status:** documentation-only inventory. All entries are proposed/planning artifacts unless their own status says otherwise. This manifest makes no implementation, approval, provider, legal, test, deployment or mainnet claim.

## Specifications

1. `docs/specifications/00-charter-scope-and-terminology.md`
2. `docs/specifications/01-domain-data-and-module-boundaries.md`
3. `docs/specifications/02-financial-authority-and-policy-kernel.md`
4. `docs/specifications/03-ledger-and-accounting.md`
5. `docs/specifications/04-payments.md`
6. `docs/specifications/05-withdrawals-and-wallets.md`
7. `docs/specifications/06-markets-venues-and-chains.md`
8. `docs/specifications/07-dex-arbitrage-and-lp.md`
9. `docs/specifications/08-strategy-ai-risk-and-execution.md`
10. `docs/specifications/09-reconciliation-audit-observability.md`
11. `docs/specifications/10-auth-trust-threat-and-security.md`
12. `docs/specifications/11-environment-maturity.md`
13. `docs/specifications/12-ci-release-and-compliance.md`

## Contracts

1. `docs/contracts/00-contract-catalogue.md`
2. `docs/contracts/01-event-envelope-idempotency-and-correlation.md`
3. `docs/contracts/02-state-machines-and-invariants.md`

## Architecture decision records

1. `docs/adr/ADR-0001-deterministic-financial-authority.md`
2. `docs/adr/ADR-0002-singular-double-entry-availability-ledger.md`
3. `docs/adr/ADR-0003-modular-monolith-module-owned-persistence.md`
4. `docs/adr/ADR-0004-postgres-inbox-outbox-broker-neutral-events.md`
5. `docs/adr/ADR-0005-attenuated-privileged-adapter-capabilities.md`
6. `docs/adr/ADR-0006-owned-provider-capability-claim-register.md`
7. `docs/adr/ADR-0007-signed-per-operation-mainnet-authorization.md`
8. `docs/adr/ADR-0008-audit-integrity-claim-boundary.md`
9. `docs/adr/ADR-0009-narrow-maturity-gates.md`
10. `docs/adr/ADR-0010-evidence-gated-language-selection.md`
11. `docs/adr/ADR-0011-withdrawal-wallet-denial-by-default.md`
12. `docs/adr/ADR-0012-high-risk-only-traceability.md`

## Mermaid diagrams

1. `docs/diagrams/architecture-and-trust-boundaries.mmd`
2. `docs/diagrams/financial-authority-and-ledger-sequence.mmd`
3. `docs/diagrams/withdrawal-state-machine.mmd`
4. `docs/diagrams/payment-state-machine.mmd`

## Planning control plane

1. `.planning/README.md`
2. `.planning/hyperplan-executable-formalization.md`
3. `.planning/input-gates-q001-q010.md`
4. `.planning/mainnet-readiness-matrix.md`
5. `.planning/traceability-matrix.md`
6. `.planning/pr-queue.md`
7. `.planning/verification-catalog.md`
8. `.planning/adversarial-review.md`
9. `.planning/formalization-dag.mmd`
