# Queue Index and Milestones

## Milestone distribution

| Milestone | Cards | Anchor |
|---|---:|---|
| M1 Repository Foundation | 7 | PR-001 |
| M2 Identity & Security | 9 | PR-008 |
| M3 Ledger | 10 | PR-017 |
| M4 Payments | 8 | PR-027 |
| M5 Wallet Infrastructure | 6 | PR-035 |
| M6 Market Data | 7 | PR-041 |
| M7 Exchange Integration | 6 | PR-048 |
| M8 Risk Engine | 7 | PR-054 |
| M9 Execution Engine | 7 | PR-061 |
| M10 Paper Trading | 6 | PR-068 |
| M11 Arbitrage | 6 | PR-074 |
| M12 Blockchain | 7 | PR-080 |
| M13 DEX | 7 | PR-087 |
| M14 Liquidity Pools | 6 | PR-094 |
| M15 AI Layer | 6 | PR-100 |
| M16 Portfolio Automation | 6 | PR-106 |
| M17 Testnet | 5 | PR-112 |
| M18 Security Hardening | 6 | PR-117 |
| M19 Compliance Readiness | 5 | PR-123 |
| M20 Mainnet Readiness | 6 | PR-128 |

## Critical path

PR-001 → PR-008 → PR-017 → PR-027 → PR-035 → PR-041 → PR-048 → PR-054 → PR-061 → PR-068 → PR-074 → PR-080 → PR-087 → PR-094 → PR-100 → PR-106 → PR-112 → PR-117 → PR-123 → PR-128

Other cards within a milestone may begin after their anchor if their contract ownership is disjoint. Shared ledger, policy, state-machine, migration, public-schema and workflow changes serialize semantically even if files differ.
