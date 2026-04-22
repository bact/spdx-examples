---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset profile example 05 — Sensitive personal data (clinical notes)

## Description

This example illustrates an SBOM for a sensitive medical dataset:
`ClinicalNotes-DeID`, a corpus of 180,000 de-identified clinical notes
(discharge summaries, progress notes, radiology reports) from a hospital EHR
system, annotated for clinical named entity recognition.

The SBOM ([spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json))
demonstrates Dataset-profile properties for **datasets containing sensitive
personal information**:

- `dataset_anonymizationMethodUsed` — the two-stage de-identification pipeline
  applied (rule-based PHI detection + NLP-based residual detection + manual
  review + re-identification audit)
- `dataset_confidentialityLevel: amber` — Traffic Light Protocol AMBER: access
  restricted to approved research organizations under data use agreements
- `dataset_datasetAvailability: query` — accessible only via controlled query
  interface, not direct download
- `dataset_datasetSize` — size in bytes; **deprecated in SPDX 3.1**,
  replaced by `software_artifactSize` (same unit: bytes)
- `dataset_hasSensitivePersonalInformation: yes` — the dataset originates from
  patient health records
- `dataset_intendedUse` — clinical NLP research only (not clinical decision
  support); **deprecated in SPDX 3.1**, moved to Core-level `intendedUse`
- `dataset_knownBias` — single-institution demographic bias documented

## SPDX 3.0 vs 3.1 note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | Dataset-profile property | **deprecated** → use `software_artifactSize` |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

In SPDX 3.1, the new Core `inLanguage` property can also be used to record
`"en"` (English) directly. See
[spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json).

## Profile conformance

`core`, `dataset`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) |

## Key properties demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_anonymizationMethodUsed` | 4-step de-identification pipeline |
| `dataset_confidentialityLevel` | `amber` |
| `dataset_datasetAvailability` | `query` |
| `dataset_datasetSize` | `2684354560` bytes (~2.5 GB) (SPDX 3.0, deprecated in 3.1) |
| `dataset_hasSensitivePersonalInformation` | `yes` |
| `dataset_intendedUse` | Clinical NLP research only (SPDX 3.0, deprecated in 3.1) |
