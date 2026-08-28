# Policy Decision

**Status:** `PROPOSED · PLANNING_ONLY`. Exact semantics are supplemented and take precedence from `docs/security/ADVERSARIAL_CLOSURE_SPEC.md` §1.2 and §5.

## Decision contract

`PolicyDecision.v1` binds proposal/action fingerprint, tenant, environment, correlation ID, policy/risk version, input-snapshot digests/timestamps, limits, maturity, expiration/revocation and deterministic status: `ALLOW`, `DENY`, `REQUIRES_REVIEW`, `EXPIRED`, `REVOKED`.

It is distinct from these mandatory future decisions:

- `ComplianceDecision.v1`: subject/payer/destination/asset-network, screening provider/list/rule version, screening time/expiry and `ALLOW|DENY|HOLD|REVIEW`.
- `FraudRiskDecision.v1`: privacy-classified device/recovery context, linkage/velocity/dispute aggregates, model/rule version and `ALLOW|DENY|HOLD|REVIEW`.
- `AccountingCommand.v1`: the only type the Ledger accepts for economic mutation.

Every signed decision binds schema version, decision ID, canonical payload digest, issuer ID/key ID/algorithm, trust-anchor reference, issuance/expiry, revocation reference, tenant, environment and operation fingerprint. Unknown issuer/key/schema/algorithm, mismatched scope/digest, expired/revoked decision, HOLD or REVIEW has no signing/submission/ledger-mutation path.

## Required future tests

Unknown version/action, malformed payload, issuer/key forgery, decision substitution, duplicate/conflict, tenant substitution, replay, expiry/revocation, changed recovery context, correlation preservation and redaction must deny.
