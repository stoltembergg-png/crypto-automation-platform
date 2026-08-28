# Adversarial Closure Test Catalogue

**Status:** future implementation tests; this file does not claim the described controls exist.

| Test ID | Required negative scenario | Contract |
|---|---|---|
| ACT-001 | balanced journal entry attempts a cross-tenant or cross-environment posting | closure §1.1 |
| ACT-002 | payload claims `GLOBAL` for a financial/authority object | closure §1 |
| ACT-003 | policy/authorization uses unknown issuer/key, digest, scope, expiry or revocation | closure §1.2 |
| ACT-004 | Q-ID semantic mismatch across registry, readiness and queue | closure §2 |
| ACT-005 | replayed/conflicting provider event and subsequent dispute/reversal | closure §3.1 |
| ACT-006 | withdrawal denial/expiry before `LOCK_POSTED` | closure §3.2 |
| ACT-007 | ambiguous broadcast attempts retry/rebroadcast on same intent | closure §3.2 |
| ACT-008 | adapter submission lacks durable intent, lock, outbox or capability | closure §3.2 |
| ACT-009 | incomplete/stale reconciliation cut requests match/correction | closure §3.3 |
| ACT-010 | partial fill leaves unhedged residual or stale quote/reservation | closure §4.1 |
| ACT-011 | hidden nested permit/sweep, proxy code change, reorg or nonce conflict | closure §4.2 |
| ACT-012 | MEV channel fallback occurs without fresh authorization | closure §4.3 |
| ACT-013 | sanctioned/mule/rapid-cash-out/recovery-context-change operation seeks spend | closure §5 |
| ACT-014 | concurrent audit append races predecessor or uses wrong signing authority | closure §5 |
| ACT-015 | scoped kill switch does not deny its matching in-flight/new execution | closure §6 |
| ACT-016 | build/release evidence root or static Vercel boundary is substituted | closure §6 |

Every future test must be deterministic, tenant/environment scoped, tied to the named PR card, and fail closed on missing provider/legal evidence.
