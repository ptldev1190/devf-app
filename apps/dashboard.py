import streamlit as st
import yfinance

def app():
    st.title('Dashboard')
    
    symbols = 'SBIN.NS'
    st.write(symbols)
    # df = yfinance.download(symbols, period='1d', interval='1m')
    # st.write(df)
