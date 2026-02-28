# CodeT5 Baseline (Kaggle Implementation)

This notebook contains the Kaggle-based implementation of CodeT5
used to establish a transformer-based baseline for conditional bug detection.

## Model
- Model name: Salesforce/codet5-base
- Architecture: Encoder-Decoder Transformer
- Pretrained on source code data

## Environment
- Platform: Kaggle
- GPU: Tesla T4 (or Kaggle default GPU)
- Framework: PyTorch + HuggingFace Transformers

## Dataset
- Reduced dataset derived from the original author dataset
- Dataset size adjusted due to hardware constraints
- Same dataset split used for CodeBERT baseline

## Purpose
This model serves as a transformer-based baseline to compare against:
- CodeBERT baseline
- Original CFGNN
- Improved CFGNN versions

## Notes
This notebook reflects the exact training process used to generate
the reported baseline results under constrained computational resources.