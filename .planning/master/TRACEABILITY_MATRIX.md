# Requirement Traceability Matrix

All rows are planning mappings. `future test` and `PR` describe obligations, not executed proof.

| User requirement | Topic | Canonical specification | Future test family | Queue cards |
|---|---|---|---|---|
| USR-001 | product/account/modes | `specifications/PRODUCT_SPEC.md` | contract/state/property/adversarial as applicable | PR-001, PR-004 |
| USR-002 | AI authority pipeline | `architecture/SYSTEM_ARCHITECTURE.md` | contract/state/property/adversarial as applicable | PR-002, PR-007 |
| USR-003 | Pix deposit | `architecture/DOMAIN_MODEL.md` | contract/state/property/adversarial as applicable | PR-003, PR-010 |
| USR-004 | Pix withdrawal | `architecture/DATA_MODEL.md` | contract/state/property/adversarial as applicable | PR-004, PR-013 |
| USR-005 | crypto withdrawal | `security/TRUST_BOUNDARIES.md` | contract/state/property/adversarial as applicable | PR-005, PR-016 |
| USR-006 | MetaMask | `security/THREAT_MODEL.md` | contract/state/property/adversarial as applicable | PR-006, PR-019 |
| USR-007 | custody | `architecture/CUSTODY_MODEL.md` | contract/state/property/adversarial as applicable | PR-007, PR-022 |
| USR-008 | double-entry ledger | `specifications/LEDGER_SPEC.md` | contract/state/property/adversarial as applicable | PR-008, PR-025 |
| USR-009 | exchange adapters | `specifications/PAYMENTS_SPEC.md` | contract/state/property/adversarial as applicable | PR-009, PR-028 |
| USR-010 | chains | `specifications/WITHDRAWALS_SPEC.md` | contract/state/property/adversarial as applicable | PR-010, PR-031 |
| USR-011 | DEX | `specifications/WALLET_SPEC.md` | contract/state/property/adversarial as applicable | PR-011, PR-034 |
| USR-012 | arbitrage | `specifications/MARKET_DATA_SPEC.md` | contract/state/property/adversarial as applicable | PR-012, PR-037 |
| USR-013 | triangular arbitrage | `specifications/EXCHANGE_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-013, PR-040 |
| USR-014 | liquidity pools | `specifications/CHAIN_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-014, PR-043 |
| USR-015 | risk limits | `specifications/DEX_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-015, PR-046 |
| USR-016 | AI provider | `specifications/ARBITRAGE_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-016, PR-049 |
| USR-017 | strategy plugins | `specifications/LIQUIDITY_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-017, PR-052 |
| USR-018 | portfolio manager | `specifications/STRATEGY_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-018, PR-055 |
| USR-019 | simulation | `specifications/AI_ORCHESTRATOR_SPEC.md` | contract/state/property/adversarial as applicable | PR-019, PR-058 |
| USR-020 | transaction guard | `specifications/RISK_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-020, PR-061 |
| USR-021 | protocol security | `specifications/EXECUTION_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-021, PR-064 |
| USR-022 | MEV | `specifications/TRANSACTION_GUARD_SPEC.md` | contract/state/property/adversarial as applicable | PR-022, PR-067 |
| USR-023 | bridges | `specifications/RECONCILIATION_SPEC.md` | contract/state/property/adversarial as applicable | PR-023, PR-070 |
| USR-024 | market data | `specifications/AUDIT_SPEC.md` | contract/state/property/adversarial as applicable | PR-024, PR-073 |
| USR-025 | real-time UX | `specifications/AUTH_SPEC.md` | contract/state/property/adversarial as applicable | PR-025, PR-076 |
| USR-026 | frontend | `specifications/SECURITY_SPEC.md` | contract/state/property/adversarial as applicable | PR-026, PR-079 |
| USR-027 | technology decision | `specifications/OBSERVABILITY_SPEC.md` | contract/state/property/adversarial as applicable | PR-027, PR-082 |
| USR-028 | data schema | `specifications/BACKTESTING_SPEC.md` | contract/state/property/adversarial as applicable | PR-028, PR-085 |
| USR-029 | security controls | `specifications/PAPER_TRADING_SPEC.md` | contract/state/property/adversarial as applicable | PR-029, PR-088 |
| USR-030 | secret management | `specifications/TESTNET_SPEC.md` | contract/state/property/adversarial as applicable | PR-030, PR-091 |
| USR-031 | audit | `specifications/MAINNET_ACTIVATION_SPEC.md` | contract/state/property/adversarial as applicable | PR-031, PR-094 |
| USR-032 | observability | `specifications/CI_CD_SPEC.md` | contract/state/property/adversarial as applicable | PR-032, PR-097 |
| USR-033 | reconciliation | `specifications/RELEASE_SPEC.md` | contract/state/property/adversarial as applicable | PR-033, PR-100 |
| USR-034 | idempotency | `compliance/COMPLIANCE_REVIEW.md` | contract/state/property/adversarial as applicable | PR-034, PR-103 |
| USR-035 | state machines | `specifications/PRODUCT_SPEC.md` | contract/state/property/adversarial as applicable | PR-035, PR-106 |
| USR-036 | paper trading | `architecture/SYSTEM_ARCHITECTURE.md` | contract/state/property/adversarial as applicable | PR-036, PR-109 |
| USR-037 | testnet | `architecture/DOMAIN_MODEL.md` | contract/state/property/adversarial as applicable | PR-037, PR-112 |
| USR-038 | mainnet gates | `architecture/DATA_MODEL.md` | contract/state/property/adversarial as applicable | PR-038, PR-115 |
| USR-039 | capital limits | `security/TRUST_BOUNDARIES.md` | contract/state/property/adversarial as applicable | PR-039, PR-118 |
| USR-040 | chaos engineering | `security/THREAT_MODEL.md` | contract/state/property/adversarial as applicable | PR-040, PR-121 |
| USR-041 | property tests | `architecture/CUSTODY_MODEL.md` | contract/state/property/adversarial as applicable | PR-041, PR-124 |
| USR-042 | adversarial tests | `specifications/LEDGER_SPEC.md` | contract/state/property/adversarial as applicable | PR-042, PR-127 |
| USR-043 | CI/CD | `specifications/PAYMENTS_SPEC.md` | contract/state/property/adversarial as applicable | PR-043, PR-130 |
| USR-044 | auto-merge | `specifications/WITHDRAWALS_SPEC.md` | contract/state/property/adversarial as applicable | PR-044, PR-133 |
| USR-045 | releases | `specifications/WALLET_SPEC.md` | contract/state/property/adversarial as applicable | PR-045, PR-003 |
| USR-046 | supply chain | `specifications/MARKET_DATA_SPEC.md` | contract/state/property/adversarial as applicable | PR-046, PR-006 |
| USR-047 | regulation/compliance | `specifications/EXCHANGE_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-047, PR-009 |
| USR-048 | privacy | `specifications/CHAIN_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-048, PR-012 |
| USR-049 | multi-tenancy | `specifications/DEX_ADAPTER_SPEC.md` | contract/state/property/adversarial as applicable | PR-049, PR-015 |
| USR-050 | admin | `specifications/ARBITRAGE_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-050, PR-018 |
| USR-051 | feature flags | `specifications/LIQUIDITY_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-051, PR-021 |
| USR-052 | automation modes | `specifications/STRATEGY_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-052, PR-024 |
| USR-053 | explainability | `specifications/AI_ORCHESTRATOR_SPEC.md` | contract/state/property/adversarial as applicable | PR-053, PR-027 |
| USR-054 | backtesting | `specifications/RISK_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-054, PR-030 |
| USR-055 | performance | `specifications/EXECUTION_ENGINE_SPEC.md` | contract/state/property/adversarial as applicable | PR-055, PR-033 |
| USR-056 | architecture decomposition | `specifications/TRANSACTION_GUARD_SPEC.md` | contract/state/property/adversarial as applicable | PR-056, PR-036 |
| USR-057 | planning artifacts | `specifications/RECONCILIATION_SPEC.md` | contract/state/property/adversarial as applicable | PR-057, PR-039 |
| USR-058 | ADRs | `specifications/AUDIT_SPEC.md` | contract/state/property/adversarial as applicable | PR-058, PR-042 |
| USR-059 | diagrams | `specifications/AUTH_SPEC.md` | contract/state/property/adversarial as applicable | PR-059, PR-045 |
| USR-060 | PR queue | `specifications/SECURITY_SPEC.md` | contract/state/property/adversarial as applicable | PR-060, PR-048 |
| USR-061 | DAG | `specifications/OBSERVABILITY_SPEC.md` | contract/state/property/adversarial as applicable | PR-061, PR-051 |
| USR-062 | milestones | `specifications/BACKTESTING_SPEC.md` | contract/state/property/adversarial as applicable | PR-062, PR-054 |
| USR-063 | MVP | `specifications/PAPER_TRADING_SPEC.md` | contract/state/property/adversarial as applicable | PR-063, PR-057 |
| USR-064 | mainnet criteria | `specifications/TESTNET_SPEC.md` | contract/state/property/adversarial as applicable | PR-064, PR-060 |
| USR-065 | adversarial review | `specifications/MAINNET_ACTIVATION_SPEC.md` | contract/state/property/adversarial as applicable | PR-065, PR-063 |
| USR-066 | non-goals | `specifications/CI_CD_SPEC.md` | contract/state/property/adversarial as applicable | PR-066, PR-066 |
| USR-067 | quality principles | `specifications/RELEASE_SPEC.md` | contract/state/property/adversarial as applicable | PR-067, PR-069 |
| USR-068 | final pipeline | `compliance/COMPLIANCE_REVIEW.md` | contract/state/property/adversarial as applicable | PR-068, PR-072 |
