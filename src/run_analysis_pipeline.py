import os
import subprocess

def run_pipeline(news_file, stock_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Normalize dates
    normalized_news = f"{output_dir}/normalized_news.csv"
    normalized_stock = f"{output_dir}/normalized_stock.csv"
    subprocess.run([
        "python", "src/normalize_dates.py",
        "--news_file", news_file,
        "--stock_file", stock_file,
        "--output_news_file", normalized_news,
        "--output_stock_file", normalized_stock
    ])

    # Step 2: Perform sentiment analysis
    sentiment_file = f"{output_dir}/sentiment_results.csv"
    subprocess.run([
        "python", "src/sentiment_analysis.py",
        "--news_file", normalized_news,
        "--output_file", sentiment_file
    ])

    # Step 3: Calculate stock movements
    stock_movements_file = f"{output_dir}/stock_movements.csv"
    subprocess.run([
        "python", "src/calculate_stock_movements.py",
        "--stock_file", normalized_stock,
        "--output_file", stock_movements_file
    ])

    # Step 4: Perform correlation analysis
    final_output = f"{output_dir}/final_results.csv"
    subprocess.run([
        "python", "src/correlation_analysis.py",
        "--sentiment_file", sentiment_file,
        "--stock_file", stock_movements_file,
        "--output_file", final_output
    ])
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run the full financial sentiment analysis pipeline.")
    parser.add_argument("--news_file", required=True, help="Path to the news dataset.")
    parser.add_argument("--stock_file", required=True, help="Path to the stock dataset.")
    parser.add_argument("--output_dir", required=True, help="Directory to save outputs.")
    args = parser.parse_args()

    run_pipeline(args.news_file, args.stock_file, args.output_dir)
