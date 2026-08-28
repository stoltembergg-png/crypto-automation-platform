# Planning Control Plane

**Planning state:** FORMALIZATION_ONLY

This directory is the executable documentation control plane for the crypto-automation SDD. “Executable” means its work items, dependencies, required inputs, approval gates, proof artifacts, and rejection conditions are unambiguous enough to schedule and audit. It does **not** mean code was run or a production capability exists.

## Contents

- `hyperplan-executable-formalization.md` — ordered delivery plan, scope, milestones M0–M20, verification and mitigation rules.
- `input-gates-q001-q010.md` — blocking external/owner decisions. Dependent implementation remains blocked until a recorded decision meets the stated acceptance standard.
- `mainnet-readiness-matrix.md` — explicit PASS/FAIL/BLOCKED/NO_PROOF readiness ledger; overall mainnet status is BLOCKED.
- `pr-queue.md` — recommended reviewable documentation/implementation queue, exact 21-card baseline, rules, DAG references, and critical path.
- `traceability-matrix.md` — high-risk-only requirement-to-proof mapping; it has no card-count target.
- `verification-catalog.md` — architecture, contract, adversarial, negative-path, and release evidence expectations.
- `adversarial-review.md` — hostile review records and rejection rules.
- `formalization-dag.mmd` — Mermaid dependency graph.

## Evidence convention

Every actual proof artifact added later requires: immutable locator or digest, producing identity, UTC timestamp, scope/tenant/environment, verifier, expiry/revalidation trigger, and disposition. Missing evidence is `NO_PROOF`; unresolved external decisions are `BLOCKED`; observed contradiction is `FAIL`. Only a completed, independently verified requirement may be `PASS`, and only for its exact stated scope.
