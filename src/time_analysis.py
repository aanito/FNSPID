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

def analyze_trends_over_time(df):
    """
    Analyze publication trends over time based on the article dates.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    trends = df.groupby(df['date'].dt.date).size()
    return trends

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze publication trends over time in the financial news dataset.")
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
    trends = analyze_trends_over_time(df)
    print("Publication Trends Over Time:\n", trends)