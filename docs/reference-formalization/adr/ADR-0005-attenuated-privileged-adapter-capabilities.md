# ADR-0005: Attenuated Privileged Adapter Capabilities

**Status:** Proposed — pending Q-003/Q-006 security decisions.

## Decision
Privileged adapters accept only short-lived, revocable capabilities bound to service identity, tenant, operation/resource, audience, environment, expiry and rotation/revocation version.

## Consequences
Generic provider credentials and caller identity are insufficient. Provider failures/payloads remain untrusted/contained. Capability substitution, expiry and revocation become mandatory denial tests.
