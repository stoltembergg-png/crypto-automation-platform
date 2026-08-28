# Planning Requirements Catalog

This catalog normalizes the user-provided mandate into stable requirement groups. It is a traceability input, not evidence of implementation.

| Group | Stable ID | Requirement boundary | Canonical planned specs |
|---|---|---|---|
| Product and modes | RQ-PROD | Account, security, Pix funding, visibility, real-time UX, MANUAL/ADVISORY/PROPOSE/AUTO modes, feature flags, phased MVP. | PRODUCT_SPEC, AUTH_SPEC, PAPER_TRADING_SPEC, MAINNET_ACTIVATION_SPEC |
| Financial authority | RQ-FIN | BRL/asset accounting, pending/reserved/available funds, deposits, withdrawals, fees, PnL, reconciliation, immutable audit. | LEDGER_SPEC, PAYMENTS_SPEC, WITHDRAWALS_SPEC, RECONCILIATION_SPEC, AUDIT_SPEC |
| Safe automation | RQ-SAFE | AI proposes only; risk/policy/simulation/transaction guard/signer/reconciliation pipeline with no direct LLM-to-transaction path. | AI_ORCHESTRATOR_SPEC, RISK_ENGINE_SPEC, EXECUTION_ENGINE_SPEC, TRANSACTION_GUARD_SPEC |
| Custody and wallets | RQ-CUST | Custody decision, key isolation, KMS/HSM/MPC/multisig evaluation, hot/warm/cold separation, MetaMask as external wallet initially. | CUSTODY_MODEL, WALLET_SPEC, SECURITY_SPEC |
| Trading connectivity | RQ-CONN | Capability-negotiated exchange, chain, DEX, bridge abstractions; leverage/margin/futures disabled initially. | EXCHANGE_ADAPTER_SPEC, CHAIN_ADAPTER_SPEC, DEX_ADAPTER_SPEC, MARKET_DATA_SPEC |
| Strategy domain | RQ-STRAT | Arbitrage, triangular graph detection, LP/concentrated-liquidity management, portfolio allocation and future plugins. | ARBITRAGE_ENGINE_SPEC, LIQUIDITY_ENGINE_SPEC, STRATEGY_ENGINE_SPEC, BACKTESTING_SPEC |
| Security and resilience | RQ-SEC | Zero trust, strong auth, tenant isolation, idempotency, state machines, protocol due diligence, MEV, chaos, adversarial and property-based testing. | THREAT_MODEL, TRUST_BOUNDARIES, AUTH_SPEC, SECURITY_SPEC, TESTING_STRATEGY |
| Operations and governance | RQ-OPS | Observability, alerting, administrative kill switches, CI/CD, supply chain, release, auto-merge governance and mainnet gates. | OBSERVABILITY_SPEC, CI_CD_SPEC, RELEASE_SPEC, MAINNET_ACTIVATION_SPEC |
| Compliance and privacy | RQ-COMP | Brazilian legal/regulatory review, AML/KYC/KYT/sanctions, tax, LGPD, retention, operator and provider obligations. | COMPLIANCE_REVIEW, DATA_MODEL, SECURITY_SPEC |

## Non-negotiable acceptance themes

- **Capital preservation:** no subsystem may spend, reserve, release, or report a user asset outside ledger, policy, and reconciliation controls.
- **Determinism:** user- and system-defined policy decides authorization; model output is untrusted structured input.
- **Fail closed:** stale price, provider outage, mismatch, missing proof, bad state transition, unavailable guard, or unknown capability blocks the affected action.
- **Auditability:** every financial decision is correlated across actor, policy, proposal, simulation, signed intent, external reference, ledger posting, reconciliation, and result.
- **Isolation:** cross-tenant access is denied by both application authorization and database row-level policy when persistence is introduced.
- **Truthful readiness:** planned artifacts are not implementation evidence; skipped/no-op tests are not PASS.
