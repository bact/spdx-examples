---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI Profile Example 06 — Energy Consumption Reporting

## Description

This example illustrates an SBOM for a large vision transformer model
(ViT-Large/16) that classifies land use from multispectral satellite imagery
for deforestation monitoring.

The SBOM ([spdx3.0/example06.spdx3.json](./spdx3.0/example06.spdx3.json))
demonstrates the **`ai_energyConsumption` structure** — the primary focus of
this example — covering all three lifecycle stages required by emerging AI
transparency and sustainability regulations (e.g., EU AI Act, ISO/IEC 42001):

```
ai_energyConsumption
├── ai_trainingEnergyConsumption    → 4,823.5 kWh  (32× A100, 14 days)
├── ai_finetuningEnergyConsumption  →   187.2 kWh  (domain adaptation)
└── ai_inferenceEnergyConsumption   →     0.0041 kWh (per batch job)
```

Each stage uses an `ai_EnergyConsumptionDescription` object with
`ai_energyQuantity` (decimal) and `ai_energyUnit`
(`kilowattHour` / `megajoule` / `other`).

The example also uses `ai_autonomyType` (SPDX 3.0) to record autonomy level.

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `ai_autonomyType` | `"noAssertion"` (PresenceType) | **deprecated** → use `isoAutomationLevel` |

In SPDX 3.1, the Core-level `intendedUse` property also allows describing
deployment purpose at the artifact level. See
[spdx3.1/example06.spdx3.json](./spdx3.1/example06.spdx3.json).

## Profile Conformance

`core`, `ai`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example06.spdx3.json](./spdx3.0/example06.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example06.spdx3.json](./spdx3.1/example06.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `ai_energyConsumption` | All 3 stages (training, finetuning, inference) |
| `ai_trainingEnergyConsumption` | 4,823.5 kWh |
| `ai_finetuningEnergyConsumption` | 187.2 kWh |
| `ai_inferenceEnergyConsumption` | 0.0041 kWh per batch |
| `ai_standardCompliance` | ISO/IEC 42001:2023 |
| `ai_autonomyType` | `noAssertion` (SPDX 3.0, deprecated in 3.1) |
