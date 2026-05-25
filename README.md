# Conditional Bug Detection using CFG-aware Graph Neural Networks

This repository contains the implementation and experimental study for my graduation thesis on detecting bugs related to conditional statements using graph neural networks based on Control Flow Graphs (CFG).

---

## Research Topic

**Vietnamese**  
Phát hiện lỗi liên quan đến điều kiện bằng mạng nơ-ron đồ thị dựa trên đồ thị luồng điều khiển (CFG).

**English**  
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
- Due to preprocessing and CFG extraction requirements, additional intermediate CSV files are generated during execution.
- The original dataset exhibits severe class imbalance between buggy and non-buggy samples.

---

## Repository Structure

```text
conditional-bug-detection-cfgnn/
├── baselines/      # Baseline models and comparative results
├── data/           # Contains raw dataset .zip and processed data splits
├── docs/           # weekly-logs, proposal, and methodology
├── experiments/    # Results (baseline models + cfgnn_attn)
├── notebooks/      # Experimental notebooks (ready for Kaggle execution)
│   └── cfgnn_attn_experiments.ipynb
├── spoon/          # Java-based static analysis module for CFG extraction
└── src/            # Core Python scripts for data pipeline & preparation
    ├── data_split.py
    └── prepare.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to run


1. py src/data_split.py
2. py src/prepare.py train 1
3. py src/prepare test 1
4. cd spoon/
mvn compile
5. mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_train.csv ../data/dataset_train_final.csv' exec:java
6. mvn -q -DskipTests '-Dexec.mainClass=fr.inria.controlflow.Main' '-Dexec.args=../data/dataset_test.csv ../data/dataset_test_final.csv' exec:java
7. cd ..
8. py src/prepare.py train 2
9. py src/prepare.py train 3
10. py src/prepare.py test 2


## Model Training & Evaluation

Once the pipeline is complete, upload the processed graph data along with the main notebook to Kaggle:

1. Open notebooks/cfgnn_attn_experiments.ipynb on Kaggle.
2. Enable the Tesla T4 GPU accelerator.
3. Execute the cells to train the CFGNN-Attn model and review results.