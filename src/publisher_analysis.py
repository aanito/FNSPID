import argparse
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified file path.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

def analyze_most_active_publishers(df):
    """
    Count the number of articles per publisher and identify the most active ones.
    """
    publisher_counts = df['publisher'].value_counts()
    return publisher_counts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze the most active publishers in the financial news dataset.")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the dataset CSV file (data/raw/raw_analyst_ratings.csv).",
    )
    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)

    # Perform analysis
    publisher_counts = analyze_most_active_publishers(df)
    print("Most Active Publishers:\n", publisher_counts)
