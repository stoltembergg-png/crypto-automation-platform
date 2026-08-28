# Audit Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines append-only operational audit events and their claim boundary.

## Normative requirements

- Every financial action records actor, timestamp, intent, policy, decision, transaction/result, correlation, causation, idempotency, environment and evidence refs.
- Events are hash-linked, signed with a separately controlled key and periodically anchored to independently retained immutable storage in a future approved design.
- Audit read access is role/tenant-scoped and redacted.

## Component contracts

AuditEvent, AuditAnchor, AuditVerification, SecurityDenial, OverrideAttempt.

## Invariants and deny conditions

Hash chain in one database is tamper detection only; it is not compliance proof. No raw secret/PII/private target IDs in logs or denial records.

## State and failure semantics

APPENDED→VERIFIED→ANCHORED|ANCHOR_FAILED→INCIDENT. Append does not authorize execution.

## Future verification

Chain verification, tamper/reorder/delete fixtures, anchor-failure, redaction, access-control and incident response drill tests.

## Queue ownership

Implementation is decomposed in `PR-117..PR-122`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/09-reconciliation-audit-observability.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
