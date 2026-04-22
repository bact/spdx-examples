---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI profile example 05 — Object detection model with performance metrics

## Description

This example illustrates an SBOM for a YOLOv8-based object detection model
deployed on edge devices for warehouse safety monitoring (detecting workers,
forklifts, pallets, and hazards in camera feeds).

The SBOM ([spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json))
demonstrates AI-profile properties relevant to **model evaluation and deployment
decisions**:

- `ai_autonomyType` — SPDX 3.0 property indicating autonomy level (`no` =
  human safety operators make final response decisions)
- `ai_domain` — application domain context for the model
- `ai_metric` — quantitative performance measures (mAP50, mAP50-95, precision,
  recall, inference latency)
- `ai_metricDecisionThreshold` — thresholds applied at inference time
  (confidence threshold for alert trigger, IoU threshold for NMS, minimum
  worker detection confidence)
- `ai_modelDataPreprocessing` — frame extraction, resizing, augmentation steps
- `trainedOn` relationship — links to the annotated `WarehouseSafety-Train`
  dataset, which itself carries `dataset_confidentialityLevel: amber` and
  `dataset_hasSensitivePersonalInformation: yes` (worker imagery)

## SPDX 3.0 vs 3.1 note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `ai_autonomyType` | `"no"` (PresenceType) | **deprecated** → use Core `isoAutomationLevel`; here: `partialAutomation` |
| `dataset_datasetSize` | Dataset-profile property | **deprecated** → use `software_artifactSize` |

See [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) for the
updated form using `isoAutomationLevel: partialAutomation`
and `software_artifactSize`.

## Profile conformance

`core`, `ai`, `dataset`

## SPDX files

| Version | File |
| --------- | ------ |
| SPDX 3.0 | [spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) |

## Key properties demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `ai_autonomyType` | `no` (SPDX 3.0, deprecated in 3.1) |
| `ai_metric` | mAP50=0.892, mAP50-95=0.741, latency=18ms |
| `ai_metricDecisionThreshold` | confidence=0.75, IoU=0.45 |
| `dataset_confidentialityLevel` | `amber` (worker imagery) |
| `dataset_hasSensitivePersonalInformation` | `yes` |
