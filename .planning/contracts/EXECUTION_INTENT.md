# Execution Intent

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Intent binds exact decoded template, plan/simulation/guard hashes, nonce, chain, value, recipient, token, signer policy and authorization artifact. Any mismatch denies.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
