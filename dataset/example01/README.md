---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Example 01

## Description

An example of a simple dataset in tabular format.

```text
content
├── codebook.csv
└── data.csv
```

Both `codebook.csv` and `data.csv` are plain text files in CSV (comma-separated
values) format.

The file `data.csv` contains records of gas emission data for each year in a
country. It has a header on the first line that defines the column names.
Each record consists mostly of numerical data with some categorical data.

The file `codebook.csv` contains the column names from the header of
`data.csv`, together with their description, unit, and source.

The content of this example is an excerpt of the Our World in Data CO2 and
Greenhouse Gas Emissions dataset. It is available in full, under Creative
Commons Attribution 4.0 International License, at
<https://github.com/owid/co2-data/>.

This simplified
[Unified Modeling Language (UML)](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
class diagram illustrates Example 01.  Long string values are truncated and the
spdxIds are shortened (by removing the UUID suffix), for brevity.

[![A diagram of a bill of materials of Dataset Example 01](./spdx3.0/example01.png "A diagram of a bill of materials of Dataset Example 01")](./spdx3.0/example01.png)

## SPDX 3.0 vs 3.1 note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | Dataset-profile property | **deprecated** → use `software_artifactSize` |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

See [spdx3.1/example01.spdx3.json](./spdx3.1/example01.spdx3.json) for the
updated form using `software_artifactSize: 204800` (~200 KB) and Core
`intendedUse`.

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example01.spdx3.json](./spdx3.0/example01.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example01.spdx3.json](./spdx3.1/example01.spdx3.json) |
