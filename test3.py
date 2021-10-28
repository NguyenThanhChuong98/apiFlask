from datetime import date, timedelta, datetime
from calendar import monthrange
import pandas as pd


def get_numb_days_of_month(start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        pr = pd.period_range(start=startdate, end=enddate, freq='M')
        new_list = tuple([(period.month, period.year) for period in pr])
        new_list1 = []
        for x in new_list:
            get_days_in_month = monthrange(x[1], x[0])[1]
            new_list1.append(get_days_in_month)
        print(new_list1)
        return new_list1
    except Exception as e:
        pass


new_list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def reformat_date_output_hour(result, indicator, start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)

        delta = (enddate - startdate) + timedelta(1) # as timedelta
        diff_in_hours = delta.total_seconds() // 3600
        data = []
        for i in range(int(diff_in_hours) + 1):
            hour = startdate + timedelta(hours=i)
            week = hour.isocalendar()[1]
            data.append({
                "year": hour.year,
                "month": hour.month,
                "week": week,
                "day": hour.day,
                "hour": hour.hour,
                indicator: result
            })
        for d, datas in enumerate(data):
            for i in new_list1:
                datas["NB_MONTH"] = result / (24 * i)
        new_dict = {
            "error": {},
            "data": data
        }
        return new_dict
    except Exception as e:
        pass



def get_days_each_month(start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        pr = pd.period_range(start=startdate, end=enddate, freq='M')
        new_list = tuple([(period.month, period.year) for period in pr])
        for x in new_list:
            get_days = monthrange(x[1], x[0])[1]
        return get_days
    except Exception as e:
        pass


start_date = "2019-1-1T00:00:00"
end_date = "2020-12-31T23:59:00"
print(get_days_each_month(start_date,end_date))
