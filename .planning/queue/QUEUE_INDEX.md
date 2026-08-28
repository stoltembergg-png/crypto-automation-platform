# Queue Index and Milestones

## Amendment overlay

PR-134–PR-141 are additive post-documentation adversarial-closure cards. Stable IDs PR-001–PR-133 are unchanged. Their DAG edges deliberately insert the amendment contracts before the affected future implementation anchors; numeric IDs are identifiers, not schedule authority.

## Milestone distribution

| Milestone | Cards | Anchor |
|---|---:|---|
| M0 Post-Review Planning Closure | 1 | PR-134 |
| M1 Repository Foundation | 7 | PR-001 |
| M2 Identity & Security | 9 | PR-008 |
| M3 Ledger | 11 | PR-017 + PR-135 |
| M4 Payments | 8 | PR-027 |
| M5 Wallet Infrastructure | 7 | PR-035 + PR-136 |
| M6 Market Data | 7 | PR-041 |
| M7 Exchange Integration | 6 | PR-048 |
| M8 Risk Engine | 7 | PR-054 |
| M9 Execution Engine | 8 | PR-061 + PR-137 |
| M10 Paper Trading | 6 | PR-068 |
| M11 Arbitrage | 7 | PR-074 + PR-138 |
| M12 Blockchain | 7 | PR-080 |
| M13 DEX | 8 | PR-087 + PR-139 |
| M14 Liquidity Pools | 6 | PR-094 |
| M15 AI Layer | 6 | PR-100 |
| M16 Portfolio Automation | 6 | PR-106 |
| M17 Testnet | 5 | PR-112 |
| M18 Security Hardening | 6 | PR-117 |
| M19 Compliance Readiness | 6 | PR-123 + PR-140 |
| M20 Mainnet Readiness | 7 | PR-128 + PR-141 |

## Critical path

PR-001 → PR-134 → PR-008 → PR-135 → PR-017 → PR-027 → PR-136 → PR-035 → PR-041 → PR-048 → PR-054 → PR-137 → PR-061 → PR-068 → PR-138 → PR-074 → PR-139 → PR-080 → PR-087 → PR-094 → PR-100 → PR-106 → PR-112 → PR-117 → PR-140 → PR-123 → PR-128 → PR-132 → PR-133 → PR-141

Other cards within a milestone may begin only after all graph predecessors and named authority gates. Shared ledger, policy, state-machine, public-schema, migration, workflow and release changes serialize semantically even if files differ.
