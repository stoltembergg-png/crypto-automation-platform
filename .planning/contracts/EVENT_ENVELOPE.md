# Event Envelope

**Status:** Proposed contract; future implementation must use generated schema plus compatibility tests.

Envelope fields: contract_name, semantic_version, schema_digest, event_id, producer_identity, tenant_id, environment, occurred_at, correlation_id, causation_id, idempotency_scope/key, sensitivity, payload_hash. Delivery may duplicate/reorder; consumer inbox decides same-fingerprint duplicate vs conflict.

## Required tests
Unknown version/action, malformed payload, duplicate/conflict, tenant substitution, replay, expiry/revocation, correlation preservation and redaction are negative cases.
