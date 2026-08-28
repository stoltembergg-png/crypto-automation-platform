# SDD-00 — Charter, Scope and Terminology

**Status:** Proposed planning baseline. **No runtime capability is asserted.**

## Objective
Define the language and hard boundaries for a multi-tenant crypto-automation platform whose financial authority is deterministic and whose economic facts are recorded in one availability ledger.

## Normative terms
- **MUST / MUST NOT:** mandatory design constraint.
- **Proposal:** typed, versioned, non-authoritative suggested action emitted by a user, workflow or AI.
- **Kernel action:** a member of the finite privileged action vocabulary evaluated by deterministic policy.
- **Accounting event:** the only declared event capable of changing an economic balance.
- **External evidence:** untrusted observation from a provider, venue, chain, wallet or workflow; it never directly changes a balance.
- **Correlation record:** links external evidence, workflow attempts, accounting events, delivery facts and reconciliation cases without asserting cross-system atomicity.
- **Capability:** attenuated permission binding subject, tenant, operation/resource, audience, environment, expiry, rotation and revocation.
- **Legal disposition:** `ALLOWED`, `PROHIBITED`, or `REQUIRES_LEGAL_REVIEW`; the latter is non-overridable.

## Scope
The later platform may formalize proposals, policies, accounting, external integrations, market observations, risk decisions and reconciliation. This SDD specifies their guardrails only. It does not establish legal permission, custody, user eligibility, asset/venue support, provider support, or mainnet readiness.

## Non-goals
No capital-protection promise; no autonomous AI spending; no implicit provider support; no non-ledger balance update; no shared database writes across modules; no microservice/broker default; no claim that hash chaining alone prevents audit tampering; no withdrawal/MetaMask enablement by this document.

## Invariants
1. Unknown/invalid/stale/revoked authority defaults to deny.
2. Economic balances change only after a valid accounting event is posted once.
3. Evidence, dispatch, settlement and reconciliation are separate facts with explicit correlation.
4. Maturity evidence is scope-limited and never implies legal, provider, custody or mainnet readiness.
5. Every privileged action is tenant/environment bound and auditable.

## Acceptance evidence
A future reviewer must confirm all terms are used consistently by `SDD-01` through `SDD-12`, ADRs, contracts and planning gates. Any undefined financial term blocks approval until added here or explicitly imported.
