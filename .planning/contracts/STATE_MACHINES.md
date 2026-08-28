# State Machines

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Canonical machines: proposal, accounting event, payment, withdrawal, external delivery/reconciliation, order/fill, LP position and maturity authorization. Terminal and ambiguous states cannot be skipped by retry.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
