# LightShift-PatchCore

### Robust Industrial Anomaly Detection Under Lighting Distribution Shifts

Investigating lightweight adaptation strategies for PatchCore using feature-statistics alignment and conformal threshold calibration.

---

## Overview

Industrial anomaly detection systems are often deployed in environments where illumination conditions change due to lamp aging, different production stations, or environmental variations.

Although PatchCore achieves strong performance under reference conditions, changes in lighting can affect feature representations, anomaly scores, and detection thresholds.

**LightShift-PatchCore** investigates the robustness of PatchCore under photometric distribution shifts, with a particular focus on distinguishing between:

- **Ranking degradation:** Whether defective products can still be distinguished from normal products.
- **Calibration degradation:** Whether the original anomaly detection threshold remains reliable under new lighting conditions.

The objective is to investigate lightweight adaptation strategies that improve detection reliability without requiring model retraining.

## Research Objectives

- Analyze the impact of illumination changes on PatchCore feature representations.
- Investigate the relationship between feature-statistics drift and detection performance.
- Evaluate feature-statistics alignment under changing lighting conditions.
- Apply conformal prediction to recalibrate anomaly detection thresholds.
- Study how the number of available normal target-domain images affects performance.
- Measure computational overhead and deployment feasibility.

## Proposed Methodology

The research investigates four complementary components:

| Component | Description |
|---|---|
| **B1 – Invariant Memory Bank** | Build a memory bank using photometric augmentations while maintaining a fixed coreset budget. |
| **B2 – Feature Statistics Alignment** | Align test feature statistics with reference statistics through channel-wise normalization or covariance alignment. |
| **B3 – Conformal Threshold Calibration** | Calibrate anomaly detection thresholds using normal target-domain calibration images. |
| **B4 – Learned Adapter (Optional)** | Investigate a lightweight residual adapter trained using photometric consistency. |

The primary research direction focuses on combining **B2 + B3**. Components B1 and B4 will be investigated through additional experiments.

## Datasets

The experimental evaluation will consider:

- **MVTec AD:** Primary benchmark for industrial anomaly detection and controlled synthetic lighting shifts.
- **MVTec AD 2:** External validation under real-world illumination variations.
- **VisA (Optional):** Additional evaluation of generalization across industrial object categories.

Datasets will not be distributed through this repository. Users must obtain them from their official sources and comply with the applicable licenses and usage restrictions.

## Experimental Evaluation

### Image-Level Metrics
- AUROC
- Average Precision (AP)
- F1-score
- False Positive Rate (FPR)

### Pixel-Level Metrics
- AU-PRO
- Pixel-level AUROC

### System-Level Metrics
- Median inference latency
- 95th percentile latency (p95)
- Memory bank size
- Calibration time

### Experimental Comparisons

- Vanilla PatchCore
- PatchCore + B1
- PatchCore + B2
- PatchCore + B3
- PatchCore + B2 + B3
- PatchCore + B1 + B2 + B3
- Optional learned adapter (B4)
- Selected alternative anomaly detection methods

Ablation studies will examine feature layers, coreset size, photometric augmentations, and the number of target-domain calibration images.

## Proposed Architecture

```text
         Industrial Images
                 |
                 v
      Photometric Shift Generation
                 |
                 v
          Feature Extraction
                 |
                 v
       Memory Bank + Coreset
                 |
                 v
      Feature Statistics Alignment
                 |
                 v
      Nearest Neighbor Scoring
                 |
                 v
     Conformal Threshold Calibration
                 |
                 v
       Anomaly Maps + Decisions
                 |
                 v
         FastAPI + Dashboard
```

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Computer Vision | Torchvision, OpenCV |
| Anomaly Detection | PatchCore |
| Backend | FastAPI |
| Experiment Tracking | MLflow |
| Containerization | Docker |
| Testing | Pytest |
| Version Control | Git, GitHub |

The frontend technology will be selected during implementation.

## Planned API

| Endpoint | Description |
|---|---|
| `GET /health` | Check service availability |
| `POST /predict` | Generate anomaly predictions |
| `POST /calibrate` | Calibrate thresholds using normal target-domain images |
| `GET /metrics` | Retrieve system metrics |

## Reproducibility

The project will follow a reproducible experimental protocol:

- Fixed random seeds.
- Documented dataset splits.
- Controlled photometric transformations.
- Consistent memory-bank and coreset budgets.
- Multiple experimental runs.
- Bootstrap confidence intervals.
- Separation of calibration, validation, and test data.
- Documented configurations and experimental results.

Conformal calibration guarantees will be evaluated under their exchangeability assumptions. They will not be treated as guarantees under arbitrary distribution shifts.

## Project Status

**Current phase:** Research preparation and implementation planning.

- [ ] Literature review
- [ ] Dataset preparation
- [ ] Synthetic lighting-shift generation
- [ ] Vanilla PatchCore reproduction
- [ ] Feature-statistics alignment (B2)
- [ ] Conformal threshold calibration (B3)
- [ ] Invariant memory bank (B1)
- [ ] Experimental evaluation and ablation studies
- [ ] External validation
- [ ] FastAPI implementation
- [ ] Web dashboard
- [ ] Docker integration
- [ ] Final research report

## Repository Structure

The repository structure will evolve as implementation progresses.

```text
lightshift-patchcore/
├── README.md
├── .gitignore
├── configs/
├── data/
├── docs/
├── experiments/
├── notebooks/
├── scripts/
├── src/
│   └── lightshift/
├── tests/
├── api/
└── dashboard/
```

## Scientific Scope

The project investigates whether combining feature-statistics alignment and conformal threshold calibration can improve industrial anomaly detection under photometric distribution shifts.

The contribution, performance improvements, and limitations will be established through experiments rather than assumed in advance.

## References

- Roth et al. — Towards Total Recall in Industrial Anomaly Detection (PatchCore), CVPR 2022.
- MVTec AD — Industrial Anomaly Detection Dataset.
- MVTec AD 2 — Industrial Anomaly Detection under Real-World Lighting Variations.
- Li et al. — Adaptive Batch Normalization (AdaBN), 2016.
- Sun et al. — Deep CORAL, 2016.
- Angelopoulos & Bates — A Gentle Introduction to Conformal Prediction.

## License

No open-source license has currently been assigned to this repository. All rights are reserved unless and until an appropriate license is added.

Dataset licenses and institutional intellectual-property requirements must be respected independently of this repository's licensing status.
