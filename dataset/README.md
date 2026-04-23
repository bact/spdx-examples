---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# SPDX Dataset profile examples

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
| [01](./example01/) | 2 CSV files | - | 1 document | 1 document | Tabular CSV dataset; `/Dataset/datasetType: structured, timestamp`; **3.0→3.1**: `/Dataset/datasetSize` → `/Software/artifactSize`, `/Dataset/intendedUse` → `/Core/intendedUse` |
| [02](./example02/) | Images | - | 1 document | 1 document | Image dataset; `/Dataset/knownBias`, `/Dataset/hasSensitivePersonalInformation`; **3.0→3.1**: `/Dataset/datasetSize` → `/Software/artifactSize` |
| [03](./example03/) | Text | - | 1 document | 1 document | Multilingual text corpus; **3.0→3.1**: `/Dataset/intendedUse` → `/Core/intendedUse`, language added via `inLanguage` (new in 3.1) |
| [04](./example04/) | Sensor/CSV | - | 1 document | 1 document | Sensor/time series data; `/Dataset/datasetType: sensor, timestamp`, `/Dataset/datasetUpdateMechanism`; **3.0→3.1**: `/Dataset/datasetSize` → `/Software/artifactSize` |
| [05](./example05/) | Text | - | 1 document | 1 document | Sensitive clinical data; `/Dataset/hasSensitivePersonalInformation: yes`, `/Dataset/confidentialityLevel: amber`, `/Dataset/anonymizationMethodUsed`; **3.0→3.1**: deprecated properties replaced |
| [06](./example06/) | CSV | - | 1 document | 1 document | Synthetic data; `/Dataset/datasetType: structured`, `/Dataset/datasetNoise`; **3.0→3.1**: `/Dataset/datasetSize` → `/Software/artifactSize` |
