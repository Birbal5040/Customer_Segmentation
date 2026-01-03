
#Python libraries

import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df = df.copy()

    #Clean column names

    df.columns = df.columns.str.strip()

    # Rename columns

    rename_map = {}
    for col in df.columns:
        if "Annual Income" in col:
            rename_map[col] = "Income"
        if "Spending" in col:
            rename_map[col] = "Spending"

    df = df.rename(columns=rename_map)

    #Convert required columns to numeric

    required_cols = ["Age", "Income", "Spending"]
    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    #Drop rows with missing values

    df = df.dropna(subset=required_cols)

    # check rows
    print("Rows after cleaning:", df.shape[0])

    # check
    if df.shape[0] == 0:
        raise ValueError(
            "Dataset has 0 valid rows after cleaning. "
            "Check CSV values in Age, Income, Spending columns."
        )

    features = df[required_cols]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    return df, scaled_features
