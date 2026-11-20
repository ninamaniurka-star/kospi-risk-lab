"""Download daily closes for the 5 KOSPI stocks and EUR/KRW and save data/kospi_prices.csv.
Run by the GitHub Action every weekday; keeps the old file if the download fails."""
import sys
from pathlib import Path
import pandas as pd
import yfinance as yf

TICKERS = {"005930.KS": "Samsung Electronics", "000660.KS": "SK Hynix", "005380.KS": "Hyundai Motor",
           "035420.KS": "NAVER", "105560.KS": "KB Financial"}
FX = "EURKRW=X"
OUT = Path(__file__).resolve().parents[1] / "data" / "kospi_prices.csv"

try:
    raw = yf.download(list(TICKERS) + [FX], period="3y", auto_adjust=True, progress=False)["Close"]
    raw[FX] = raw[FX].ffill()                         # FX trades on Korean holidays
    px = raw.dropna(subset=list(TICKERS)).dropna()[list(TICKERS) + [FX]]
    px.columns = list(TICKERS.values()) + ["EUR/KRW"]
    if len(px) < 250:
        raise ValueError(f"only {len(px)} rows")
except Exception as e:
    print(f"Download failed, keeping previous file: {e}")
    sys.exit(0)

OUT.parent.mkdir(exist_ok=True)
px.round(4).to_csv(OUT, index_label="Date", date_format="%Y-%m-%d")
print(f"Saved {len(px)} rows to {OUT}, last date {px.index[-1]:%Y-%m-%d}")
