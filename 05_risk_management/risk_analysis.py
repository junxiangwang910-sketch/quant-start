import pandas as pd
import matplotlib.pyplot as plt

# Load strategy return data from the previous project
data = pd.read_csv("../04_strategy_development/strategy_daily_returns.csv", index_col=0, parse_dates=True)

strategy = data["Strategy"]
benchmark = data["SPY"]

results = pd.DataFrame({
    "Strategy": strategy,
    "SPY": benchmark
})

# Cumulative returns
cumulative = (1 + results).cumprod()

# Drawdown
drawdown = cumulative / cumulative.cummax() - 1

# Rolling volatility (20-day)
rolling_volatility = results.rolling(20).std()

# Simple Sharpe ratio approximation
sharpe = results.mean() / results.std()

# Max drawdown
max_drawdown = drawdown.min()

summary = pd.DataFrame({
    "Mean Daily Return": results.mean(),
    "Volatility": results.std(),
    "Sharpe Approx": sharpe,
    "Max Drawdown": max_drawdown
})

print("Risk Analysis Summary:")
print(summary)

# Save outputs
summary.to_csv("risk_summary.csv")
drawdown.to_csv("drawdown_series.csv")
rolling_volatility.to_csv("rolling_volatility.csv")

# Plot drawdown
drawdown.plot(figsize=(12, 6), title="Strategy vs SPY Drawdown")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.grid(True)
plt.tight_layout()
plt.savefig("drawdown_chart.png", dpi=300)
plt.show()

# Plot rolling volatility
rolling_volatility.plot(figsize=(12, 6), title="Rolling 20-Day Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.grid(True)
plt.tight_layout()
plt.savefig("rolling_volatility_chart.png", dpi=300)
plt.show()
