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

def compute_headline_stats(df):
    """
    Compute basic statistics for headline lengths.
    """
    df['headline_length'] = df['headline'].apply(len)
    return df['headline_length'].describe()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze headline lengths in a financial news dataset.")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the dataset CSV file (e.g., data/raw/raw_analyst_ratings.csv).",
    )
    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)

    # Perform analysis
    stats = compute_headline_stats(df)
    print("Headline Length Statistics:\n", stats)


# import pandas as pd

# def compute_headline_stats(df):
#     """
#     Computes basic statistics for headline lengths.
#     """
#     df['headline_length'] = df['headline'].apply(len)
#     stats = {
#         'mean': df['headline_length'].mean(),
#         'median': df['headline_length'].median(),
#         'std_dev': df['headline_length'].std(),
#         'max': df['headline_length'].max(),
#         'min': df['headline_length'].min(),
#     }
#     return stats
