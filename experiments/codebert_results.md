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
| Accuracy  | 0.7395  |
| Precision | 0.2482  |
| Recall    | 0.5344  |
| F1-score  | 0.3390  |

## Notes
This baseline serves as a transformer-based comparison
against CFGNN-based approaches.