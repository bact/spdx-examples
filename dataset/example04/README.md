---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset profile example 04 — Sensor and time series data

## Description

This example illustrates an SBOM for a dataset of sensor readings collected
from industrial equipment, used to train models that predict when maintenance
is needed.

The SBOM demonstrates Dataset-profile properties for
**sensor and time series datasets**, including collection process,
multiple dataset types, update mechanism, known bias, and access controls.

## Profile conformance

`core`, `dataset`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example04.spdx3.json-draft](./spdx3.1/example04.spdx3.json-draft) |

[![A diagram of Dataset profile example 04 — Sensor and time series data.](./example04.spdx3.png "A diagram of Dataset profile example 04 — Sensor and time series data.")](./example04.spdx3.png)

## Key properties demonstrated

| Property | Notes |
| ---------- | ------- |
| `dataset_confidentialityLevel` | `green` — data may be shared within a defined partner community |
| `dataset_dataCollectionProcess` | How sensor readings were recorded and labeled |
| `dataset_datasetSize` | `5798205850` bytes (~5.4 GB) — deprecated in SPDX 3.1, use `software_artifactSize` |
| `dataset_datasetType` | `sensor`, `timestamp` — multiple types combined; `sensor` = physical readings, `timestamp` = time-indexed records |
| `dataset_datasetUpdateMechanism` | Quarterly appended snapshots |
| `dataset_hasSensitivePersonalInformation` | `no` |
| `dataset_intendedUse` | Research use cases — deprecated in SPDX 3.1, use Core `intendedUse` |
| `dataset_knownBias` | Gaps in equipment and failure type coverage documented |
