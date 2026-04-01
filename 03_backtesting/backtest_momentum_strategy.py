import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to rotate
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Parameters
lookback_days = 20

# Download close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
data = data.dropna(axis=1)

# Calculate daily returns
daily_returns = data.pct_change(fill_method=None)

# Calculate momentum signal
momentum = data.pct_change(periods=lookback_days)

# Strategy: each day hold the asset with the highest momentum
selected_assets = momentum.idxmax(axis=1)

strategy_returns = []

for i in range(len(data)):
    if i < lookback_days:
        strategy_returns.append(0)
        continue

    date = data.index[i]
    chosen_asset = selected_assets.loc[date]
    asset_return = daily_returns.loc[date, chosen_asset]

    if pd.isna(asset_return):
        strategy_returns.append(0)
    else:
        strategy_returns.append(asset_return)

strategy = pd.Series(strategy_returns, index=data.index, name="Strategy")
benchmark = daily_returns["SPY"].fillna(0)
benchmark.name = "SPY"

results = pd.concat([strategy, benchmark], axis=1)
cumulative = (1 + results).cumprod()

summary = pd.DataFrame({
    "Total Return": cumulative.iloc[-1] - 1,
    "Volatility": results.std(),
    "Mean Daily Return": results.mean()
})

print("Backtest Summary:")
print(summary)

# Save outputs
results.to_csv("backtest_daily_returns.csv")
summary.to_csv("backtest_summary.csv")

# Plot cumulative returns
cumulative.plot(figsize=(12, 6), title="Momentum Strategy Backtest vs SPY")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.tight_layout()
plt.savefig("momentum_strategy_backtest.png", dpi=300)
plt.show()
