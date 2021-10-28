from datetime import datetime, timedelta
from calendar import monthrange
import pandas as pd

#get day input and last day of the year
sdate = datetime(2019, 1, 1, 00, 00, 00)
nb_day_in_year_st = datetime(2019, 12, 31, 23, 59, 00)
#get day remaining
remaining_day_st = nb_day_in_year_st - sdate #start date
final_st = remaining_day_st.days + 1
print(final_st)

#get day input and first day of the year
edate = datetime(2020, 12, 31, 23, 59, 00)
nb_day_in_year_end = datetime(2020, 1, 1, 00, 00, 00)
#get day remaining
remaining_day_end = edate - nb_day_in_year_end  #end date
final_end = remaining_day_end.days + 1
print(final_end)

#For partial aggregation
#get day_name of the week
st_week = sdate.isoweekday()
print(st_week)
end_week = edate.isoweekday()
print(end_week)
delta = (edate - sdate) + timedelta(1)
print(delta)
#case in the same year
if sdate.year == edate.year:
    #get rest days of the week
    rs = (7 - st_week) + 1
    res_st = rs / delta
    print("week_start_day", res_st)
    res_end = end_week
    res_end_date = res_end / delta
    print("week_end_day", res_end_date)
#case in the difference year
else:
    #get rest days of the week
    rs = (7 - st_week) + 1
    res_st = rs / final_st
    print("week_start_day", rs)
    res_end = end_week
    res_end_date = res_end / final_end
    print("week_end_day", res_end_date)


#For reformate_date_ouput_weekly "NB_MONTH"
sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
edate = datetime(2020, 12, 31, 23, 59, 00)  # end date

delta = edate - sdate  # as timedelta
diff_in_day = delta.days + 1
print(diff_in_day)
data = []
indicator = "NB_MONTH"
#for in list of deltaday with range no more than 7
for i in range(0, int(diff_in_day) + 1, 7):
    hour = sdate + timedelta(days=i)
    week = hour.isocalendar()[1]
    data.append({
        "year": hour.year,
        "month": hour.month,
        "week": week
    })
#run two variable in data list with cases same year,3 conditional: start year, end year, between year
for d, datas in enumerate(data):
    if sdate.year == edate.year:
        if d == 0:
            datas["NB_MONTH"] = res_st
        elif d == (len(datas) - 1):
            datas["NB_MONTH"] = res_end_date
        else:
            datas["NB_MONTH"] = 7 / delta
#run two variable in data list with cases difference year,3 conditional: start year, end year, between year
    else:
        if d == 0:
            datas["NB_MONTH"] = res_st
        elif d == (len(datas) - 1):
            datas["NB_MONTH"] = res_end_date
        else:
            nb_day_in_year = datetime(datas["year"], 12, 31, 23, 59, 00).day
            datas["NB_MONTH"] = 7 / nb_day_in_year
new_dict = {
    "error": {},
    "data": data
}


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