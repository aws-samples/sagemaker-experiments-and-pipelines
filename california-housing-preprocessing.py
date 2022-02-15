# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

if __name__=="__main__":
    databunch = fetch_california_housing()

    dataset = np.concatenate((databunch["target"].reshape(-1, 1), databunch["data"]), axis=1)

    print(f"Dataset shape = {dataset.shape}")

    train, other = train_test_split(dataset, test_size=0.1)
    validation, test = train_test_split(other, test_size=0.5)

    print(f"Train shape = {train.shape}")
    print(f"Validation shape = {validation.shape}")
    print(f"Test shape = {test.shape}")

    base_dir = "/opt/ml/processing"

    pd.DataFrame(train).to_csv(f"{base_dir}/train/train.csv", header=False, index=False)
    pd.DataFrame(validation).to_csv(
            f"{base_dir}/validation/validation.csv", header=False, index=False
        )
    pd.DataFrame(test).to_csv(f"{base_dir}/test/test.csv", header=False, index=False)

