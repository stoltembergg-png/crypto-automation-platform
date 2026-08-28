# Recommended PR / Review-Card Queue

**Queue baseline:** exactly **21** cards (`P01`–`P21`); allowable range **20–24** only by split/merge under the rules below. These are planned review units, **not generated pull requests**, and no card is represented as merged.

## Composition rules

1. A card must have a single coherent acceptance boundary, named reviewer roles, explicit dependencies, evidence expected, rejection action, and revalidation trigger.
2. A card may add only documentation in this phase. It cannot create a runtime implementation, grant capability, alter Vercel deployment behavior, or infer legal/provider/custody approval.
3. If one document change touches accounting, privileged authority, signing, withdrawal, provider claims, policy grammar, audit claims or legal disposition, require Security + domain owner + affected independent reviewer before approval.
4. Never increase the queue merely to meet a metric. High-risk traceability cards remain demand-driven; see `traceability-matrix.md`.
5. A blocked upstream Q gate means the card may document the block but cannot select a solution or close a readiness item.

| Phase / count | Card | Scope and concrete acceptance evidence | Depends on |
|---|---|---|---|
| A — Foundation (3) | P01 | Charter, scope, glossary, evidence vocabulary, planning-only attestation | M0 |
|  | P02 | Domain data/module ownership, trust map and diagrams | P01, M2 |
|  | P03 | ADR-0001..0004 and contract governance | P01–P02, M3 |
| B — Authority and financial semantics (4) | P04 | ADR-0005..0008: capability, claims, signed auth, audit boundary | P03, Q-002/Q-003/Q-008 dispositions |
|  | P05 | ADR-0009..0012: maturity, language gate, withdrawal denial, traceability | P03, Q-009 disposition |
|  | P06 | Ledger/accounting spec, accounting events, invariants, contract tests | P03, Q-004 |
|  | P07 | Proposal/policy kernel, strategy/AI/risk formal model | P03, P06, Q-007 |
| C — External and economic workflows (4) | P08 | Payment lifecycle and payment state-machine/negative-path contracts | P06, Q-001/Q-002/Q-004 |
|  | P09 | Withdrawal/wallet/MetaMask denied-by-default and one-lock ambiguity protocol | P06, P04, Q-001/Q-002/Q-003/Q-004 |
|  | P10 | Exchange/market capability, order/fill, idempotency and reconciliation contracts | P02, P04, Q-002/Q-005 |
|  | P11 | Chain/DEX finality/reorg contracts and evidence envelope | P10, Q-002/Q-005 |
| D — Strategy and execution (4) | P12 | Arbitrage strategy constraints, deterministic inputs and no-guarantee wording | P11, P07, Q-005/Q-007 |
|  | P13 | LP lifecycle, drift/fee/range observations and exit risk conditions | P11, P07, Q-005/Q-007 |
|  | P14 | Execution guards, authorization verification and adapter containment contracts | P07–P11, Q-003/Q-007 |
|  | P15 | Reconciliation, exception/compensation and external evidence correlation | P08–P14, P06 |
| E — Security, operations and maturity (4) | P16 | Auth/trust/threat/security model and adversarial test catalogue | P02–P05, Q-006/Q-007 |
|  | P17 | Audit integrity/observability/incident evidence and retention limits | P15–P16, Q-008 |
|  | P18 | Backtest/paper/testnet/mainnet maturity and readiness matrix | P12–P17, Q-005/Q-007/Q-008 |
|  | P19 | CI, release, provenance, rollback and Vercel `develop` planning-only rule | P18, Q-009/Q-010 |
| F — Assurance and freeze (2) | P20 | High-risk traceability, contract coverage and adversarial-review record | P01–P19 |
|  | P21 | Formal DAG, critical path, Q-gate audit, no-runtime attestation and baseline handoff | P20 |

## Merge/acceptance protocol

For each card: (a) static document/link and terminology review; (b) contract/ADR consistency review; (c) domain/security/legal owner review where triggered; (d) blocker and revalidation review; (e) capture disposition `PASS`, `FAIL`, `BLOCKED`, or `NO_PROOF`. A documentation `PASS` means the card has met document criteria only; it does not change `MAINNET = BLOCKED`.

## Formal dependency edges

`P01→P02→P03→P06→P08→P09→P14→P15→P17→P18→P19→P20→P21` is the review-queue critical path. P04/P05/P07/P10/P16 can proceed after their declared dependencies and owner gates; P11 follows P10; P12/P13 follow P11/P07. A downstream card must cite the upstream approved/proposed version and cannot silently substitute semantics.
