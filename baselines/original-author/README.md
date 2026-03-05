# Original CFGNN Baseline (Reproduced)

This implementation reproduces the original CFGNN model proposed by the author
for conditional bug detection.

## Purpose
To reproduce the original model performance under the same dataset
used in this project for fair comparison.

## Notes on Modifications
The original implementation was slightly modified to run on Kaggle:

- Adjusted file paths for Kaggle environment
- Adapted dataset loading to the reduced dataset
- Minor changes to ensure compatibility with Kaggle runtime

The core architecture and training logic remain unchanged.

## Environment
- Platform: Kaggle
- Framework: PyTorch
- GPU: Tesla T4

## Dataset
- Reduced dataset derived from the original dataset
- Reduction applied due to hardware constraints

## Role in Project
This model serves as the **graph-based baseline** and will be compared with:

- Transformer baselines (CodeBERT, CodeT5)
- Improved CFGNN variants proposed in this research

### Spoon-based Data Processing

For AST-level and control-flow analysis, this project uses **Spoon**, following the original implementation provided by the authors.

**Environment requirements (as specified by the original implementation):**
- Apache Maven 3.3.9
- Java 1.8.0_282

**Usage:**
```bash
cd spoon/
mvn compile
mvn exec:java \
  -Dexec.mainClass="fr.inria.controlflow.Main" \
  -Dexec.args="../data/dataset.csv ../data/dataset_final.csv"
