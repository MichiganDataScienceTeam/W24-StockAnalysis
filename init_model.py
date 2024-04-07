import streamlit as st

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import yfinance as yf
import pandas_ta as ta
import pickle

st.set_page_config(layout = "wide")

user_input = st.text_input("Input a stock ticker", "GOOG")

tick = yf.Ticker(user_input)

company_name = tick.info['longName']

data = yf.download(tickers = user_input)
# Explaination 

st.title("Initial Model")
st.markdown("""
            This is the initial model that was used as a baseline for learning tensorflow and getting aquainted with technical indicators
            """)





st.header("Initial Plots", divider="gray")
cc1, cc2 = st.columns([2.5,5])
with cc1:

    st.subheader("The Data")
    st.dataframe(data, height=250, width = 1000)


with cc2:
    st.subheader(f"Closing Prices of {company_name}")
    st.line_chart(data=data["Adj Close"])

st.header("Feature Engineering", divider="gray")
st.markdown("""
            testestesteststestestesteststestestestests testestesteststestestestests testestestests testestestests testestesteststestestestests 
            """)

data['RSI']=ta.rsi(data.Close, length=15)
data['EMAF']=ta.ema(data.Close, length=20)
data['EMAM']=ta.ema(data.Close, length=100)
data['EMAS']=ta.ema(data.Close, length=150)


data["OBV"] = ta.obv(data.Close, data.Volume)



data['Target'] = data['Adj Close']-data.Open
data['Target'] = data['Target'].shift(-1)
data['TargetClass'] = [1 if data.Target[i]>0 else 0 for i in range(len(data))]
data['TargetNextClose'] = data['Adj Close'].shift(-1)

data.dropna(inplace=True)
data.reset_index(inplace = True)
data.drop(['Volume', 'Close', 'Date'], axis=1, inplace=True)

cc3, cc4 = st.columns([4.5,5])
with cc3:
    st.code("""# Technical Indicators 
    data['RSI']=ta.rsi(data.Close, length=15)
    data['EMAF']=ta.ema(data.Close, length=20)
    data['EMAM']=ta.ema(data.Close, length=100)
    data['EMAS']=ta.ema(data.Close, length=150)
    data["OBV"] = ta.obv(data.Close, data.Volume)

    # Different Response Variables
    data['Target'] = data['Adj Close']-data.Open
    data['Target'] = data['Target'].shift(-1)
    data['TargetClass'] = [1 if data.Target[i]>0 else 0 for i in range(len(data))]
    data['TargetNextClose'] = data['Adj Close'].shift(-1)

    data.dropna(inplace=True)
    data.reset_index(inplace = True)
    data.drop(['Volume', 'Close', 'Date'], axis=1, inplace=True)
        """)

with cc4:
    st.dataframe(data)