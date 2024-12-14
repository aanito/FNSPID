import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse

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

def main(args):
    try:
        # Input file (CSV) and output directory
        data_path = args.data_file
        output_dir = "/root/FNSPID/data/processed"  # Output directory for saved plots

        # Verify if the input dataset exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset not found at path: {data_path}")
        
        # Load stock data
        stock_data = pd.read_csv(data_path, parse_dates=['Date'])
        stock_data = stock_data.sort_values(by="Date")

        # Extract brand name from the file name (for labeling the plot)
        brand_name = os.path.basename(data_path).split('_')[0]  # Assumes the filename starts with the brand name

        # Debug: Check loaded data
        print(f"Dataset Loaded for {brand_name}:")
        print(stock_data.info())

        # Plot the stock data for the given company
        plot_stock_data(stock_data, brand_name, output_dir)

    except Exception as e:
        print(f"Error in script execution: {e}")

if __name__ == "__main__":
    # Set up argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="Plot stock data for a given company")
    parser.add_argument('data_file', type=str, help="Path to the stock data CSV file")
    args = parser.parse_args()

    # Run main function with the parsed arguments
    main(args)
