import pandas as pd
import yfinance as yf
import streamlit as st
import stocks

# Define the function to get S&P 500 tickers
def get_sp500_tickers():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df.Symbol.tolist()

# Define the function to get stock data and calculate the standard deviation
def get_data(ticker):
    stock_data = yf.download(ticker)
    volume_std = stock_data['Volume'].std()
    return stock_data, volume_std

# Define the Streamlit app layout
st.write("""
# S&P 500 Trading Volume Alert App
""")

# Get the S&P 500 tickers
tickers = get_sp500_tickers()

# Loop through each ticker and check if the volume deviates from the standard deviation
alert_tickers = []
for ticker in tickers:
    try:
        stock_data, volume_std = get_data(ticker)
        last_volume = stock_data['Volume'][-1]
        if last_volume > volume_std:
            alert_tickers.append(ticker)
    except:
        pass

# Display the list of alert tickers
st.write(f"### Alert: {len(alert_tickers)} stocks deviate from the standard deviation!")
st.write(alert_tickers)

#Closing Message

st.write('This list of tickers represents unusual volume activity. This can mean many things and is only an indiciation of heavy movement in the market.')