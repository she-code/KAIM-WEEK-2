import pandas as pd
import os
import pytest
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.data_preprocesser import preprocess_bank_reviews

@pytest.fixture
def sample_data(tmp_path):
    # Create a small sample CSV with duplicates, inconsistent dates, and missing review
    data = {
        "review": ["Good", "Bad", "Good", None],
        "rating": [5, 1, 5, 3],
        "date": ["2023-01-01", "Jan 5, 2023", "2023-01-01", "2023-02-01"],
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "test_reviews.csv"
    df.to_csv(file_path, index=False)
    return str(file_path)

def test_preprocess_bank_reviews(sample_data):
    bank_name = "Test Bank"
    cleaned_df = preprocess_bank_reviews(sample_data, bank_name)
    print(cleaned_df)

    # Confirm it's a DataFrame and has expected columns
    assert isinstance(cleaned_df, pd.DataFrame)
    assert set(["review", "rating", "date", "bank","source"]).issubset(cleaned_df.columns)

    # No duplicates
    assert cleaned_df.duplicated().sum() == 0

    # One duplicate and one missing review should be removed → expect 2 rows
    assert len(cleaned_df) == 1

    # No missing reviews
    assert cleaned_df["review"].isna().sum() == 0

    # No missing or invalid dates
    assert cleaned_df["date"].isna().sum() == 0

    # Date format should be consistent
    try:
        pd.to_datetime(cleaned_df["date"], format="%Y-%m-%d")
    except Exception:
        pytest.fail("Date format is not YYYY-MM-DD")
