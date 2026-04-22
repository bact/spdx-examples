---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# Dataset Profile Example 04 — Sensor and Time Series Data

## Description

This example illustrates an SBOM for an industrial IoT sensor dataset:
`PumpHealth-Sensors`, multivariate time series data collected from 47
centrifugal pumps at manufacturing facilities, used for training predictive
maintenance models.

The SBOM ([spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json))
demonstrates Dataset-profile properties for **sensor and time series datasets**:

- `dataset_datasetType: ["sensor", "timestamp"]` — multiple types can be
  combined; `sensor` indicates physical sensor readings, `timestamp` indicates
  time-indexed records
- `dataset_datasetUpdateMechanism` — describes how the dataset evolves over time
  (quarterly snapshots with versioning)
- `dataset_confidentialityLevel: green` — data may be shared within a defined
  peer/partner community (Traffic Light Protocol)
- `dataset_dataCollectionProcess` — sensor calibration, OPC-UA logging,
  expert fault labeling from work orders
- `dataset_knownBias` — single-manufacturer bias, fault class imbalance
- `dataset_datasetSize` — record count (48,254,400 sensor readings);
  **deprecated in SPDX 3.1**, replaced by `software_artifactSize`
- `dataset_intendedUse` — predictive maintenance research;
  **deprecated in SPDX 3.1**, moved to Core-level `intendedUse`

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `dataset_datasetSize` | `48254400` (record count) | **deprecated** → use `software_artifactSize` (bytes) |
| `dataset_intendedUse` | Dataset-profile property | **deprecated** → use Core `intendedUse` |

See [spdx3.1/example04.spdx3.json](./spdx3.1/example04.spdx3.json) for the
updated form using `software_artifactSize: 5798205850` (~5.4 GB) and Core
`intendedUse`.

## Profile Conformance

`core`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example04.spdx3.json](./spdx3.0/example04.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example04.spdx3.json](./spdx3.1/example04.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `dataset_datasetType` | `sensor`, `timestamp` |
| `dataset_datasetSize` | `48254400` records (SPDX 3.0, deprecated in 3.1) |
| `dataset_datasetUpdateMechanism` | Quarterly appended snapshots |
| `dataset_confidentialityLevel` | `green` (consortium partner sharing) |
| `dataset_hasSensitivePersonalInformation` | `no` |
