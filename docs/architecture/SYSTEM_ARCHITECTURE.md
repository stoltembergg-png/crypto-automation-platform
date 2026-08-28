# System Architecture

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines a modular monolith around a language-neutral safety contract. The container shape may later use Next.js/TypeScript UI and a Rust critical kernel only after ADR-001 evidence gate; the architecture does not assume language capability as proof.

## Normative requirements

- Modules own persistence and expose versioned commands/events; cross-module writes are forbidden except a capability-scoped transaction kernel.
- PostgreSQL is the initial authoritative relational store; local inbox/outbox is the only delivery mechanism until workload evidence justifies a broker.
- UI/API, identity, ledger, payment, market, strategy, risk, execution, reconciliation and audit are modules, not premature services.
- SSE is preferred for initial server→browser activity; WebSocket needs a named bidirectional use case.

## Component contracts

CommandEnvelope, EventEnvelope, TransactionKernel, ModuleContract, ReadProjection, CapabilityGrant.

## Invariants and deny conditions

No distributed transaction claim. No module may bypass ledger, policy, transaction guard, audit or tenant context. Unknown action/environment/capability contracts default deny.

## State and failure semantics

Command flow: API→module validation→policy/risk→simulation→guard→local transaction+outbox→privileged adapter (when authorized)→evidence→reconciliation→projection.

## Future verification

Architecture dependency test, forbidden shared-write test, transaction-kernel integration test, outbox/inbox replay test and no-privileged-bypass test.

## Queue ownership

Implementation is decomposed in `PR-001..PR-018`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/01-domain-data-and-module-boundaries.md; docs/reference-formalization/specifications/02-financial-authority-and-policy-kernel.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
