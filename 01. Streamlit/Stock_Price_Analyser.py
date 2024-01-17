import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser
    """
)

ticker_symbol = st.text_input("Enter Stock Symbol", "GOOG", key="placeholder")
data = yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter the start date", datetime.date(2023, 1, 1))

with col2:
    end_date = st.date_input("Enter the end date", datetime.date(2023, 12, 31))

st.write(f"""
          ###  {ticker_symbol}'s daily stock prices
""")

df = data.history(period="1d", start=f"{start_date}", end=f"{end_date}")
st.dataframe(df)

# Showcasing chart
st.write("## Daily closing price chart")
st.line_chart(df.Close)

st.write("## Volume of shares trades each day")
st.line_chart(df.Volume)