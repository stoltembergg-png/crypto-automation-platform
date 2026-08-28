# Open Questions and Assumptions Register

All entries are blocking only for their named future scope. They do **not** authorize financial activity; documentation planning remains allowed while each decision is unresolved. Q-ID semantics are defined only by `.planning/master/GATE_REGISTRY.md`.

## Open questions

| ID | Canonical decision needed | Owner | Blocks | Required evidence to evaluate |
|---|---|---|---|---|
| Q-001 | Legal entity, jurisdictions, target customer categories, operating model, and whether the product ever holds/administers third-party assets. | Founder + Brazilian financial/regulatory counsel | Any real-money scope | Written legal classification, scope/exceptions and operating-model approval. |
| Q-002 | Mercado Pago account/product eligibility, production webhook/payout semantics, exchange/venue roster, and authenticated provider capability for the exact environment. | Provider operations + payments + counsel | Production Pix, venue or provider activation | Versioned provider terms/configuration, authenticated scope, sandbox/test boundary result and provider approval where required. |
| Q-003 | Custody model, licensed/qualified custodian or MPC/HSM provider selection, wallet funding/withdrawal recovery, and signer key ceremony. | Founder + security + counsel | Wallet funding, crypto withdrawal, signing, mainnet | Vendor due diligence/contracts, threat review, key-ceremony/runbook and scoped behavior evidence. |
| Q-004 | Loss allocation, insolvency/segregation, fee schedule, tax reporting, chart of accounts and correction/reconciliation accounting policy. | Finance + counsel + accountant | Real funds, statements, corrections, withdrawals | Written accounting/tax/legal policy and finance-controller approval. |
| Q-005 | Asset universe, supported BRL pairs, network/protocol/exchange registry, geographic restrictions and stablecoin policy. | Product + treasury + compliance | Asset, protocol, exchange or strategy activation | Approved allowlist with risk assessment, monitoring and revocation process. |
| Q-006 | Data-controller/processor roles, purpose limitation, retention, deletion/export, immutable-record exception, DPO/privacy contact and transfer basis. | Privacy owner + counsel | Real PII and privacy-sensitive provider integration | LGPD data map, legal basis, retention approval and required assessment/records. |
| Q-007 | KYC/KYT, sanctions, PEP/adverse-media, transaction monitoring, case management, investor/product suitability, automation classification and fraud limits. | Compliance + risk + counsel + product | Onboarding, credit availability, withdrawal or any real-money automation | Approved compliance/fraud/suitability policy, vendor/process evidence, escalation ownership and boundary tests. |
| Q-008 | Security control ownership, break-glass/reset approvers, emergency contacts, vulnerability disclosure, incident response, insurance and audit retention. | Founder + security/operations | Testnet, mainnet or privileged operations | Approved runbooks, drill evidence, immutable-retention design and ownership roster. |
| Q-009 | Kernel implementation language/toolchain, reproducibility, module-boundary checks and team-operability evidence. | Engineering owner | Production kernel implementation selection | Comparative spike, threat-aware verification plan and team-operability decision. |
| Q-010 | CI/release authority, protected supply chain, static Vercel boundary, mainnet admission authority, capital source/limits and distinct-principal approval quorum. | Release/governance + founder + treasury + counsel | Release/mainnet feature flag | Signed governance decision, protected configuration snapshot, provenance evidence and gate evidence. |

## Assumptions used only to shape the plan

| ID | Assumption | Status | Containment |
|---|---|---|---|
| ASM-001 | Brazil/Pix/Mercado Pago is the first operating context. | supplied, not legal conclusion | Compliance material labels resulting obligations `REQUIRES_LEGAL_REVIEW`. |
| ASM-002 | Initial production scope, if ever admitted, is conservative and capital-limited rather than high-frequency or leveraged. | architectural recommendation | Futures, margin, leverage, bridges and arbitrary contracts remain disabled-by-default. |
| ASM-003 | EVM networks can share an adapter family; Solana needs a separate adapter family and is deferred. | architectural hypothesis | ADR and contract tests must validate this before code creates a universal chain abstraction. |
| ASM-004 | A modular monolith is sufficient only with module-owned persistence, explicit contracts, no-cross-module-write rule and a capability-scoped transaction kernel. | refined by adversarial review | Boundary tests and extraction criteria are mandatory before implementation. |
| ASM-005 | The Vercel `develop` page is a static planning-status view only. | supplied delivery interpretation | It exposes no financial/operational control, credentials, balances or provider integration. |
