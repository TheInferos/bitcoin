# Source : https://stackoverflow.com/a/15969361
import datetime as dt
import requests

def dateRange(sYear, sMonth, sDay, eYear, eMonth, eDate):
    start_date = dt.datetime(sYear, sMonth,sDay)
    end_date = dt.datetime(eYear, eMonth, eDate)
    total_days = (end_date - start_date).days + 1 #inclusive 5 days
    rangeOfDates = []
    for day_number in range(total_days):
        current_date = (start_date + dt.timedelta(days = day_number)).date()
        rangeOfDates.append(current_date)
    return rangeOfDates

def blocksInRange(dRange):
    blocksByDay = []
    for day in dRange:
        res = requests.get("https://test-insight.bitpay.com/api/blocks?limit=2000Date=" + str(day)).json()
        dayHashes = []
        for i in range(res["length"]):
            block = res["blocks"][i]["hash"]
            dayHashes.append(block)
        blocksByDay.append(dayHashes)

# Test case dRange =dateRange(2012, 5, 1, 2012, 5, 16)