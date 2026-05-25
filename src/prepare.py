import pandas as pd
from itertools import chain
from tqdm import tqdm
import sys
import ast


# covert raw data
def position(row):
    method, bugs, normals = row['method'], row['bugs'], row['normals']
    items = []

    bugs = ast.literal_eval(bugs)
    normals = ast.literal_eval(normals)

    for bug in bugs:
        items.append({
            "id": row.name,
            "method": method,
            "target": bug,
            "label": 1
        })

    for normal in normals:
        items.append({
            "id": row.name,
            "method": method,
            "target": normal,
            "label": 0
        })

    return items


def convert_data(input_csv, output_csv):
    print(f"[Convert] {input_csv} → {output_csv}")
    all_data = pd.read_csv(input_csv)
    data = all_data.apply(lambda x: position(x), axis=1)
    data = list(chain.from_iterable(data))
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)

# Remove duplicates & resampling
def remove_duplicates_and_sample(input_csv, output_csv):
    print(f"[Clean] {input_csv} → {output_csv}")

    csv_data = pd.read_csv(input_csv, chunksize=1000)
    chunks = []
    for chunk in csv_data:
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)

    # Remove duplicates
    df.drop_duplicates(
        subset=['method', 'cfg', 'target', 'node'],
        inplace=True
    )

    # Sampling: keep all buggy, sample 1 non-buggy per method
    data = []
    groups = df.groupby('method', sort=False)

    for _, group in tqdm(groups, desc="Sampling by method"):
        buggy = group[group['label'] == 1]
        non_buggy = group[group['label'] == 0]

        if len(buggy) > 0:
            data.append(buggy)
        if len(non_buggy) > 0:
            data.append(non_buggy.sample(n=1, random_state=3))

    data = pd.concat(data, ignore_index=True)
    data.to_csv(output_csv, index=False)


# Split train/valid
def split_train_valid(input_csv, train_csv, valid_csv, ratio=0.8):
    print(f"[Split] {input_csv} → train / valid")

    csv_data = pd.read_csv(input_csv, chunksize=1000)
    chunks = []
    for chunk in csv_data:
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)

    # Shuffle
    df = df.sample(frac=1, random_state=3).reset_index(drop=True)

    total = len(df)
    train_size = int(total * ratio)

    train = df.iloc[:train_size]
    valid = df.iloc[train_size:]

    train.to_csv(train_csv, index=False)
    valid.to_csv(valid_csv, index=False)

if __name__ == "__main__":
    """
    Usage:
    py src/prepare.py train 1
    py src/prepare.py train 2
    py src/prepare.py train 3

    py src/prepare.py test 1
    py src/prepare.py test 2
    """

    mode = sys.argv[1]
    step = sys.argv[2]

    if mode == "train":

        # Step 1: convert
        if step == "1":
            convert_data(
                "data/dataset_train_all.csv",
                "data/dataset_train.csv"
            )

        # Step 2: clean
        elif step == "2":
            remove_duplicates_and_sample(
                "data/dataset_train_final.csv",
                "data/dataset_train_clean.csv"
            )

        # Step 3: split
        elif step == "3":
            split_train_valid(
                "data/dataset_train_clean.csv",
                "data/train.csv",
                "data/valid.csv"
            )

        else:
            raise ValueError("Train step must be 1, 2, or 3")

    elif mode == "test":

        # Step 1: convert
        if step == "1":
            convert_data(
                "data/dataset_test_all.csv",
                "data/dataset_test.csv"
            )

        # Step 2: clean
        elif step == "2":
            remove_duplicates_and_sample(
                "data/dataset_test_final.csv",
                "data/test.csv"
            )

        else:
            raise ValueError("Test step must be 1 or 2")

    else:
        raise ValueError("Mode must be 'train' or 'test'")
