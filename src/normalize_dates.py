import pandas as pd

def normalize_dates(news_file, stock_file, output_news_file, output_stock_file):
    # Load datasets
    news_df = pd.read_csv(news_file)
    stock_df = pd.read_csv(stock_file)

    # # Normalize dates
    # news_df['date'] = pd.to_datetime(news_df['date']).dt.date
    # stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
        # Handle news dataset dates
    news_df['Date'] = pd.to_datetime(news_df['date'], errors='coerce', format='%Y-%m-%d %H:%M:%S').dt.date

    # Handle stock dataset dates
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce', format='%Y-%m-%d').dt.date



    # Save normalized datasets
    news_df.to_csv(output_news_file, index=False)
    stock_df.to_csv(output_stock_file, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Normalize dates in news and stock datasets.")
    parser.add_argument("--news_file", required=True, help="Path to the news file.")
    parser.add_argument("--stock_file", required=True, help="Path to the stock file.")
    parser.add_argument("--output_news_file", required=True, help="Output path for normalized news file.")
    parser.add_argument("--output_stock_file", required=True, help="Output path for normalized stock file.")
    args = parser.parse_args()

    normalize_dates(args.news_file, args.stock_file, args.output_news_file, args.output_stock_file)
