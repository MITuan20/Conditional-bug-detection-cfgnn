# Weekly Log – Week 7

## Milestone: Exploring GNN Backbones and Improving Node Representation

### 1. Objectives of the Week

The objective of this week was to further improve the CFGNN model by:

- Comparing different **GNN backbones** for CFG propagation.
- Enhancing node representation using **subword-based tokenization (BPE)**.

---

### 2. Completed Tasks

During this week, two main experimental directions were conducted:

- **Experiment 11 — CFGNN + GNN Backbone Comparison**
- **Experiment 12 — CFGNN + BPE-based Node Tokenization**

These experiments focus on both **model architecture** and **input representation**.

---

### 3. Experimental Details

- Conducted a controlled comparison between **GraphSAGE, GCN, and TransformerConv**.
- Identified performance differences across GNN backbones under the same setup.
- Implemented a **BPE tokenizer** to replace the manually constructed vocabulary.
- Converted node text into **subword token IDs** for better semantic representation.

---

### 4. Experimental Challenges

- Different GNN backbones showed varying performance, requiring careful comparison.
- BPE-based tokenization increased preprocessing complexity and required additional training steps.
- Trade-offs observed between **precision and recall** when changing representation methods.

---

### 5. Dataset

All experiments were conducted using the **preprocessed dataset derived from the original dataset**, with CFG structures and labeled conditional statements.

---

### 6. Key Outcome

At the end of this week:

- A comparative analysis of **GNN backbones** was completed.
- The **Transformer-based propagation** showed the best F1-score among tested variants.
- The **BPE-based representation** significantly improved recall and overall F1-score.
- The experimental pipeline now supports both **architecture-level** and **representation-level** improvements.

These results provide important insights for selecting the final model configuration in the next stage.