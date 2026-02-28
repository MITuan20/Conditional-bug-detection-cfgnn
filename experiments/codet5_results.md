# CodeT5 Baseline Results

## Environment
- Platform: Kaggle
- GPU: Tesla T4
- Model: Salesforce/codet5-base
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
| Accuracy  | 0.7805  |
| Precision | 0.2824  |
| Recall    | 0.4906  |
| F1-score  | 0.3585  |

## Comparison Note
This baseline is used for comparison with:
- CodeBERT baseline
- Original CFGNN
- Improved CFGNN versions