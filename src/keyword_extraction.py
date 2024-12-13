import argparse
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from rake_nltk import Rake

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

def extract_keywords(df):
    """
    Extract common keywords from the headlines.
    """
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(' '.join(df['headline'].dropna()))
    filtered_words = [word.lower() for word in words if word.isalpha() and word not in stop_words]
    keyword_counts = Counter(filtered_words).most_common(10)
    return keyword_counts

def extract_phrases(df):
    """
    Extract significant phrases from the headlines using RAKE.
    """
    rake = Rake()
    text = ' '.join(df['headline'].dropna())
    rake.extract_keywords_from_text(text)
    phrases = rake.get_ranked_phrases_with_scores()
    return phrases[:10]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract keywords and phrases from news headlines.")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the dataset CSV file (e.g., data/raw/financial_news.csv).",
    )
    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)

    # Perform keyword extraction
    keywords = extract_keywords(df)
    print("Top Keywords:\n", keywords)

    # Perform phrase extraction
    phrases = extract_phrases(df)
    print("Top Phrases:\n", phrases)
