# Customer Experience Analytics for Fintech Apps

## Challenge Overview

This project is part of the **10 Academy Artificial Intelligence Mastery Week 2 Challenge**. The goal is to simulate real-world analytics and data engineering workflows to help Ethiopian fintech institutions improve customer satisfaction based on mobile app reviews.

## Target Banks & Apps
We focus on the Google Play Store reviews for the following Ethiopian banking apps:

| Bank                        | Package Name                        |
|-----------------------------|--------------------------------------|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking`      |
| Bank of Abyssinia           | `com.boa.boaMobileBanking`          |
| Dashen Bank                 | `com.dashen.dashensuperapp`         |

## Project Structure

---
```
KAIM-WEEK-2/
├── .github/
│ └── workflows/ # GitHub Actions workflows
├── data/
│ ├── raw/ # Raw data (should never be modified)
│ └── processed/ # Processed/cleaned data (gitignored)
├── notebooks/
│ ├── data_preprocess.ipynb # Data preprocessing notebook
│ ├── sentiment_thematic_analysis.ipynb # Analysis notebook
│ └── README.md # Documentation for notebooks
├── scripts/
│ ├── scrape_reviews.py # Web scraping script
│ ├── preprocess_reviews.py # Data preprocessing script
│ ├── scraper.log # Log file from scraping
│ └── README.md # Documentation for scripts
├── src/
│ ├── data_loader.py # Data loading utilities
│ ├── data_preprocessor.py # Data preprocessing utilities
│ ├── sentiment_analyzers.py # Sentiment analysis logic
│ └── utils/ # Utility functions
│ └── README.md # Documentation for source code
├── tests/
│ ├── test_preprocess.py # Tests for preprocessing
│ └── README.md # Testing documentation
├── .gitattributes
├── .gitignore
├── README.md # Main project documentation
└── requirements.txt # Python dependencies
```
## Tech Stack

**Languages & Libraries:**  
Python, Pandas, SpaCy, Scikit-learn, Hugging Face Transformers, Matplotlib, Seaborn

**Web Scraping:**  
[google-play-scraper](https://pypi.org/project/google-play-scraper/)

**Natural Language Processing (NLP):**  
VADER, TextBlob, DistilBERT (Hugging Face)

**Database:**  
Oracle XE, [oracledb Python Client](https://python-oracledb.readthedocs.io/en/latest/)

**Version Control:**  
Git, GitHub

**Visualization:**  
Matplotlib, Seaborn, WordCloud

---
## Data Fields

Each collected review will include:

- **review**: The user’s text feedback

- **rating**: Rating score (1 to 5 stars)

- **date**: Review date (normalized to YYYY-MM-DD)

- **bank**: App/bank name

- **source**: "Google Play"
---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/she-code/KAIM-WEEK-2.git
cd KAIM-WEEK-2
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt

```
