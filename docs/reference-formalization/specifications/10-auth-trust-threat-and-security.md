# SDD-10 — Authentication, Trust, Threat and Security

**Status:** proposed; Q-006/Q-007 required for approval.

## Identity and authorization
All requests have an authenticated principal/service identity, tenant, environment, audience, session/credential freshness and requested operation/resource. Authorization is deny-by-default and uses least privilege. Privileged adapters receive attenuated, short-lived, revocable capabilities—not general API credentials. Service identity, tenant, resource, operation, audience, environment, expiry and revocation version must all verify at use time.

## Trust boundaries
Untrusted: browser/wallet input, AI output, provider APIs/webhooks, venue/chain events, market data, user-supplied addresses/identifiers, imported files and telemetry ingress. Trusted only after validation: contract parsing, tenant/resource binding, schema/unit validation, signature/nonce checks where applicable, authorization/capability decision, and redaction/classification.

## Threat model priorities
Cross-tenant data/action substitution; privilege/capability escalation; replay; authorization/policy downgrade; environment confusion; key/secret compromise; malicious provider payload; webhook spoofing; dependency/supply-chain compromise; sensitive logging; idempotency collision; audit tampering; denial-of-service and ambiguous external outcomes. The threat register must link each risk to preventive, detective, containment and recovery controls.

## Security rules
No secrets in proposal, event, audit or telemetry payload. Encrypt/classify sensitive material under Q-006 policy; access requires purpose and tenant scope. Rotate/revoke credentials and capabilities. Signatures and nonces are scoped and time-limited. A mismatch in tenant, resource, audience, environment, policy/authorization version, expiry or revocation denies action and logs a bounded audit fact.

## Required adversarial tests
Tenant substitution; role escalation; confused deputy; capability replay/revocation; token audience/environment mismatch; malformed oversized payload; webhook/provider spoof; deserialization/injection; secret-log scan; rate/resource exhaustion; compromised adapter response. Tests must assert no privileged side effect and correct typed denial.
