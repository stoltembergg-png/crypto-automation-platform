# Evidence Claim

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Claim holds owner, source/config snapshot, boundary-test result, scope, reviewer, expiry/revalidation trigger and legal disposition. Legal BLOCK cannot be overridden technically.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
