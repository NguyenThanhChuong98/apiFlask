from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

from datetime import date, timedelta, datetime

sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
edate = datetime(2020, 12, 31, 23, 59, 00)  # end date

delta = edate - sdate  # as timedelta

for i in range(delta.days + 1):
    hour = sdate + timedelta(hours=i)
    week_number = hour.isocalendar()[1]
    obj = {
        "year": hour.year,
        "month": hour.month,
        "day": hour.day,
        "week": week_number,
        "hour": hour.hour
    }
    print(obj)
