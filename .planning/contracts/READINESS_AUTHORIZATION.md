# Readiness Authorization

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Mainnet authorization is signed/versioned and binds tenant, operation, environment attestation, legal state, risk/policy/simulation/guard hashes, expiry, revocation and replay nonce.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
