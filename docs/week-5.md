# Weekly Log – Week 5

## Milestone: Integrating Graph Frameworks and Exploring Pretrained Code Representations

### 1. Objectives of the Week

The objective of this week was to further improve the CFGNN model by
enhancing the graph propagation mechanism and exploring more powerful
representations for source code nodes.

Two main directions were explored:

* Optimizing the CFG propagation implementation using a graph neural
  network framework.
* Investigating the use of pretrained code models to replace the
  manually constructed vocabulary used for node tokenization.

---

### 2. Completed Tasks

#### 2.1 Implementing CFGNN with PyTorch Geometric

To improve computational efficiency and scalability, the CFG propagation
module was reimplemented using **PyTorch Geometric**.

Main changes:

* Introduced the **PyTorch Geometric** library into the project.
* Implemented a new propagation module `CFGPropagationPyG`.
* Replaced manual message passing with the `GATConv` layer.
* Converted batched CFG graphs into a flattened node representation
  suitable for PyTorch Geometric.

In this approach, nodes from all graphs in a batch are merged into a
single node tensor, while edges are represented using a sparse
`edge_index` structure.

This change eliminates inefficient Python loops used in previous
versions and allows the model to utilize optimized graph operations
provided by the framework.

---

#### 2.2 Experimenting with Pretrained Code Representations

Another experiment conducted this week focused on replacing the
manually constructed vocabulary used for tokenizing node text.

Previously, node text was converted into token IDs using a manually
built vocabulary derived from the dataset. To improve semantic
representation, an alternative approach was explored using a
**pretrained code model (CodeT5)**.

In this experiment:

* Node text was tokenized using the **CodeT5 tokenizer**.
* The tokenized sequences were used as input representations for CFG
  nodes instead of the manually constructed vocabulary.
* The goal was to leverage pretrained code representations to capture
  richer semantic information from source code.

---

### 3. Experimental Challenges

During experimentation with CodeT5-based representations, a major
challenge was encountered related to computational cost.

Training with CodeT5 tokenization significantly increased the training
time. In multiple runs on Kaggle, the training process exceeded the
platform's execution limits.

As a result:

* Training runs often lasted **more than 12 hours**.
* The Kaggle runtime was terminated before the experiments could finish.

Due to these limitations, it was not possible to obtain complete
experimental results for this approach within the available computing
resources.

---

### 4. Dataset

The experiments were conducted using the **reduced dataset derived from the
original dataset** used by the author. This dataset was previously created
during the preprocessing stage to ensure compatibility with the available
computational resources.

---

### 5. Key Outcome

At the end of this week:

* The **CFGNN + PyTorch Geometric GAT** version was successfully
  implemented and integrated into the experimental pipeline.
* Initial attempts to incorporate **CodeT5-based node representations**
  were conducted, but training constraints prevented full evaluation.

These experiments provide valuable insights for future improvements,
particularly regarding the trade-off between representation quality
and computational efficiency.

---
