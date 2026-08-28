# Mainnet-Readiness Matrix

## Status semantics

- **PASS** — the exact requirement has independently verified evidence for a declared scope. A planning document alone does not qualify.
- **FAIL** — evidence shows the declared requirement is violated.
- **BLOCKED** — a mandatory decision/approval/dependency is unresolved; attempting the capability is forbidden.
- **NO_PROOF** — no adequate current evidence exists; it is not equivalent to PASS.

**Planning-phase baseline:** Overall mainnet status is **BLOCKED**. No row below is evidence of a deployed or authorized mainnet capability.

| Readiness dimension | Required proof before an operational PASS | Current planning-phase status | Blocking reason / needed gate |
|---|---|---:|---|
| Legal, regulatory and customer disclosure | Scope-specific legal opinion/disposition, entity/jurisdiction/customer/asset coverage, approved non-misleading copy | BLOCKED | Q-001; no “capital protection” promise allowed |
| Provider/venue/wallet capability | Owned active claim-register entries, config snapshots, expiring/revocable proof and boundary tests | NO_PROOF | Q-002; no provider capability assumed |
| Asset/chain/venue scope | Approved supported inventory plus reorg/finality/partial-fill/oracle/LP drift handling proof | BLOCKED | Q-005 |
| Financial authority | Running kernel evidence proving finite action vocabulary, proposal-only AI, policy pinning and default denial | NO_PROOF | ADR-0001/contract tests later |
| Accounting/ledger | Independent ledger conservation, availability lock and correction test evidence plus accounting approval | BLOCKED | Q-004 and M4 implementation/test evidence |
| Payment lifecycle | Authorization/capture/fee/reversal/refund/settlement/correction/malformed/conflict test evidence and reconciliation proof | BLOCKED | Q-001/Q-002/Q-004 |
| Withdrawal and wallet | Legal/custody/provider/signing proof, one-lock/ambiguous-broadcast test proof and recovery procedure | BLOCKED | Q-001/Q-002/Q-003/Q-004 |
| Signing and authorization | Per-operation signed/versioned authorization; tenant/environment/legal/expiry/revocation/replay verification; separate issuer controls | BLOCKED | Q-003 |
| Environment attestation | Sign/network/broadcast denials on mismatch with bounded telemetry evidence | NO_PROOF | Q-003/Q-010 |
| Authn/authz/tenant isolation | Threat-reviewed identity model, tenant isolation and privileged capability substitution/revocation test evidence | BLOCKED | Q-006/Q-007 |
| Risk/strategy/AI | Approved risk appetite/limits and proof that AI cannot directly act; kill-switch/exception evidence | BLOCKED | Q-007 |
| Market/execution/DEX/LP | Partial-fill, timeout, stale data, reorg, slippage, gas and LP-drift evidence per approved venue | BLOCKED | Q-002/Q-005/Q-007 |
| Reconciliation | Independent observed evidence vs. ledger event correlation; exception handling and aged-unreconciled procedures | NO_PROOF | M11/M13 evidence |
| Audit integrity | Hash-link integrity test plus external anchor, separate signing keys, immutable retention and incident procedure evidence before stronger claim | BLOCKED | Q-008 |
| Observability / operations | Alerting, bounded telemetry, access control, incident drill, recovery objectives and accountable owner evidence | BLOCKED | Q-008 |
| Backtest / paper / testnet | Reproducible evidence datasets, deterministic replay, scoped environment isolation; no readiness inference | NO_PROOF | M14 |
| CI / supply chain | Protected policy, provenance/SBOM, dependency/secret/security/contract test gates, reproducibility and reviewed exceptions | BLOCKED | Q-009/Q-010 |
| Release / rollback | Signed release, environment-specific approval, rollback and incident communications exercises | BLOCKED | Q-010 |
| Compliance records | Retention, legal holds, review schedule and non-overridable legal disposition enforcement | BLOCKED | Q-001/Q-008 |

## Overall decision

`MAINNET = BLOCKED`. No single category, including testnet success or a completed planning document, can lift this state. A future release authority must re-evaluate every row with contemporaneous scope-specific evidence and record the final decision; no inference from this matrix is permitted.
