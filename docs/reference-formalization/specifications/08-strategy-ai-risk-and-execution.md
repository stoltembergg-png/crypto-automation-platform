# SDD-08 — Strategy, AI, Risk and Execution

**Status:** proposed decision flow. AI is a proposal surface only.

## Strategy and AI
A strategy is versioned code/specification plus declared data sources, assumptions, parameter schema, approved environment, risk class and evaluation artifacts. AI output is treated as untrusted text/data and must be transformed into a typed proposal; it never receives a signing key, privileged adapter capability, direct ledger interface, network/broadcast access or authority to alter policy/risk/legal disposition.

## Risk gate
Risk consumes a normalized proposal, market/evidence freshness, tenant exposure, asset/venue/chain scope, limits, scenario assumptions, and kill-switch state. Q-007 supplies concrete limits and independent exception authority. Outcomes are deterministic typed dispositions with reason codes; a risk allow is necessary but not sufficient for execution.

## Execution guard
The guard is the sole bridge from authorized proposal to privileged adapter command. It rechecks schema/action/resource hash, tenant, environment attestation, policy hash, legal disposition, risk version, capability, signed authorization, expiry/revocation and replay nonce immediately before sign/network/broadcast. It emits a correlation/audit record on every decision and returns bounded redacted telemetry on mismatch.

## Reconciliation interface
Execution reports dispatch/evidence facts to Reconciliation; it does not infer settlement or mutate economic balances. Ledger posts remain separate, declared accounting events. Unknown/ambiguous external outcomes default to a frozen/reconciliation state.

## Tests
AI prompt/output fuzzing; missing/unknown action; policy substitution; risk limit breach and kill-switch; stale/conflicting quote; cross-tenant/environment/audience substitution; replay and revocation; adapter error. Assert that denial has no external privileged effect and no ledger event.
