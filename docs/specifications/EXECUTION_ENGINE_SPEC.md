# Execution Engine Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Orchestrates approved/simulated deterministic plans and records external evidence; it never directly broadens authority.

## Normative requirements

- Execution accepts only plan hash plus current policy/risk/simulation/guard/capability/mainnet authorization artifacts.
- Simulation is mandatory; `eth_call`, quote, gas/fee, state and slippage evidence are time-bounded.
- Local transaction commits intent/audit/outbox atomically; external delivery is separate and reconciled.

## Component contracts

ExecutionPlan, SimulationEvidence, ExecutionIntent, SubmissionEvidence, ExecutionOutcome.

## Invariants and deny conditions

Hash mismatch, expiry, simulation drift, unavailable adapter, policy/risk change or scope mismatch denies. No arbitrary transaction/calldata/credentials reach executor.

## State and failure semantics

PROPOSED→RISK_VALIDATED→SIMULATED→AUTHORIZED→SUBMITTED→PARTIALLY_FILLED|FILLED|FAILED|UNKNOWN→RECONCILED.

## Future verification

Plan-hash equivalence, simulation TTL, adapter outage, partial result, unknown submission and reconciliation tests.

## Queue ownership

Implementation is decomposed in `PR-061..PR-067`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/08-strategy-ai-risk-and-execution.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
