# Mainnet Activation Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines `MAINNET = BLOCKED` until every critical readiness row is independently PASS at the exact scope and identity.

## Normative requirements

- Per-operation authorization binds exact action/resource fingerprint, tenant, capability, amount/asset/network/destination or envelope digest, environment attestation, named Q-gate registry digest and IDs, evidence, policy/risk/simulation/guard/compliance/fraud hashes, capital reservations, expiry, revocation and replay nonce.
- Capital limits start minimal: global/per-strategy/per-trade/daily-loss/daily-volume/per-protocol and use atomic reservation/commit/release lifecycle; an authorization cannot reuse or exceed a reservation.
- Manual distinct-principal multiparty approval and non-spend break-glass containment are required governance gates; generic `Q-001..Q-010 as applicable` is invalid.

## Component contracts

MainnetAuthorization, ReadinessEvidence, ActivationDecision, CapitalLimit, BreakGlassRecord.

## Invariants and deny conditions

PASS cannot be inferred from planning, paper, testnet, source URL, prior approval or different deployment. Any expired/conflicting/missing evidence denies with no signing/network side effect.

## State and failure semantics

BLOCKED→EVIDENCE_COLLECTING→REVIEWED→AUTHORIZED_LIMITED→SUSPENDED|REVOKED. No automatic broadening.

## Future verification

Authorization signature/replay/expiry/revocation, environment mismatch, capital limit, kill switch and readiness regression tests.

## Queue ownership

Implementation is decomposed in `PR-128..PR-133`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/11-environment-maturity.md; .planning/master/MAINNET_READINESS_MATRIX.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
