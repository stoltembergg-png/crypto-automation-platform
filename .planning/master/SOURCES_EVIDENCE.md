# External Source Evidence Ledger

This ledger separates **documentation reachability** from **provider capability, account authorization, legal approval, or production readiness**. It is intentionally conservative.

| ID | Source | Observation in this planning session | Permitted use in this plan |
|---|---|---|---|
| [1] | Lei nº 14.478/2022 (Planalto) | URL recorded; content request timed out. | Legal-review reference only; no interpretation treated as verified. |
| [2] | LGPD (Planalto) | URL recorded; content request timed out. | Legal-review reference only; no interpretation treated as verified. |
| [3] | Banco Central — Criptoativos | HTTP 200 at `https://www.bcb.gov.br/estabilidadefinanceira/criptoativos`; fetched body SHA-256 `40df034b6b4f975c96f785a359da4ce4bf48572fcbc52ee96ad2a2d934f37952`. | Official regulatory discovery point; regulation/version/eligibility must be re-checked by counsel and compliance owner. |
| [4] | Mercado Pago — Pix | HTTP 200 after canonical redirect; fetched body SHA-256 `e1a7bf7a70985dd1247d74aabc2b8812c96f08731af7bfb156fb50c18548686b`. | Interface-design reference only; sandbox contract tests must retrieve current schemas. |
| [5] | Mercado Pago — Webhooks | HTTP 200; fetched body SHA-256 `8e1037ea05d454b133c4ffe331c8ecca45fb4fa6203169d55323c1ff0b2c7779`. | Interface-design reference only; signature algorithm/header behavior is re-validated in future sandbox PR. |
| [6] | EIP-1193 | HTTP 200; fetched body SHA-256 `7a29e3f43c262ad3f663b8f419257132c127e1580c91cbe837d59f86a5bd7ab4`. | Wallet-provider compatibility reference for future MetaMask adapter. |
| [7] | ERC-4361 | HTTP 200; fetched body SHA-256 `0530d2eb496ab9f9061474a68a4b1e280692c46c533f1a5f1541a1a741aed663`. | Sign-In with Ethereum compatibility reference; authentication is still bound to backend nonce, domain, URI, chain, expiry, and one-time use. |
| [8] | WebAuthn Level 3 | HTTP 200; fetched body SHA-256 `157030c980d44a3ce4b1ec5bcfaa16790c7dfefac20709af6ed2b11c7120970b`. | Strong-authentication standards reference; platform support and UX policy require future compatibility tests. |

## Retrieval limitation

The configured `web_search` and `web_extract` services returned a billing/quota error. Browser automation additionally needs the user to allow Chrome remote debugging, and was not retried. Direct HTTP retrieval is the sole content evidence represented here. Raw normalized retrieval files and `fetch_manifest.json` live under `.planning/master/research/`.

## Required revalidation events

- Before signing a Mercado Pago sandbox agreement or developing against its current API.
- Before every provider/account activation, production webhook registration, or credential grant.
- Before legal classification, licensing, KYC/KYT, AML/sanctions, tax, consumer-law, or LGPD conclusion.
- Before every testnet or mainnet activation gate.
- On source version, provider contract, regulation, or policy change.
