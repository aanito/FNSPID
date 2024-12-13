import argparse
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

def analyze_publication_frequency(df):
    """
    Analyze publication frequency over time.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    publication_counts = df.groupby(df['date'].dt.date).size()
    return publication_counts

def plot_publication_frequency(publication_counts, output_path):
    """
    Plot the publication frequency over time.
    """
    plt.figure(figsize=(10, 6))
    publication_counts.plot(kind='line', title='Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid()
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze publication frequency over time.")
    parser.add_argument("--file", type=str, required=True, help="Path to the dataset CSV file.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the output plot.")
    args = parser.parse_args()

    df = load_data(args.file)
    publication_counts = analyze_publication_frequency(df)
    plot_publication_frequency(publication_counts, args.output)
