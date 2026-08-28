# Authentication Specification

**Status:** `PROPOSED` — planning contract only; no control described here exists until its named implementation, test, audit, and activation evidence are independently PASS.

## Purpose and boundary

Defines passkey-first strong authentication, sessions and authorization context.

## Normative requirements

- WebAuthn/passkeys are primary; TOTP is recovery/optional factor.
- Sessions use rotation, device tracking, risk signals, CSRF/CSP/rate limits and step-up challenge for withdrawal/security changes.
- Wallet signatures are additional proof, not account recovery/custody authority.

## Component contracts

AuthMethod, Session, Device, StepUpChallenge, SecurityEvent, AuthorizationContext.

## Invariants and deny conditions

Session refresh rotation detects reuse; sensitive action requires fresh authentication and relevant capability. Tenant/object access denies before existence disclosure.

## State and failure semantics

REGISTERED→CHALLENGED→VERIFIED→AUTHENTICATED→STEP_UP_REQUIRED→REVOKED|EXPIRED.

## Future verification

WebAuthn/TOTP/session-reuse/CSRF/brute-force/device-change tests and authorization matrix negative tests.

## Queue ownership

Implementation is decomposed in `PR-008..PR-016`. Every dependent card is blocked by unresolved Q-gates, missing provider evidence, or a non-PASS predecessor.

## Detailed reference and provenance

Planning detail is cross-checked against `docs/reference-formalization/specifications/10-auth-trust-threat-and-security.md`. External facts remain subject to `.planning/master/SOURCES_EVIDENCE.md`; source reachability is never capability, contractual, regulatory, or production proof.
