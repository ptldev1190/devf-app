import schedule
import time
import datetime as dt
from shared import util
from shared.trading import Trading

def tradingRun():
    print(Trading.getRealData())
    util.notify('Trading on @ ' + str(dt.datetime.now()))

def tradingStart():
    util.notify('Trading stared @ ' + str(dt.datetime.now()))
    schedule.every(15).minutes.at(":01").do(tradingRun).tag('trading')

def tradingEnd():
    util.notify('Trading ended @ ' + str(dt.datetime.now()))
    schedule.clear('trading')

schedule.clear()
schedule.every().day.at("09:15").do(tradingStart).tag('start')
schedule.every().day.at("15:31").do(tradingEnd).tag('end')
print("Trading Schedule Running... Don't Stop!!")

while True:
    schedule.run_pending()
    time.sleep(1)
    # jobs = schedule.get_jobs()
    # print(jobs)
