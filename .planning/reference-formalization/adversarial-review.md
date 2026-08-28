# Adversarial Review Record and Required Hostile Review

## Evidence boundary

This plan was formalized from a **reviewed insight bundle supplied by the requester**. The bundle is treated as a set of constraints, not proof of provider, legal, runtime, audit, security, or mainnet readiness. No new independent runtime test, provider test, legal review, or live-system verification is claimed by this record.

## Mandatory pre-implementation hostile review

Before any implementation card that could affect privileged financial behavior is approved, conduct a five-role review. Preserve every finding ID and disposition; remove claims defeated in review.

| Role | Required attack | Required output |
|---|---|---|
| Skeptic | Scope creep, premature services/broker/provider/language selection, unjustified readiness claims | Numbered subtraction findings with evidence requirement |
| Validator | Illegal state transitions, idempotency/tenant boundaries, failure/retry/reorg/partial-fill/LP-drift vectors | Numbered negative paths and tests |
| Researcher | Unsupported capabilities, legal claims, performance/security assertions and source freshness | Citation or explicit `NO_PROOF` per material claim |
| Architect | Cross-module writes, leaky contracts, false atomicity, adapter bypass and brittle coupling | Boundary/consequence/simpler alternative |
| Creative | First-thought assumptions, authority inversions, safer constrained alternatives | Concrete alternative and its winning condition |

## Non-waivable attack targets

1. AI proposal output attempts direct kernel/adapter/sign/network/broadcast access.
2. Duplicate/replayed/cross-tenant payment or withdrawal input locks/reverses/debits more than once.
3. Ambiguous broadcast causes automatic resubmission or a second economic accounting mutation.
4. A raw provider/chain/venue status changes an availability balance without a declared accounting event.
5. Policy/authorization/version/legal/tenant/environment/audience/expiry/revocation/replay binding is omitted or downgraded.
6. A provider claim is inferred from marketing, defaults, a generic API, or a testnet behavior.
7. Audit wording exceeds hash-linked tamper detection without anchor/key/retention/incident evidence.
8. Testnet, backtest or paper success is presented as legal, custody, provider or mainnet readiness.
9. Partial fill, reorg/finality, cancellation race, oracle disagreement, gas/slippage or LP drift is collapsed into final settlement.
10. Any customer-facing sentence promises capital protection or omits required legal disposition.

## Review exit criteria

A review card is `PASS` only if each finding is `DEFEND`ed with cited evidence, `REFINE`d into a narrower verifiable requirement, or `CONCEDE`d and removed. “Uncontested” is valid only when the record shows the finding was exposed to the relevant independent reviewer. No closed review finding lifts a mainnet readiness row without its separate operational proof.

## Current formalization disposition

`FORMALIZATION_COMPLETE / ADVERSARIAL_RUNTIME_EVIDENCE = NO_PROOF`. The planning package contains a review protocol and hardened constraints; it does not fabricate a completed five-role review transcript or an implementation result.
