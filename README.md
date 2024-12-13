# Financial News Dataset Analysis

## Overview

This project analyzes financial news articles to extract insights such as:

1. Headline length statistics.
2. Publisher activity.
3. Trends in publication frequency.

## Installation

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

## Usage Instructions

### Running Analysis Scripts

Each script accepts a `--file` argument to specify the dataset path.

#### Example

python src/text_statistics.py --file data/raw/raw_analyst_ratings.csv

Sentiment Analysis

Objective: Gauge the sentiment (positive, negative, neutral) associated with the news headlines.

Steps Undertaken
Dataset Loading: The dataset was loaded into a pandas DataFrame for processing. The headline column contained the text data for sentiment analysis.
Preprocessing: Headlines were cleaned by removing punctuation, numbers, and converting them to lowercase.
Sentiment Analysis: The TextBlob library was used to compute sentiment polarity scores. Based on the polarity:
Polarity > 0: Positive
Polarity < 0: Negative
Polarity = 0: Neutral
Result: Each headline was labeled with its respective sentiment.

Keyword and Phrase Extraction

Objective: Identify common keywords, phrases, and significant events like "FDA approval" or "price target."

Steps Undertaken
Tokenization: Headlines were split into words using the nltk library.
Stopword Removal: Common stopwords (e.g., "the", "and") were removed to focus on meaningful words.
Keyword Extraction: The most frequent words were identified using term frequency.
Phrase Extraction: The RAKE (Rapid Automatic Keyword Extraction) algorithm was employed to extract relevant phrases.
Topic Clustering: The Latent Dirichlet Allocation (LDA) model was used to group similar phrases into topics.
