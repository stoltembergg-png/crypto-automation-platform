# Strategy Proposal

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Proposal includes finite strategy/action vocabulary, input/evidence hashes, policy version, confidence/rationale/assumptions, capital/duration/cost/risk estimates. It cannot include secret, private key or arbitrary calldata.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
