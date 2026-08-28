# SDD-12 — CI, Release and Compliance

**Status:** proposed control specification. No pipeline or deployment has been executed or configured by this document.

## CI requirements
Future CI must run static formatting/type/lint/secret/dependency/supply-chain checks, architecture-boundary checks, schema/contract compatibility, property/model/state-machine tests, security/adversarial suites, documentation link/terminology validation and release-provenance generation. Exceptions require an owner, expiry, risk acceptance and independent review; no exception can override `REQUIRES_LEGAL_REVIEW` or mainnet gate requirements.

## Release controls
A release request binds source revision, artifact digest, contract/ADR/policy versions, test evidence, environment, capability scope, approvals and rollback plan. Release provenance, SBOM and signing/attestation requirements await Q-010. Vercel `develop` remains planning-only: it may expose non-operational documentation but MUST NOT connect wallets, invoke providers, collect secrets, authorize payments/withdrawals/trades, or imply production/mainnet readiness.

## Compliance posture
Legal/regulatory/AML/KYC/tax/licensing/custody and customer-disclosure answers are outside technical inference. The required disposition is `REQUIRES_LEGAL_REVIEW` until Q-001 records scope-specific decision. The system must not market or promise capital protection. Retention, legal holds, access/export/deletion and incident records are Q-006/Q-008 governed.

## Release rejection conditions
Reject any release if evidence is missing/expired, environment differs, contracts are incompatible, a provider claim is invalid, ledger/authority/security test gate fails, audit integrity is overstated, legal disposition is unresolved, rollback is unavailable, or any readiness matrix row needed by scope is not `PASS`. Documentation-only release does not change operational status.
