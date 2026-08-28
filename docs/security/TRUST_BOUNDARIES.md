# Trust Boundaries

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines identity, browser, API, tenant, provider, signer, database, observability and operator boundaries.

## Normative requirements

- Browser/MetaMask, Mercado Pago, exchanges, RPCs, DEXes and AI providers are untrusted external systems.
- Privileged adapters use attenuated capabilities bound to service identity, tenant, operation/resource, audience, environment, expiry, rotation and revocation.
- LLM input/output, webhook payloads, market data, calldata candidates and provider status are untrusted input.

## Component contracts

CapabilityGrant, ServiceIdentity, EvidenceClaim, AdapterResponse, HumanApproval, EnvironmentAttestation.

## Invariants and deny conditions

No ambient provider credential in tenant-facing code. No raw private key in SQL, environment variables, logs or LLM context. Denials use generic response plus pseudonymous audit evidence.

## State and failure semantics

Boundary crossings validate schema, signature/authentication where supported, scope, freshness, allowlist, replay, rate limit and policy disposition.

## Future verification

Threat-driven negative tests: cross-tenant substitution, stale capability, audience mismatch, impersonated provider, replay, malformed payload and log redaction.

## Queue ownership

Implementation is decomposed in `PR-027..PR-040`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/10-auth-trust-threat-and-security.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
