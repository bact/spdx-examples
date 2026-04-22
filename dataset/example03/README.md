---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset Profile Example 03 — Multilingual Text Corpus

## Description

This example illustrates an SBOM for a multilingual news article corpus:
`MultiNews-SEA`, a collection of 2.4 million articles in five Southeast Asian
languages (Thai, Indonesian, Vietnamese, Filipino, Malay) designed for
pretraining and evaluating NLP models.

The SBOM ([spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json))
demonstrates Dataset-profile properties for **text corpora**, with an
emphasis on properties that change between SPDX 3.0 and 3.1:

- `dataset_datasetType: ["text"]` — text content type
- `dataset_datasetSize` — item count (2.4 million articles); **deprecated in
  SPDX 3.1**, replaced by `software_artifactSize`
- `dataset_intendedUse` — appropriate NLP use cases; **deprecated in SPDX 3.1**,
  moved to Core-level `intendedUse`
- `dataset_dataCollectionProcess` — RSS crawling, deduplication, terms-of-service
  compliance
- `dataset_dataPreprocessing` — language detection, near-duplicate removal, PII
  scrubbing
- `dataset_knownBias` — urban/online source bias and regional language gaps
- `dataset_datasetUpdateMechanism` — annual incremental releases

### Language Information: SPDX 3.0 vs 3.1

A notable limitation of SPDX 3.0 is the **absence of a standard property for
recording the human languages** present in a dataset. Language information can
only be noted in `description` or `comment` fields in SPDX 3.0.

SPDX 3.1 introduces the Core `inLanguage` property (BCP 47 language tags),
directly addressing this gap. The SPDX 3.1 version of this example uses:

```json
"inLanguage": ["th", "id", "vi", "fil", "ms"]
```

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | `2400000` (item count) | **deprecated** → use `software_artifactSize` |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |
| Language metadata | description/comment only | `inLanguage` (new Core property, BCP 47) |

See [spdx3.1/example03.spdx3.json](./spdx3.1/example03.spdx3.json).

## Profile Conformance

`core`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example03.spdx3.json](./spdx3.0/example03.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example03.spdx3.json](./spdx3.1/example03.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_datasetType` | `text` |
| `dataset_datasetSize` | `2400000` items (SPDX 3.0, deprecated in 3.1) |
| `dataset_intendedUse` | NLP pretraining/benchmarking (SPDX 3.0, deprecated in 3.1) |
| Language (SPDX 3.0) | In `description` only (no standard property) |
| `inLanguage` (SPDX 3.1) | `["th", "id", "vi", "fil", "ms"]` |
| `dataset_datasetUpdateMechanism` | Annual incremental releases |
