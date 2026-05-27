# Weekly Log – Week 2

## Milestone: Reproducing the Original CFGNN Model

### 1. Objectives of the Week

The objective of this week was to reproduce the original CFGNN model proposed by the author and evaluate its performance on the reduced dataset used in this project. This step is necessary to establish a graph-based baseline for fair comparison with the improved CFGNN variants that will be developed later.

---

### 2. Completed Tasks

#### 2.1 Preparing the Model Environment

* Studied the original CFGNN implementation and project structure.
* Reviewed dependencies and runtime requirements.
* Adapted the code to ensure compatibility with the Kaggle environment.

#### 2.2 Running the Original CFGNN Model

* Executed the original CFGNN training pipeline using the reduced dataset created in the preprocessing stage.
* Adjusted dataset paths and runtime configurations for Kaggle.
* Ensured that the core architecture and training logic of the original implementation remained unchanged.

#### 2.3 Recording Baseline Results

* Completed training and evaluation of the reproduced CFGNN model.
* Collected evaluation metrics including Precision, Recall, F1-score, and Accuracy.
* Stored the results in the `experiments` directory of the repository.

---

### 3. Experimental Setup

* Platform: Kaggle
* GPU: Tesla T4
* Framework: PyTorch

---

### 4. Dataset

The experiments were conducted on a reduced dataset derived from the original dataset used by the author.
The reduction was necessary due to hardware limitations of the available computing environment.

---

### 5. Key Outcome

The original CFGNN model was successfully reproduced and evaluated on the reduced dataset.
These results will serve as the **graph-based baseline** for comparing future CFGNN improvements developed in this project.

---
