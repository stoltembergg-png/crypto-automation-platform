# Canonical Gate Registry

**Status:** `PLANNING_ONLY` — this is the sole canonical meaning of `Q-001` through `Q-010`.

## Authority and use

1. This registry is the only definition of Q-gate semantics. A Q-ID may never be reused with a different decision, owner, or activation effect.
2. `OPEN_QUESTIONS.md`, readiness matrices, ADRs, contracts, queue cards, and future automation must reference this registry by ID and semantic title.
3. A gate is **not** PASS because an URL is reachable, a document exists, an environment deploys, or a plan describes a control. Missing, expired, contradictory, improperly scoped, or unreproducible evidence is `NO_PROOF` and fails closed.
4. Each evaluated gate record must bind: `gate_id`, registry digest/version, decision title, owner, scope, evidence digest/path, observed-at UTC, expiry/revalidation trigger, reviewer disposition, and revocation state.
5. This is a planning registry. It grants no provider, legal, custody, signing, CI, deployment, or mainnet permission.

| ID | Canonical decision | Accountable owner | Minimum future evidence to evaluate | Current disposition |
|---|---|---|---|---|
| Q-001 | Legal entity, jurisdiction, licensing and regulatory disposition | Legal/compliance accountable executive | signed legal review with scope, effective date, exceptions and expiry | `REQUIRES_LEGAL_REVIEW` |
| Q-002 | Provider, exchange, payment and venue capability/contract eligibility | Provider operations owner | versioned provider terms/configuration, authenticated scope and boundary behavior proof | `NO_PROOF` |
| Q-003 | Custody, signing, key recovery and signer-control model | Security/custody accountable executive | architecture approval, key-ceremony/control evidence and scoped non-production behavior proof | `NO_PROOF` |
| Q-004 | Accounting policy, chart of accounts, tax treatment and correction authority | Finance controller | approved accounting policy, reconciliation/correction rules and review evidence | `NO_PROOF` |
| Q-005 | Supported assets, networks, protocols and contract registry | Risk/protocol owner | allowlist, risk disposition, verification evidence and revocation process | `NO_PROOF` |
| Q-006 | Identity, tenancy, privacy, LGPD purpose/retention/deletion and immutable-record exception | Privacy/security owner | data inventory, lawful-basis review, retention schedule and privacy approval | `REQUIRES_LEGAL_REVIEW` |
| Q-007 | Risk appetite, suitability, fraud, AML/KYC/KYT/sanctions policy | Risk/compliance owner | approved limits, compliance/fraud rules, decision-model version and boundary tests | `REQUIRES_LEGAL_REVIEW` |
| Q-008 | Operations, incident response, audit retention and break-glass governance | Security/operations owner | exercised incident drills, immutable-retention design and accountable reset/revocation policy | `NO_PROOF` |
| Q-009 | Kernel language, toolchain, module-boundary verification and reproducibility | Engineering owner | comparative spike, threat-aware verification plan and team-operability evidence | `NO_PROOF` |
| Q-010 | CI/CD, release authority, environment attestation and mainnet governance quorum | Release/governance owner | protected supply-chain configuration snapshot, OIDC/provenance evidence and distinct-principal approval rules | `NO_PROOF` |

## Non-overridable rule

`MAINNET = BLOCKED` unless the exact operation/tenant/environment has current, non-contradictory, scope-matching evidence for **all applicable named Q-gates**, and independently satisfies the signed per-operation authorization contract. A generic `Q-001..Q-010 as applicable` statement is invalid for a spend-capable action.
