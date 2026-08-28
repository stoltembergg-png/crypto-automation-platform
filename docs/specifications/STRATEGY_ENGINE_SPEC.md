# Strategy Engine Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines plugin contracts with no signer, secret or direct ledger access.

## Normative requirements

- Interface: analyze(context), propose(context), simulate(proposal), execute(plan), monitor(position), exit(position).
- Plugin sees normalized, redacted context; execute is a request to Execution Engine, not direct provider access.
- Capability negotiation declares strategy environment, assets, venues, limits and maturity prerequisites.

## Component contracts

StrategyPluginManifest, StrategyContext, StrategyProposal, StrategyPlan, PositionMonitorEvent.

## Invariants and deny conditions

Plugins cannot call private key, KMS, raw credentials, ledger posting, policy mutation or arbitrary network action. Unknown plugin/capability/version denies.

## State and failure semantics

REGISTERED→DISABLED|PAPER_READY→TESTNET_READY→LIMITED_MAINNET_READY; readiness can regress.

## Future verification

Manifest compatibility tests, sandbox/contract tests, forbidden-import tests, malicious strategy output fixtures and deterministic replay tests.

## Queue ownership

Implementation is decomposed in `PR-100..PR-105`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/08-strategy-ai-risk-and-execution.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
