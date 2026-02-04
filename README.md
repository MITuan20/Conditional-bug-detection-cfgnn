# Conditional Bug Detection using CFG-aware Graph Neural Networks

This repository contains the implementation and experimental study for my graduation thesis on detecting bugs related to conditional statements using graph neural networks based on Control Flow Graphs (CFG).

---

## 📌 Research Topic

**Vietnamese**  
Phát hiện lỗi liên quan đến điều kiện bằng mạng nơ-ron đồ thị dựa trên đồ thị luồng điều khiển (CFG).

**English**  
Conditional bug detection using CFG-aware Graph Neural Networks for source code analysis.

---

## 🎯 Motivation

Conditional statements (e.g., `if`, `else`, `while`, `switch`) play a critical role in program logic and are a common source of subtle bugs.  
Traditional sequence-based models often fail to capture control-flow semantics, motivating the use of graph-based representations.

This project explores how **Control Flow Graphs (CFG)** combined with **Graph Neural Networks (GNNs)** can improve bug detection performance, especially under severe class imbalance.

---

## 🧠 Methodology Overview

The proposed approach consists of:

1. Source code preprocessing and CFG construction  
2. Node-level feature engineering (e.g., conditional node types)  
3. CFG-aware Graph Neural Network (CFGNN) for representation learning  
4. Binary classification (buggy vs. non-buggy methods)  
5. Evaluation under imbalanced data settings

Baseline models and comparisons with pretrained code models (e.g., CodeT5) are also included.

---

## 📊 Dataset

- The dataset is **not included** in this repository due to size and license constraints.
- The original dataset exhibits a severe class imbalance (buggy : non-buggy ≈ 1 : 7).
- Preprocessing steps and data handling strategies are documented in the `docs/` directory.

---

## 🧪 Experiments

Experiments are organized by version and method, including:
- Baseline implementations
- Reproduction of original author code under adjusted settings
- CFGNN-based models with incremental improvements

Each experiment includes configuration details, evaluation metrics, and observations.

---

## 📁 Repository Structure

```text
conditional-bug-detection-cfgnn/
├── docs/          # Research notes, methodology, weekly progress
├── baselines/     # Baseline implementations and results
├── notebooks/     # Experimental and exploratory notebooks
├── src/           # Core model and training code
├── experiments/   # Experiment summaries and results
├── data/          # Dataset placeholder (no raw data included)
├── logs/          # Log placeholder (no raw logs included)
└── requirements.txt
