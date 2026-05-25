import pandas as pd

FILE_ORIGINAL = 'data/dataset_all_backup.csv'
FILE_TRAIN = 'data/dataset_train_all.csv'
FILE_TEST = 'data/dataset_test_all.csv'

TARGET_TRAIN_SIZE = 100000 
TARGET_TEST_SIZE = 25000 
ORIGINAL_NEG_POS_RATIO = 7  # Ratio Normal:Buggy (7:1)

print("Starting data splitting...")

try:
    df_raw = pd.read_csv(FILE_ORIGINAL)

    print(f"- Total original methods: {len(df_raw):,}")

    # len('bugs') > 2: Buggy, <= 2: Normal
    df_buggy = df_raw[df_raw['bugs'].astype(str).str.len() > 2]
    df_normal = df_raw[df_raw['bugs'].astype(str).str.len() <= 2]

    actual_pos = len(df_buggy)
    actual_neg = len(df_normal)
    print(f"- Original Buggy samples: {actual_pos:,}")
    print(f"- Original Normal samples: {actual_neg:,}")

    # sample sizes calculation
    
    # 2. Calculate target sample sizes for each set
    
    # Test (25,000)
    req_test_buggy = int(TARGET_TEST_SIZE / (ORIGINAL_NEG_POS_RATIO + 1)) # 3,125
    req_test_normal = TARGET_TEST_SIZE - req_test_buggy                   # 21,875

    # Train/Val (100,000)
    req_train_buggy = int(TARGET_TRAIN_SIZE / (ORIGINAL_NEG_POS_RATIO + 1)) # 12,500
    req_train_normal = TARGET_TRAIN_SIZE - req_train_buggy               # 87,500
    
    # Sample for test set 
    
    # 3. Sample Buggy Test
    n_test_buggy = min(actual_pos, req_test_buggy) 
    df_test_buggy = df_buggy.sample(
        n=n_test_buggy, 
        random_state=42
    )
    
    # 4. Sample Normal Test
    n_test_normal = min(actual_neg, req_test_normal) 
    df_test_normal = df_normal.sample(
        n=n_test_normal, 
        random_state=42
    )
    
    # Sample for train/val from the remaining data
    
    # 5. Remove samples selected for Test from the original set
    df_buggy_remaining = df_buggy.drop(df_test_buggy.index)
    df_normal_remaining = df_normal.drop(df_test_normal.index)
    
    # Sample for train/val from the remaining data
    
    # 6. Sample Buggy Train/Val
    n_train_buggy = min(len(df_buggy_remaining), req_train_buggy)
    df_train_buggy = df_buggy_remaining.sample(
        n=n_train_buggy, 
        random_state=42
    )
    
    # 7. Sample Normal Train/Val
    n_train_normal = min(len(df_normal_remaining), req_train_normal) 
    df_train_normal = df_normal_remaining.sample(
        n=n_train_normal, 
        random_state=42
    )

    # Combine and shuffle data
    
    # 8. Test
    df_test = pd.concat([df_test_buggy, df_test_normal])
    df_test = df_test.sample(frac=1, random_state=42).reset_index(drop=True)

    # 9. Train
    df_train = pd.concat([df_train_buggy, df_train_normal])
    df_train = df_train.sample(frac=1, random_state=42).reset_index(drop=True)
    
    df_test.to_csv(FILE_TEST, index=False)
    df_train.to_csv(FILE_TRAIN, index=False)

    print(f"\n STATISTICS AFTER SPLITTING:")
    
    # Statistics for TEST set
    print(f"\n[TEST SET - {len(df_test):,} samples]")
    print(f"- File created: {FILE_TEST}")
    print(f"- Buggy samples taken: {n_test_buggy:,}")
    print(f"- Normal samples taken: {n_test_normal:,}")
    final_test_ratio = round(n_test_normal / n_test_buggy, 2) if n_test_buggy > 0 else "N/A"
    print(f"- Final Normal:Buggy ratio: {final_test_ratio}:1")

    # Statistics for TRAIN set
    print(f"\n[TRAIN SET - {len(df_train):,} samples]")
    print(f"- File created: {FILE_TRAIN}")
    print(f"- Buggy samples taken: {n_train_buggy:,}")
    print(f"- Normal samples taken: {n_train_normal:,}")
    final_train_ratio = round(n_train_normal / n_train_buggy, 2) if n_train_buggy > 0 else "N/A"
    print(f"- Final Normal:Buggy ratio: {final_train_ratio}:1")

    print("\n SPLITTING COMPLETED ")

except Exception as e:
    print("An error occurred:", e)