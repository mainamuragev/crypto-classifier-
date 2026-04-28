# Crypto Classifier – Data Extraction

This repository documents the process of extracting cryptocurrency market data from the Binance API.  
The extraction step provides the raw OHLCV (Open, High, Low, Close, Volume) data that forms the foundation of the ML pipeline.

---

## Process of Extraction

### 1. Project Setup
- Created project directories: `src/` for scripts and `data/raw/` for storing raw data.
- Initialized environment using **uv** for reproducible package management.
- Installed dependencies: `requests` and `pandas`.

### 2. Data Fetcher Script
- Implemented `src/data_fetcher.py`:
  - Connects to Binance API endpoint `/api/v3/klines`.
  - Retrieves OHLCV data for a chosen symbol and interval.
  - Converts JSON response into a pandas DataFrame.
  - Casts timestamps to datetime format and numeric fields to floats.
  - Drops unused fields.
  - Saves the cleaned DataFrame as a CSV file under `data/raw/`.

### 3. Running the Script
Executed in terminal with:
```bash
uv run python src/data_fetcher.py
```

### 4. Output
- Printed the first rows of BTCUSDT daily candles to terminal.
- Saved the dataset as:
```
data/raw/BTCUSDT_1d.csv
```

Example terminal preview:
```
Saved raw data to data/raw/BTCUSDT_1d.csv
   open_time      open      high  ...  num_trades  taker_base_volume  taker_quote_volume
0 2023-08-03  29186.00  29433.33  ...      651970        12901.09228        3.768567e+08
1 2023-08-04  29193.65  29333.08  ...      544850        10539.62903        3.072847e+08
...
```

---

## Current Status
The repository currently contains:
- Environment setup with uv
- Data fetcher script
- Successfully extracted and saved raw Binance OHLCV data

This completes the **data extraction step** of the project.
```
