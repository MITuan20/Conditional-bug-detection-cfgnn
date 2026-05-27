# Weekly Log – Week 6

## Milestone: Improving Model Performance and Feature Representation

### 1. Objectives of the Week

The objective of this week was to continue improving the CFGNN model
for detecting buggy conditional statements by focusing on handling
class imbalance and enhancing node feature representation.

Three experimental directions were explored:

- Applying **Focal Loss** to improve learning on imbalanced datasets.
- Introducing **node role embeddings** to enrich CFG node features.
- Improving prediction performance through **dynamic threshold selection** during evaluation.

---

### 2. Completed Tasks

During this week, three experimental versions of the model were implemented:

- **Experiment 5 — CFGNN + PyTorch Geometric GAT + Focal Loss**
- **Experiment 6 — CFGNN + Node Role Embedding**
- **Experiment 7 — CFGNN + Tuned Focal Loss + Dynamic Threshold**

These experiments aim to improve the robustness of the model, enrich node
representations, and optimize prediction decisions for imbalanced data.

---

### 3. Experimental Challenges

Some challenges were encountered during experimentation:

- The dataset remains **highly imbalanced**, which affects model training
  and evaluation.
- Hyperparameters such as **Focal Loss parameters** and prediction thresholds
  require careful tuning.

Further experiments are needed to determine the most effective model configuration.

---

### 4. Dataset

All experiments were conducted using the **preprocessed dataset derived
from the original dataset** used in previous weeks.

The dataset contains control flow graphs extracted from Java methods,
with labels indicating whether a conditional statement is buggy or not.

---

### 5. Key Outcome

At the end of this week:

- Three new experimental model versions were implemented.
- The training and evaluation pipeline was improved to better handle
  imbalanced data.
- Additional node features and evaluation strategies were introduced to
  improve model performance.

These experiments provide a basis for selecting the final model configuration
in the next stage of the project.