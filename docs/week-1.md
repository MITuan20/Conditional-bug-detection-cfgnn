# Weekly Log – Week 1
## Milestone: Establish Transformer Baselines (CodeBERT & CodeT5)

### 1. Objectives of the Week
- Implement transformer-based baselines for conditional bug detection.
- Train CodeBERT and CodeT5 models on the reduced dataset.
- Obtain quantitative evaluation metrics for comparison with CFGNN-based approaches.

---

### 2. Completed Tasks

#### 2.1 CodeBERT Baseline
- Implemented fine-tuning pipeline using HuggingFace Transformers.
- Trained `microsoft/codebert-base` on reduced dataset.
- Evaluated model on test set.
- Recorded Precision, Recall, F1-score, and Accuracy.
- Committed implementation and results to repository.

#### 2.2 CodeT5 Baseline
- Implemented fine-tuning using `Salesforce/codet5-base`.
- Used same dataset split and preprocessing pipeline as CodeBERT.
- Conducted training and evaluation on Kaggle GPU.
- Stored final evaluation metrics for comparison.
- Committed implementation and documentation.

---

### 3. Experimental Setup

- Platform: Kaggle
- GPU: Tesla T4
- Dataset: Reduced subset of original dataset (hardware constrained)
- Task: Binary classification (conditional bug detection)

---

### 6. Next Week Plan

- Reproduce original CFGNN model using the reduced dataset.
- Compare original CFGNN performance against transformer baselines.
- Improve CFGNN versions.