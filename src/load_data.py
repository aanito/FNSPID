import pandas as pd
import os

def load_and_prepare_data(file_paths):
    """
    Load and prepare stock data from multiple files.
    """
    data_frames = []
    for file_path in file_paths:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        df['Stock Symbol'] = os.path.basename(file_path).split('.')[0]  # Extract brand from filename
        df.sort_values('Date', inplace=True)
        df.fillna(method='ffill', inplace=True)
        df.fillna(method='bfill', inplace=True)
        data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)

if __name__ == "__main__":
    files = ["data/raw/yfinance_data/AAPL_historical_data.csv", "data/raw/yfinance_data/AMZN_historical_data.csv", "data/raw/yfinance_data/GOOG_historical_data.csv", "data/raw/yfinance_data/META_historical_data.csv", "data/raw/yfinance_data/MSFT_historical_data.csv", "data/raw/yfinance_data/NVDA_historical_data.csv", "data/raw/yfinance_data/TSLA_historical_data.csv"]  # All file paths
    combined_data = load_and_prepare_data(files)
    combined_data.to_csv("data/raw/yfinance_data/combined_data.csv", index=False)
