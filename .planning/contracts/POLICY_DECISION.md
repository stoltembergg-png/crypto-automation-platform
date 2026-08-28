# Policy Decision

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Decision binds proposal/action, policy/risk version, snapshot timestamps, limits, maturity, legal/provider disposition and expiration. Status is ALLOW, DENY, REQUIRES_REVIEW, EXPIRED or REVOKED.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
