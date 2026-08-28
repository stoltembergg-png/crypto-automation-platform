# Threat Model

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Uses STRIDE plus financial abuse cases: forged payment evidence, duplicate debit, address poisoning, credential exfiltration, AI manipulation, stale market data, reorg, MEV, operator abuse and recovery failure.

## Normative requirements

- Every threat names asset, actor, trust boundary, precondition, abuse path, detection, mitigation, owner and test.
- Risk acceptance requires Security + domain owner + Legal/Compliance when customer funds or data are involved.
- Threats lacking evidence remain open, never silently accepted.

## Component contracts

ThreatRecord, SecurityControl, RiskAcceptance, IncidentCase, DetectionSignal.

## Invariants and deny conditions

No threat mitigation is called implemented by documentation. Controls fail closed where absence can create spend, disclosure, cross-tenant access or policy bypass.

## State and failure semantics

Emergency shutdown has global, user, strategy, protocol, chain and exchange scopes; containment actions cannot broaden spend authority.

## Future verification

Adversarial fixtures for all high-risk flows, fuzzing of parser/decoder boundaries, red-team attempt register and chaos scenario tests.

## Queue ownership

Implementation is decomposed in `PR-041..PR-052`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/10-auth-trust-threat-and-security.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
