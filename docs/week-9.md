# Weekly Log – Week 9

## Milestone: Backbone Comparison and Sensitivity Analysis for CFGNN-Attn

### 1. Objectives of the Week

The objective of this week was to further analyze and optimize the
CFGNN-Attn architecture through:

- Comparing multiple GNN backbones
- Conducting sensitivity analysis on important hyperparameters
- Evaluating the contribution of the BiLSTM component

---

### 2. Completed Tasks

During this week, the following experiments were conducted:

- **Experiment 13 — CFGNN-Attn + BPE + GNN Backbone Comparison**
- **Experiment 14 — CFGNN-Attn + Max Node Sensitivity Analysis**
- **Experiment 15 — CFGNN-Attn + GAT Heads Sensitivity Analysis**
- **Experiment 16 — CFGNN without BiLSTM**

---

### 3. Experimental Details

#### 3.1 GNN Backbone Comparison

Different graph neural network backbones were evaluated under the same
CFGNN-Attn framework using BPE-based node representation.

Tested models:

- GraphSAGE
- GCN
- TransformerConv

The comparison focused on understanding how different graph propagation
mechanisms affect conditional bug detection performance.

---

#### 3.2 Max Node Sensitivity Analysis

Experiments were conducted with multiple `max_node` settings to analyze
the impact of CFG size on model performance.

Tested values:

- 150
- 200
- 250
- 350
- 400

This analysis helps determine the trade-off between preserving CFG
information and computational efficiency.

---

#### 3.3 GAT Heads Sensitivity Analysis

Different numbers of GAT attention heads were evaluated to study how
multi-head attention influences graph message passing.

Tested values:

- 2
- 4
- 8
- 16
- 32

---

#### 3.4 Removing the BiLSTM Layer

An ablation experiment was conducted by removing the BiLSTM layer from
the architecture.

The purpose of this experiment was to evaluate whether graph-based
message passing alone is sufficient without additional sequential
modeling.

---

### 4. Key Outcomes

At the end of this week:

- TransformerConv achieved the best F1-score among tested GNN backbones.
- Larger `max_node` settings generally improved overall performance.
- Increasing the number of GAT heads improved model stability and precision.
- Removing BiLSTM reduced performance, indicating that sequential
  modeling still contributes useful contextual information.

These experiments provide important insights into both architectural
design choices and hyperparameter selection for the proposed CFGNN-Attn model.