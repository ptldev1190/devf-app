import datetime as dt
import config
from shared import util

class Trading:

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

        # st.write(now)
        if now == startTime:
            util.notify('Market Opening time!')
        elif now == endTime:
            util.notify('Market Closing time!')

        if now >= startTime and now <= endTime:
            return True
        else:
            return False
