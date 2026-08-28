# Contract Catalogue and Versioning Rules

**Status:** normative design contract; no schemas are implemented here.

| Contract | Producer | Consumers | Authority / mutation rule |
|---|---|---|---|
| `Proposal.v1` | User/workflow/AI translator | Policy/Risk | Non-authoritative input only |
| `AuthorityDecision.v1` | Policy kernel | Execution/Ledger workflow | Typed disposition; no adapter command itself |
| `AccountingCommand.v1` / `AccountingEvent.v1` | Authorized workflow / Ledger | Ledger/read models/audit | Only Ledger posts balanced event |
| `PaymentFact.v1` | Payments/provider adapter | Reconciliation/Payments | External evidence; no direct ledger update |
| `WithdrawalIntent.v1` / `BroadcastFact.v1` | Withdrawal/adapter | Execution/Reconciliation | Intent may lock once; evidence cannot double mutate |
| `MarketObservation.v1` / `OrderFact.v1` | Venue adapter | Strategy/Risk/Reconciliation | Untrusted/source scoped facts |
| `ChainObservation.v1` / `DexOperationFact.v1` | Chain/DEX adapter | Reconciliation | Network/finality/reorg scoped evidence |
| `RiskDecision.v1` | Risk | Authority/Execution | Necessary independent gate, not spend authority |
| `ReconciliationCase.v1` | Reconciliation | Finance/Operations | Correlates/flags; does not post |
| `AuditEntry.v1` | Every security-relevant module | Audit | Append-only detection record |

All contracts require name, semantic version, schema digest, tenant/environment where applicable, correlation/causation, timestamp, producer identity, classification and idempotency semantics. Breaking change = major version and an explicit migration/replay/compatibility plan. The consumer must reject unknown privileged action/enumeration values; permissive unknown fields require documented compatibility behavior.
