---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset Profile Example 05 — Sensitive Personal Data (Clinical Notes)

## Description

This example illustrates an SBOM for a sensitive medical dataset:
`ClinicalNotes-DeID`, a corpus of 180,000 de-identified clinical notes
(discharge summaries, progress notes, radiology reports) from a hospital EHR
system, annotated for clinical named entity recognition.

The SBOM ([spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json))
demonstrates Dataset-profile properties for **datasets containing sensitive
personal information**:

- `dataset_hasSensitivePersonalInformation: yes` — the dataset originates from
  patient health records
- `dataset_confidentialityLevel: amber` — Traffic Light Protocol AMBER: access
  restricted to approved research organizations under data use agreements
- `dataset_anonymizationMethodUsed` — the two-stage de-identification pipeline
  applied (rule-based PHI detection + NLP-based residual detection + manual
  review + re-identification audit)
- `dataset_datasetAvailability: query` — accessible only via controlled query
  interface, not direct download
- `dataset_knownBias` — single-institution demographic bias documented
- `dataset_datasetSize` — item count (180,000 notes);
  **deprecated in SPDX 3.1**, replaced by `software_artifactSize`
- `dataset_intendedUse` — clinical NLP research only (not clinical decision
  support); **deprecated in SPDX 3.1**, moved to Core-level `intendedUse`

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | `180000` (item count) | **deprecated** → use `software_artifactSize` (bytes) |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

In SPDX 3.1, the new Core `inLanguage` property can also be used to record
`"en"` (English) directly. See
[spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json).

## Profile Conformance

`core`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_hasSensitivePersonalInformation` | `yes` |
| `dataset_confidentialityLevel` | `amber` |
| `dataset_anonymizationMethodUsed` | 4-step de-identification pipeline |
| `dataset_datasetAvailability` | `query` |
| `dataset_datasetSize` | `180000` notes (SPDX 3.0, deprecated in 3.1) |
| `dataset_intendedUse` | Clinical NLP research only (SPDX 3.0, deprecated in 3.1) |
