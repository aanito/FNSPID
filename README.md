# Financial News Dataset Analysis

## Overview

This project analyzes financial news articles to extract insights such as:

1. Headline length statistics.
2. Publisher activity.
3. Trends in publication frequency.

## Installation

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

## Usage Instructions

### Running Analysis Scripts

Each script accepts a `--file` argument to specify the dataset path.

python3 src/text_statistics.py --file data/raw/raw_analyst_ratings.csv

Tasks

Sentiment Analysis

Objective: Gauge the sentiment (positive, negative, neutral) associated with the news headlines.

Steps Undertaken
Dataset Loading: The dataset was loaded into a pandas DataFrame for processing. The headline column contained the text data for sentiment analysis.
Preprocessing: Headlines were cleaned by removing punctuation, numbers, and converting them to lowercase.
Sentiment Analysis: The TextBlob library was used to compute sentiment polarity scores. Based on the polarity:
Polarity > 0: Positive
Polarity < 0: Negative
Polarity = 0: Neutral
Result: Each headline was labeled with its respective sentiment.

Keyword and Phrase Extraction

Objective: Identify common keywords, phrases, and significant events like "FDA approval" or "price target."

Steps Undertaken
Tokenization: Headlines were split into words using the nltk library.
Stopword Removal: Common stopwords (e.g., "the", "and") were removed to focus on meaningful words.
Keyword Extraction: The most frequent words were identified using term frequency.
Phrase Extraction: The RAKE (Rapid Automatic Keyword Extraction) algorithm was employed to extract relevant phrases.
Topic Clustering: The Latent Dirichlet Allocation (LDA) model was used to group similar phrases into topics.

Analysis of Publication Frequency and Publishing Times

Objective

Publication Frequency Over Time: To determine variations in publication frequency and identify spikes related to specific market events.
Analysis of Publishing Times: To examine if there’s a specific time when most news is released and derive insights for traders or automated systems.

Steps Undertaken

1. Publication Frequency Over Time
   Data Preprocessing:
   Loaded the dataset and converted the date column to a datetime format.
   Extracted the publication year, month, and day.
   Aggregation:
   Grouped data by date and counted the number of articles published on each date.
   Visualization:
   Created a time-series plot to observe patterns and spikes over time.
   Annotated significant spikes with possible market events for better insights.

2. Analysis of Publishing Times
   Data Preprocessing:
   Extracted the hour from the date column to understand time-based publication trends.
   Aggregation:
   Grouped data by hour and counted articles published during each hour of the day.
   Visualization:
   Created a bar chart showing the distribution of articles by publishing time.

Results Presentation

Publication Frequency: The time-series chart highlighted periods of increased news activity, often aligning with significant market events like earnings seasons or major regulatory announcements.
Publishing Times: The bar chart revealed peak publishing times, typically clustered around the start of trading hours and during market-close summaries.

Analysis of Publisher Contributions and Unique Domains in the News Feed

Objective
Publisher Contributions: Identify which publishers contribute the most to the news feed and examine differences in the type of news they report.
Domain Analysis: If publisher names are email addresses, extract and analyze unique domains to identify organizations contributing frequently.
Steps Undertaken

1. Publisher Contributions
   Data Preprocessing:
   The publisher column was examined to identify the unique names of publishers.
   Counts of articles per publisher were calculated to rank publishers based on their contribution.
   News Type Analysis:
   Articles were grouped by publisher, and the headline text was analyzed for sentiment and keywords using the earlier scripts.
   Publishers were categorized based on the tone of their content (e.g., positive, negative) and common keywords.
2. Domain Analysis
   Email Identification:
   Checked if publisher names in the publisher column resembled email addresses (e.g., using a regex pattern).
   Domain Extraction:
   Extracted the domain portion of email addresses (e.g., "example.com" from "user@example.com").
   Counted the frequency of each domain to identify prominent contributors.
   Visualization and Presentation
   Created bar charts to display:
   Top contributing publishers.
   Top contributing domains (if applicable).
   Included a table summarizing publisher contributions alongside sentiment and keyword insights

Quantitative Analysis of Stock Price Data Using PyNance and TA-Lib
Objective
The analysis aimed to:

Load and prepare stock price data for seven independent brands.
Apply technical analysis indicators using TA-Lib.
Use PyNance to compute financial metrics.
Visualize stock price trends and the impact of technical indicators on price movements.
Steps Undertaken

1. Data Loading and Preparation
   The stock price data, including columns like Open, High, Low, Close, Adj Close, Volume, Dividends, and Stock Splits, was loaded into a pandas DataFrame.
   Data was validated for missing or inconsistent values:
   Missing values were imputed using forward fill and backfill techniques.
   Ensured consistent column formatting across datasets.
   Each brand's dataset was appended with a Stock Symbol column to identify the respective brand.
2. Technical Analysis Indicators Using TA-Lib
   Installed and imported the TA-Lib library to calculate key indicators:
   Moving Averages (e.g., 50-day and 200-day SMA).
   Relative Strength Index (RSI) to measure momentum.
   Moving Average Convergence Divergence (MACD) to assess price trends.
   Added calculated indicators as new columns in the DataFrame.
3. Financial Metrics Using PyNance
   PyNance was employed to calculate additional metrics:
   Sharpe Ratio to evaluate risk-adjusted returns.
   Volatility to assess stock price fluctuations.
   Consolidated metrics into summary tables for each brand.
4. Visualization
   Used Matplotlib and Seaborn to create visualizations:
   Line plots to show stock prices over time.
   Overlay of technical indicators (e.g., RSI and MACD) on stock price charts.
   Heatmaps to depict correlations between indicators and price movements.

Results
Technical Indicators:

SMA: Highlighted key trends and crossovers, providing buy/sell signals.
RSI: Identified overbought (>70) and oversold (<30) levels.
MACD: Indicated momentum shifts.
