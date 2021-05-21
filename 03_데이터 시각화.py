import yfinance as yf
import datetime
import streamlit as st
import plotly.graph_objects as go

"""
# 주식 데이터 시각화
"""

ticker = st.text_input("티커 입력")
# ticker = "GOOGL"

data = yf.Ticker(ticker)
df = data.history(period='1d', start='2015-1-1', end=datetime.datetime.today().strftime("%Y-%m-%d"))

print(df)
"## 주가"
# st.line_chart(df["Close"])
layout = go.Layout(yaxis = {"fixedrange":False})
data = go.Candlestick(x=df.index,
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])
fig = go.Figure(data=[data], layout=layout)
st.plotly_chart(fig)

"## 거래량"
st.bar_chart(df["Volume"])

