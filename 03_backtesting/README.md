# 03 Backtesting

This project is my first beginner-friendly backtesting project in quantitative trading.

## Research Goal

The goal of this project is to turn a simple momentum signal into a trading strategy and test how it would have performed over time.

## Strategy Idea

This project uses a simple momentum rotation rule:

- calculate 20-day momentum for each asset
- select the asset with the highest momentum
- hold that asset for the next trading day
- repeat the process through time

The strategy is compared against a benchmark:

- SPY buy-and-hold

## Assets Analyzed

- SPY
- QQQ
- AAPL
- MSFT
- NVDA

## Methodology

The backtest follows these steps:

1. Download historical daily close prices
2. Compute daily returns
3. Compute 20-day momentum for each asset
4. Select the highest-momentum asset on each date
5. Use that signal to build a daily strategy return series
6. Compare strategy performance with SPY

## Files

- `backtest_momentum_strategy.py`: main backtesting script
- `requirements.txt`: required Python packages
- `backtest_daily_returns.csv`: daily strategy and benchmark returns
- `backtest_summary.csv`: strategy summary statistics
- `momentum_strategy_backtest.png`: cumulative return chart

## Results

The backtest outputs two main return series:

- `Strategy`: daily returns from the momentum rotation rule
- `SPY`: benchmark daily returns from buy-and-hold SPY

The cumulative return chart shows how the strategy performed relative to the benchmark through time.

## Key Observation

In this sample period, the simple momentum strategy outperformed the SPY benchmark.

However, this result should be interpreted carefully because the backtest is still highly simplified.

## Limitations

This is only a beginner-level backtest, so several important real-world factors are not included:

- no transaction costs
- no slippage
- no portfolio constraints
- no turnover analysis
- small asset universe
- short backtest period

Because of these limitations, the result should be seen as a learning exercise rather than a production-ready strategy.

## Next Improvements

Possible future upgrades include:

- add transaction costs
- test different rebalance frequencies
- expand the asset universe
- compare multiple strategy rules
- evaluate drawdown and Sharpe ratio

## Status

- [x] Create backtesting script
- [x] Download market data
- [x] Define trading rule
- [x] Simulate strategy returns
- [x] Plot cumulative returns
- [x] Compare with benchmark
