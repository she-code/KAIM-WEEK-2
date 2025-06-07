# Notebooks

This folder contains Jupyter notebooks demonstrating the usage and exploration of the data preprocessing module.

## : data_preprocessor.py

- The notebooks showcase how to load raw data and apply preprocessing steps using `data_preprocessor.py`.
- They include:
  - Data cleaning demonstrations
  - Handling missing data and duplicates
  - Date formatting examples
  - Sample workflows integrating preprocessing in analysis pipelines

## sentiment_thematic_analysis.py
  Performs sentiment and thematic analysis on bank app reviews, including:

  - Cleaning and preprocessing review text
  - Applying multiple sentiment analysis techniques:
    - **DistilBERT** (transformer-based model for nuanced sentiment classification)
    - **TextBlob** (rule-based polarity and subjectivity scoring)
    - **VADER** (lexicon and rule-based sentiment analyzer optimized for social media text)
  - Comparing and evaluating sentiment results across these methods
  - Identifying review themes using keyword clusters and fuzzy matching for better coverage
  - Grouping reviews into categories like user experience, app performance, mobile banking, and more
  - Producing enriched output datasets for reporting and visualization

## Running Notebooks

To run the notebooks:

1. Install required dependencies (see `requirements.txt`).
2. Launch Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```