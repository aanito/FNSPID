import pandas as pd
import talib

def apply_ta_indicators(df):
    """
    Apply TA-Lib indicators to the dataset.
    """
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    return df

if __name__ == "__main__":
    data = pd.read_csv("../data/raw/yfinance_data/combined_data.csv", parse_dates=['Date'])
    data_with_indicators = apply_ta_indicators(data)
    data_with_indicators.to_csv("../data/raw/yfinance_data/ta_indicators.csv", index=False)
