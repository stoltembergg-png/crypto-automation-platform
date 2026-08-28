# Crypto Automation Platform — Planning Baseline

> **Status:** Planning only. No financial runtime, provider credentials, funds, wallets, trades, testnet or mainnet capability exists in this repository.

This repository contains the specification-driven baseline for a deterministic capital-protection platform with optional AI proposals. It does **not** claim legal approval, provider authorization, custody readiness or production capability.

## Start here

- [Executive product specification](docs/specifications/PRODUCT_SPEC.md)
- [System architecture](docs/architecture/SYSTEM_ARCHITECTURE.md)
- [Threat model](docs/security/THREAT_MODEL.md)
- [Compliance blockers](docs/compliance/COMPLIANCE_REVIEW.md)
- [Mainnet readiness matrix](.planning/master/MAINNET_READINESS_MATRIX.md)
- [Executable PR queue — 133 cards](.planning/queue/PR_CARDS.md)
- [Dependency DAG](.planning/queue/DEPENDENCY_DAG.mmd)
- [Requirement traceability](.planning/master/TRACEABILITY_MATRIX.md)
- [Adversarial review result](.planning/reviews/HYPERPLAN_INSIGHT_BUNDLE.md)

## Public development status

The static, non-financial progress page is served at `/develop`. It shows planning counts and `MAINNET BLOCKED`; it neither connects to providers nor accepts any financial action.

## Verification

```bash
node --test tests/planning_sdd.test.mjs
node C:/Users/Gabriel/AppData/Local/hermes/skills/onp-spec-driven/scripts/onp-spec.mjs verify crypto-automation-platform-planning
node C:/Users/Gabriel/AppData/Local/hermes/skills/onp-spec-driven/scripts/onp-spec.mjs audit --ci
```

The last two commands validate documentation traceability only. They are not evidence for product security, legal compliance, provider authority, execution behavior or mainnet readiness.
