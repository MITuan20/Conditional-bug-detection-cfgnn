# Conditional Bug Detection using CFG-aware Graph Neural Networks

This repository contains the implementation and experimental study for my graduation thesis on detecting bugs related to conditional statements using graph neural networks based on Control Flow Graphs (CFG).

---

## Research Topic

### Vietnamese
Phát hiện lỗi liên quan đến điều kiện bằng mạng nơ-ron đồ thị dựa trên đồ thị luồng điều khiển (CFG).

### English
Conditional bug detection using CFG-aware Graph Neural Networks for source code analysis.

---

## Motivation

Conditional statements (e.g., `if`, `else`, `while`, `switch`) play a critical role in program logic and are a common source of subtle bugs.

Traditional sequence-based models often fail to capture control-flow semantics, motivating the use of graph-based representations.

This project explores how **Control Flow Graphs (CFG)** combined with **Graph Neural Networks (GNNs)** can improve bug detection performance, especially under severe class imbalance.

---

## Dataset

- The original dataset from the referenced paper is included in the `data/` directory as compressed `.zip` files.
- The uploaded dataset is the raw dataset before preprocessing.
- Additional intermediate CSV files are generated during preprocessing and CFG extraction.
- The dataset is highly imbalanced between buggy and non-buggy samples.

---

## Repository Structure

```text
conditional-bug-detection-cfgnn/
├── baselines/      # Baseline models and comparative results
├── data/           # Raw dataset and processed CSV files
├── docs/           # Weekly logs, proposal, methodology
├── experiments/    # Experimental results
├── notebooks/      # Kaggle-ready notebooks
│   └── cfgnn_attn_experiments.ipynb
├── spoon/          # Java CFG extraction module
└── src/            # Python preprocessing pipeline
    ├── data_split.py
    └── prepare.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Environment Setup

## 1. Clone Repository

```bash
git clone https://github.com/MITuan20/Conditional-bug-detection-cfgnn.git
cd Conditional-bug-detection-cfgnn
```

---

## 2. Create Python Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Local Python Dependencies

The local preprocessing pipeline requires only lightweight dependencies:

```bash
pip install -r requirements.txt
```

This step is required for:
- `src/data_split.py`
- `src/prepare.py`

Model training is performed separately on Kaggle using the provided notebook environment.

---

## 4. Install Java & Maven

CFG extraction requires:

- Spoon Core 8.4.0-beta-6
- Java JDK 8+ (recommended)
- Apache Maven

Check installation:

```bash
java -version
mvn -version
```

---

## How to run

``` bash
1. `py src/data_split.py`
2. `py src/prepare.py train 1`
3. `py src/prepare test 1`
4. `cd spoon/`
`mvn compile`
5. `mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_train.csv ../data/dataset_train_final.csv' exec:java`
6. `mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_test.csv ../data/dataset_test_final.csv' exec:java`
7. `cd ..`
8. `py src/prepare.py train 2`
9. `py src/prepare.py train 3`
10. `py src/prepare.py test 2`
```
``` bash
1. `py src/data_split.py`
2. `py src/prepare.py train 1`
3. `py src/prepare test 1`
4. `cd spoon/`
`mvn compile`
5. `mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_train.csv ../data/dataset_train_final.csv' exec:java`
6. `mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_test.csv ../data/dataset_test_final.csv' exec:java`
7. `cd ..`
8. `py src/prepare.py train 2`
9. `py src/prepare.py train 3`
10. `py src/prepare.py test 2`
```

## Model Training & Evaluation

Once the pipeline is complete, upload the processed graph data along with the main notebook to Kaggle:

1. Open notebooks/cfgnn_attn_experiments.ipynb on Kaggle.
2. Enable the Tesla T4 GPU accelerator.
3. Execute the cells to train the CFGNN-Attn model and review results.

## Kaggle Environment

Training experiments were conducted on Kaggle using:
- Tesla T4 GPU
- PyTorch (preinstalled in Kaggle)
- torch-geometric

## Kaggle Environment

Training experiments were conducted on Kaggle using:
- Tesla T4 GPU
- PyTorch (preinstalled in Kaggle)
- torch-geometric