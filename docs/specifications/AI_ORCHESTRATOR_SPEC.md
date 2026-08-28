# AI Orchestrator Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Supports multiple AI providers as untrusted analysts, not decision authorities.

## Normative requirements

- AIProvider receives normalized/redacted context only; no credentials, private keys, raw PII, secret metadata or unsigned transaction candidate.
- A proposal schema contains strategy, confidence, expected return/risk, capital required, duration, rationale, required actions, assumptions and input/evidence hashes.
- Multi-agent roles are optional analytical lenses; no agent-to-agent authority chain or autonomous privileged tool access.

## Component contracts

AIProvider, ModelInvocationRecord, StrategyProposal, ProposalEvidence, AIRejectionReason.

## Invariants and deny conditions

Malformed/unknown/oversize/model-unavailable output denies and records bounded/redacted provenance. Model confidence is not a risk limit or approval.

## State and failure semantics

REQUESTED→RECEIVED→SCHEMA_VALIDATED→POLICY_EVALUATED→PROPOSED|DENIED|EXPIRED.

## Future verification

Structured-output schema/fuzz tests, prompt-injection fixtures, redaction tests, provider-timeout tests and proposal-policy pin tests.

## Queue ownership

Implementation is decomposed in `PR-100..PR-105`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/08-strategy-ai-risk-and-execution.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
