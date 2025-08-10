import pandas as pd
import yfinance as yf

class YfinanceWrapper:
    """
    A wrapper class to fetch historical stock data using yfinance.
    """
    def __init__(self, tickers:list[str]) -> None:
        """
        Initializes the YfinanceWrapper with a list of stock tickers.

        Args:
            tickers (list[str]): A list of ticker symbols (e.g., ["BND", "TSLA", "SPY"]).
        """
        self.tickers = tickers

    def fetch_historical_data(self, start_date:str, end_date:str, output_dir:str="data"):
        """
        Fetches historical daily data for all initialized tickers and saves each to a CSV file.

        Args:
            start_date (str): The start date for data fetching in 'YYYY-MM-DD' format.
            end_date (str): The end date for data fetching in 'YYYY-MM-DD' format.
            output_dir (str, optional): The directory where the CSV files will be saved.Defaults to data."""
        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date, interval='1d', auto_adjust=False)
            if data is not None:
                data = data.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()
                data.to_csv(f'{output_dir}/{ticker}.csv')


if __name__ == "__main__":
    ticker_lst = ["BND", "TSLA","SPY"]
    finance = YfinanceWrapper(ticker_lst)
    finance.fetch_historical_data("2015-6-1", "2025-7-1")
