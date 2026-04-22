---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# SPDX Dataset Profile Examples

This repository includes demonstrations of [SPDX documents](https://spdx.dev)
for a Dataset Profile.

## Format of examples

Directories of the form `example##` are structured as follows:

- `content/`: contains the example's content (data files, source code, etc.)
- `spdx3.0/`: contains SPDX 3.0 documents for the example
- `spdx3.1/`: contains SPDX 3.1 documents for the example
- `README.md`: more details about the particular example

## Examples

| # | Data | Sources | SPDX 3.0 | SPDX 3.1 | Focus |
| - | ---- | ------- | -------- | -------- | ----- |
| [01](./example01/) | 2 CSV files | - | 1 document | 1 document | Tabular CSV dataset; `dataset_datasetType: structured, timestamp`; **3.0→3.1**: `dataset_datasetSize` → `software_artifactSize`, `dataset_intendedUse` → Core `intendedUse` |
| [02](./example02/) | Images | - | 1 document | 1 document | Image dataset; `dataset_knownBias`, `dataset_hasSensitivePersonalInformation`; **3.0→3.1**: `dataset_datasetSize` → `software_artifactSize` |
| [03](./example03/) | Text | - | 1 document | 1 document | Multilingual text corpus; **3.0→3.1**: `dataset_intendedUse` → Core `intendedUse`, language added via `inLanguage` (new in 3.1) |
| [04](./example04/) | Sensor/CSV | - | 1 document | 1 document | Sensor/time series data; `dataset_datasetType: sensor, timestamp`, `dataset_datasetUpdateMechanism`; **3.0→3.1**: `dataset_datasetSize` → `software_artifactSize` |
| [05](./example05/) | Text | - | 1 document | 1 document | Sensitive clinical data; `dataset_hasSensitivePersonalInformation: yes`, `dataset_confidentialityLevel: amber`, `dataset_anonymizationMethodUsed`; **3.0→3.1**: deprecated properties replaced |
| [06](./example06/) | CSV | - | 1 document | 1 document | Synthetic data; `dataset_datasetType: structured`, `dataset_datasetNoise`; **3.0→3.1**: `dataset_datasetSize` → `software_artifactSize` |
