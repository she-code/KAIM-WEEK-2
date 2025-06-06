from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import logging
import argparse
import os

# Set up logging
logging.basicConfig(
    filename='scraper.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_play_store_reviews(app_id, bank_name, output_dir):
    logging.info(f"🔄 Fetching reviews for {app_id}...")

    try:
        results, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=5000,
            filter_score_with=None
        )

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{bank_name}_raw_reviews.csv"
        filepath = os.path.join(output_dir, filename)

        # Write to CSV
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['review', 'rating', 'date', 'bank', 'source'])
            writer.writeheader()

            for entry in results:
                writer.writerow({
                    'review': entry['content'],
                    'rating': entry['score'],
                    'date': entry['at'].strftime('%Y-%m-%d'),
                    'bank': bank_name,
                    'source': 'Google Play'
                })

        logging.info(f"✅ Saved {len(results)} reviews to {filepath}")
        print(f"Success! Reviews saved to: {filepath}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Google Play Store reviews")
    parser.add_argument("--app-id", required=True, help="Google Play Store App ID (e.g., 'com.dashen.dashensuperapp')")
    parser.add_argument("--bank-name", required=True, help="Name of the bank (e.g., 'Commercial Bank of Ethiopia')")
    parser.add_argument("--output-dir", default=".", help="Directory to save CSV (default: current folder)")
    
    args = parser.parse_args()
    
    scrape_play_store_reviews(args.app_id, args.bank_name, args.output_dir)