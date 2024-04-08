import requests
import pandas as pd


def get_data(symbol):
    alphavantageurl = "https://www.alphavantage.co/query"
    API_KEY = "UKVFE0JLE0TBPDEF"

    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "15min",
        "apikey": API_KEY
    }

    resp = requests.get(alphavantageurl, params=params)

    df = pd.DataFrame(resp.json()['Time Series (15min)']).transpose()
    df['symbol'] = symbol
    return df


def clean_data(data):
    cols = [c for c in data.columns if c != 'symbol']
    newnames = [c[2:] for c in cols]
    newnames = [c.strip() for c in newnames]
    df = data.rename(columns=dict(zip(cols, newnames)))
    for c in newnames:
        df[c] = pd.to_numeric(df[c])

    return df


def combined_daily_time_series(symbols):
    dfs = []
    for s in symbols:
        dfs.append(clean_data(get_data(s)))
    return pd.concat(dfs)


def get_total_volume(combined_data):
    return combined_data.groupby('symbol')['volume'].sum()
