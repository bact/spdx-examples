---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI profile example 03 — Medical AI with safety classification

## Description

This example illustrates an SBOM for a medical AI model that analyzes eye
images to assess disease severity.

The SBOM ([spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json))
demonstrates AI-profile properties relevant to **high-risk regulated AI systems**,
covering safety classification, regulatory compliance, explainability, and
sensitive data handling.

## Profile conformance

`core`, `ai`

## SPDX files

| Version | File |
| ------- | ---- |
| SPDX 3.0 | [spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json) |

## Key properties demonstrated

| Property | Notes |
| -------- | ----- |
| `ai_limitation` | Out-of-scope equipment, pediatric patients |
| `ai_modelExplainability` | Methods for interpreting model decisions |
| `ai_safetyRiskAssessment` | `high` |
| `ai_standardCompliance` | IEC 62304, ISO 14971, EU MDR 2017/745 |
| `ai_typeOfModel` | convolutional neural network, supervised |
| `ai_useSensitivePersonalInformation` | `yes` — processes patient medical imagery |
