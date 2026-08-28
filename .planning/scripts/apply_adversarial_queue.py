from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(r"E:/BOT")
Q = ROOT / ".planning/queue/queue.json"
CARDS = ROOT / ".planning/queue/PR_CARDS.md"
DAG = ROOT / ".planning/queue/DEPENDENCY_DAG.mmd"
INDEX = ROOT / ".planning/queue/QUEUE_INDEX.md"
REPORT = ROOT / ".planning/master/PLANNING_INTEGRITY_REPORT.json"

new_cards = [
    {
        "id": "PR-134", "milestone": "M0 Post-Review Planning Closure", "title": "Canonical gate registry and specification precedence", "slug": "canonical-gate-registry-and-precedence", "deps": ["PR-001"],
        "gates": "Registry semantics only; it grants no Q-gate PASS or financial capability.",
        "objective": "Make gate semantics and document precedence machine-checkable so evidence cannot close the wrong decision.",
        "scope": "Canonical GateId registry, authority precedence, semantic-parity validator and migration of all Q references; excludes provider/legal evaluation.",
        "files": "`.planning/master/GATE_REGISTRY.md`, `docs/architecture/SPEC_PRECEDENCE.md`, tests and all affected planning references.",
        "implementation": "Implement a versioned server-independent registry model and documentation validator; reject duplicate Q-ID meanings, generic mainnet gate sets and stale registry digests.",
        "tests": "ACT-004; negative semantic mismatch, stale digest and generic-gate-set tests.",
        "acceptance": "Every Q reference resolves to exactly one semantic decision/owner; no consumer treats URL retrieval as gate PASS.",
        "security": "Prevents approval-confusion paths across legal, provider, custody, accounting and release authority.",
        "observability": "Emit registry version/digest, gate evaluation scope, evidence digest, expiry and denial reason without raw evidence payload.",
        "rollback": "Disable gate evaluator; retain registry/audit history; forward-fix mappings without deleting prior evidence.",
    },
    {
        "id": "PR-135", "milestone": "M3 Ledger Amendment", "title": "Tenant and environment ledger boundary", "slug": "tenant-environment-ledger-boundary", "deps": ["PR-008", "PR-134"],
        "gates": "Q-004, Q-006, Q-009; unresolved or mismatched gate denies claimed implementation readiness.",
        "objective": "Make cross-tenant/environment financial mutation impossible even to service-role and migration paths.",
        "scope": "Composite scoped keys, AccountingCommand-only writer boundary and server-owned contract classification; excludes real ledger operation.",
        "files": "`docs/specifications/LEDGER_SPEC.md`, `docs/architecture/DATA_MODEL.md`, future ledger migration/schema and focused tests.",
        "implementation": "Require tenant/environment on every financial/authority row; enforce composite FKs and deny forged GLOBAL classification or direct adapter/reconciliation/AI ledger calls.",
        "tests": "ACT-001, ACT-002; service-role cross-tenant, balanced cross-tenant and forged-GLOBAL negative tests.",
        "acceptance": "No balanced entry can span tenant/environment; Ledger accepts only current AccountingCommand.v1 with matching scope.",
        "security": "Contains privileged-worker, migration and object-substitution blast radius.",
        "observability": "Record bounded tenant/environment mismatch reason, command digest and correlation ID.",
        "rollback": "Feature-disable new writer path; use forward-compatible schema migration/compensating records; never drop journal history.",
    },
    {
        "id": "PR-136", "milestone": "M5 Withdrawal Amendment", "title": "Withdrawal intent, one-lock and ambiguous broadcast protocol", "slug": "withdrawal-intent-one-lock-ambiguous-broadcast", "deps": ["PR-027", "PR-135"],
        "gates": "Q-002, Q-003, Q-004, Q-007; all named decisions remain deny-by-default.",
        "objective": "Serialize withdrawal authorization, economic locking, outbox submission and ambiguous recovery without duplicate spend.",
        "scope": "Withdrawal state machine, lock protocol, adapter request boundary and provider-UNKNOWN handling; excludes enabled payout/wallet provider.",
        "files": "`docs/specifications/WITHDRAWALS_SPEC.md`, `EXCHANGE_ADAPTER_SPEC.md`, contracts, future state-machine code and tests.",
        "implementation": "Require PREAUTHORIZED before one atomic LOCK_POSTED; require durable intent/outbox/capability for submit; prohibit retry/rebroadcast on BROADCAST_AMBIGUOUS.",
        "tests": "ACT-006, ACT-007, ACT-008 plus denial/expiry/revocation-before-lock and linked-recovery tests.",
        "acceptance": "Pre-lock failure has no posting; same intent cannot double-lock or rebroadcast; new recovery intent has fresh authority/evidence.",
        "security": "Prevents timeout double debit, destination mutation, ambient adapter withdrawal and cash-out bypass.",
        "observability": "Emit intent/lock/outbox/evidence correlation and opaque ambiguity state; redact destination/PII.",
        "rollback": "Disable withdrawal capability; preserve lock and audit history; resolve through reconciled compensating workflow only.",
    },
    {
        "id": "PR-137", "milestone": "M9 Reconciliation Amendment", "title": "Comparable-cut reconciliation and accounting authority", "slug": "comparable-cut-reconciliation-authority", "deps": ["PR-054", "PR-135"],
        "gates": "Q-004, Q-008; any missing source completeness or correction authority keeps the scope blocked.",
        "objective": "Ensure reconciliation evaluates comparable evidence and can only propose—not post—financial corrections.",
        "scope": "ReconciliationRun/EvidenceSet/CorrrectionProposal contracts, authority diagram and future negative tests; excludes provider data retrieval.",
        "files": "`docs/specifications/RECONCILIATION_SPEC.md`, diagrams, future reconciliation module and tests.",
        "implementation": "Require cutoffs, scope, cursors, completeness, finality and tolerance; gate MATCHED; route CorrectionProposal through Accounting Authority to AccountingCommand.",
        "tests": "ACT-009 and negative direct-ledger-write, stale/paginated evidence and correction-authorization tests.",
        "acceptance": "Incomplete evidence never matches; reconciliation identity has no Ledger-write capability.",
        "security": "Prevents external evidence or worker compromise from changing balances.",
        "observability": "Record evidence digest/cutoff/completeness, mismatch age/owner and capability-block scope.",
        "rollback": "Suspend correction capability; preserve cases/evidence; issue only authorized compensating records.",
    },
    {
        "id": "PR-138", "milestone": "M11 Arbitrage Amendment", "title": "Residual PnL, quote reservation and non-vacuous backtesting", "slug": "residual-pnl-quote-reservation-backtesting", "deps": ["PR-068"],
        "gates": "Q-005 and Q-007; no strategy claim or funded path before approved asset/risk evidence.",
        "objective": "Prevent full-cycle theoretical spreads from hiding residual, partial-fill, freshness or correlation loss.",
        "scope": "NetPnL, QuoteReservation, recovery semantics, correlation/IL stress and backtest evidence contract; excludes live strategy execution.",
        "files": "`ARBITRAGE_ENGINE_SPEC.md`, `BACKTESTING_SPEC.md`, future simulator/backtest tests and reports.",
        "implementation": "Compute realised and conservative residual economics; serialize quote/capital reservations; fail closed on stale/future/zero-scenario data or unavailable hedge.",
        "tests": "ACT-010 plus partial-fill unavailable-hedge, stale/future-data mutation, changed-cost and zero/skip-scenario tests.",
        "acceptance": "Recovery-required outcome cannot meet profit threshold; runner proves point-in-time inputs, calibration and non-vacuous scenarios.",
        "security": "Limits model laundering and capital exposure under stale or adversarial market data.",
        "observability": "Record snapshots, model/calibration/cost hashes, reservations, residual valuation and recovery outcome.",
        "rollback": "Disable strategy/capital capability; expire reservations; retain simulation evidence and no destructive PnL rewrite.",
    },
    {
        "id": "PR-139", "milestone": "M13 DEX Amendment", "title": "Recursive transaction envelope, finality and MEV submission policy", "slug": "recursive-envelope-finality-mev-policy", "deps": ["PR-074"],
        "gates": "Q-003, Q-005, Q-007; absence of allowed chain/protocol/signing evidence denies all submission.",
        "objective": "Bind every nested DEX action and chain observation to a safe plan, finality and submission-channel policy.",
        "scope": "Recursive envelope grammar, proxy/code pinning, nonce lifecycle, reorg/LP finality and MEV fallback policy; excludes chain enablement.",
        "files": "`DEX_ADAPTER_SPEC.md`, `CHAIN_ADAPTER_SPEC.md`, `TRANSACTION_GUARD_SPEC.md`, `LIQUIDITY_ENGINE_SPEC.md` and future contract tests.",
        "implementation": "Deny unknown nested calls; bind permits/sweeps/approvals; pin implementation/hash/block; require fresh simulation for changes; serialize nonce/reorg/channel fallback.",
        "tests": "ACT-011, ACT-012 plus hidden recipient/permit, proxy change, equivocation, nonce race, LP reorg and public-channel fallback tests.",
        "acceptance": "No nested field or fallback changes after authorization; ACTIVE LP requires finality; no channel claims privacy/inclusion guarantee.",
        "security": "Stops calldata smuggling, approval drain, proxy drift, reorg and mempool-risk fallback.",
        "observability": "Record envelope/proxy/block/simulation/submission-policy digests and opaque denial reason.",
        "rollback": "Revoke protocol/chain/channel capability; do not resubmit ambiguous operations; reconcile evidence before any linked recovery.",
    },
    {
        "id": "PR-140", "milestone": "M19 Compliance Amendment", "title": "Execution-bound compliance, fraud and privacy decisions", "slug": "execution-bound-compliance-fraud-privacy", "deps": ["PR-117"],
        "gates": "Q-001, Q-006, Q-007; require separately approved legal/privacy/compliance evidence before any activation.",
        "objective": "Make compliance, fraud and privacy decisions explicit spend gates rather than labels in a review document.",
        "scope": "ComplianceDecision/FraudRiskDecision, data lifecycle, step-up invalidation and cash-out holds; excludes provider/legal approval.",
        "files": "`docs/compliance/COMPLIANCE_REVIEW.md`, `POLICY_DECISION.md`, `RISK_ENGINE_SPEC.md`, future decision services/tests.",
        "implementation": "Bind subject/payer/destination/screening and privacy-classified velocity/recovery signals; HOLD/REVIEW denies credit availability, lock and broadcast.",
        "tests": "ACT-013 plus sanctions destination, mule linkage, rapid cash-out, device/credential recovery change and retention/immutable-exception tests.",
        "acceptance": "No spend path accepts stale/missing/HOLD/REVIEW decision; PII lifecycle has purpose, owner, retention/deletion and exception reference.",
        "security": "Reduces sanctioned destination, mule, takeover and privacy over-collection risk.",
        "observability": "Use bounded/pseudonymous reason codes, decision versions and correlation IDs; never log raw screening/PII payloads.",
        "rollback": "Fail closed to HOLD; retain legally required minimised audit records; forward-fix rules with versioned re-evaluation.",
    },
    {
        "id": "PR-141", "milestone": "M20 Mainnet Assurance Amendment", "title": "Exact mainnet gate binding, audit order and supply-chain boundary", "slug": "exact-mainnet-gates-audit-supply-chain", "deps": ["PR-129", "PR-130", "PR-131", "PR-132", "PR-133", "PR-140"],
        "gates": "Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009 and Q-010, each explicit, current and scope-matching.",
        "objective": "Close release/mainnet assurance around exact authorization, atomic reservations, audit ordering, kill drills and protected evidence root.",
        "scope": "MainnetAuthorization verification, audit sequencing/anchors, scoped kill drills, CI/OIDC/provenance and Vercel static-only boundary; excludes mainnet activation.",
        "files": "`MAINNET_ACTIVATION_SPEC.md`, `READINESS_AUTHORIZATION.md`, `AUDIT_SPEC.md`, `CI_CD_SPEC.md`, `RELEASE_SPEC.md`, future tests/config snapshots.",
        "implementation": "Verify exact action/resource/amount/destination/gates/evidence/reservations/quorum; protect evidence root and release provenance; verify scoped kill propagation and static deploy boundary.",
        "tests": "ACT-003, ACT-014, ACT-015, ACT-016 plus duplicate-principal quorum, reservation race, CI evidence substitution and Vercel-boundary negatives.",
        "acceptance": "Any mismatched/expired/revoked gate/evidence/signer/reservation/quorum denies before signing; static status deployment has no financial authority.",
        "security": "Prevents approval laundering, audit rewrite races, kill-switch gaps and supply-chain/evidence-root substitution.",
        "observability": "Record signed authorization/gate/evidence/reservation/quorum/provenance digests and drill results, never secret values.",
        "rollback": "Revoke mainnet capability and freeze promotion; preserve immutable evidence/audit; containment only, never spend break-glass.",
    },
]

queue = json.loads(Q.read_text(encoding="utf-8"))
assert len(queue) == 133, len(queue)
assert not {x["id"] for x in queue} & {x["id"] for x in new_cards}
queue.extend([{k: c[k] for k in ("id", "milestone", "title", "slug", "deps")} for c in new_cards])
Q.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

md = CARDS.read_text(encoding="utf-8")
replacements = {
    "- **Dependencies:** PR-123; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.": "- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.",
    "- **Dependencies:** PR-128; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.": "- **Dependencies:** PR-128; exact Q-ID set is operation-bound and registry-digested; generic Q ranges deny.",
    "- **Dependencies:** PR-128, PR-132; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.": "- **Dependencies:** PR-128, PR-132; Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010; each must be exact, current and scope-matching.",
}
for old, new in replacements.items():
    md = md.replace(old, new)
for c in new_cards:
    deps = ", ".join(c["deps"])
    md += f"\n## {c['id']} — {c['title']}\n"
    md += f"- **Milestone:** {c['milestone']}\n"
    md += f"- **Objective:** {c['objective']}\n"
    md += f"- **Scope:** {c['scope']}\n"
    md += f"- **Files:** {c['files']}\n"
    md += f"- **Dependencies:** {deps}; {c['gates']}\n"
    md += f"- **Implementation:** {c['implementation']}\n"
    md += f"- **Tests:** {c['tests']}\n"
    md += f"- **Acceptance criteria:** {c['acceptance']}\n"
    md += f"- **Security implications:** {c['security']}\n"
    md += f"- **Observability:** {c['observability']}\n"
    md += f"- **Rollback:** {c['rollback']}\n"
    md += f"- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.\n"
CARDS.write_text(md, encoding="utf-8")

edges = [
    ("PR_001", "PR_134"), ("PR_134", "PR_008"),
    ("PR_008", "PR_135"), ("PR_134", "PR_135"), ("PR_135", "PR_017"),
    ("PR_027", "PR_136"), ("PR_135", "PR_136"), ("PR_136", "PR_035"),
    ("PR_054", "PR_137"), ("PR_135", "PR_137"), ("PR_137", "PR_061"),
    ("PR_068", "PR_138"), ("PR_138", "PR_074"),
    ("PR_074", "PR_139"), ("PR_139", "PR_080"),
    ("PR_117", "PR_140"), ("PR_140", "PR_123"),
    ("PR_129", "PR_141"), ("PR_130", "PR_141"), ("PR_131", "PR_141"),
    ("PR_132", "PR_141"), ("PR_133", "PR_141"), ("PR_140", "PR_141"),
]
dag = DAG.read_text(encoding="utf-8")
dag += "\n  %% Post-documentation adversarial closure overlay\n"
dag += "\n".join(f"  {a} --> {b}" for a, b in edges) + "\n"
DAG.write_text(dag, encoding="utf-8")

INDEX.write_text("""# Queue Index and Milestones

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
""", encoding="utf-8")

report = json.loads(REPORT.read_text(encoding="utf-8"))
report.update({"required_files": 87, "queue_card_count": 141, "dag_acyclic": True, "note": "PASS validates documented topology and adversarial-closure references only; it is not implementation, provider, legal, security, test, deployment or mainnet proof."})
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("applied 8 adversarial closure cards")
