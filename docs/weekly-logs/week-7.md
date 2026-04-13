# Weekly Log – Week 7

## Milestone: Regularization and Feature Simplification

### 1. Objectives of the Week

The objective of this week was to improve the CFGNN model by:

- Enhancing **generalization** through regularization techniques.
- Tuning **training hyperparameters** for imbalanced data.
- Evaluating the impact of **simplifying node features**.

---

### 2. Completed Tasks

During this week, three experimental versions were implemented:

- **Experiment 8 — CFGNN + Dropout Regularization**
- **Experiment 9 — CFGNN + Weight Decay & Class Weight Tuning**
- **Experiment 10 — CFGNN + Binary Node Annotation (Revisited)**

These experiments focus on improving model robustness, optimizing training
configuration, and comparing feature representation strategies.

---

### 3. Experimental Highlights

- Introduced **Dropout** to reduce overfitting and improve generalization.
- Explored different combinations of **weight decay** and **class weights**
  to handle class imbalance.
- Evaluated the trade-off between **precision and recall** across configurations.
- Simplified node representation from **multi-class roles** to **binary annotation**
  and updated the model accordingly.

---

### 4. Experimental Challenges

- The dataset remains **highly imbalanced**, making it difficult to balance
  precision and recall.
- Hyperparameter tuning (weight decay, class weights) significantly affects
  model performance and requires careful experimentation.

---

### 5. Dataset

All experiments were conducted on the **preprocessed dataset derived from
the original dataset**, consistent with previous weeks.

---

### 6. Key Outcome

At the end of this week:

- The model achieved improved **F1-score stability** through regularization
  and hyperparameter tuning.
- The best-performing configuration showed a better balance between
  precision and recall.
- A comparison between **complex node roles** and **binary annotation**
  was conducted, providing insights into feature design.

These results help guide the selection of the final model configuration
for subsequent experiments and evaluation.