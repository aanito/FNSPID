import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, brand_name, output_dir):
    """
    Plot stock data and save the figure to the output directory.

    Args:
    - df (pd.DataFrame): The stock data.
    - brand_name (str): The name of the brand for labeling the plot.
    - output_dir (str): The directory to save the output plot.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Plot stock data
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Close'], label=f"{brand_name} Close Price", color="blue")
        plt.title(f"{brand_name} Stock Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.legend()

        # Save the plot
        output_path = os.path.join(output_dir, f"{brand_name}_stock_plot.png")
        plt.savefig(output_path)
        plt.close()
        print(f"Plot saved to: {output_path}")
    except Exception as e:
        print(f"Error in plotting data: {e}")

if __name__ == "__main__":
    try:
        # Input and output paths
        data_path = "../data/raw/brand1_stock.csv"
        output_dir = "src/output"

        # Load data
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset not found at path: {data_path}")
        
        stock_data = pd.read_csv(data_path, parse_dates=['Date'])
        stock_data = stock_data.sort_values(by="Date")

        # Debug: Check loaded data
        print("Dataset Loaded:")
        print(stock_data.info())

        # Plot the data
        plot_stock_data(stock_data, "Brand1", output_dir)

    except Exception as e:
        print(f"Error in script execution: {e}")


# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_stock_with_indicators(df, stock_symbol, output_dir):
#     """
#     Plot stock price and technical indicators for a specific stock.
#     """
#     stock_data = df[df['Stock Symbol'] == stock_symbol]
#     plt.figure(figsize=(12, 6))
#     plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price', color='blue')
#     plt.plot(stock_data['Date'], stock_data['SMA_50'], label='SMA 50', color='green')
#     plt.plot(stock_data['Date'], stock_data['SMA_200'], label='SMA 200', color='red')
#     plt.title(f"{stock_symbol} Stock Price and Indicators")
#     plt.xlabel("Date")
#     plt.ylabel("Price")
#     plt.legend()
#     plt.grid()
#     plt.savefig(f"{output_dir}/{stock_symbol}_stock_plot.png")
#     plt.show()

# if __name__ == "__main__":
#     data = pd.read_csv("../data/raw/yfinance_data/ta_indicators.csv", parse_dates=['Date'])
#     plot_stock_with_indicators(data, "brand1", "output")
