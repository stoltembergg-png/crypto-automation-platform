# Security Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines zero-trust application, secret, data and operational controls.

## Normative requirements

- KMS/Vault/cloud key provider decision is evidence-gated; app stores references and encrypted envelopes only.
- Secret redaction middleware covers logs, audit, errors, AI context and support exports.
- RBAC plus tenant policy/RLS, CSP, CSRF, rate limit, WAF/abuse detection and secure headers apply.

## Component contracts

SecretReference, EncryptionEnvelope, Role, Permission, DataClassification, SecurityPolicy.

## Invariants and deny conditions

No secret value in code, SQL, common environment, test fixture, log, trace or LLM. Security configuration change is privileged/audited and may force capability regression.

## State and failure semantics

Security control changes use proposed→reviewed→approved→applied→verified|reverted; unverified change cannot loosen financial restriction.

## Future verification

Secret scan, SAST, dependency/license, RLS/tenant, redaction, authorization and configuration-drift tests.

## Queue ownership

Implementation is decomposed in `PR-117..PR-122`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/10-auth-trust-threat-and-security.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
