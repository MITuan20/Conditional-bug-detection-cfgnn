# Weekly Log – Week 3

## Milestone: Initial CFGNN Experimental Versions

### 1. Objectives of the Week

The objective of this week was to begin developing experimental versions of the CFGNN model based on the reproduced baseline from Week 2.
These experiments aim to explore potential improvements in the model implementation, training pipeline, and graph processing mechanisms in order to achieve better performance on the reduced dataset.

---

### 2. Completed Tasks

#### 2.1 Implementing the First Experimental CFGNN Version

* Reconstructed the training pipeline to run efficiently in the Kaggle environment.
* Adapted dataset loading and graph construction modules for compatibility with the new implementation.

#### 2.2 Running Experimental Training

* Executed training and evaluation of the first experimental CFGNN version.
* Verified the correctness of the model pipeline including data loading, graph construction, training loop, and evaluation.
* Ensured that the experimental setup remained consistent with the baseline experiments for fair comparison.

#### 2.3 Recording Experiment Results

* Collected evaluation metrics including **Accuracy, Precision, Recall, and F1-score**.
* Documented experiment configurations and results in the `experiments` directory.
* Prepared the experiment tracking file to record results of future CFGNN versions.

---

### 3. Experimental Setup

* Platform: Kaggle
* GPU: Tesla T4
* Framework: PyTorch

---

### 4. Dataset

The experiments continued to use the **reduced dataset** derived from the original dataset used by the author.
This dataset was previously prepared during the preprocessing stage to ensure that experiments could be executed within the available hardware constraints.

---

### 5. Key Outcome

The first experimental version of CFGNN was successfully implemented and trained.
This marks the beginning of the experimental phase of the project, where multiple CFGNN variants will be explored and compared against the established baselines.
