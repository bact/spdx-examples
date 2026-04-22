---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Example 02

## Description

This example illustrates a software bill of materials (SBOM) for an AI
application that employs machine learning to perform a text sentiment analysis.

The SBOM ([spdx3.0/sbom.spdx3.json](./spdx3.0/sbom.spdx3.json)) demonstrates
the structure between `AIPackage`, `DatasetPackage`, and their technical
documentation through (lifecycle-scoped) relationship types such as
`dependsOn`,
`generates`,
`hasDataFile`,
`hasDocumentation`,
`testedOn`, and
`trainedOn`.

## SPDX 3.0 vs 3.1 note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `ai_autonomyType` | `"yes"` (PresenceType) | **deprecated** → use Core `isoAutomationLevel`; here: `conditionalAutomation` |
| `dataset_datasetSize` | Dataset-profile property | **deprecated** → use `software_artifactSize` |

See [spdx3.1/sbom.spdx3.json](./spdx3.1/sbom.spdx3.json) for the updated form
using `isoAutomationLevel: conditionalAutomation` and
`software_artifactSize: 11534336` (~11 MB).

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/sbom.spdx3.json](./spdx3.0/sbom.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/sbom.spdx3.json](./spdx3.1/sbom.spdx3.json) |

[![A diagram showing relationships between elements in the Sentiment Demo package (Example 2).](./sbom-spdx3.png "A diagram showing relationships between elements in the Sentiment Demo package (Example 2).")](sbom-spdx3.png)

See the [package README](./content/README.md) inside the
[content/](./content/) directory for more details.
