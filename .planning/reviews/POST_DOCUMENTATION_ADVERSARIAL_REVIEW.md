# Post-Documentation Adversarial Review Register

**Scope:** read-only review of the planning baseline at `E:/BOT`; no finding is evidence that a runtime exists.
**Roster:** security, quantitative/arbitrage/LP, exchange/custody, blockchain/DEX, backend/ledger, SRE, financial audit/compliance, fraud, red team.
**Disposition:** all findings below are **ACCEPTED AS DOCUMENTATION GAPS** and remediated by `docs/security/ADVERSARIAL_CLOSURE_SPEC.md`, `.planning/master/GATE_REGISTRY.md`, `docs/architecture/SPEC_PRECEDENCE.md`, corrected diagrams, and PR-134–PR-141. The implementation status remains `NOT_IMPLEMENTED`.

## Consolidated findings and closure mapping

| Review finding | Severity | Closure section / queue owner |
|---|---:|---|
| Conflicting Q-gate IDs and generic mainnet gates | Critical/High | §2; PR-134, PR-141 |
| Security traceability points to unrelated specs | High | precedence §; PR-134 |
| Decision issuer verification and exact spend binding absent | High | §1.2, §2; PR-141 |
| Cross-tenant ledger/account mutation possible | Critical | §1.1; PR-135 |
| `GLOBAL` payload classification can evade tenancy | High | §1; PR-135 |
| Withdrawal locking precedes final authorization / terminal handling diverges | High/Critical | §3.2; PR-136 |
| Withdrawal idempotency/ambiguous broadcast/retry gap | High | §3.2; PR-136 |
| Adapter submission lacks durable intent/outbox boundary | High | §3.2; PR-136 |
| Provider UNKNOWN and payment lifecycle/disputes underspecified | High | §3.1–§3.2; PR-136 |
| Reconciliation lacks comparable cut/freshness and can write Ledger directly | Critical/High | §3.3; PR-137 |
| Withdrawal/reconciliation queue ownership was unrelated | High | PR-136, PR-137 |
| Partial-fill economics, quote freshness and capital reservation gaps | High | §4.1; PR-138 |
| Correlation/impermanent-loss stress and non-vacuous backtests absent | High | §4.1; PR-138 |
| Nested router/permit/proxy safety gap | High | §4.2; PR-139 |
| Chain equivocation/finality, nonce and LP-reorg lifecycles absent | High | §4.2; PR-139 |
| MEV policy/fallback not executable | High | §4.3; PR-139 |
| Compliance disposition is generic; KYC/KYT/sanctions not execution-bound | High | §5; PR-140 |
| Pix cash-out, mule/beneficiary/device velocity and step-up invalidation gap | High | §5; PR-140 |
| Privacy lifecycle and source snapshot reproducibility gap | High | §2, §5; PR-134, PR-140 |
| Audit ordering/key boundary, kill propagation, measurable incident/chaos gates gap | High | §5–§6; PR-141 |
| CI/AI evidence root and GitHub/Vercel supply-chain boundary gap | High | §6; PR-141 |

## Review artifacts

The immutable subagent result files remain external review evidence under the Hermes delegation cache; they were used to create this traceable in-repository register. The full findings are not treated as source-of-truth contracts; the closure specification is.
