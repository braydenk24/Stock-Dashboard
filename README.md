# Stock-Dashboard
This web app provides financial data (mostly pricing) regarding any stock in the S&P 500
The Trader Radar Page shows unusual trading volume for all stocks in the S&P 500
the program is using the data from the nearest closing volume for each stock in the S&P 500. The yf.download() function from the yfinance library retrieves historical stock data, including the volume, based on the current date and time when the program is run. If the program is run during closing market hours, it will retrieve the volume data for the most recent closing session.

However, it's worth noting that the volume data for the current trading session will not be available until after the market closes. So, if the program is run during market hours, it will not have access to the latest volume data for the current session. It will only have access to the data from the most recent closing session. 
