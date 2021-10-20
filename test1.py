from datetime import datetime, timedelta
import pandas as pd

# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("timestamp =", a.timestamp())
#
#
#
# sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
# edate = datetime(2020, 12, 31, 23, 59, 00)  # end date
#
# delta = edate - sdate  # as timedelta
# for i in range(delta.days + 1):
#     hour = sdate + timedelta(hours=i)
#     week_number = hour.isocalendar()[1]
#     obj = {
#         "year": hour.year,
#         "month": hour.month,
#         "day": hour.day,
#         "week": week_number,
#         "hour": hour.hour
#     }
#     print(obj)
# date_format = '%Y-%m-%dT%H:%M:%S'
# startdate = datetime.strptime("2019-01-01T00:00:00", date_format)
# enddate = datetime.strptime("2020-12-31T23:59:00", date_format)
# result = enddate - startdate
# a = result.days + 1
# count_date_range = pd.date_range(startdate, periods=a, freq="D")
# print(count_date_range)
# for x in count_date_range:
#     df = pd.Timestamp(x)
#     print(df.dayofweek + 1)

start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 12, 31)
years = range(start_date.year, end_date.year + 1)
start, end = start_date, end_date + timedelta(1)
b = list()
for year in years:
    year_start = datetime(year, 1, 1, 0, 0)
    year_end = datetime(year + 1, 1, 1, 0, 0)
    a = min(end, year_end) - max(start, year_start)
    b.append(a.days)
print(b)
