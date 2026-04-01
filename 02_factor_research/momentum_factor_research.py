import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to analyze
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Parameters
lookback_days = 20
forward_days = 5

# Download close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
data = data.dropna(axis=1)

# Calculate momentum factor: past 20-day return
momentum = data.pct_change(periods=lookback_days)

# Calculate forward 5-day return
forward_returns = data.pct_change(periods=forward_days).shift(-forward_days)

high_group_returns = []
low_group_returns = []
dates = []

for date in momentum.index:
    factor_values = momentum.loc[date].dropna()
    future_values = forward_returns.loc[date].dropna()

    common_assets = factor_values.index.intersection(future_values.index)
    factor_values = factor_values.loc[common_assets]
    future_values = future_values.loc[common_assets]

    if len(common_assets) < 2:
        continue

    ranked = factor_values.sort_values(ascending=False)

    top_asset = ranked.index[0]
    bottom_asset = ranked.index[-1]

    high_group_returns.append(future_values[top_asset])
    low_group_returns.append(future_values[bottom_asset])
    dates.append(date)

results = pd.DataFrame({
    "High_Momentum_Forward_Return": high_group_returns,
    "Low_Momentum_Forward_Return": low_group_returns
}, index=dates)

results["Long_Short"] = (
    results["High_Momentum_Forward_Return"] - results["Low_Momentum_Forward_Return"]
)

summary = pd.DataFrame({
    "Average Forward Return": [
        results["High_Momentum_Forward_Return"].mean(),
        results["Low_Momentum_Forward_Return"].mean(),
        results["Long_Short"].mean()
    ]
}, index=["High Momentum", "Low Momentum", "Long-Short"])

print("Factor Research Summary:")
print(summary)

# Save results
results.to_csv("momentum_backtest_results.csv")
summary.to_csv("momentum_backtest_summary.csv")

# Plot cumulative returns
cumulative = (1 + results).cumprod()

cumulative.plot(figsize=(12, 6), title="Momentum Factor Research")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.tight_layout()
plt.savefig("momentum_factor_backtest.png", dpi=300)
plt.show()
