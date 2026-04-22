---
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: CC-BY-4.0
---

# AI Profile Example 05 — Object Detection Model with Performance Metrics

## Description

This example illustrates an SBOM for a YOLOv8-based object detection model
deployed on edge devices for warehouse safety monitoring (detecting workers,
forklifts, pallets, and hazards in camera feeds).

The SBOM ([spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json))
demonstrates AI-profile properties relevant to **model evaluation and deployment
decisions**:

- `ai_metric` — quantitative performance measures (mAP50, mAP50-95, precision,
  recall, inference latency)
- `ai_metricDecisionThreshold` — thresholds applied at inference time
  (confidence threshold for alert trigger, IoU threshold for NMS, minimum
  worker detection confidence)
- `ai_modelDataPreprocessing` — frame extraction, resizing, augmentation steps
- `ai_domain` — application domain context for the model
- `trainedOn` relationship — links to the annotated `WarehouseSafety-Train`
  dataset, which itself carries `dataset_confidentialityLevel: amber` and
  `dataset_hasSensitivePersonalInformation: yes` (worker imagery)
- `ai_autonomyType` — SPDX 3.0 property indicating autonomy level (`no` =
  human safety operators make final response decisions)

## SPDX 3.0 vs 3.1 Note

| Property | SPDX 3.0 | SPDX 3.1 |
| ---------- | ---------- | ---------- |
| `ai_autonomyType` | `"no"` (PresenceType) | **deprecated** → use `isoAutomationLevel` |
| `dataset_datasetSize` | `28000` (item count) | **deprecated** → use `software_artifactSize` (bytes) |

See [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) for the
updated form using `isoAutomationLevel: humanDecisionWithPartialAutomation`
and `software_artifactSize`.

## Profile Conformance

`core`, `ai`, `dataset`

## SPDX Files

| Version | File |
| --------- | ------ |
| SPDX 3.0.1 | [spdx3.0/example05.spdx3.json](./spdx3.0/example05.spdx3.json) |
| SPDX 3.1 (draft) | [spdx3.1/example05.spdx3.json](./spdx3.1/example05.spdx3.json) |

## Key Properties Demonstrated

| Property | Value / Notes |
| ---------- | --------------- |
| `ai_metric` | mAP50=0.892, mAP50-95=0.741, latency=18ms |
| `ai_metricDecisionThreshold` | confidence=0.75, IoU=0.45 |
| `ai_autonomyType` | `no` (SPDX 3.0, deprecated in 3.1) |
| `dataset_confidentialityLevel` | `amber` (worker imagery) |
| `dataset_hasSensitivePersonalInformation` | `yes` |
