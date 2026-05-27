# Weekly Log – Week 10

## Milestone: Repository Refinement and Additional Ablation Experiments

### 1. Objectives of the Week

The objective of this week was to:

- Refine and reorganize the project repository structure.
- Improve documentation and running instructions.
- Continue conducting ablation experiments on the CFGNN-Attn architecture.

---

### 2. Completed Tasks

During this week, the following tasks were completed:

- Added and organized preprocessing-related files.
- Integrated the Spoon-based preprocessing component into the repository.
- Added dataset preparation scripts and raw dataset files.
- Updated project documentation and running instructions.
- Cleaned the repository structure by removing unnecessary preprocessing files from the project root.
- Conducted an additional ablation experiment by replacing attention pooling with mean pooling.

---

### 3. Experimental Details

An additional experiment was conducted to evaluate the contribution of
the attention pooling mechanism in CFGNN-Attn.

Main modification:

- Replaced attention pooling with mean pooling while keeping:
  - GAT-based CFG propagation
  - BiLSTM
  - BPE-based node representation
  - Node role embeddings

The experiment was designed to analyze whether attention-based graph
aggregation provides meaningful benefits over simpler pooling methods.

---

### 4. Key Outcome

At the end of this week:

- The repository structure became more organized and reproducible.
- Documentation and preprocessing instructions were significantly improved.
- Additional ablation analysis on the attention mechanism was completed.

These improvements strengthen both the experimental pipeline and the
overall research reproducibility of the project.

---