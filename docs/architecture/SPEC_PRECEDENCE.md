# Specification Precedence and Contract Authority

**Status:** `PLANNING_ONLY` — prevents documentation drift from becoming an authorization path.

## Precedence order

1. `.planning/master/EVIDENCE_AND_BOUNDARY.md` — scope boundary and fail-closed evidence classification.
2. `.planning/master/GATE_REGISTRY.md` — sole meanings of Q-001..Q-010.
3. `docs/security/ADVERSARIAL_CLOSURE_SPEC.md` — corrective high-risk contracts and explicit overrides following the post-documentation review.
4. Component specifications and contracts under `docs/specifications/` and `.planning/contracts/`.
5. Diagrams, queue cards, ADRs and testing plans, which must conform to the documents above.
6. `docs/reference-formalization/` and `.planning/reference-formalization/` — retained provenance/input only. They are not an implementation authority, do not define a Q-ID, and may not override a higher-precedence contract.

A contradiction is resolved by the highest numbered document in this list that covers the subject; it must also be added to the remediation traceability matrix before implementation begins.

## Normative vocabulary

- **Authority** is the deterministic component allowed to issue an authorized command. AI, adapter, reconciliation worker, diagram, report and external receipt are not authority.
- **Evidence** is an observation with provenance; it does not mutate economic state.
- **AccountingCommand** is a typed, authorized, tenant/environment-scoped command accepted by the ledger. The ledger denies all other writers.
- **Planning-only** means no described behavior is live, enabled, safe, legally approved, provider-authorized or production-ready.

## Change rule

Any amendment affecting Q-gates, economic mutation, external submission, tenant isolation, signing, reconciliation, privacy or release authority requires: a focused adversarial review, updated future tests, a new/updated queue card, updated traceability, and planning-integrity validation.
