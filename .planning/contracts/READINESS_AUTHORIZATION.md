# Readiness Authorization

**Status:** `PROPOSED · PLANNING_ONLY`. This contract never enables mainnet; it supplements `docs/security/ADVERSARIAL_CLOSURE_SPEC.md` §1.2 and §2.

## MainnetAuthorization.v1

A signed authorization is valid only for one exact operation and contains: schema/authorization ID; canonical action vocabulary; tenant/environment; operation/resource fingerprint; amount, asset, network, destination or transaction-envelope digest; environment attestation digest; Gate Registry version/digest; explicit required Q-ID list; evidence digests; policy/risk/simulation/guard/compliance/fraud decision digests; capital reservation IDs; expiry; replay nonce; issuer identities/key IDs; distinct-principal quorum; and revocation state.

A generic `Q-001..Q-010 as applicable`, source URL, prior approval, paper/testnet result, deployment or UI state is invalid. The verifier uses only the trust registry; unknown/mismatched/expired/revoked issuer, evidence, scope, action, amount, destination, environment, limit reservation or quorum denies before signing or submission.

## Required future tests

Test signature/issuer/key substitution, operation and destination mutation, exact gate-set mismatch, catalog-digest drift, stale evidence, duplicate principal quorum, environment mismatch, replay, capital-reservation race, expiry, revocation and scoped kill switch denial.
