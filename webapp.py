
import yfinance   as yf
import streamlit  as st
import pandas     as pd
import sys

st.write("""
# Simple Stock Price App
## Courtesy of Developex Ltd
Charts below show the closing price and volume of Google
""")

# Manual list of tickers
options = ['TSLA', 'GOOGL', 'MSFT', 'META', 'NVDA', 'AMD']

# Create drop-down list
tickerSymbol = st.selectbox('Select a ticker', options)


# Get data on selected ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for chosen ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-3-3')
# Open  High  Low Close   Volume  Dividends   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

if st.button('Exit'):
    st.stop()