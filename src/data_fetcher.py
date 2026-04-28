import requests
import pandas as pd
import os

def fetch_binance(symbol="BTCUSDT", interval="1d", limit=1000, save=True):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    df = pd.DataFrame(data, columns=[
        "open_time","open","high","low","close","volume",
        "close_time","quote_asset_volume","num_trades",
        "taker_base_volume","taker_quote_volume","ignore"
    ])
    
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
    numeric_cols = ["open","high","low","close","volume",
                    "quote_asset_volume","taker_base_volume","taker_quote_volume"]
    df[numeric_cols] = df[numeric_cols].astype(float)
    df = df.drop(columns=["ignore"])
    
    if save:
        os.makedirs("data/raw", exist_ok=True)
        file_path = f"data/raw/{symbol}_{interval}.csv"
        df.to_csv(file_path, index=False)
        print(f"Saved raw data to {file_path}")
    
    return df

if __name__ == "__main__":
    df = fetch_binance(symbol="BTCUSDT", interval="1d", limit=1000)
    print(df.head())
