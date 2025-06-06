import sys
import pandas as pd
sys.path.append('../src') 

from utils.data_loader import load_data


def inspect_data(df, bank_name):
    print(f"--- {bank_name} INFO ---")
    print(df.info())
    print(df.isna().sum())
    df = df.dropna()
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(df[df.duplicated(keep=False)])

def clean_data(df):
    df = df.drop_duplicates().copy()
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    df = df.dropna().copy()
    df["date"] = df["date"].dt.normalize()
    return df




def preprocess_bank_reviews(file_path, bank_name):
    df = load_data(file_path)
    inspect_data(df, bank_name)
    df['bank'] = bank_name
    df["source"] = "Google Play Store"

    df = clean_data(df)
    print(f"Duplicates after cleaning ({bank_name}): {df.duplicated().sum()}")
    return df
