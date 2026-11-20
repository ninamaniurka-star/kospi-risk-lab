# KOSPI Risk Lab

**Live site:** https://ninamaniurka-star.github.io/kospi-risk-lab/
&nbsp;·&nbsp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ninamaniurka-star/kospi-risk-lab/blob/main/notebook/Monte_Carlo_KOSPI_VaR.ipynb)

Korea's market has been one of the wildest rides of 2026, carried up and dragged down by two chipmakers. This project asks what that volatility could cost a euro investor once you add the won on top.

A Monte Carlo Value-at-Risk model for a €100,000 portfolio of five KOSPI stocks (Samsung Electronics, SK Hynix, Hyundai Motor, NAVER, KB Financial) held by a euro-based investor, with EUR/KRW currency risk.

## What it does
- Estimates volatilities and the 6×6 covariance matrix from daily log returns
- Simulates correlated returns with geometric Brownian motion (Cholesky decomposition), Student-t fat tails, or historical bootstrap
- Reports 10-day VaR and Expected Shortfall, the currency's contribution, and each position's share of the tail loss
- Stress tests, a rolling VaR backtest with the Kupiec test, and a comparison of five VaR methods

## Contents
| Path | What it is |
|---|---|
| `index.html` | The interactive website (runs entirely in the browser) |
| `notebook/` | Python version with charts. Open it in Colab with the badge above |
| `excel/` | Excel version built with formulas only |
| `scripts/update_prices.py` | Downloads prices from Yahoo Finance |
| `.github/workflows/` | Updates the prices every weekday and republishes the site |

## Data
Prices come from Yahoo Finance (tickers 005930.KS, 000660.KS, 005380.KS, 035420.KS, 105560.KS, EURKRW=X) and refresh automatically each weekday. Educational project, not investment advice.

By Nina Maniurka
