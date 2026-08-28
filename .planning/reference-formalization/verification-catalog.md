# Verification Catalogue — Future Architecture and Contract Evidence

**Status:** specification only. This catalogue names evidence required before later work can claim a gate has passed. No test, scan, deployment, provider call or runtime process was executed in this planning phase.

## Verification policy

- A green unit test alone is never sufficient for a privileged financial claim. Every gate needs scope, environment, independent review and revalidation.
- Tests must assert both **no prohibited side effect** and the exact typed denial reason.
- Generated/property/model tests must persist their seed, contract version, policy hash and environment label on failure.
- Test fixtures must never contain production credentials, personal data, real signing keys, user wallet secrets or executable mainnet authorization.

| Family | Required evidence and must-fail cases | Primary sources |
|---|---|---|
| A1 Architecture boundary | Static module dependency/ownership report; rejection of direct cross-module writes; only contract/read projections cross modules; inbox/outbox transaction boundary scoped to one database | 01, ADR-0003/0004 |
| A2 Authority kernel | Finite action grammar; unknown action, untyped proposal, policy hash mismatch, expired/revoked authorization and missing independent approval all deny without dispatch | 02, 08, ADR-0001 |
| A3 Contract compatibility | Schema and semantic-version compatibility matrix; producer/consumer examples; unknown/duplicate/conflict/malformed envelope cases; exact correlation/causation/idempotency propagation | contracts, ADR-0003 |
| A4 Ledger properties | Debits equal credits per accounting event/batch; asset/tenant conservation; availability never below permitted constraints; post once; correction by compensating event; raw external evidence changes no balance | 03, ADR-0002 |
| A5 Payment model | Authorization/capture/fees/reversal/refund/settlement/correction/malformed/conflict permutations; order-independence; duplicate webhooks; no payment event bypasses accounting policy | 04 |
| A6 Withdrawal model | Intent lock exactly once; ownership and available-balance checks; stale/revoked/forged auth denial; broadcast ambiguous branch creates no second lock/debit/retry; reorg/failed/cancel branches reconcile explicitly | 05, ADR-0007/0011 |
| A7 Privileged adapter | Capability requires service identity, tenant, operation/resource, audience, environment, expiry and non-revocation; cross-tenant/substituted/audience-mismatch/timeout/malformed-provider inputs deny or quarantine | 06, 10, ADR-0005 |
| A8 Venue/chain/DEX | Venue-specific partial fill/cancel/timeout/stale price; chain duplicate log/reorg/finality; DEX gas/slippage/oracle discrepancy; no observation itself becomes settlement | 06, 07 |
| A9 Arbitrage/LP | Stale/non-comparable quote detection; fee/gas/slippage bound policy; LP range/price/fee drift observation and exit constraints; no profitability/capital-protection claim | 07, 08 |
| A10 AI/risk/execution | Prompt/model output fuzzing; invalid or out-of-vocabulary proposal; risk limit/kill-switch; policy downgrade; AI cannot sign, network or broadcast | 02, 08 |
| A11 Reconciliation/audit | Late/conflicting/absent evidence, unmatched ledger vs. provider fact, correction/compensation, audit hash break; separate test for external anchor/key/retention before stronger audit wording | 09, ADR-0008 |
| A12 Identity/security | Authentication failure, tenant isolation, role/capability attenuation, replay/nonce, key rotation/revocation, secret redaction, injection/serialization abuse, retention access control | 10 |
| A13 Observability/operations | Bound telemetry for denial/mismatch, alert routing without sensitive leakage, incident evidence package, recoverability and drill requirements | 09, 10 |
| A14 Maturity/release | Environment matrix isolation, backtest/replay determinism, paper/testnet scoping, mainnet attestation denial, CI provenance/SBOM/scan/contract gates, signed release/rollback exercises | 11, 12 |

## Evidence gate protocol

A future verifier records: test/spec ID; contract/ADR/policy hash; source revision; immutable result locator/digest; environment and fixture classification; executing identity; independent reviewer; result; exceptions; expiry/revalidation trigger. A test that cannot be tied to an approved scope remains `NO_PROOF` for readiness purposes.
