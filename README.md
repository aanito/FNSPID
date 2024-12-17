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

python3 src/text_statistics.py --file data/raw/raw_analyst_ratings.csv

Tasks

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

Analysis of Publication Frequency and Publishing Times

Objective

Publication Frequency Over Time: To determine variations in publication frequency and identify spikes related to specific market events.
Analysis of Publishing Times: To examine if there’s a specific time when most news is released and derive insights for traders or automated systems.

Steps Undertaken

1. Publication Frequency Over Time
   Data Preprocessing:
   Loaded the dataset and converted the date column to a datetime format.
   Extracted the publication year, month, and day.
   Aggregation:
   Grouped data by date and counted the number of articles published on each date.
   Visualization:
   Created a time-series plot to observe patterns and spikes over time.
   Annotated significant spikes with possible market events for better insights.

2. Analysis of Publishing Times
   Data Preprocessing:
   Extracted the hour from the date column to understand time-based publication trends.
   Aggregation:
   Grouped data by hour and counted articles published during each hour of the day.
   Visualization:
   Created a bar chart showing the distribution of articles by publishing time.

Results Presentation

Publication Frequency: The time-series chart highlighted periods of increased news activity, often aligning with significant market events like earnings seasons or major regulatory announcements.
Publishing Times: The bar chart revealed peak publishing times, typically clustered around the start of trading hours and during market-close summaries.

Analysis of Publisher Contributions and Unique Domains in the News Feed

Objective
Publisher Contributions: Identify which publishers contribute the most to the news feed and examine differences in the type of news they report.
Domain Analysis: If publisher names are email addresses, extract and analyze unique domains to identify organizations contributing frequently.
Steps Undertaken

1. Publisher Contributions
   Data Preprocessing:
   The publisher column was examined to identify the unique names of publishers.
   Counts of articles per publisher were calculated to rank publishers based on their contribution.
   News Type Analysis:
   Articles were grouped by publisher, and the headline text was analyzed for sentiment and keywords using the earlier scripts.
   Publishers were categorized based on the tone of their content (e.g., positive, negative) and common keywords.
2. Domain Analysis
   Email Identification:
   Checked if publisher names in the publisher column resembled email addresses (e.g., using a regex pattern).
   Domain Extraction:
   Extracted the domain portion of email addresses (e.g., "example.com" from "user@example.com").
   Counted the frequency of each domain to identify prominent contributors.
   Visualization and Presentation
   Created bar charts to display:
   Top contributing publishers.
   Top contributing domains (if applicable).
   Included a table summarizing publisher contributions alongside sentiment and keyword insights

Quantitative Analysis of Stock Price Data Using PyNance and TA-Lib
Objective
The analysis aimed to:

Load and prepare stock price data for seven independent brands.
Apply technical analysis indicators using TA-Lib.
Use PyNance to compute financial metrics.
Visualize stock price trends and the impact of technical indicators on price movements.
Steps Undertaken

1. Data Loading and Preparation
   The stock price data, including columns like Open, High, Low, Close, Adj Close, Volume, Dividends, and Stock Splits, was loaded into a pandas DataFrame.
   Data was validated for missing or inconsistent values:
   Missing values were imputed using forward fill and backfill techniques.
   Ensured consistent column formatting across datasets.
   Each brand's dataset was appended with a Stock Symbol column to identify the respective brand.
2. Technical Analysis Indicators Using TA-Lib
   Installed and imported the TA-Lib library to calculate key indicators:
   Moving Averages (e.g., 50-day and 200-day SMA).
   Relative Strength Index (RSI) to measure momentum.
   Moving Average Convergence Divergence (MACD) to assess price trends.
   Added calculated indicators as new columns in the DataFrame.
3. Financial Metrics Using PyNance
   PyNance was employed to calculate additional metrics:
   Sharpe Ratio to evaluate risk-adjusted returns.
   Volatility to assess stock price fluctuations.
   Consolidated metrics into summary tables for each brand.
4. Visualization
   Used Matplotlib and Seaborn to create visualizations:
   Line plots to show stock prices over time.
   Overlay of technical indicators (e.g., RSI and MACD) on stock price charts.
   Heatmaps to depict correlations between indicators and price movements.

Results
Technical Indicators:

SMA: Highlighted key trends and crossovers, providing buy/sell signals.
RSI: Identified overbought (>70) and oversold (<30) levels.
MACD: Indicated momentum shifts.

Sentiment Analysis and Correlation with Stock Price Movements
Objective
To analyze the relationship between financial news sentiment and stock price movements using prepared datasets. The report involves:

Normalizing dates between the news and stock datasets.
Assigning sentiment scores to headlines.
Calculating daily stock returns.
Correlating average sentiment scores with stock price movements.

1. Data Preparation
   a. Align Dates
   Both financial news and stock datasets should be normalized to ensure consistent date formats.
   Dates in the news dataset are mapped to stock trading days for precise matching.
   Steps:

Parse dates in both datasets.
Align and merge datasets on trading days. 2. Sentiment Analysis
Perform sentiment analysis on news headlines using a library like TextBlob or VADER.
Assign sentiment scores:
Positive: Sentiment > 0
Neutral: Sentiment ≈ 0
Negative: Sentiment < 0
Steps:

Use a sentiment analysis tool to compute sentiment polarity for each headline.
Aggregate sentiment scores (average) for days with multiple news articles. 3. Calculate Stock Movements
Compute daily returns to quantify stock price movements using the formula:
Daily Return
=
Close
𝑡
−
Close
𝑡
−
1
Close
𝑡
−
1
Daily Return=
Close
t−1
​

Close
t
​
−Close
t−1
​

​

4. Correlation Analysis
   Use Pearson correlation to assess the relationship between average daily sentiment scores and stock daily returns.
   Steps:

Merge the stock daily returns with average sentiment scores.
Compute Pearson correlation to understand how sentiment relates to stock price movements.
Python Script
Here is the complete script to solve the above tasks:

python
Copy code
import pandas as pd
from textblob import TextBlob # Sentiment Analysis
from scipy.stats import pearsonr # Correlation Analysis

def normalize_dates(news_df, stock_df):
"""
Normalize and align dates between news and stock datasets.
"""
news_df['Date'] = pd.to_datetime(news_df['Date']).dt.date
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
return news_df, stock_df

def perform_sentiment_analysis(news_df):
"""
Perform sentiment analysis on news headlines using TextBlob.
"""
news_df['Sentiment'] = news_df['Headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
return news_df

def calculate_daily_returns(stock_df):
"""
Calculate daily returns for stock data.
"""
stock_df['Daily_Return'] = stock_df['Close'].pct_change()
return stock_df

def aggregate_sentiments(news_df):
"""
Aggregate sentiment scores by date.
"""
daily_sentiment = news_df.groupby('Date')['Sentiment'].mean().reset_index()
return daily_sentiment

def merge_and_calculate_correlation(stock_df, sentiment_df):
"""
Merge stock returns with sentiment scores and calculate correlation.
"""
merged_df = pd.merge(stock_df[['Date', 'Daily_Return']], sentiment_df, on='Date', how='inner')
correlation, p_value = pearsonr(merged_df['Daily_Return'].dropna(), merged_df['Sentiment'].dropna())
return merged_df, correlation, p_value

def main(news_file, stock_file, output_file): # Load datasets
news_df = pd.read_csv(news_file)
stock_df = pd.read_csv(stock_file)

    # Step 1: Normalize dates
    news_df, stock_df = normalize_dates(news_df, stock_df)

    # Step 2: Perform sentiment analysis
    news_df = perform_sentiment_analysis(news_df)

    # Step 3: Calculate stock daily returns
    stock_df = calculate_daily_returns(stock_df)

    # Step 4: Aggregate daily sentiment scores
    daily_sentiment = aggregate_sentiments(news_df)

    # Step 5: Merge datasets and compute correlation
    merged_df, correlation, p_value = merge_and_calculate_correlation(stock_df, daily_sentiment)

    # Output results
    print("Correlation between Sentiment and Daily Stock Returns:", round(correlation, 4))
    print("P-value:", round(p_value, 4))

    # Save results
    merged_df.to_csv(output_file, index=False)
    print(f"Results saved to: {output_file}")

if **name** == "**main**":
import argparse

    parser = argparse.ArgumentParser(description="Analyze financial news sentiment and stock price correlation")
    parser.add_argument('--news_file', type=str, help="Path to the financial news dataset CSV")
    parser.add_argument('--stock_file', type=str, help="Path to the stock price dataset CSV")
    parser.add_argument('--output_file', type=str, help="Path to save the output merged dataset")

    args = parser.parse_args()

    main(args.news_file, args.stock_file, args.output_file)

Script Execution
Run the Script from Command Line:

Prepare your news dataset and stock dataset in CSV format.
Execute the script by passing the file paths:
bash
Copy code
python sentiment_correlation.py --news_file data/news_data.csv --stock_file data/stock_data.csv --output_file output/correlation_results.csv
Input Dataset Requirements:

News Dataset:

Date Headline
2024-06-14 "Stock markets rise amid optimism"
2024-06-14 "Analysts predict strong earnings"
Stock Dataset:

Date Open High Low Close Volume
2024-06-13 100.0 105.0 99.0 104.0 1200000
2024-06-14 104.0 106.0 103.5 105.5 1500000
Output:

The script will compute:
Daily returns for stock prices.
Average sentiment scores for each day.
Correlation coefficient and p-value.
The merged dataset is saved in the specified output directory.
