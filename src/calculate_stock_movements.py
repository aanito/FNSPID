import pandas as pd

def calculate_stock_movements(stock_file, output_file):
    stock_df = pd.read_csv(stock_file)
    stock_df['Daily_Return'] = stock_df['Close'].pct_change()
    stock_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate daily stock movements.")
    parser.add_argument("--stock_file", required=True, help="Path to the stock file.")
    parser.add_argument("--output_file", required=True, help="Output path for stock movements data.")
    args = parser.parse_args()

    calculate_stock_movements(args.stock_file, args.output_file)
