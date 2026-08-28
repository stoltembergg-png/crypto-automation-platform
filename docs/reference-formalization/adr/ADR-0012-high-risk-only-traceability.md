# ADR-0012: High-Risk-Only Traceability

**Status:** Proposed.

## Decision
Traceability is mandatory for high-risk requirements/flows only. Each trace card requires a proof value, named owner, source versions and revalidation trigger. There is no target card count.

## Consequences
Traceability remains meaningful rather than performative. Changes to authority, ledger, provider claims, signing, tenant security, audit integrity, external settlement and release gates must update their cards.
