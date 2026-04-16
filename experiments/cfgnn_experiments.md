# CFGNN Experiments

This file records all experiments conducted for improving the CFGNN model
for conditional bug detection.

Dataset used in these experiments:
- Source: Reduced dataset derived from the original dataset
- Class distribution: Highly imbalanced (Bug : Normal ≈ 1 : 7)

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-score

---

# Experiment 1 — CFGNN

## Description
First implementation of CFGNN.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7509 |
| Precision | 0.2630 |
| Recall    | 0.2337 |
| F1-score  | 0.2926 |

---

# Experiment 2 — CFGNN + Custom CFG Propagation

## Description
This experiment introduces a custom CFG propagation module to improve
information aggregation across control flow graph nodes.

Main changes:
- Implemented a new `CFGPropagation` module.
- Node embeddings are aggregated from incoming neighbors using
  mean aggregation.
- A linear transformation is applied to the aggregated representation.
- Residual connections are used to stabilize training.

Propagation mechanism:

1. For each CFG edge `(u → v)`, the embedding of node `u` contributes to node `v`.
2. Neighbor embeddings are averaged using degree normalization.
3. A linear transformation is applied to the aggregated features.
4. Residual connection with the original node embedding is applied.

This version still uses a **manual CFG message passing implementation**
without external graph libraries.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7789 |
| Precision | 0.2642 |
| Recall    | 0.3287 |
| F1-score  | 0.2930 |

---

# Experiment 3 — CFGNN + Graph Attention Propagation

## Description
This experiment extends the CFG propagation mechanism by introducing an
attention-based message passing strategy inspired by Graph Attention Networks (GAT).

Instead of uniformly averaging information from neighboring nodes, the model
learns attention weights to determine the importance of each neighbor during
message passing.

Main changes:
- Added a custom `CFGPropagationGAT` module.
- Introduced attention-based aggregation for CFG nodes.
- Each edge `(u → v)` is assigned an attention score computed from the
  transformed node embeddings.
- Neighbor messages are aggregated using normalized attention weights.
- Residual connections are used to stabilize training.

Propagation process:

1. Node embeddings are first transformed using a linear layer `W`.
2. For each CFG edge `(u → v)`, an attention score is computed:

   e_uv = LeakyReLU(aᵀ [Wh_u || Wh_v])

3. Attention weights are computed using exponential normalization.
4. Neighbor embeddings are aggregated using attention-weighted messages.
5. Residual connection is applied with the original node embeddings.

This version still implements the graph propagation **manually using PyTorch**
without relying on external graph libraries such as PyTorch Geometric.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7337 |
| Precision | 0.2624 |
| Recall    | 0.5073 |
| F1-score  | 0.3459 |

---------

# Experiment 4 — CFGNN + PyTorch Geometric GAT

## Description
This experiment replaces the manual graph propagation implementation with
a Graph Attention Network layer provided by PyTorch Geometric.

Instead of iterating through CFG edges using Python loops, this version
uses the `GATConv` layer from PyTorch Geometric to perform attention-based
message passing more efficiently.

Main changes:
- Introduced the PyTorch Geometric library.
- Implemented a new `CFGPropagationPyG` module using `GATConv`.
- Converted CFG graphs in a batch into a flattened node representation.
- Constructed a unified `edge_index` representation for all graphs in the batch.
- Residual connections are used to stabilize training.

Propagation process:

1. Nodes from all graphs in the batch are flattened into a single tensor:

   x ∈ R^(B*N × D)

   where B is the batch size and N is the maximum number of nodes.

2. CFG edges from each sample are merged into a single sparse edge list
   with index offsets applied to maintain graph structure.

3. Message passing is performed using the `GATConv` layer.

4. Residual connections are applied to combine propagated features with
   the original node embeddings.

This version improves computational efficiency and aligns the implementation
with standard graph neural network frameworks.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7834 |
| Precision | 0.3034 |
| Recall    | 0.4326 |
| F1-score  | 0.3566 |

----------

# Experiment 5 — CFGNN + PyTorch Geometric GAT + Focal Loss

## Description
This experiment focuses on improving the model's performance on the
imbalanced dataset by replacing the standard cross-entropy loss with
**Focal Loss**.

The dataset used in this project is highly imbalanced, where the number
of normal samples is significantly larger than the number of bug samples.
In such cases, standard cross-entropy loss often causes the model to bias
toward the majority class.

To address this issue, **Focal Loss** was introduced to emphasize
difficult and misclassified samples during training.

Main changes:
- Implemented a custom `FocalLoss` module.
- Replaced the standard `CrossEntropyLoss` with `FocalLoss`.
- Applied class balancing using parameter `alpha`.
- Used focusing parameter `gamma` to concentrate learning on difficult samples.

Loss configuration used in this experiment:

   criterion = FocalLoss(alpha=0.4, gamma=2.0).to(device)


### Focal Loss Mechanism

Focal Loss modifies the standard cross-entropy loss by introducing a
modulating factor that reduces the contribution of easy samples and
focuses training on hard examples.

The loss function is defined as:

   FL(p_t) = alpha * (1 - p_t)^gamma * CE

Where:

- `p_t` is the predicted probability of the true class
- `alpha` balances the importance of the minority class
- `gamma` controls how strongly the model focuses on misclassified samples

In this experiment:

- `alpha = 0.4`
- `gamma = 2.0`

These settings were chosen to help the model pay more attention to
difficult bug samples while reducing the dominance of the majority class.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.8519 |
| Precision | 0.4373 |
| Recall    | 0.2336 |
| F1-score  | 0.3045 |

------

# Experiment 6 — CFGNN + Node Role Embedding

## Description
This experiment focuses on improving node representation by introducing
a more fine-grained **node role annotation** during the preprocessing stage.

In previous versions, nodes were annotated using a simple binary
indicator that only detected whether the node contained an API call.
This representation was limited and could not distinguish between
different types of control flow statements.

To address this limitation, the preprocessing pipeline was modified to
assign **semantic roles** to each node based on the type of statement
appearing in the source code.

These roles provide additional structural information that may help the
model better understand the behavior of nodes within the control flow graph.

Main changes:
- Replaced the previous binary annotation with **multi-class node roles**.
- Introduced **six semantic node categories** based on code structure.
- Modified the model to support multi-type node embeddings.
- Updated the node type embedding layer from:

   self.type_emb = nn.Embedding(2, D)

to

   self.type_emb = nn.Embedding(7, D)

This change allows the model to learn richer representations for
different types of CFG nodes.

### Node Role Categories

Each node in the CFG is assigned one of the following roles:

| Role ID | Description |
|--------|-------------|
| 1 | BEGIN / EXIT node |
| 2 | Conditional statements (`if`, `else`, `switch`, `case`) |
| 3 | Loop statements (`for`, `while`, `do`) |
| 4 | Control transfer statements (`return`, `throw`, `break`, `continue`) |
| 5 | API or method call |
| 6 | Normal statements (assignments or declarations) |

These role labels are generated during preprocessing and provided to the
model as additional node features.

### Reasons

By distinguishing between different types of code statements, the model
can better capture the structural semantics of the control flow graph.
For example:

- Conditional nodes often determine different execution paths.
- Loop nodes indicate repeated execution.
- Control transfer statements may terminate or redirect execution flow.

Providing explicit role information may help the model learn more
meaningful representations of program structure.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.859  |
| Precision | 0.4793 |
| Recall    | 0.1870 |
| F1-score  | 0.2690 |

---

# Experiment 7 — CFGNN + Tuned Focal Loss + Dynamic Threshold

## Description
This experiment improves performance on the imbalanced dataset by
adjusting the **Focal Loss parameters** and introducing **dynamic
threshold selection** during evaluation.

Instead of using a fixed prediction threshold (0.5), the optimal
threshold is selected from the **precision–recall curve** based on
the maximum F1-score.

Main changes:
- Updated Focal Loss parameters.
- Added dynamic threshold selection during validation.
- Selected the threshold that maximizes the validation F1-score.

Loss configuration:

   criterion = FocalLoss(alpha=0.6, gamma=2.0)


### Threshold Optimization

The optimal threshold is determined using the precision–recall curve:

   precisions, recalls, thresholds = precision_recall_curve(labels, probs)
   f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-8)
   best_idx = np.argmax(f1_scores)
   best_threshold = thresholds[best_idx]


Final predictions are generated using:

   final_preds = (probs >= best_threshold)


## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.8050 |
| Precision | 0.3059 |
| Recall    | 0.319  |
| F1-score  | 0.3123 |
| Threshold | 0.3847 |

---

# Experiment 8 — CFGNN + Dropout Regularization

## Description

This experiment introduces **Dropout (p = 0.3)** to improve model
generalization and reduce overfitting.

Main changes:

- Added Dropout after **node embedding**, **CFG propagation**, and **BiLSTM**.
- Replaced **Focal Loss** with **weighted CrossEntropyLoss**.
- Removed dynamic threshold selection.
- Added **weight decay (1e-5)** in the optimizer.

## Training Setup

Loss:

   criterion = nn.CrossEntropyLoss(
   weight=torch.tensor([1.0, 7.0]).to(device)
   )


Optimizer:
   
   optimizer = Adam(..., weight_decay=1e-5)


## Results

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.7405 |
| Precision | 0.2692 |
| Recall    | 0.507  |
| F1-score  | 0.3517 |

---

# Experiment 9 — CFGNN + Weight Decay & Class Weight Tuning

## Description

This experiment focuses on improving performance on the imbalanced dataset
by tuning **weight decay** and **class weights** in the loss function.

Instead of changing the model architecture, this version explores how
regularization and class balancing affect the trade-off between
precision and recall.

Main changes:

- Tuned **weight decay** in the optimizer.
- Adjusted **class weights** in `CrossEntropyLoss`.

---

## Configurations

### Setting 1

   weight_decay = 1e-4
   weight = [1.0, 5.0]

## Results

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.7995 |
| Precision | 0.2998 |
| Recall    | 0.3326 |
| F1-score  | 0.3153 |

---

### Setting 2

   weight_decay = 1e-5
   weight = [1.0, 6.0]

## Results

| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.7617 |
| Precision | 0.2849 |
| Recall    | 0.4745 |
| F1-score  | 0.356  |

---

# Experiment 10 — CFGNN + Binary Node Annotation (Revisited)

## Description

This experiment revisits the **binary node annotation strategy**
while keeping all optimized training settings from previous experiments
(e.g., dropout, weight decay, class weights).

Instead of using multi-class node roles, node types are simplified
to a binary indicator based on API calls.

Main changes:

- Replaced **node role embedding** with **binary annotation**:
  - `1`: node contains API/method call
  - `0`: otherwise
- Updated model embedding layer:

   self.type_emb = nn.Embedding(2, D)


- Kept all other configurations unchanged:
  - Dropout
  - Weight decay
  - Class weights

Annotation rule:

   annotation = 1 if re.findall(r'.\s*\w+\s*(', node_text) else 0


## Motivation

This experiment evaluates whether a **simpler node feature**
can achieve competitive performance compared to the more complex
multi-class node role embeddings.

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7872 |
| Precision | 0.3054 |
| Recall    | 0.418  |
| F1-score  | 0.3529 |

---

# Experiment 11 — CFGNN + GNN Backbone Comparison

## Description

This experiment compares different **graph neural network backbones**
for CFG propagation within the CFGNN framework.

Instead of using a single propagation method, three variants were tested:

- **GraphSAGE**
- **GCN**
- **TransformerConv**

All other components and training settings were kept unchanged to ensure
a fair comparison.

---

## Configurations

The following GNN layers were used:

- SAGE: `SAGEConv`
- GCN: `GCNConv`
- Transformer: `TransformerConv`

---

## Results

| Model        | Accuracy | Precision | Recall | F1-score |
|--------------|----------|-----------|--------|----------|
| GraphSAGE    | 0.7903   | 0.3072    | 0.407  | 0.3501   |
| GCN          | 0.7875   | 0.2922    | 0.3732 | 0.3278   |
| Transformer  | 0.781    | 0.3009    | 0.4362 | 0.3561   |

---

# Experiment 12 — CFGNN + BPE-based Node Tokenization

## Description

This experiment improves node text representation by replacing the
manually constructed vocabulary with a **Byte Pair Encoding (BPE) tokenizer**.

Instead of mapping tokens using a fixed vocabulary, node text is
converted into **subword token IDs**, allowing the model to better
capture semantic patterns in source code.

Main changes:

- Trained a **BPE tokenizer** on node text from the training dataset.
- Replaced manual token-to-id mapping with **subword tokenization**.
- Limited each node to a maximum of **20 subword tokens**.
- Kept the existing **node role labels (6 classes)** unchanged.

---

## Tokenization Process

- Tokenizer: BPE (Byte Pair Encoding)
- Vocab size: 50,000
- Pre-tokenization: whitespace-based splitting

Each node is processed as follows:

1. Encode node text into subword tokens.
2. Convert tokens to IDs.
3. Truncate to maximum length (20 tokens per node).

---

## Motivation

The manually built vocabulary may not effectively capture the semantics
of source code, especially for rare or unseen tokens.

Using BPE helps:

- Handle **out-of-vocabulary tokens**
- Capture **subword-level patterns**
- Improve representation of code structure

---

## Results

| Metric    | Value |
|-----------|--------|
| Accuracy  | 0.7346 |
| Precision | 0.2829 |
| Recall    | 0.5943 |
| F1-score  | 0.3833 |
