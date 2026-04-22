---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI profile example 04 — Fine-tuned language model with reproducibility metadata

## Description

This example illustrates an SBOM for a language model fine-tuned to classify
clauses in legal contracts.

The SBOM ([spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json))
demonstrates AI-profile and Dataset-profile properties relevant to
**model reproducibility and lifecycle tracking**, including hyperparameters,
data preprocessing, explainability methods, and dataset size documentation.
The embedded `DatasetPackage` (`ContractClauses-v2`) shows dataset
documentation alongside the model.

## Profile conformance

`core`, `ai`, `dataset`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example04.spdx3.json](./spdx3.1/example04.spdx3.json) |

## Key properties demonstrated

| Property / Relationship | Notes |
| ---------- | ------- |
| `ai_hyperparameter` | Training settings (learning rate, epochs, optimizer, seed, precision, …) |
| `ai_modelExplainability` | Methods for interpreting model output |
| `ai_typeOfModel` | transformer, fine-tuned, supervised |
| `dataset_datasetSize` | 524288000 bytes (~500 MB) — deprecated in SPDX 3.1, use `software_artifactSize` |
| `dependsOn` | Fine-tuned model → base model |
| `trainedOn` | Model → ContractClauses-v2 dataset |
