# Adapter Capability

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Capability binds service identity, tenant, operation/resource, audience, environment, claim reference, expiry, rotation and revocation. Adapters have no authority to post ledger or change policy.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
