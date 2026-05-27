# Weekly Log – Week 4

## Milestone: Improving CFGNN Propagation Mechanisms

### 1. Objectives of the Week

The objective of this week was to explore improvements to the message passing
mechanism of the CFGNN model. Building upon the reproduced baseline from the
previous weeks, this stage focuses on modifying how information is propagated
between nodes in the control flow graph (CFG).

Two experimental propagation strategies were investigated:

* a custom mean-based CFG propagation mechanism
* an attention-based propagation mechanism inspired by Graph Attention Networks (GAT)

The goal was to evaluate whether these changes could improve the model's ability
to capture relationships between nodes in the control flow graph.

---

### 2. Completed Tasks

#### 2.1 Implementing Custom CFG Propagation

* Implemented a new propagation module named `CFGPropagation`.
* Designed a message passing mechanism where each node aggregates information
  from its incoming neighbors using **mean aggregation**.
* Applied a linear transformation to the aggregated features.
* Added **residual connections** to maintain stability during training.

This experiment aimed to improve the baseline CFGNN propagation mechanism while
keeping the implementation lightweight and fully controllable in PyTorch.

#### 2.2 Implementing Attention-Based CFG Propagation

* Developed an additional propagation module named `CFGPropagationGAT`.
* Introduced an **attention mechanism** to learn the importance of neighboring
  nodes during message passing.
* Computed attention scores between node pairs using transformed node embeddings.
* Aggregated neighbor information using attention-weighted message passing.

This experiment was designed to investigate whether attention-based propagation
could better capture important control-flow relationships in the CFG.

#### 2.3 Running Experimental Training

* Trained and evaluated both experimental versions of the CFGNN model.
* Maintained consistent dataset and training settings to ensure fair comparison
  with previous experiments.
* Recorded evaluation metrics including **Accuracy, Precision, Recall, and F1-score**.

All experiment results were documented in the repository under the
`experiments/cfgnn_experiments.md` file.

---

### 3. Experimental Setup

* Platform: Kaggle
* GPU: Tesla T4
* Framework: PyTorch

---

### 4. Dataset

The experiments were conducted using the **reduced dataset derived from the
original dataset** used by the author. This dataset was previously created
during the preprocessing stage to ensure compatibility with the available
computational resources.

---

### 5. Key Outcome

Two improved CFGNN variants were successfully implemented and evaluated:

* CFGNN with **custom mean-based propagation**
* CFGNN with **attention-based propagation**

The attention-based propagation showed improved recall and F1-score compared
to previous experiments, indicating that attention mechanisms may help capture
important control-flow relationships between nodes.

These results provide useful insights for further improvements in the CFGNN
architecture in the next stages of the project.

---
