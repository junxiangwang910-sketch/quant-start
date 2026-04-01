import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to analyze
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Download adjusted close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]

# Remove assets with missing data
data = data.dropna(axis=1)

# Calculate daily returns
returns = data.pct_change(fill_method=None).dropna()

# Summary statistics
summary = pd.DataFrame({
    "Mean Return": returns.mean(),
    "Volatility": returns.std(),
    "Total Return": (data.iloc[-1] / data.iloc[0]) - 1
})

# Correlation matrix
correlation = returns.corr()

# Print results
print("Summary Statistics:")
print(summary)

print("\nCorrelation Matrix:")
print(correlation)

# Save tables
summary.to_csv("summary_statistics.csv")
correlation.to_csv("correlation_matrix.csv")

# Plot normalized prices
normalized = data / data.iloc[0]
normalized.plot(figsize=(12, 6), title="Normalized Price Trends")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.grid(True)

# Save chart
plt.savefig("normalized_price_trends.png", dpi=300, bbox_inches="tight")
plt.show()
