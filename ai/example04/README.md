---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI Profile Example 04 — Fine-tuned Language Model with Reproducibility Metadata

## Description

This example illustrates an SBOM for a BERT model fine-tuned on commercial
contract clauses for legal clause-type classification (15 categories including
liability, indemnification, and governing law).

The SBOM ([spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json))
demonstrates AI-profile and Dataset-profile properties relevant to
**model reproducibility and lifecycle tracking**:

- `ai_hyperparameter` — full set of training hyperparameters (learning rate,
  optimizer, scheduler, random seed, precision, etc.) enabling experiment
  reproduction
- `ai_modelDataPreprocessing` — tokenization and preprocessing steps applied to
  training data
- `ai_modelExplainability` — LIME explanations and attention weight logging
- `trainedOn` relationship — links the AI model to its training dataset
  (`ContractClauses-v2`)
- `dependsOn` relationship — links to the base model (`bert-base-uncased`) used
  as the fine-tuning starting point

The embedded `DatasetPackage` (`ContractClauses-v2`) demonstrates dataset
documentation alongside the model.

## SPDX 3.0 vs 3.1 Note

The embedded `DatasetPackage` uses `dataset_datasetSize` (item count: 42,000
clauses), which is **deprecated in SPDX 3.1** in favor of `software_artifactSize`
(artifact size in bytes). See the SPDX 3.1 version for the updated form.

## Profile Conformance

`core`, `ai`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example04.spdx3.json](./spdx3.1/example04.spdx3.json) |

## Key Properties Demonstrated

| Property | Notes |
| ---------- | ------- |
| `ai_hyperparameter` | 11 entries (lr, epochs, optimizer, seed, precision, …) |
| `ai_modelExplainability` | LIME, attention weights |
| `ai_typeOfModel` | transformer, fine-tuned, supervised |
| `dataset_datasetSize` | 42,000 clauses (SPDX 3.0, deprecated in 3.1) |
| `trainedOn` | Model → ContractClauses-v2 dataset |
| `dependsOn` | Fine-tuned model → bert-base-uncased base model |
