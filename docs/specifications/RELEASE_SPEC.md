# Release Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines SemVer, provenance, rollback and operational release evidence.

## Normative requirements

- Release only from healthy main, signed/tagged artifact, changelog, SBOM, checksum, provenance and environment approval.
- Vercel `develop` is planning-status only; never a financial endpoint or readiness proof.
- Rollback is forward-safe with migration compatibility, capability disablement and audit preservation.

## Component contracts

ReleaseCandidate, ReleaseEvidence, SBOM, Provenance, RollbackPlan, DeploymentRecord.

## Invariants and deny conditions

Deployment completion is not public accessibility, product readiness or mainnet authorization. Capability disable path cannot weaken required checks.

## State and failure semantics

DRAFT→VALIDATED→APPROVED→DEPLOYED→VERIFIED|ROLLED_BACK.

## Future verification

Release provenance/checksum/SBOM, rollback, deployment alias access, migration compatibility and emergency-disable tests.

## Queue ownership

Implementation is decomposed in `PR-001..PR-007`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/12-ci-release-and-compliance.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
