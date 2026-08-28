# Legal and Compliance Review

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Records `REQUIRES_LEGAL_REVIEW` rather than legal conclusions for Brazilian financial, crypto, payment, AML and privacy topics.

## Normative requirements

- Mandatory review areas: legal entity/jurisdiction, custody, administration of third-party resources, automated investment/discretion, intermediation, Pix/payment provider contract, KYC/KYT/sanctions/AML/source of funds, tax/reporting, consumer disclosures, LGPD, retention and automated-decision accountability.
- A legal disposition is non-overridable by technical policy and expires/revalidates on scope change.
- Production money movement is blocked while a critical legal issue is open.

## Component contracts

LegalDisposition, ComplianceCase, KYCDecision, KYTAlert, SanctionsScreening, PrivacyAssessment.

## Invariants and deny conditions

No documentation, vendor statement or source URL constitutes legal approval. Data minimization, purpose limitation, retention, access/export/deletion and immutable accounting exceptions must be approved.

## State and failure semantics

OPEN→EVIDENCE_COLLECTING→COUNSEL_REVIEW→APPROVED_LIMITED|REJECTED|EXPIRED.

## Future verification

Policy-bypass tests, disposition expiry/revocation tests, data-map/retention tests and independent legal handoff checklist.

## Queue ownership

Implementation is decomposed in `PR-123..PR-127`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/12-ci-release-and-compliance.md; .planning/master/SOURCES_EVIDENCE.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
