import streamlit as st
import yfinance
import schedule
from shared.trading import Trading

def app():
    st.title('Dashboard')
    
    symbols = 'SBIN.NS'
    # df = yfinance.download(symbols, period='1d', interval='1m')
    # st.write(df)
    
    # schedule.clear()
    # schedule.every().minutes.do(isMarketHours)
    
    # st.write(schedule.get_jobs())
    # while True:
        # schedule.run_pending()
        # time.sleep(1)
        