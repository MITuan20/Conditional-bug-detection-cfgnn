# CodeBERT Baseline Results

## Environment
- Platform: Kaggle
- GPU: Tesla T4
- Model: microsoft/codebert-base
- Dataset: Reduced dataset (hardware-constrained subset)

## Hyperparameters
- Max length: 192
- Batch size: 32
- Learning rate: 2e-5
- Epochs: 5
- Seed: 42

## Test Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7745  |
| Precision | 0.2683  |
| Recall    | 0.4653  |
| F1-score  | 0.3403  |

## Notes
This baseline serves as a transformer-based comparison
against CFGNN-based approaches.