# SDD-11 — Backtest, Paper, Testnet and Mainnet Maturity

**Status:** maturity framework only; `MAINNET = BLOCKED`.

## Environment separation
Every artifact carries one environment: `BACKTEST`, `PAPER`, `TESTNET`, `MAINNET`. Data, identities, credentials, authorizations, endpoints, asset scopes, audit records and release gates are environment-bound. A mismatch at a privileged sign/network/broadcast boundary must deny and emit bounded telemetry. No testnet or paper credential can be accepted as mainnet authorization.

## Maturity capabilities
| Environment | Permitted future scope after its own gates | Explicitly does not prove |
|---|---|---|
| Backtest | Historical/replay analysis over versioned datasets and assumptions | future performance, live liquidity, provider capability, legal/custody readiness |
| Paper | Simulated proposal/risk/execution/reconciliation workflows | live execution, settlement, user protection, provider/legal readiness |
| Testnet | Approved test-network adapter and chain observation exercise | mainnet chain/provider/asset support, signing/custody/legal readiness |
| Mainnet | Only after every readiness-matrix row has contemporaneous operational proof | perpetual correctness or capital protection |

## Gate design
A maturity promotion has a scoped target capability, asset/venue/network, policy/contract version, environment attestation, independent reviewers, expiry and rollback. It is not a global “environment certified” flag. Backtest/paper/testnet exits cannot waive Q-001 legal, Q-002 provider claims, Q-003 custody/signing, Q-004 accounting, Q-005 scope, Q-007 risk, Q-008 operations or Q-010 release authority.

## Required evidence
Reproducible dataset/assumption provenance; deterministic replay/test seed where applicable; environment isolation; failure/rollback tests; escalation/incident drill; evidence expiry/revalidation. For mainnet, signed authorization and environment attestation must be validated immediately before privileged boundary use.
