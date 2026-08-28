# Domain Model

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines aggregates and authority ownership for Identity, Tenant, Ledger, Payment, Withdrawal, Wallet, Capability Claim, Market Snapshot, Strategy Proposal, Risk Decision, Execution Intent, Position, Reconciliation Case and Audit Event.

## Normative requirements

- Aggregates publish immutable versioned events and have one command owner.
- Financial authority is separated from external observation and user-facing projections.
- Strategy/AI objects are non-authoritative recommendations; ExecutionIntent is created only by deterministic authorization.

## Component contracts

TenantId, AssetId, Money, Quantity, CorrelationId, CausationId, IdempotencyScope, PolicyVersion, EvidenceRef, CapabilityGrantRef.

## Invariants and deny conditions

All IDs carry tenant/environment context where relevant; Money uses integer atoms plus asset scale, never IEEE float. A projection cannot be command authority.

## State and failure semantics

Proposal, payment, withdrawal, execution, order, LP and reconciliation lifecycles are defined in `.planning/contracts/STATE_MACHINES.md`.

## Future verification

Generated model/state-machine tests, aggregate command idempotency tests, ownership tests and domain-event compatibility tests.

## Queue ownership

Implementation is decomposed in `PR-011..PR-026`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/contracts/02-state-machines-and-invariants.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
