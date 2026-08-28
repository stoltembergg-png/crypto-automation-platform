# Ledger Posting

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Posting requires balanced debit/credit per asset, immutable accounting event, tenant/action/intent idempotency and compensating correction only. Direct mutable balance updates are forbidden.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
