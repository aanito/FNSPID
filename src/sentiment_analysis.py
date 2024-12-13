import argparse
import pandas as pd
from textblob import TextBlob

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

def perform_sentiment_analysis(df):
    """
    Perform sentiment analysis on the headlines.
    """
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment_label'] = df['sentiment'].apply(
        lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral')
    )
    return df[['headline', 'sentiment', 'sentiment_label']]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform sentiment analysis on news headlines.")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the dataset CSV file (e.g., data/raw/financial_news.csv).",
    )
    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)

    # Perform sentiment analysis
    results = perform_sentiment_analysis(df)
    print(results.head())
