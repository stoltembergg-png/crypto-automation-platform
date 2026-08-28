# ADR-0003: Modular Monolith and Module-Owned Persistence

**Status:** Proposed.

## Decision
Start with a modular monolith. Each bounded context owns its persistence and migrations; cross-module writes are forbidden. Modules communicate through versioned commands/events/read contracts.

## Consequences
The architecture is simpler to audit and transact locally. A service split requires measured workload/failure-isolation evidence and a new ADR; it is not a default response to domain count.
