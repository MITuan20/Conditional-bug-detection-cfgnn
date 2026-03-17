# CFGNN Experiments

This file records all experiments conducted for improving the CFGNN model
for conditional bug detection.

Dataset used in these experiments:
- Source: Reduced dataset derived from the original dataset
- Class distribution: Highly imbalanced (Bug : Normal ≈ 1 : 7)

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-score

---

# Experiment 1 — CFGNN

## Description
First implementation of CFGNN.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7509 |
| Precision | 0.2630 |
| Recall    | 0.2337 |
| F1-score  | 0.2926 |

---

# Experiment 2 — CFGNN + Custom CFG Propagation

## Description
This experiment introduces a custom CFG propagation module to improve
information aggregation across control flow graph nodes.

Main changes:
- Implemented a new `CFGPropagation` module.
- Node embeddings are aggregated from incoming neighbors using
  mean aggregation.
- A linear transformation is applied to the aggregated representation.
- Residual connections are used to stabilize training.

Propagation mechanism:

1. For each CFG edge `(u → v)`, the embedding of node `u` contributes to node `v`.
2. Neighbor embeddings are averaged using degree normalization.
3. A linear transformation is applied to the aggregated features.
4. Residual connection with the original node embedding is applied.

This version still uses a **manual CFG message passing implementation**
without external graph libraries.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7789 |
| Precision | 0.2642 |
| Recall    | 0.3287 |
| F1-score  | 0.2930 |

---