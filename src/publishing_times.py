import argparse
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)

def analyze_publishing_times(df):
    """
    Analyze the distribution of publishing times.
    """
    df['date'] = pd.to_datetime(df['Date'], errors='coerce')
    publishing_times = df.groupby(df['date'].dt.hour).size()
    return publishing_times

def plot_publishing_times(publishing_times, output_path):
    """
    Plot the distribution of publishing times.
    """
    plt.figure(figsize=(10, 6))
    publishing_times.plot(kind='bar', color='skyblue', title='Publishing Times Distribution')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze publishing times in the dataset.")
    parser.add_argument("--file", type=str, required=True, help="Path to the dataset CSV file.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the output plot.")
    args = parser.parse_args()

    df = load_data(args.file)
    publishing_times = analyze_publishing_times(df)
    plot_publishing_times(publishing_times, args.output)
