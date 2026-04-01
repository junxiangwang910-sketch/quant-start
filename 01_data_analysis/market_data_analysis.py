import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to analyze
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Download adjusted close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]

# Calculate daily returns
returns = data.pct_change().dropna()

# Summary statistics
summary = pd.DataFrame({
    "Mean Return": returns.mean(),
    "Volatility": returns.std(),
    "Total Return": (data.iloc[-1] / data.iloc[0]) - 1
})

print("Summary Statistics:")
print(summary)

# Plot normalized prices
normalized = data / data.iloc[0]
normalized.plot(figsize=(12, 6), title="Normalized Price Trends")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.grid(True)
plt.show()

# Plot correlation heatmap
correlation = returns.corr()
print("\nCorrelation Matrix:")
print(correlation)
