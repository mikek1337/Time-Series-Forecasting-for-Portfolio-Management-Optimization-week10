## Notebook Contents (eda.ipynb)

The `eda.ipynb` notebook covers the following aspects:

- **Importing Libraries**: Essential libraries for data manipulation, plotting, and statistical tests.
    
- **Loading Dataset**: Loads historical data for BND, SPY, and TSLA from local CSV files.
    
- **Descriptive Statistics**: Provides summary statistics for each dataset.
    
- **Combining Datasets**: Merges the adjusted closing prices for comparative analysis.
    
- **Calculating Daily Returns**: Computes percentage changes to analyze volatility.
    
- **Augmented Dickey-Fuller (ADF) Test**: Performs stationarity tests on closing prices and daily returns.
    
- **Calculating Rolling Mean and Standard Deviation**: Computes 30-day rolling statistics for TSLA's returns to understand dynamic trends and volatility.
    
- **Calculating Sharpe Ratio and Value at Risk (VaR) for TSLA**: Quantifies risk-adjusted return and potential loss for Tesla stock.


## Notebook Contents (model.ipynb)

The `model.ipynb` notebook covers the following aspects:

- **Loading Dataset**: Loads historical data for BND, SPY, and TSLA from local CSV files.

- **Train models**: Trains ARIMA and LTSM model based on historical data
- **Optimize parameters**: using grid search to optimize parameters


## Notebook Contents (portfolio.ipynb)

- **Creating Portfoilo**: based on the model creating a portfolio
- **Backtestint**: Backtest on portfolio strategy and make summary


