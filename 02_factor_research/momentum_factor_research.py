import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to analyze
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Download close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
data = data.dropna(axis=1)

# Define momentum factor as past 20-day return
momentum = data.pct_change(periods=20)

# Use the most recent available momentum values
latest_momentum = momentum.iloc[-1].sort_values(ascending=False)

# Calculate forward 5-day return for illustration
forward_returns = data.pct_change(periods=5).shift(-5)
latest_forward_returns = forward_returns.iloc[-6]

# Combine into one table
results = pd.DataFrame({
    "Momentum_20D": latest_momentum,
    "Forward_5D_Return": latest_forward_returns.reindex(latest_momentum.index)
})

print("Momentum Factor Ranking:")
print(results)

# Save results
results.to_csv("momentum_factor_results.csv")

# Plot factor values
latest_momentum.plot(kind="bar", figsize=(10, 6), title="20-Day Momentum Factor")
plt.ylabel("Momentum")
plt.xlabel("Ticker")
plt.grid(True)
plt.tight_layout()
plt.savefig("momentum_factor_chart.png", dpi=300)
plt.show()
