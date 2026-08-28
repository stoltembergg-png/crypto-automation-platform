# Open Questions and Assumptions Register

All entries are blocking only for the named future scope. They do **not** block documentation-only planning, paper-market-data research, or non-financial repository governance.

## Open questions

| ID | Decision needed | Owner | Blocks | Required evidence to close |
|---|---|---|---|---|
| Q-001 | Legal entity, jurisdictions, target customer categories, and whether the product ever holds or administers third-party assets. | Founder + Brazilian financial/regulatory counsel | Any real-money scope | Written legal classification and operating model approval. |
| Q-002 | Custody model and licensed/qualified custodian or MPC/HSM provider selection. | Founder + security + counsel | Wallet funding, crypto withdrawals, mainnet | Vendor due diligence, contracts, threat review, key-ceremony/runbook approval. |
| Q-003 | Mercado Pago account type, contractual eligibility, Pix product/API, production webhook and payout capabilities. | Founder + payments + counsel | Production Pix funding or payout | Authenticated sandbox/production documentation and provider approval. |
| Q-004 | KYC/KYT, sanctions, PEP/adverse media, transaction monitoring and case-management providers/processes. | Compliance owner + counsel | Onboarding and any real-money activity | Compliance program, vendor contract, test evidence, escalation ownership. |
| Q-005 | Asset universe, supported BRL pairs, exchange roster, geographic restrictions, and stablecoin policy. | Product + treasury + compliance | Exchange/strategy activation | Approved asset/protocol/exchange registry with risk assessment. |
| Q-006 | Investor/product suitability rules and whether automated execution is discretionary, advisory, or user-directed in each automation mode. | Counsel + product + compliance | AI_PROPOSE and AI_AUTO_WITH_LIMITS | Legal/product policy decision and user disclosures. |
| Q-007 | Loss allocation, insolvency/segregation model, fee schedule, tax reporting obligations, and accounting policy. | Finance + counsel + accountant | Real funds, statements, withdrawals | Written accounting/tax/legal policy and reconciliation model approval. |
| Q-008 | Security governance: named control owners, break-glass approvers, emergency contacts, vulnerability disclosure, incident response and insurance. | Founder + security | Testnet/mainnet | Approved runbooks, exercises and ownership roster. |
| Q-009 | Mainnet admission authority, capital limits, capital source, and manual approval quorum. | Founder + treasury + counsel | MAINNET feature flag | Signed governance decision, funds provenance, gate evidence. |
| Q-010 | Data-controller/processor roles, retention schedules, deletion/export rules, DPO/privacy-contact requirements, and cross-border transfer basis. | Privacy owner + counsel | Real PII | LGPD data map, legal basis, DPIA/records where required, retention approval. |

## Assumptions used only to shape the plan

| ID | Assumption | Status | Containment |
|---|---|---|---|
| ASM-001 | Brazil/Pix/Mercado Pago is the first operating context. | supplied, not legal conclusion | Compliance document labels every resulting obligation `REQUIRES_LEGAL_REVIEW`. |
| ASM-002 | Initial production scope, if ever admitted, is conservative and capital-limited rather than high-frequency or leveraged. | architectural recommendation | Futures, margin, leverage, bridges, and arbitrary contracts are disabled-by-default. |
| ASM-003 | EVM networks can share an adapter family; Solana needs a separate adapter family and is deferred. | architectural hypothesis | ADR and contract tests must validate this before code creates a universal chain abstraction. |
| ASM-004 | A modular monolith is sufficient for early phases. | pending adversarial review | Module contracts and transactional outbox preserve a later extraction path. |
| ASM-005 | The Vercel `develop` page is a static planning-status view only. | supplied delivery interpretation | It exposes no financial or operational control, credentials, balances, or provider integrations. |
