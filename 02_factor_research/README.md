# 02 Factor Research

This project is my first beginner-friendly factor research project in quantitative trading.

## Research Question

Can a simple momentum factor help identify assets with stronger short-term future returns?

## Factor Definition

This project uses a **20-day momentum factor**:

- Momentum = past 20-day return

A higher factor value means the asset performed better over the past 20 trading days.

## Assets Analyzed

- SPY
- QQQ
- AAPL
- MSFT
- NVDA

## Methodology

This project tests momentum in two stages.

### Stage 1: Single-Point Ranking

First, I calculate the latest 20-day momentum value for each asset and rank them from strongest to weakest.

### Stage 2: Rolling Factor Research

Then I extend the analysis into a simple rolling test:

- For each date, calculate the 20-day momentum factor
- Identify the highest-momentum asset
- Identify the lowest-momentum asset
- Compare their forward 5-day returns
- Build a long-short series:
  - Long high-momentum asset
  - Short low-momentum asset

This makes the project closer to a real factor research workflow.

## Files

- `momentum_factor_research.py`: main factor research script
- `requirements.txt`: required Python packages
- `momentum_backtest_results.csv`: detailed rolling test results
- `momentum_backtest_summary.csv`: summary statistics for the factor test
- `momentum_factor_backtest.png`: cumulative return chart

## Results

The project compares three return series:

- `High_Momentum_Forward_Return`
- `Low_Momentum_Forward_Return`
- `Long_Short`

The cumulative return chart helps visualize whether high-momentum assets outperform low-momentum assets over time.

## Key Observation

In this small sample, the high-momentum group generally performed better than the low-momentum group for part of the test period.

However, the long-short spread was not consistently strong throughout the full sample. This suggests that the simple momentum signal may work in some periods, but is not always stable.

## Limitations

This is only a beginner-level research project, so it has several limitations:

- Only a small number of assets were tested
- The universe is not broad enough for a robust factor study
- The test period is short
- Transaction costs and slippage are ignored
- Portfolio construction is simplified to one top asset versus one bottom asset

## Next Steps

Possible improvements for future versions:

- Expand the asset universe
- Test multiple lookback windows
- Use portfolio groups instead of only top vs bottom
- Add transaction cost assumptions
- Compare momentum with other factors

## Status

- [x] Create factor research script
- [x] Download market data
- [x] Calculate momentum factor
- [x] Rank assets by factor
- [x] Run a rolling factor test
- [x] Save research outputs
