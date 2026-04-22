---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI Profile Example 07 — Third-Party AI Supply Chain

## Description

This example illustrates an SBOM for a consumer finance application
(`FinApp Credit Advisor`) that embeds two AI components sourced from third
parties:

1. **CreditSense API** — a proprietary credit risk scoring model consumed via
   REST API from an external vendor (Acme Credit Analytics). Model internals are
   undisclosed; `noAssertion` is used for unknown properties.
2. **DocExtract ML** — an open-source document understanding model downloaded
   from HuggingFace Hub and deployed in-process.

The SBOM ([spdx3.0/example07.spdx3.json](./spdx3.0/example07.spdx3.json))
demonstrates **AI supply chain transparency** — the ability of a product owner
to document AI components they depend on but do not control — as required by
regulations such as the EU AI Act for deployers of high-risk AI systems:

- `dependsOn` relationships link the application to both AI components
- `originatedBy` / `suppliedBy` distinguish the vendor from the integrating
  organization
- `externalIdentifier` records vendor API identifiers and HuggingFace Hub model
  IDs
- `ai_autonomyType` — SPDX 3.0 property set to `noAssertion` for the opaque
  vendor model (vendor has not disclosed autonomy level), and `no` for the
  open-source model (extraction results reviewed by human loan officers)
- `ai_standardCompliance` — notes vendor's claimed EU AI Act and ECOA compliance
- `ai_useSensitivePersonalInformation: yes` — both AI components process
  personal financial data

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `ai_autonomyType` | `"noAssertion"` / `"no"` | **deprecated** → use `isoAutomationLevel` |

See [spdx3.1/example07.spdx3.json](./spdx3.1/example07.spdx3.json) for the
updated form using `isoAutomationLevel`.

## Profile Conformance

`core`, `ai`, `software`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example07.spdx3.json](./spdx3.0/example07.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example07.spdx3.json](./spdx3.1/example07.spdx3.json) |

## Key Properties Demonstrated

| Property | Notes |
| ---------- | ------- |
| `dependsOn` | Application → two AI components |
| `originatedBy` / `suppliedBy` | Vendor attribution for CreditSense API |
| `externalIdentifier` | Vendor API endpoint and HuggingFace model ID |
| `ai_autonomyType` | `noAssertion` (vendor model), `no` (open-source model) — SPDX 3.0, deprecated in 3.1 |
| `ai_useSensitivePersonalInformation` | `yes` (both AI components) |
| `software_downloadLocation: noAssertion` | Vendor model not directly downloadable |
