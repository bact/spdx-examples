---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI profile example 07 — Third-party AI supply chain

## Description

This example illustrates an SBOM for a consumer finance application
(`FinApp Credit Advisor`) that embeds two AI components sourced from third
parties:

1. **CreditSense API** — a proprietary credit scoring model accessed via API
   from an external vendor. Model internals are undisclosed; `noAssertion` is
   used for unknown properties.
2. **DocExtract ML** — an open-source document understanding model downloaded
   from a public model repository and deployed in-process.

The SBOM ([spdx3.0/example07.spdx3.json](./spdx3.0/example07.spdx3.json))
demonstrates **AI supply chain transparency** — the ability of a product owner
to document AI components they depend on but do not control, including autonomy
levels, regulatory compliance claims, sensitive data handling, and vendor
attribution.

## Profile conformance

`core`, `ai`, `software`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example07.spdx3.json](./spdx3.0/example07.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example07.spdx3.json](./spdx3.1/example07.spdx3.json) |

## Key properties demonstrated

| Property | Notes |
| ---------- | ------- |
| `ai_autonomyType` | `noAssertion` (vendor model), `no` (open-source model) — deprecated in SPDX 3.1, use `isoAutomationLevel` |
| `ai_standardCompliance` | Regulatory standards the vendor claims compliance with |
| `ai_useSensitivePersonalInformation` | `yes` — both AI components process personal financial data |
| `dependsOn` | Application → two AI components |
| `externalIdentifier` | Vendor API endpoint and public model repository ID |
| `originatedBy` / `suppliedBy` | Vendor attribution for CreditSense API |
| `software_downloadLocation` | `noAssertion` — vendor model not directly downloadable |
