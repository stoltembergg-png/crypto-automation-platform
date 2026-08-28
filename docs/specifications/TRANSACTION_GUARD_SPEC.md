# Transaction Guard Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines last deterministic pre-signing validation.

## Normative requirements

- Pipeline: decoder→allowlist→amount/token/contract/function→slippage→risk→simulation→authorization binding→signer request.
- Permit finite action templates only; decoded candidate and signer payload must hash-equate approved plan.
- The accepted envelope is finite/versioned and recursively decoded: every nested permit, approval, unwrap/sweep, recipient, spender, value, deadline and target must bind to the approved plan; unsupported dynamic subcalls deny.
- Simulation/guard evidence binds a pinned block and target code/proxy implementation digest. Changed state/finality assumption, code, channel or fallback requires fresh simulation and authorization.
- Verify mainnet authorization/environment attestation at privileged spend boundary.

## Component contracts

DecodedAction, GuardDecision, AllowlistRegistry, SignerRequest, AuthorizationBinding.

## Invariants and deny conditions

Any unknown selector, proxy implementation, token, recipient, amount, nonce, chain, allowance, slippage, price impact, gas or authorization mismatch denies before signing/network operation.

## State and failure semantics

CANDIDATE→DECODED→VALIDATED→GUARDED→SIGNER_REQUESTED|DENIED.

## Future verification

Decoder fuzzing, malicious calldata, template bypass, plan-hash mismatch, wrong chain, stale sim, nonce conflict and signer equivalence tests.

## Queue ownership

Implementation is decomposed in `PR-061..PR-067`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/08-strategy-ai-risk-and-execution.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
