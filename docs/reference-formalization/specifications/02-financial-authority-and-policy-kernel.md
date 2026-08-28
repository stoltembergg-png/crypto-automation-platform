# SDD-02 — Financial Authority and Policy Kernel

**Status:** Proposed control model; no action is authorized by this specification.

## Authority model
AI, strategy engines, users, workflows and external events may create a **proposal**, never a privileged effect. The authority kernel accepts only typed/versioned proposals for a finite action vocabulary: `CREATE_PAYMENT_INTENT`, `POST_ACCOUNTING_EVENT`, `CREATE_WITHDRAWAL_INTENT`, `REQUEST_ORDER`, `REQUEST_DEX_OPERATION`, `CANCEL_ORDER`, `REQUEST_RECONCILIATION`, and `REQUEST_RELEASE_GATE`. The vocabulary is illustrative until Q-001–Q-007 approves concrete scope; unknown actions MUST deny.

A proposal includes `proposal_id`, `schema_version`, `tenant_id`, `environment`, `action`, `resource_scope`, `parameters_hash`, `policy_version`, `policy_hash`, `risk_context_hash`, `legal_disposition`, `created_at`, `expires_at`, `idempotency_key`, proposer identity, and provenance. The kernel evaluates schema, tenant, environment, action grammar, policy pin, legal disposition, capability, risk, independent approval requirement, expiry, revocation and replay before it can return `AUTHORIZED`.

## Mandatory dispositions
`ACCEPTED`, `DENIED`, `DUPLICATE`, `CONFLICT`, `PENDING_EXTERNAL_EVIDENCE`, `REQUIRES_LEGAL_REVIEW`, `INVALID`. `REQUIRES_LEGAL_REVIEW` is terminal for automated execution; no role/policy flag may downgrade it.

## Independent gates
A financially privileged action must traverse: syntactic validation → deterministic policy → legal disposition → risk decision → capability/tenant/environment verification → per-operation authorization (when required) → execution guard. The same unreviewed proposal producer cannot satisfy all independent gate identities.

## Mainnet boundary
At any privileged spend/sign/network/broadcast boundary, a signed and versioned authorization MUST bind tenant, operation/resource, parameters hash, environment, legal disposition, policy hash/version, expiry, revocation version and replay nonce. Environment-attestation mismatch denies sign/network/broadcast and emits bounded redacted telemetry.

## Required tests
Fuzz unknown schemas/actions; policy downgrade/pin mismatch; forged/stale/revoked/replayed auth; cross-tenant and audience substitution; AI output direct adapter access; environment mismatch. Each must show no dispatch and no accounting event.
