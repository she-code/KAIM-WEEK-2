import pandas as pd
import sys
import os
sys.path.append('../src') 

from utils.data_preprocesser import preprocess_bank_reviews

if __name__ == "__main__":
    # File paths
    paths = {
        "Commercial Bank of Ethiopia": "../data/raw/Commercial Bank of Ethiopia_raw_reviews.csv",
        "Bank of Abyssinia": "../data/raw/Bank of Abyssinia_raw_reviews.csv",
        "Dashen Bank": "../data/raw/Dashen Bank_raw_reviews.csv",
    }

    output_dir = "../data/processed/"
    os.makedirs(output_dir, exist_ok=True)

    dfs = []
    # preprocess all banks' reviews one by one
    for bank, path in paths.items():
        df = preprocess_bank_reviews(path, bank)

        # Create a clean filename
        bank_clean = bank.lower().replace(" ", "_")
        output_path = os.path.join(output_dir, f"{bank_clean}_clean.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Saved cleaned data for {bank} to {output_path}")

        dfs.append(df)


    # Merge and save all
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_output_path = os.path.join(output_dir, "clean_reviews_all_banks.csv")
    merged_df.to_csv(merged_output_path, index=False)
    print(f"\n✅ Merged cleaned data saved to {merged_output_path}")
