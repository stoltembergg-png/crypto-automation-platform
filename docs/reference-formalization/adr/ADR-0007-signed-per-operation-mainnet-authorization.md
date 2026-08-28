# ADR-0007: Signed Per-Operation Mainnet Authorization

**Status:** Proposed — Q-001/Q-003/Q-010 required.

## Decision
At the privileged spend/sign/network/broadcast boundary, verify a signed/versioned authorization binding tenant, operation/resource, parameters hash, environment, legal disposition, policy version/hash, expiry, revocation and replay nonce. Verify environment attestation again at the boundary.

## Consequences
An attestation mismatch denies sign/network/broadcast with bounded telemetry. A UI approval, AI proposal or prior workflow state is not sufficient authorization. Key/recovery/revocation proof remains blocked pending Q-003.
