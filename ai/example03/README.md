---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI profile example 03 — Medical AI with safety classification

## Description

This example illustrates an SBOM for a medical AI system: a convolutional neural
network that grades diabetic retinopathy severity from retinal fundus photographs.

The SBOM ([spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json))
demonstrates AI-profile properties relevant to **high-risk regulated AI systems**:

- `ai_limitation` — documents known constraints and out-of-scope populations
- `ai_modelExplainability` — describes how model decisions can be interpreted
  (Grad-CAM saliency maps, MC Dropout uncertainty)
- `ai_safetyRiskAssessment` — classifies the model's safety risk level
  (`serious` / `high` / `medium` / `low`)
- `ai_standardCompliance` — lists regulatory and technical standards the system
  must comply with (IEC 62304, ISO 14971, EU MDR)
- `ai_useSensitivePersonalInformation` — declared `yes` because the model
  processes patient medical imagery

## SPDX 3.0 vs 3.1 note

`ai_autonomyType` (SPDX 3.0, `PresenceType`: yes / no / noAssertion) is the
property used in SPDX 3.0 to indicate whether the AI system operates
autonomously. For this model the value would be `no` (human clinician reviews
all classifications). This property is **deprecated in SPDX 3.1** and replaced
by `isoAutomationLevel` (a Core property with an ISO 22989-aligned vocabulary).

This example does not have a separate SPDX 3.1 file because the deprecated
`ai_autonomyType` property is documented only in a `comment` field here, not
used as a data property. See
[ai/example05](../example05/) and [ai/example06](../example06/) for examples
that explicitly set `ai_autonomyType` and provide 3.1 counterparts.

## Profile conformance

`core`, `ai`

## SPDX files

| Version | File |
| ------- | ---- |
| SPDX 3.0 | [spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json) |

## Key properties demonstrated

| Property | Value |
| -------- | ----- |
| `ai_limitation` | Out-of-scope equipment, pediatric patients |
| `ai_modelExplainability` | Grad-CAM, MC Dropout |
| `ai_safetyRiskAssessment` | `high` |
| `ai_standardCompliance` | IEC 62304, ISO 14971, EU MDR 2017/745 |
| `ai_typeOfModel` | convolutional neural network, supervised |
| `ai_useSensitivePersonalInformation` | `yes` |
