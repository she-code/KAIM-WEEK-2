import re
import nltk
import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK resources (you may call this once in your main script)
def download_nltk_resources():
    nltk.download('vader_lexicon')

# Clean review text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s.,!?']", '', text)  # keep basic punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# VADER sentiment analyzer
def vader_sentiment(text, sia=None):
    if sia is None:
        sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']
    label = 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral'
    return pd.Series([score, label])

# TextBlob sentiment analyzer
def textblob_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    label = 'positive' if polarity > 0.1 else 'negative' if polarity < -0.1 else 'neutral'
    return pd.Series([polarity, label])

# Wrapper to apply preprocessing and both sentiment models
def apply_sentiment_analysis(df, text_col='review'):
    df = df[df[text_col].notna()].copy()
    # df['review_id'] = df.index
    # df['clean_review'] = df[text_col].apply(clean_text)

    sia = SentimentIntensityAnalyzer()
    df[['vader_score', 'vader_label']] = df['review'].apply(lambda x: vader_sentiment(x, sia))
    df[['textblob_score', 'textblob_label']] = df['review'].apply(textblob_sentiment)

    return df

def get_textblob_label(polarity):
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'
