---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset profile example 02 — Image dataset

## Description

This example illustrates an SBOM for an image dataset used to train facial
expression recognition models: `FaceExpress-50K`, a collection of 50,000
labeled photographs of human faces showing seven basic emotions.

The SBOM ([spdx3.0/example02.spdx3.json](./spdx3.0/example02.spdx3.json))
demonstrates Dataset-profile properties for **image datasets**, including
data collection, preprocessing, known bias, and privacy sensitivity:

- `dataset_confidentialityLevel: clear` — freely distributable (with license)
- `dataset_dataCollectionProcess` — how images were sourced (lab sessions,
  stock photos, Creative Commons)
- `dataset_dataPreprocessing` — face detection, alignment, quality filtering
- `dataset_datasetSize` — size in bytes; **deprecated in SPDX 3.1**,
  replaced by `software_artifactSize` (same unit: bytes)
- `dataset_datasetType: ["image"]` — dataset content type classification
- `dataset_hasSensitivePersonalInformation: yes` — dataset contains human
  facial imagery
- `dataset_intendedUse` — description of appropriate uses;
  **deprecated in SPDX 3.1**, moved to Core-level `intendedUse`
- `dataset_knownBias` — documented demographic imbalances

## SPDX 3.0 vs 3.1 note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | Dataset-profile property | **deprecated** → use `software_artifactSize` |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

See [spdx3.1/example02.spdx3.json](./spdx3.1/example02.spdx3.json) for the
updated form using `software_artifactSize: 21474836480` (~20 GB) and Core
`intendedUse`.

## Profile conformance

`core`, `dataset`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example02.spdx3.json](./spdx3.0/example02.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example02.spdx3.json](./spdx3.1/example02.spdx3.json) |

## Key properties demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_confidentialityLevel` | `clear` |
| `dataset_datasetSize` | `21474836480` bytes (~20 GB) (SPDX 3.0, deprecated in 3.1) |
| `dataset_datasetType` | `image` |
| `dataset_hasSensitivePersonalInformation` | `yes` |
| `dataset_intendedUse` | Training/evaluation of expression recognition (SPDX 3.0, deprecated in 3.1) |
| `dataset_knownBias` | Skin tone and age distribution imbalances documented |
