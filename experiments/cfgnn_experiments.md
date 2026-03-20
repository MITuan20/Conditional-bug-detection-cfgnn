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

# Experiment 3 — CFGNN + Graph Attention Propagation

## Description
This experiment extends the CFG propagation mechanism by introducing an
attention-based message passing strategy inspired by Graph Attention Networks (GAT).

Instead of uniformly averaging information from neighboring nodes, the model
learns attention weights to determine the importance of each neighbor during
message passing.

Main changes:
- Added a custom `CFGPropagationGAT` module.
- Introduced attention-based aggregation for CFG nodes.
- Each edge `(u → v)` is assigned an attention score computed from the
  transformed node embeddings.
- Neighbor messages are aggregated using normalized attention weights.
- Residual connections are used to stabilize training.

Propagation process:

1. Node embeddings are first transformed using a linear layer `W`.
2. For each CFG edge `(u → v)`, an attention score is computed:

   e_uv = LeakyReLU(aᵀ [Wh_u || Wh_v])

3. Attention weights are computed using exponential normalization.
4. Neighbor embeddings are aggregated using attention-weighted messages.
5. Residual connection is applied with the original node embeddings.

This version still implements the graph propagation **manually using PyTorch**
without relying on external graph libraries such as PyTorch Geometric.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7337 |
| Precision | 0.2624 |
| Recall    | 0.5073 |
| F1-score  | 0.3459 |

---------