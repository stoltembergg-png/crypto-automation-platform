# High-Risk Traceability Matrix

Only high-risk requirements and flows are traced. There is deliberately **no trace-card count target**: create/retain a card only when it adds proof value, has a named owner and a revalidation trigger.

| Trace ID | High-risk requirement / flow | Source specification / ADR | Required proof value | Owner | Revalidation trigger |
|---|---|---|---|---|---|
| TR-001 | AI cannot execute financial action directly | 02, 08, ADR-0001 | Proposal/action grammar and denial-test evidence | Risk + Security | policy/action version change |
| TR-002 | Ledger remains balanced and singular | 03, ADR-0002 | property/model test and accounting review | Finance | chart/event schema change |
| TR-003 | External fact cannot mutate balance directly | 03, 09 | correlation/separation test evidence | Finance + Platform | adapter or reconciliation change |
| TR-004 | Capability claim is current and legally allowed | 06, ADR-0006 | owned claim record + boundary test + legal disposition | Provider owner | expiry/config/provider change |
| TR-005 | Withdrawal locks once; ambiguity does not double-mutate | 05, contract states | generated state-machine test and incident procedure | Custody + Finance | signing/broadcast/provider change |
| TR-006 | Mainnet authorization binds scope and is replay-safe | 02, 11, ADR-0007 | signature/revocation/replay/attestation denial tests | Security | auth/key/environment change |
| TR-007 | Cross-tenant privileged use is denied | 10, ADR-0005 | capability substitution/revocation test | Security | identity/capability change |
| TR-008 | Audit claim is not overstated | 09, ADR-0008 | anchor/key/retention/incident proof or wording remains limited | Operations | retention/key/anchor change |
| TR-009 | Reorg, partial fill and LP drift are not treated as settled | 06–09 | per-venue negative tests/reconciliation evidence | Market Risk | venue/chain/strategy change |
| TR-010 | Legal disposition cannot be bypassed | 04, 05, 12 | rule evaluation and approval-path test | Legal + Security | jurisdiction/flow change |
| TR-011 | Maturity does not imply readiness | 11, ADR-0009 | gate-evaluation test and release review | Release owner | environment/release change |
| TR-012 | Release only consumes verified evidence | 12, readiness matrix | provenance and release gate record | Release owner | pipeline/attestor change |
