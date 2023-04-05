import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.express as px
from stocknews import StockNews



#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()


st.title('Stock Display')
st.text('This web app displays stock prices from companies in the S&P 500')
st.text('Select a ticker and any time frame desired~')
st.markdown('Additionally, the **Trader Radar** will display tickers with unusual volume deviations from the mean')

#variable declaration
ticker = st.text_input('Ticker')
startDate = st.date_input('Start Date')
endDate = st.date_input('End Date')

#Daily Percent Change
#TRY TO ADD!!!!!


if ticker:

    #Graph
    data = yf.download(ticker,start=startDate, end=endDate)
    fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
    st.plotly_chart(fig)


    #Pricing Data, Fundamental Data, News

    pricingData, fundamentalData, news = st.tabs(["Pricing Data", "Fundamental Data", "Relevant News"])

    with pricingData:
        st.write('Pricing Information')
        daily=data
        daily['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1)-1
        annualReturn = daily['% Change'].mean()*252*100
        st.write('Annual Return:' , annualReturn, '%')
        st.write(daily)
    with fundamentalData:
        st.write('Fundamental')

    with news:
        sn = StockNews(ticker, save_news=False)
        df_news = sn.read_rss()
        for i in range (7):
       
            st.subheader(df_news['title'][i])
            article_name = df_news['title'][i].replace(" ", "-").lower() + ".html" # replace spaces with hyphens and convert to lowercase
            st.write(f"[Link to article]({'https://finance.yahoo.com/m/' + df_news['guid'][i] + article_name})") # add hyperlink to title
            #st.write(f"[Link to article]({df_news['guid'][i] + article_name})")
            st.write(df_news['summary'][i])
            title_sentiment = df_news['sentiment_title'][i]
            st.write(f'Title Sentiment {title_sentiment}')
            news_sentiment = df_news['sentiment_summary'][i]
            st.write(f'News Sentiment {news_sentiment}')


