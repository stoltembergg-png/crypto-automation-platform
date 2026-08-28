# ADR-0002: Singular Double-Entry Availability Ledger

**Status:** Proposed — pending Q-004 accounting approval.

## Decision
Use one Ledger module with balanced immutable accounting events as the only source of economic availability changes. External evidence, delivery, workflow and reconciliation facts remain correlated but separate.

## Consequences
No provider/chain/UI state can mutate balance directly. Corrections are compensating events. A local transaction may atomically post and write an outbox record but no cross-system atomicity is claimed.
