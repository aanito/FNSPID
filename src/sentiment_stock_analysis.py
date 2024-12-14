import pandas as pd
import argparse
import os
from textblob import TextBlob
from scipy.stats import pearsonr
from pathlib import Path


def normalize_dates(news_df, stock_df):
    """
    Align the date columns in the news and stock dataframes.
    """
    # Handle news dataset dates
    news_df['Date'] = pd.to_datetime(news_df['date'], errors='coerce', format='%Y-%m-%d %H:%M:%S').dt.date

    # Handle stock dataset dates
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce', format='%Y-%m-%d').dt.date

    return news_df, stock_df


def perform_sentiment_analysis(news_df):
    """
    Perform sentiment analysis on news headlines and assign scores.
    """
    news_df['Sentiment_Score'] = news_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    return news_df

def calculate_daily_returns(stock_df):
    """
    Calculate daily percentage returns in stock prices.
    """
    stock_df['Daily_Return'] = stock_df['Close'].pct_change()
    return stock_df

def aggregate_sentiments(news_df):
    """
    Aggregate daily sentiment scores by averaging scores for each day.
    """
    daily_sentiment = news_df.groupby('Date')['Sentiment_Score'].mean().reset_index()
    return daily_sentiment

def merge_and_calculate_correlation(stock_df, sentiment_df):
    """
    Merge stock returns and sentiment scores, and compute correlation.
    """
    merged_df = pd.merge(stock_df, sentiment_df, on='Date', how='inner')
    merged_df = merged_df.dropna(subset=['Daily_Return', 'Sentiment_Score'])
    
    if len(merged_df) > 1:  # Ensure enough data points for correlation
        correlation, p_value = pearsonr(merged_df['Daily_Return'], merged_df['Sentiment_Score'])
    else:
        correlation, p_value = None, None

    return merged_df, correlation, p_value

def main(news_file, stock_files, output_dir):
    # Load the news dataset
    news_df = pd.read_csv(news_file)
    
    # Process each stock dataset independently
    for stock_file in stock_files:
        company_name = Path(stock_file).stem  # Extract company name from the file name
        print(f"Processing analysis for company: {company_name}")

        # Load the stock dataset
        stock_df = pd.read_csv(stock_file)

        # Align and normalize dates
        news_df, stock_df = normalize_dates(news_df, stock_df)

        # Perform sentiment analysis and calculate stock movements
        sentiment_scores = perform_sentiment_analysis(news_df)
        daily_returns = compute_daily_returns(stock_df)

        # Merge and calculate correlation
        merged_df = merge_sentiment_and_stock(news_df, sentiment_scores, daily_returns)
        correlation = calculate_correlation(merged_df)

        print(f"Correlation between sentiment and stock returns for {company_name}: {correlation}")

        # Save output
        output_file = Path(output_dir) / f"{company_name}_sentiment_stock_analysis.csv"
        merged_df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Correlate news sentiment with stock movements for multiple companies.")
    parser.add_argument("--news_file", required=True, help="Path to the news dataset CSV file.")
    parser.add_argument("--stock_files", required=True, help="Comma-separated list of stock dataset CSV file paths.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the output correlation results.")
    
    args = parser.parse_args()
    
    # Parse stock file paths into a list
    stock_files = args.stock_files.split(",")
    
    # Run the main function
    main(args.news_file, stock_files, args.output_dir)
