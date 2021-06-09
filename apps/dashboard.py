import streamlit as st
import yfinance
import schedule
import datetime as dt
import time
import config


def app():
    st.title('Dashboard')

    symbols = 'SBIN.NS'
    # df = yfinance.download(symbols, period='1d', interval='1m')
    # st.write(df)
    
    schedule.clear()
    schedule.every().minutes.do(isMarketHours)
    
    st.write(schedule.get_jobs())
    # while True:
        # schedule.run_pending()
        # time.sleep(1)


def isMarketHours():
    # Current time
    now = dt.datetime.now()
    # Today's date
    today = dt.datetime.now().strftime('%Y-%m-%d')
    # Start & End time string
    todayStartTime = today + ' ' + config._trading_start_time
    todayEndTime = today + ' ' + config._trading_end_time
    # Actual Start & End time for today
    startTime = dt.datetime.strptime(todayStartTime, '%Y-%m-%d %H:%M:%S')
    endTime = dt.datetime.strptime(todayEndTime, '%Y-%m-%d %H:%M:%S')

    st.write(now)
    if now >= startTime and now <= endTime:
        st.write('Market Online')
    else:
        st.write('Ssshhh...')
    