# ADR-0008: Audit Integrity Claim Boundary

**Status:** Proposed — Q-008 required for stronger claims.

## Decision
Postgres hash-linked audit records may be described as tamper detection only. Stronger claims require external anchoring, separate signing keys, immutable retention and incident/restore procedure evidence.

## Consequences
Audit language remains precise under database/operational compromise. Failure of chain verification is observable but does not prove prevention. Retention and legal holds await Q-006/Q-008.
