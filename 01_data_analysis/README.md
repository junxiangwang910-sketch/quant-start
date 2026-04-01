# 01 Data Analysis

This project is my first quantitative trading practice project.  
It focuses on downloading historical market data, calculating basic return metrics, and visualizing asset performance.

## Objective

- Download historical market data
- Compute returns, volatility, and total return
- Visualize normalized price trends
- Examine correlations between assets

## Assets Analyzed

- SPY
- QQQ
- AAPL
- MSFT
- NVDA

## Tools Used

- Python
- yfinance
- pandas
- matplotlib

## Files

- `market_data_analysis.py`: main analysis script
- `requirements.txt`: required Python packages
- `summary_statistics.csv`: summary statistics for each asset
- `correlation_matrix.csv`: correlation matrix of daily returns
- `normalized_price_trends.png`: normalized price trend chart

## Results

The script calculates:

- Mean daily return
- Volatility
- Total return
- Correlation matrix across selected assets

It also generates a normalized price chart to compare performance over time.

## Key Observation

In this sample period, NVDA showed the strongest total return, while SPY had relatively lower volatility and lower overall return.

## Status

- [x] Create first Python script
- [x] Download market data
- [x] Calculate return metrics
- [x] Plot normalized price trends
- [x] Save output files
