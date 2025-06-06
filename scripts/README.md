# Scripts

This folder contains standalone scripts for data-related tasks such as scraping app reviews from the Google Play Store, data preprocessing, cleaning, and transformation. Each script is designed to be run independently to assist with data collection and preparation workflows.

## Files

- `preprocess_reviews.py`: Cleans and prepares raw review data for analysis.
- `scrape_reviews.py`: This script fetches up to 5000 of the newest reviews for a specified app from the Google Play Store and saves them into a CSV file.

## Usage

```bash
python preprocess_reviews.py
```

```bash
python scrape_reviews.py --app-id <APP_ID> --bank-name "<BANK_NAME>" --output-dir <OUTPUT_DIRECTORY>

```