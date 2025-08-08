import pandas as pd
import yfinance as yf

class YfinanceWrapper:
    def __init__(self, tickers:list[str]) -> None:
        self.tickers = tickers

    def fetch_historical_data(self, start_date:str, end_date:str, output_dir:str="data"):
        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date, interval='1d', auto_adjust=False)
            if data is not None:
                data = data.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()
                data.to_csv(f'{output_dir}/{ticker}.csv')


if __name__ == "__main__":
    ticker_lst = ["BND", "TSLA","SPY"]
    finance = YfinanceWrapper(ticker_lst)
    finance.fetch_historical_data("2015-6-1", "2025-7-1")
