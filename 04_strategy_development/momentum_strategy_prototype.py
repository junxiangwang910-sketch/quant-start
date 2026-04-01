import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Assets to rotate
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

# Parameters
lookback_days = 20
rebalance_frequency = 5

# Download close prices
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
data = data.dropna(axis=1)

# Daily returns
daily_returns = data.pct_change(fill_method=None).fillna(0)

# Momentum signal
momentum = data.pct_change(periods=lookback_days)

selected_assets = []
strategy_returns = []
current_asset = "SPY"

for i in range(len(data)):
    date = data.index[i]

    if i < lookback_days:
        selected_assets.append(current_asset)
        strategy_returns.append(0)
        continue

    # Rebalance every 5 trading days
    if (i - lookback_days) % rebalance_frequency == 0:
        ranked = momentum.iloc[i].dropna().sort_values(ascending=False)
        if len(ranked) > 0:
            current_asset = ranked.index[0]

    selected_assets.append(current_asset)
    strategy_returns.append(daily_returns.loc[date, current_asset])

strategy = pd.Series(strategy_returns, index=data.index, name="Strategy")
benchmark = daily_returns["SPY"]
benchmark.name = "SPY"

results = pd.concat([strategy, benchmark], axis=1)
cumulative = (1 + results).cumprod()

# Basic metrics
max_drawdown = (cumulative / cumulative.cummax() - 1).min()
summary = pd.DataFrame({
    "Total Return": cumulative.iloc[-1] - 1,
    "Volatility": results.std(),
    "Mean Daily Return": results.mean(),
    "Max Drawdown": max_drawdown
})

positions = pd.DataFrame({
    "Selected_Asset": selected_assets
}, index=data.index)

print("Strategy Prototype Summary:")
print(summary)

# Save outputs
results.to_csv("strategy_daily_returns.csv")
summary.to_csv("strategy_summary.csv")
positions.to_csv("strategy_positions.csv")

# Plot cumulative returns
cumulative.plot(figsize=(12, 6), title="Strategy Prototype vs SPY")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.tight_layout()
plt.savefig("strategy_prototype_backtest.png", dpi=300)
plt.show()
