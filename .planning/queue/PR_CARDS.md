# Executable Implementation PR Queue

**Status:** planned only. It contains no created pull request, code, provider activation or completion claim.

**Card count:** 133. Count is a consequence of independently reviewable boundaries, not a target. Every card is blocked by its dependencies and relevant Q-gates.

## PR-001 — Repository bootstrap and contribution governance
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for repository bootstrap and contribution governance without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/repository-bootstrap-and-contribution-governance/`, future `apps/web/`, future `tests/repository-bootstrap-and-contribution-governance/` only as justified by the selected slice.
- **Dependencies:** none; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-001` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-002 — Planning validation harness
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for planning validation harness without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/planning-validation-harness/`, future `apps/web/`, future `tests/planning-validation-harness/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-002` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-003 — Workspace and package boundary decision spike
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for workspace and package boundary decision spike without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/workspace-and-package-boundary-decision-spike/`, future `apps/web/`, future `tests/workspace-and-package-boundary-decision-spike/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-003` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-004 — Language/toolchain evidence spike
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for language/toolchain evidence spike without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/language-toolchain-evidence-spike/`, future `apps/web/`, future `tests/language-toolchain-evidence-spike/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-004` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-005 — Documentation navigation and artifact manifest
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for documentation navigation and artifact manifest without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/documentation-navigation-and-artifact-manifest/`, future `apps/web/`, future `tests/documentation-navigation-and-artifact-manifest/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-005` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-006 — GitHub branch/ruleset evidence capture
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for github branch/ruleset evidence capture without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/github-branch-ruleset-evidence-capture/`, future `apps/web/`, future `tests/github-branch-ruleset-evidence-capture/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-006` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-007 — Vercel develop status-only deployment contract
- **Milestone:** M1 Repository Foundation
- **Objective:** Establish the smallest reviewable implementation slice for vercel develop status-only deployment contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/vercel-develop-status-only-deployment-contract/`, future `apps/web/`, future `tests/vercel-develop-status-only-deployment-contract/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-007` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-008 — Identity domain primitives
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for identity domain primitives without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/identity-domain-primitives/`, future `apps/web/`, future `tests/identity-domain-primitives/` only as justified by the selected slice.
- **Dependencies:** PR-001; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-008` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-009 — User registration contract
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for user registration contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/user-registration-contract/`, future `apps/web/`, future `tests/user-registration-contract/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-009` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-010 — Passkey enrollment
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for passkey enrollment without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/passkey-enrollment/`, future `apps/web/`, future `tests/passkey-enrollment/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-010` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-011 — Passkey login
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for passkey login without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/passkey-login/`, future `apps/web/`, future `tests/passkey-login/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-011` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-012 — TOTP recovery contract
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for totp recovery contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/totp-recovery-contract/`, future `apps/web/`, future `tests/totp-recovery-contract/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-012` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-013 — Session rotation
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for session rotation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/session-rotation/`, future `apps/web/`, future `tests/session-rotation/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-013` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-014 — Device/security events
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for device/security events without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/device-security-events/`, future `apps/web/`, future `tests/device-security-events/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-014` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-015 — Authorization context
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for authorization context without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/authorization-context/`, future `apps/web/`, future `tests/authorization-context/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-015` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-016 — Tenant RLS baseline
- **Milestone:** M2 Identity & Security
- **Objective:** Establish the smallest reviewable implementation slice for tenant rls baseline without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/tenant-rls-baseline/`, future `apps/web/`, future `tests/tenant-rls-baseline/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-016` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-017 — Money and quantity types
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for money and quantity types without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/money-and-quantity-types/`, future `apps/web/`, future `tests/money-and-quantity-types/` only as justified by the selected slice.
- **Dependencies:** PR-008; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-017` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-018 — Asset registry
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for asset registry without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/asset-registry/`, future `apps/web/`, future `tests/asset-registry/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-018` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-019 — Ledger chart of accounts
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for ledger chart of accounts without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ledger-chart-of-accounts/`, future `apps/web/`, future `tests/ledger-chart-of-accounts/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-019` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-020 — Journal entry schema
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for journal entry schema without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/journal-entry-schema/`, future `apps/web/`, future `tests/journal-entry-schema/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-020` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-021 — Balanced posting kernel
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for balanced posting kernel without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/balanced-posting-kernel/`, future `apps/web/`, future `tests/balanced-posting-kernel/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-021` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-022 — Availability account classes
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for availability account classes without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/availability-account-classes/`, future `apps/web/`, future `tests/availability-account-classes/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-022` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-023 — Idempotent accounting event
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for idempotent accounting event without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/idempotent-accounting-event/`, future `apps/web/`, future `tests/idempotent-accounting-event/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-023` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-024 — Compensating corrections
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for compensating corrections without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/compensating-corrections/`, future `apps/web/`, future `tests/compensating-corrections/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-024` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-025 — Ledger property tests
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for ledger property tests without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ledger-property-tests/`, future `apps/web/`, future `tests/ledger-property-tests/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-025` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-026 — Ledger read projections
- **Milestone:** M3 Ledger
- **Objective:** Establish the smallest reviewable implementation slice for ledger read projections without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ledger-read-projections/`, future `apps/web/`, future `tests/ledger-read-projections/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-026` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-027 — Payment intent domain
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for payment intent domain without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/payment-intent-domain/`, future `apps/web/`, future `tests/payment-intent-domain/` only as justified by the selected slice.
- **Dependencies:** PR-017; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-027` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-028 — Mercado Pago capability claim contract
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for mercado pago capability claim contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/mercado-pago-capability-claim-contract/`, future `apps/web/`, future `tests/mercado-pago-capability-claim-contract/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-028` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-029 — Pix request adapter sandbox contract
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for pix request adapter sandbox contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/pix-request-adapter-sandbox-contract/`, future `apps/web/`, future `tests/pix-request-adapter-sandbox-contract/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-029` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-030 — Webhook inbox/signature contract
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for webhook inbox/signature contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/webhook-inbox-signature-contract/`, future `apps/web/`, future `tests/webhook-inbox-signature-contract/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-030` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-031 — Canonical payment query contract
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for canonical payment query contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/canonical-payment-query-contract/`, future `apps/web/`, future `tests/canonical-payment-query-contract/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-031` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-032 — Payment lifecycle state machine
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for payment lifecycle state machine without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/payment-lifecycle-state-machine/`, future `apps/web/`, future `tests/payment-lifecycle-state-machine/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-032` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-033 — Payment-to-ledger settlement policy
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for payment-to-ledger settlement policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/payment-to-ledger-settlement-policy/`, future `apps/web/`, future `tests/payment-to-ledger-settlement-policy/` only as justified by the selected slice.
- **Dependencies:** PR-027, PR-032; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-033` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-034 — Payment reconciliation cases
- **Milestone:** M4 Payments
- **Objective:** Establish the smallest reviewable implementation slice for payment reconciliation cases without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/payment-reconciliation-cases/`, future `apps/web/`, future `tests/payment-reconciliation-cases/` only as justified by the selected slice.
- **Dependencies:** PR-027, PR-033; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-034` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-035 — Wallet address model
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for wallet address model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/wallet-address-model/`, future `apps/web/`, future `tests/wallet-address-model/` only as justified by the selected slice.
- **Dependencies:** PR-027; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-035` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-036 — Wallet ownership challenge
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for wallet ownership challenge without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/wallet-ownership-challenge/`, future `apps/web/`, future `tests/wallet-ownership-challenge/` only as justified by the selected slice.
- **Dependencies:** PR-035; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-036` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-037 — SIWE validation contract
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for siwe validation contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/siwe-validation-contract/`, future `apps/web/`, future `tests/siwe-validation-contract/` only as justified by the selected slice.
- **Dependencies:** PR-035; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-037` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-038 — Address allowlist/cooldown
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for address allowlist/cooldown without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/address-allowlist-cooldown/`, future `apps/web/`, future `tests/address-allowlist-cooldown/` only as justified by the selected slice.
- **Dependencies:** PR-035; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-038` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-039 — Destination mutation invalidation
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for destination mutation invalidation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/destination-mutation-invalidation/`, future `apps/web/`, future `tests/destination-mutation-invalidation/` only as justified by the selected slice.
- **Dependencies:** PR-035; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-039` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-040 — Signer request contract
- **Milestone:** M5 Wallet Infrastructure
- **Objective:** Establish the smallest reviewable implementation slice for signer request contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/signer-request-contract/`, future `apps/web/`, future `tests/signer-request-contract/` only as justified by the selected slice.
- **Dependencies:** PR-035, PR-039; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-040` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-041 — Market source capability contract
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for market source capability contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/market-source-capability-contract/`, future `apps/web/`, future `tests/market-source-capability-contract/` only as justified by the selected slice.
- **Dependencies:** PR-035; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-041` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-042 — Market snapshot schema
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for market snapshot schema without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/market-snapshot-schema/`, future `apps/web/`, future `tests/market-snapshot-schema/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-042` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-043 — Order book normalizer
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for order book normalizer without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/order-book-normalizer/`, future `apps/web/`, future `tests/order-book-normalizer/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-043` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-044 — Freshness/quality decision
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for freshness/quality decision without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/freshness-quality-decision/`, future `apps/web/`, future `tests/freshness-quality-decision/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-044` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-045 — Quote reservation
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for quote reservation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/quote-reservation/`, future `apps/web/`, future `tests/quote-reservation/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-045` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-046 — Market data replay fixtures
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for market data replay fixtures without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/market-data-replay-fixtures/`, future `apps/web/`, future `tests/market-data-replay-fixtures/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-046` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-047 — Source health telemetry
- **Milestone:** M6 Market Data
- **Objective:** Establish the smallest reviewable implementation slice for source health telemetry without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/source-health-telemetry/`, future `apps/web/`, future `tests/source-health-telemetry/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-047` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-048 — Exchange adapter trait
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for exchange adapter trait without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/exchange-adapter-trait/`, future `apps/web/`, future `tests/exchange-adapter-trait/` only as justified by the selected slice.
- **Dependencies:** PR-041; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-048` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-049 — Capability negotiation
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for capability negotiation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/capability-negotiation/`, future `apps/web/`, future `tests/capability-negotiation/` only as justified by the selected slice.
- **Dependencies:** PR-048; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-049` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-050 — Market/balance read contracts
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for market/balance read contracts without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/market-balance-read-contracts/`, future `apps/web/`, future `tests/market-balance-read-contracts/` only as justified by the selected slice.
- **Dependencies:** PR-048; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-050` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-051 — Order intent contract
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for order intent contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/order-intent-contract/`, future `apps/web/`, future `tests/order-intent-contract/` only as justified by the selected slice.
- **Dependencies:** PR-048; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-051` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-052 — Order lifecycle reconciliation
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for order lifecycle reconciliation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/order-lifecycle-reconciliation/`, future `apps/web/`, future `tests/order-lifecycle-reconciliation/` only as justified by the selected slice.
- **Dependencies:** PR-048, PR-051; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-052` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-053 — Exchange simulated adapter
- **Milestone:** M7 Exchange Integration
- **Objective:** Establish the smallest reviewable implementation slice for exchange simulated adapter without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/exchange-simulated-adapter/`, future `apps/web/`, future `tests/exchange-simulated-adapter/` only as justified by the selected slice.
- **Dependencies:** PR-048; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-053` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-054 — Risk policy schema
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for risk policy schema without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/risk-policy-schema/`, future `apps/web/`, future `tests/risk-policy-schema/` only as justified by the selected slice.
- **Dependencies:** PR-048; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-054` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-055 — Exposure snapshot
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for exposure snapshot without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/exposure-snapshot/`, future `apps/web/`, future `tests/exposure-snapshot/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-055` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-056 — Position/protocol/chain limits
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for position/protocol/chain limits without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/position-protocol-chain-limits/`, future `apps/web/`, future `tests/position-protocol-chain-limits/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-056` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-057 — Slippage/impact/gas limits
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for slippage/impact/gas limits without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/slippage-impact-gas-limits/`, future `apps/web/`, future `tests/slippage-impact-gas-limits/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-057` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-058 — Kill switch hierarchy
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for kill switch hierarchy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/kill-switch-hierarchy/`, future `apps/web/`, future `tests/kill-switch-hierarchy/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-058` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-059 — Risk decision binding
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for risk decision binding without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/risk-decision-binding/`, future `apps/web/`, future `tests/risk-decision-binding/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-059` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-060 — Risk property tests
- **Milestone:** M8 Risk Engine
- **Objective:** Establish the smallest reviewable implementation slice for risk property tests without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/risk-property-tests/`, future `apps/web/`, future `tests/risk-property-tests/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-060` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-061 — Execution plan hash
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for execution plan hash without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/execution-plan-hash/`, future `apps/web/`, future `tests/execution-plan-hash/` only as justified by the selected slice.
- **Dependencies:** PR-054; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-061` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-062 — Simulation evidence contract
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for simulation evidence contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/simulation-evidence-contract/`, future `apps/web/`, future `tests/simulation-evidence-contract/` only as justified by the selected slice.
- **Dependencies:** PR-061; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-062` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-063 — Transaction guard decoder
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for transaction guard decoder without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/transaction-guard-decoder/`, future `apps/web/`, future `tests/transaction-guard-decoder/` only as justified by the selected slice.
- **Dependencies:** PR-061, PR-062; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-063` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-064 — Allowlist/function validation
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for allowlist/function validation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/allowlist-function-validation/`, future `apps/web/`, future `tests/allowlist-function-validation/` only as justified by the selected slice.
- **Dependencies:** PR-061; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-064` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-065 — Execution intent/outbox
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for execution intent/outbox without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/execution-intent-outbox/`, future `apps/web/`, future `tests/execution-intent-outbox/` only as justified by the selected slice.
- **Dependencies:** PR-061; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-065` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-066 — Adapter submission evidence
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for adapter submission evidence without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/adapter-submission-evidence/`, future `apps/web/`, future `tests/adapter-submission-evidence/` only as justified by the selected slice.
- **Dependencies:** PR-061; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-066` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-067 — Execution state reconciliation
- **Milestone:** M9 Execution Engine
- **Objective:** Establish the smallest reviewable implementation slice for execution state reconciliation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/execution-state-reconciliation/`, future `apps/web/`, future `tests/execution-state-reconciliation/` only as justified by the selected slice.
- **Dependencies:** PR-061, PR-066; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-067` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-068 — Paper environment attestation
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for paper environment attestation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/paper-environment-attestation/`, future `apps/web/`, future `tests/paper-environment-attestation/` only as justified by the selected slice.
- **Dependencies:** PR-061; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-068` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-069 — Virtual ledger isolation
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for virtual ledger isolation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/virtual-ledger-isolation/`, future `apps/web/`, future `tests/virtual-ledger-isolation/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-069` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-070 — Paper fill model
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for paper fill model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/paper-fill-model/`, future `apps/web/`, future `tests/paper-fill-model/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-070` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-071 — Paper strategy execution
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for paper strategy execution without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/paper-strategy-execution/`, future `apps/web/`, future `tests/paper-strategy-execution/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-071` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-072 — Paper portfolio projections
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for paper portfolio projections without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/paper-portfolio-projections/`, future `apps/web/`, future `tests/paper-portfolio-projections/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-072` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-073 — Paper replay/reporting
- **Milestone:** M10 Paper Trading
- **Objective:** Establish the smallest reviewable implementation slice for paper replay/reporting without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/paper-replay-reporting/`, future `apps/web/`, future `tests/paper-replay-reporting/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-073` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-074 — Opportunity model
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for opportunity model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/opportunity-model/`, future `apps/web/`, future `tests/opportunity-model/` only as justified by the selected slice.
- **Dependencies:** PR-068; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-074` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-075 — Net profit model
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for net profit model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/net-profit-model/`, future `apps/web/`, future `tests/net-profit-model/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-075` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-076 — Triangular graph detection
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for triangular graph detection without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/triangular-graph-detection/`, future `apps/web/`, future `tests/triangular-graph-detection/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-076` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-077 — Arbitrage simulation
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for arbitrage simulation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/arbitrage-simulation/`, future `apps/web/`, future `tests/arbitrage-simulation/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-077` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-078 — Arbitrage risk policy
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for arbitrage risk policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/arbitrage-risk-policy/`, future `apps/web/`, future `tests/arbitrage-risk-policy/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-078` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-079 — Arbitrage paper dashboard
- **Milestone:** M11 Arbitrage
- **Objective:** Establish the smallest reviewable implementation slice for arbitrage paper dashboard without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/arbitrage-paper-dashboard/`, future `apps/web/`, future `tests/arbitrage-paper-dashboard/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-079` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-080 — EVM chain capability contract
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for evm chain capability contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/evm-chain-capability-contract/`, future `apps/web/`, future `tests/evm-chain-capability-contract/` only as justified by the selected slice.
- **Dependencies:** PR-074; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-080` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-081 — Chain simulation/gas
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for chain simulation/gas without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/chain-simulation-gas/`, future `apps/web/`, future `tests/chain-simulation-gas/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-081` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-082 — Nonce reservation
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for nonce reservation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/nonce-reservation/`, future `apps/web/`, future `tests/nonce-reservation/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-082` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-083 — Receipt/finality evidence
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for receipt/finality evidence without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/receipt-finality-evidence/`, future `apps/web/`, future `tests/receipt-finality-evidence/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-083` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-084 — Reorg reconciliation
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for reorg reconciliation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/reorg-reconciliation/`, future `apps/web/`, future `tests/reorg-reconciliation/` only as justified by the selected slice.
- **Dependencies:** PR-080, PR-083; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-084` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-085 — Testnet environment isolation
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for testnet environment isolation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/testnet-environment-isolation/`, future `apps/web/`, future `tests/testnet-environment-isolation/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-085` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-086 — Chain adapter simulated tests
- **Milestone:** M12 Blockchain
- **Objective:** Establish the smallest reviewable implementation slice for chain adapter simulated tests without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/chain-adapter-simulated-tests/`, future `apps/web/`, future `tests/chain-adapter-simulated-tests/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-086` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-087 — Protocol registry
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for protocol registry without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/protocol-registry/`, future `apps/web/`, future `tests/protocol-registry/` only as justified by the selected slice.
- **Dependencies:** PR-080; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-087` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-088 — DEX quote contract
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for dex quote contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/dex-quote-contract/`, future `apps/web/`, future `tests/dex-quote-contract/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-088` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-089 — Swap candidate decoder
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for swap candidate decoder without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/swap-candidate-decoder/`, future `apps/web/`, future `tests/swap-candidate-decoder/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-089` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-090 — DEX simulation/slippage
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for dex simulation/slippage without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/dex-simulation-slippage/`, future `apps/web/`, future `tests/dex-simulation-slippage/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-090` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-091 — Approval policy
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for approval policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/approval-policy/`, future `apps/web/`, future `tests/approval-policy/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-091` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-092 — DEX testnet adapter
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for dex testnet adapter without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/dex-testnet-adapter/`, future `apps/web/`, future `tests/dex-testnet-adapter/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-092` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-093 — DEX adverse fixtures
- **Milestone:** M13 DEX
- **Objective:** Establish the smallest reviewable implementation slice for dex adverse fixtures without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/dex-adverse-fixtures/`, future `apps/web/`, future `tests/dex-adverse-fixtures/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-093` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-094 — Pool risk assessment
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for pool risk assessment without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/pool-risk-assessment/`, future `apps/web/`, future `tests/pool-risk-assessment/` only as justified by the selected slice.
- **Dependencies:** PR-087; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-094` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-095 — LP position model
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for lp position model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/lp-position-model/`, future `apps/web/`, future `tests/lp-position-model/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-095` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-096 — Impermanent loss model
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for impermanent loss model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/impermanent-loss-model/`, future `apps/web/`, future `tests/impermanent-loss-model/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-096` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-097 — Range proposal policy
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for range proposal policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/range-proposal-policy/`, future `apps/web/`, future `tests/range-proposal-policy/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-097` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-098 — Rebalance cost simulation
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for rebalance cost simulation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/rebalance-cost-simulation/`, future `apps/web/`, future `tests/rebalance-cost-simulation/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-098` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-099 — LP lifecycle monitor
- **Milestone:** M14 Liquidity Pools
- **Objective:** Establish the smallest reviewable implementation slice for lp lifecycle monitor without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/lp-lifecycle-monitor/`, future `apps/web/`, future `tests/lp-lifecycle-monitor/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-099` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-100 — AI provider contract
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for ai provider contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ai-provider-contract/`, future `apps/web/`, future `tests/ai-provider-contract/` only as justified by the selected slice.
- **Dependencies:** PR-094; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-100` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-101 — Redacted context builder
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for redacted context builder without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/redacted-context-builder/`, future `apps/web/`, future `tests/redacted-context-builder/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-101` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-102 — Structured proposal schema
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for structured proposal schema without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/structured-proposal-schema/`, future `apps/web/`, future `tests/structured-proposal-schema/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-102` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-103 — Proposal provenance/audit
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for proposal provenance/audit without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/proposal-provenance-audit/`, future `apps/web/`, future `tests/proposal-provenance-audit/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-103` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-104 — AI denial and malformed output
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for ai denial and malformed output without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ai-denial-and-malformed-output/`, future `apps/web/`, future `tests/ai-denial-and-malformed-output/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-104` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-105 — AI advisory dashboard
- **Milestone:** M15 AI Layer
- **Objective:** Establish the smallest reviewable implementation slice for ai advisory dashboard without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/ai-advisory-dashboard/`, future `apps/web/`, future `tests/ai-advisory-dashboard/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-105` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-106 — Portfolio allocation policy
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for portfolio allocation policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/portfolio-allocation-policy/`, future `apps/web/`, future `tests/portfolio-allocation-policy/` only as justified by the selected slice.
- **Dependencies:** PR-100; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-106` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-107 — Cash reserve policy
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for cash reserve policy without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/cash-reserve-policy/`, future `apps/web/`, future `tests/cash-reserve-policy/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-107` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-108 — Diversification/correlation model
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for diversification/correlation model without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/diversification-correlation-model/`, future `apps/web/`, future `tests/diversification-correlation-model/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-108` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-109 — Portfolio rebalance proposal
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for portfolio rebalance proposal without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/portfolio-rebalance-proposal/`, future `apps/web/`, future `tests/portfolio-rebalance-proposal/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-109` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-110 — Automation mode gates
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for automation mode gates without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/automation-mode-gates/`, future `apps/web/`, future `tests/automation-mode-gates/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-110` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-111 — Autopilot deny-by-default
- **Milestone:** M16 Portfolio Automation
- **Objective:** Establish the smallest reviewable implementation slice for autopilot deny-by-default without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/autopilot-deny-by-default/`, future `apps/web/`, future `tests/autopilot-deny-by-default/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-111` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-112 — Testnet capability claims
- **Milestone:** M17 Testnet
- **Objective:** Establish the smallest reviewable implementation slice for testnet capability claims without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/testnet-capability-claims/`, future `apps/web/`, future `tests/testnet-capability-claims/` only as justified by the selected slice.
- **Dependencies:** PR-106; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-112` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-113 — Testnet signer isolation
- **Milestone:** M17 Testnet
- **Objective:** Establish the smallest reviewable implementation slice for testnet signer isolation without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/testnet-signer-isolation/`, future `apps/web/`, future `tests/testnet-signer-isolation/` only as justified by the selected slice.
- **Dependencies:** PR-112; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-113` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-114 — Swap testnet smoke contract
- **Milestone:** M17 Testnet
- **Objective:** Establish the smallest reviewable implementation slice for swap testnet smoke contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/swap-testnet-smoke-contract/`, future `apps/web/`, future `tests/swap-testnet-smoke-contract/` only as justified by the selected slice.
- **Dependencies:** PR-112; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-114` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-115 — LP testnet smoke contract
- **Milestone:** M17 Testnet
- **Objective:** Establish the smallest reviewable implementation slice for lp testnet smoke contract without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/lp-testnet-smoke-contract/`, future `apps/web/`, future `tests/lp-testnet-smoke-contract/` only as justified by the selected slice.
- **Dependencies:** PR-112; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-115` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-116 — Testnet reconciliation drill
- **Milestone:** M17 Testnet
- **Objective:** Establish the smallest reviewable implementation slice for testnet reconciliation drill without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/testnet-reconciliation-drill/`, future `apps/web/`, future `tests/testnet-reconciliation-drill/` only as justified by the selected slice.
- **Dependencies:** PR-112, PR-115; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-116` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-117 — Secret manager adapter
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for secret manager adapter without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/secret-manager-adapter/`, future `apps/web/`, future `tests/secret-manager-adapter/` only as justified by the selected slice.
- **Dependencies:** PR-112; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-117` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-118 — Secret redaction middleware
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for secret redaction middleware without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/secret-redaction-middleware/`, future `apps/web/`, future `tests/secret-redaction-middleware/` only as justified by the selected slice.
- **Dependencies:** PR-117; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-118` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-119 — Threat fixture suite
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for threat fixture suite without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/threat-fixture-suite/`, future `apps/web/`, future `tests/threat-fixture-suite/` only as justified by the selected slice.
- **Dependencies:** PR-117; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-119` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-120 — Audit external-anchor design
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for audit external-anchor design without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/audit-external-anchor-design/`, future `apps/web/`, future `tests/audit-external-anchor-design/` only as justified by the selected slice.
- **Dependencies:** PR-117, PR-119; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-120` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-121 — Chaos fault matrix
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for chaos fault matrix without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/chaos-fault-matrix/`, future `apps/web/`, future `tests/chaos-fault-matrix/` only as justified by the selected slice.
- **Dependencies:** PR-117; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-121` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-122 — Incident/kill-switch drill
- **Milestone:** M18 Security Hardening
- **Objective:** Establish the smallest reviewable implementation slice for incident/kill-switch drill without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/incident-kill-switch-drill/`, future `apps/web/`, future `tests/incident-kill-switch-drill/` only as justified by the selected slice.
- **Dependencies:** PR-117; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-122` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-123 — Legal disposition register
- **Milestone:** M19 Compliance Readiness
- **Objective:** Establish the smallest reviewable implementation slice for legal disposition register without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/legal-disposition-register/`, future `apps/web/`, future `tests/legal-disposition-register/` only as justified by the selected slice.
- **Dependencies:** PR-117; Q-001..Q-010 as applicable; unresolved gates yield BLOCKED.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-123` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-124 — KYC/KYT/sanctions boundary
- **Milestone:** M19 Compliance Readiness
- **Objective:** Establish the smallest reviewable implementation slice for kyc/kyt/sanctions boundary without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/kyc-kyt-sanctions-boundary/`, future `apps/web/`, future `tests/kyc-kyt-sanctions-boundary/` only as justified by the selected slice.
- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-124` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-125 — PII classification/retention
- **Milestone:** M19 Compliance Readiness
- **Objective:** Establish the smallest reviewable implementation slice for pii classification/retention without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/pii-classification-retention/`, future `apps/web/`, future `tests/pii-classification-retention/` only as justified by the selected slice.
- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-125` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-126 — Compliance case/audit
- **Milestone:** M19 Compliance Readiness
- **Objective:** Establish the smallest reviewable implementation slice for compliance case/audit without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/compliance-case-audit/`, future `apps/web/`, future `tests/compliance-case-audit/` only as justified by the selected slice.
- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-126` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-127 — Tax/accounting policy gate
- **Milestone:** M19 Compliance Readiness
- **Objective:** Establish the smallest reviewable implementation slice for tax/accounting policy gate without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/tax-accounting-policy-gate/`, future `apps/web/`, future `tests/tax-accounting-policy-gate/` only as justified by the selected slice.
- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-127` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-128 — Readiness evidence evaluator
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for readiness evidence evaluator without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/readiness-evidence-evaluator/`, future `apps/web/`, future `tests/readiness-evidence-evaluator/` only as justified by the selected slice.
- **Dependencies:** PR-123; evaluator must use the explicit Gate Registry set supplied by the target capability; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-128` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-129 — Signed activation authorization
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for signed activation authorization without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/signed-activation-authorization/`, future `apps/web/`, future `tests/signed-activation-authorization/` only as justified by the selected slice.
- **Dependencies:** PR-128; exact Q-ID set is operation-bound and registry-digested; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-129` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-130 — Environment attestation verifier
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for environment attestation verifier without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/environment-attestation-verifier/`, future `apps/web/`, future `tests/environment-attestation-verifier/` only as justified by the selected slice.
- **Dependencies:** PR-128; exact Q-ID set is operation-bound and registry-digested; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-130` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-131 — Capital limit enforcement
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for capital limit enforcement without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/capital-limit-enforcement/`, future `apps/web/`, future `tests/capital-limit-enforcement/` only as justified by the selected slice.
- **Dependencies:** PR-128; exact Q-ID set is operation-bound and registry-digested; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-131` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-132 — Mainnet denial regression suite
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for mainnet denial regression suite without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/mainnet-denial-regression-suite/`, future `apps/web/`, future `tests/mainnet-denial-regression-suite/` only as justified by the selected slice.
- **Dependencies:** PR-128; exact Q-ID set is operation-bound and registry-digested; generic Q ranges deny.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-132` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-133 — Manual activation governance
- **Milestone:** M20 Mainnet Readiness
- **Objective:** Establish the smallest reviewable implementation slice for manual activation governance without enabling financial capability.
- **Scope:** One bounded domain/contract/test surface; out of scope are unrelated provider activation, mainnet, credentials and policy broadening.
- **Files:** `docs/specifications/`, `.planning/contracts/`, future `crates/manual-activation-governance/`, future `apps/web/`, future `tests/manual-activation-governance/` only as justified by the selected slice.
- **Dependencies:** PR-128, PR-132; Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010; each must be exact, current and scope-matching.
- **Implementation:** Implement the contract and one consuming boundary; preserve module ownership, idempotency, tenant/environment binding and audit correlation. No direct provider/ledger/policy bypass.
- **Tests:** `@spec:PR-133` focused unit/contract/negative test; add property/state-machine/adversarial fixture when this card changes money, authority, signer, adapter or state transition.
- **Acceptance criteria:** Named contract is versioned; deny path is deterministic; all state changes are correlated; scope-specific tests are non-vacuous and PASS on exact head SHA.
- **Security implications:** Review least privilege, tenant isolation, secret/PII redaction, replay/expiry and fail-closed behavior; Security review required for privileged/financial scope.
- **Observability:** Emit bounded structured event/metric/trace with correlation ID and health signal; never raw secret/PII.
- **Rollback:** Disable owning feature/capability; preserve append-only audit and ledger history; use compatible forward fix/compensating record, never destructive rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no Q gate unresolved for any claimed capability; verification evidence bound to current SHA.

## PR-134 — Canonical gate registry and specification precedence
- **Milestone:** M0 Post-Review Planning Closure
- **Objective:** Make gate semantics and document precedence machine-checkable so evidence cannot close the wrong decision.
- **Scope:** Canonical GateId registry, authority precedence, semantic-parity validator and migration of all Q references; excludes provider/legal evaluation.
- **Files:** `.planning/master/GATE_REGISTRY.md`, `docs/architecture/SPEC_PRECEDENCE.md`, tests and all affected planning references.
- **Dependencies:** PR-001; Registry semantics only; it grants no Q-gate PASS or financial capability.
- **Implementation:** Implement a versioned server-independent registry model and documentation validator; reject duplicate Q-ID meanings, generic mainnet gate sets and stale registry digests.
- **Tests:** ACT-004; negative semantic mismatch, stale digest and generic-gate-set tests.
- **Acceptance criteria:** Every Q reference resolves to exactly one semantic decision/owner; no consumer treats URL retrieval as gate PASS.
- **Security implications:** Prevents approval-confusion paths across legal, provider, custody, accounting and release authority.
- **Observability:** Emit registry version/digest, gate evaluation scope, evidence digest, expiry and denial reason without raw evidence payload.
- **Rollback:** Disable gate evaluator; retain registry/audit history; forward-fix mappings without deleting prior evidence.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-135 — Tenant and environment ledger boundary
- **Milestone:** M3 Ledger Amendment
- **Objective:** Make cross-tenant/environment financial mutation impossible even to service-role and migration paths.
- **Scope:** Composite scoped keys, AccountingCommand-only writer boundary and server-owned contract classification; excludes real ledger operation.
- **Files:** `docs/specifications/LEDGER_SPEC.md`, `docs/architecture/DATA_MODEL.md`, future ledger migration/schema and focused tests.
- **Dependencies:** PR-008, PR-134; Q-004, Q-006, Q-009; unresolved or mismatched gate denies claimed implementation readiness.
- **Implementation:** Require tenant/environment on every financial/authority row; enforce composite FKs and deny forged GLOBAL classification or direct adapter/reconciliation/AI ledger calls.
- **Tests:** ACT-001, ACT-002; service-role cross-tenant, balanced cross-tenant and forged-GLOBAL negative tests.
- **Acceptance criteria:** No balanced entry can span tenant/environment; Ledger accepts only current AccountingCommand.v1 with matching scope.
- **Security implications:** Contains privileged-worker, migration and object-substitution blast radius.
- **Observability:** Record bounded tenant/environment mismatch reason, command digest and correlation ID.
- **Rollback:** Feature-disable new writer path; use forward-compatible schema migration/compensating records; never drop journal history.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-136 — Withdrawal intent, one-lock and ambiguous broadcast protocol
- **Milestone:** M5 Withdrawal Amendment
- **Objective:** Serialize withdrawal authorization, economic locking, outbox submission and ambiguous recovery without duplicate spend.
- **Scope:** Withdrawal state machine, lock protocol, adapter request boundary and provider-UNKNOWN handling; excludes enabled payout/wallet provider.
- **Files:** `docs/specifications/WITHDRAWALS_SPEC.md`, `EXCHANGE_ADAPTER_SPEC.md`, contracts, future state-machine code and tests.
- **Dependencies:** PR-027, PR-135; Q-002, Q-003, Q-004, Q-007; all named decisions remain deny-by-default.
- **Implementation:** Require PREAUTHORIZED before one atomic LOCK_POSTED; require durable intent/outbox/capability for submit; prohibit retry/rebroadcast on BROADCAST_AMBIGUOUS.
- **Tests:** ACT-006, ACT-007, ACT-008 plus denial/expiry/revocation-before-lock and linked-recovery tests.
- **Acceptance criteria:** Pre-lock failure has no posting; same intent cannot double-lock or rebroadcast; new recovery intent has fresh authority/evidence.
- **Security implications:** Prevents timeout double debit, destination mutation, ambient adapter withdrawal and cash-out bypass.
- **Observability:** Emit intent/lock/outbox/evidence correlation and opaque ambiguity state; redact destination/PII.
- **Rollback:** Disable withdrawal capability; preserve lock and audit history; resolve through reconciled compensating workflow only.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-137 — Comparable-cut reconciliation and accounting authority
- **Milestone:** M9 Reconciliation Amendment
- **Objective:** Ensure reconciliation evaluates comparable evidence and can only propose—not post—financial corrections.
- **Scope:** ReconciliationRun/EvidenceSet/CorrrectionProposal contracts, authority diagram and future negative tests; excludes provider data retrieval.
- **Files:** `docs/specifications/RECONCILIATION_SPEC.md`, diagrams, future reconciliation module and tests.
- **Dependencies:** PR-054, PR-135; Q-004, Q-008; any missing source completeness or correction authority keeps the scope blocked.
- **Implementation:** Require cutoffs, scope, cursors, completeness, finality and tolerance; gate MATCHED; route CorrectionProposal through Accounting Authority to AccountingCommand.
- **Tests:** ACT-009 and negative direct-ledger-write, stale/paginated evidence and correction-authorization tests.
- **Acceptance criteria:** Incomplete evidence never matches; reconciliation identity has no Ledger-write capability.
- **Security implications:** Prevents external evidence or worker compromise from changing balances.
- **Observability:** Record evidence digest/cutoff/completeness, mismatch age/owner and capability-block scope.
- **Rollback:** Suspend correction capability; preserve cases/evidence; issue only authorized compensating records.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-138 — Residual PnL, quote reservation and non-vacuous backtesting
- **Milestone:** M11 Arbitrage Amendment
- **Objective:** Prevent full-cycle theoretical spreads from hiding residual, partial-fill, freshness or correlation loss.
- **Scope:** NetPnL, QuoteReservation, recovery semantics, correlation/IL stress and backtest evidence contract; excludes live strategy execution.
- **Files:** `ARBITRAGE_ENGINE_SPEC.md`, `BACKTESTING_SPEC.md`, future simulator/backtest tests and reports.
- **Dependencies:** PR-068; Q-005 and Q-007; no strategy claim or funded path before approved asset/risk evidence.
- **Implementation:** Compute realised and conservative residual economics; serialize quote/capital reservations; fail closed on stale/future/zero-scenario data or unavailable hedge.
- **Tests:** ACT-010 plus partial-fill unavailable-hedge, stale/future-data mutation, changed-cost and zero/skip-scenario tests.
- **Acceptance criteria:** Recovery-required outcome cannot meet profit threshold; runner proves point-in-time inputs, calibration and non-vacuous scenarios.
- **Security implications:** Limits model laundering and capital exposure under stale or adversarial market data.
- **Observability:** Record snapshots, model/calibration/cost hashes, reservations, residual valuation and recovery outcome.
- **Rollback:** Disable strategy/capital capability; expire reservations; retain simulation evidence and no destructive PnL rewrite.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-139 — Recursive transaction envelope, finality and MEV submission policy
- **Milestone:** M13 DEX Amendment
- **Objective:** Bind every nested DEX action and chain observation to a safe plan, finality and submission-channel policy.
- **Scope:** Recursive envelope grammar, proxy/code pinning, nonce lifecycle, reorg/LP finality and MEV fallback policy; excludes chain enablement.
- **Files:** `DEX_ADAPTER_SPEC.md`, `CHAIN_ADAPTER_SPEC.md`, `TRANSACTION_GUARD_SPEC.md`, `LIQUIDITY_ENGINE_SPEC.md` and future contract tests.
- **Dependencies:** PR-074; Q-003, Q-005, Q-007; absence of allowed chain/protocol/signing evidence denies all submission.
- **Implementation:** Deny unknown nested calls; bind permits/sweeps/approvals; pin implementation/hash/block; require fresh simulation for changes; serialize nonce/reorg/channel fallback.
- **Tests:** ACT-011, ACT-012 plus hidden recipient/permit, proxy change, equivocation, nonce race, LP reorg and public-channel fallback tests.
- **Acceptance criteria:** No nested field or fallback changes after authorization; ACTIVE LP requires finality; no channel claims privacy/inclusion guarantee.
- **Security implications:** Stops calldata smuggling, approval drain, proxy drift, reorg and mempool-risk fallback.
- **Observability:** Record envelope/proxy/block/simulation/submission-policy digests and opaque denial reason.
- **Rollback:** Revoke protocol/chain/channel capability; do not resubmit ambiguous operations; reconcile evidence before any linked recovery.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-140 — Execution-bound compliance, fraud and privacy decisions
- **Milestone:** M19 Compliance Amendment
- **Objective:** Make compliance, fraud and privacy decisions explicit spend gates rather than labels in a review document.
- **Scope:** ComplianceDecision/FraudRiskDecision, data lifecycle, step-up invalidation and cash-out holds; excludes provider/legal approval.
- **Files:** `docs/compliance/COMPLIANCE_REVIEW.md`, `POLICY_DECISION.md`, `RISK_ENGINE_SPEC.md`, future decision services/tests.
- **Dependencies:** PR-117; Q-001, Q-006, Q-007; require separately approved legal/privacy/compliance evidence before any activation.
- **Implementation:** Bind subject/payer/destination/screening and privacy-classified velocity/recovery signals; HOLD/REVIEW denies credit availability, lock and broadcast.
- **Tests:** ACT-013 plus sanctions destination, mule linkage, rapid cash-out, device/credential recovery change and retention/immutable-exception tests.
- **Acceptance criteria:** No spend path accepts stale/missing/HOLD/REVIEW decision; PII lifecycle has purpose, owner, retention/deletion and exception reference.
- **Security implications:** Reduces sanctioned destination, mule, takeover and privacy over-collection risk.
- **Observability:** Use bounded/pseudonymous reason codes, decision versions and correlation IDs; never log raw screening/PII payloads.
- **Rollback:** Fail closed to HOLD; retain legally required minimised audit records; forward-fix rules with versioned re-evaluation.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.

## PR-141 — Exact mainnet gate binding, audit order and supply-chain boundary
- **Milestone:** M20 Mainnet Assurance Amendment
- **Objective:** Close release/mainnet assurance around exact authorization, atomic reservations, audit ordering, kill drills and protected evidence root.
- **Scope:** MainnetAuthorization verification, audit sequencing/anchors, scoped kill drills, CI/OIDC/provenance and Vercel static-only boundary; excludes mainnet activation.
- **Files:** `MAINNET_ACTIVATION_SPEC.md`, `READINESS_AUTHORIZATION.md`, `AUDIT_SPEC.md`, `CI_CD_SPEC.md`, `RELEASE_SPEC.md`, future tests/config snapshots.
- **Dependencies:** PR-129, PR-130, PR-131, PR-132, PR-133, PR-140; Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009 and Q-010, each explicit, current and scope-matching.
- **Implementation:** Verify exact action/resource/amount/destination/gates/evidence/reservations/quorum; protect evidence root and release provenance; verify scoped kill propagation and static deploy boundary.
- **Tests:** ACT-003, ACT-014, ACT-015, ACT-016 plus duplicate-principal quorum, reservation race, CI evidence substitution and Vercel-boundary negatives.
- **Acceptance criteria:** Any mismatched/expired/revoked gate/evidence/signer/reservation/quorum denies before signing; static status deployment has no financial authority.
- **Security implications:** Prevents approval laundering, audit rewrite races, kill-switch gaps and supply-chain/evidence-root substitution.
- **Observability:** Record signed authorization/gate/evidence/reservation/quorum/provenance digests and drill results, never secret values.
- **Rollback:** Revoke mainnet capability and freeze promotion; preserve immutable evidence/audit; containment only, never spend break-glass.
- **Definition of done:** Implementation+tests+contract/ADR links+docs+required CI checks PASS; no named Q gate unresolved for any claimed capability; verification evidence is bound to the exact SHA.
