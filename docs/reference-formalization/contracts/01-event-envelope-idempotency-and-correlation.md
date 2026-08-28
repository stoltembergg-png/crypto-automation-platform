# Contract Envelope, Idempotency and Correlation

## Common envelope

```text
contract_name, schema_version, schema_digest, message_id,
producer_identity, produced_at_utc, tenant_id?, environment,
classification, correlation_id, causation_id?, idempotency_key?,
idempotency_scope?, trace_context?, payload
```

`tenant_id` is mandatory unless the contract is classified `GLOBAL`; `environment` is always mandatory. The receiver validates schema, classification, identity, tenant/environment binding, idempotency scope and time semantics before business handling. Payloads must preserve raw-evidence locator/digest separately from normalized fields where external data is involved.

## Idempotency
The canonical scope is `tenant_id + command/action + logical-intent/resource + schema major`. Same scope/key/payload hash returns `DUPLICATE` without side effect; same scope/key with a different normalized payload hash returns `CONFLICT`; an absent required key returns `INVALID`. An idempotency key cannot be reused across tenants or privileged action types.

## Correlation
`correlation_id` joins proposal, authority/risk/legal decisions, local transaction/outbox, dispatch, external evidence, accounting event, reconciliation and audit facts. `causation_id` names the immediately preceding accepted message. Correlation demonstrates relationship, not delivery, settlement or atomicity. Missing or conflicting correlation opens a reconciliation case.

## Required contract tests
Round-trip schema parsing; known version compatibility; malformed/oversize/unknown enum; tenant/environment substitution; duplicate and conflicting key; causal-cycle prevention; classification/redaction; source-evidence digest mismatch. A failure must prove no ledger post and no privileged dispatch.
