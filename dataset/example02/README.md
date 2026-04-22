---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset Profile Example 02 — Image Dataset

## Description

This example illustrates an SBOM for an image dataset used to train facial
expression recognition models: `FaceExpress-50K`, a collection of 50,000
labeled photographs of human faces showing seven basic emotions.

The SBOM ([spdx3.0/example02.spdx3.json](./spdx3.0/example02.spdx3.json))
demonstrates Dataset-profile properties for **image datasets**, including
data collection, preprocessing, known bias, and privacy sensitivity:

- `dataset_datasetType: ["image"]` — dataset content type classification
- `dataset_datasetSize` — item count (50,000 images); **deprecated in SPDX 3.1**,
  replaced by `software_artifactSize` (artifact size in bytes)
- `dataset_intendedUse` — description of appropriate uses; **deprecated in SPDX 3.1**,
  moved to Core-level `intendedUse`
- `dataset_dataCollectionProcess` — how images were sourced (lab sessions,
  stock photos, Creative Commons)
- `dataset_dataPreprocessing` — face detection, alignment, quality filtering
- `dataset_knownBias` — documented demographic imbalances
- `dataset_hasSensitivePersonalInformation: yes` — dataset contains human
  facial imagery
- `dataset_confidentialityLevel: clear` — freely distributable (with license)

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | `50000` (item count) | **deprecated** → use `software_artifactSize` (bytes) |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

See [spdx3.1/example02.spdx3.json](./spdx3.1/example02.spdx3.json) for the
updated form using `software_artifactSize: 21474836480` (~20 GB) and Core
`intendedUse`.

## Profile Conformance

`core`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example02.spdx3.json](./spdx3.0/example02.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example02.spdx3.json](./spdx3.1/example02.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_datasetType` | `image` |
| `dataset_datasetSize` | `50000` items (SPDX 3.0, deprecated in 3.1) |
| `dataset_intendedUse` | Training/evaluation of expression recognition (SPDX 3.0, deprecated in 3.1) |
| `dataset_hasSensitivePersonalInformation` | `yes` |
| `dataset_confidentialityLevel` | `clear` |
| `dataset_knownBias` | Skin tone and age distribution imbalances documented |
