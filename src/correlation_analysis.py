import pandas as pd

def correlation_analysis(sentiment_file, stock_file, output_file):
    sentiment_df = pd.read_csv(sentiment_file)
    stock_df = pd.read_csv(stock_file)

    # Merge on the date
    combined_df = pd.merge(sentiment_df, stock_df, left_on='date', right_on='Date', how='inner')

    # Calculate correlation
    correlation = combined_df['sentiment'].corr(combined_df['Daily_Return'])
    print(f"Pearson correlation between sentiment and daily returns: {correlation}")

    combined_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate correlation between sentiment and stock movements.")
    parser.add_argument("--sentiment_file", required=True, help="Path to the sentiment analysis file.")
    parser.add_argument("--stock_file", required=True, help="Path to the stock movements file.")
    parser.add_argument("--output_file", required=True, help="Output path for merged and analyzed results.")
    args = parser.parse_args()

    correlation_analysis(args.sentiment_file, args.stock_file, args.output_file)
