# CI/CD Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines fail-closed deterministic engineering gates and non-authoritative AI reporting.

## Normative requirements

- Required: format, lint, unit/integration/property/security tests, dependency/secret/SAST/license/container scans, migration replay, architecture/ledger/risk/contract checks.
- Required check aggregation is deterministic and bound to exact SHA; skipped/missing/stale/cancelled checks are non-PASS.
- AI may summarize bounded artifacts but cannot approve, alter required status, merge, label as authority or access secrets.

## Component contracts

QualityGate, CheckEvidence, PolicyRevision, MergeEligibility, CIArtifact.

## Invariants and deny conditions

No merge on missing/failed/unknown critical check; workflow/evaluator/policy change is a trust-boundary migration and reverts auto-merge to OFF/SHADOW until re-proven.

## State and failure semantics

QUEUED→RUNNING→PASS|FAIL|BLOCKED|NO_PROOF; a future merge controller requests native auto-merge only after fresh identity checks.

## Future verification

Workflow policy fixtures, skipped-check, stale-SHA, fork PR, tampered artifact, missing reporter and merge-group tests.

## Queue ownership

Implementation is decomposed in `PR-001..PR-007`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/12-ci-release-and-compliance.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
