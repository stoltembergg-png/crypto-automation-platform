# Risk Engine Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines deterministic limits and kill switches as independent gate.

## Normative requirements

- Limits: MAX_POSITION_PER_ASSET/PROTOCOL/CHAIN/EXCHANGE, MAX_DAILY_LOSS, MAX_DRAWDOWN, MAX_SLIPPAGE, MAX_PRICE_IMPACT, MIN_POOL_LIQUIDITY, MIN_EXPECTED_PROFIT, MAX_GAS_PERCENTAGE, MAX_OPEN_POSITIONS, MAX_EXPOSURE_PER_USER, MAX_BRIDGE_EXPOSURE, MAX_STABLECOIN_EXPOSURE and MAX_SMART_CONTRACT_EXPOSURE.
- Global, per-user, strategy, protocol, chain and exchange kill switches dominate approvals. Each scope must feed the common scope-matching deny check before signing/submission, with propagation/max-staleness, in-flight handling and authorized reset/revocation evidence.
- Risk output is versioned, deterministic and bound to input snapshot/time/tenant/environment.
- Risk evaluates aggregate correlation, concentrated-LP impermanent-loss stress, beneficiary/device velocity and cross-position exposure in addition to marginal limits. Current ComplianceDecision and FraudRiskDecision ALLOW are independent spend prerequisites; Risk cannot substitute for them.

## Component contracts

RiskPolicy, RiskDecision, ExposureSnapshot, LimitBreach, KillSwitchState.

## Invariants and deny conditions

Missing/stale data, unknown exposure, policy mismatch, limit breach or disabled capability denies. Risk cannot authorize legal/provider/custody gaps.

## State and failure semantics

EVALUATED→ALLOWED|DENIED|REQUIRES_REVIEW|EXPIRED; policy changes invalidate prior decision unless explicitly backward compatible.

## Future verification

Property tests for exposure/limits/drawdown, monotonic deny tests, kill-switch priority, stale input and policy-version invalidation.

## Queue ownership

Implementation is decomposed in `PR-054..PR-060`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/08-strategy-ai-risk-and-execution.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
