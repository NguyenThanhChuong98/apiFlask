from datetime import datetime, date, timedelta
import pandas as pd
from calendar import monthrange


start_date = "2019-1-1T00:00:00"
end_date = "2020-12-31T23:59:00"


def get_numb_days_in_week(start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        get_days = enddate - startdate
        result = get_days.days + 1
        count_date_range = pd.date_range(startdate, periods=result, freq="D")
        data = []
        for x in count_date_range:
            df = pd.Timestamp(x)
            get_day_of_week = df.dayofweek + 1
            data.append(get_day_of_week)
        return data
    except Exception as e:
        pass


def get_numb_days_in_month(start_date, end_date):
    date_format = '%Y-%m-%dT%H:%M:%S'
    sdate = datetime.strptime(start_date, date_format)
    edate = datetime.strptime(end_date, date_format)
    delta = edate - sdate
    new_list = []
    for i in range(delta.days + 1):
        hour = sdate + timedelta(days=i)
        new_list.append(hour.day)
    return new_list


def reformat_date_output_hour():
    sdate = datetime(2020, 12, 31, 00, 00, 00)  # start date
    edate = datetime(2020, 12, 31, 23, 59, 00)  # end date

    delta = edate - sdate  # as timedelta
    diff_in_hours = delta.total_seconds() // 3600
    print(diff_in_hours)
    data = []
    for i in range(int(diff_in_hours) + 1):
        hour = sdate + timedelta(hours=i)
        week = hour.isocalendar()[1]
        data.append({
            "year": hour.year,
            "month": hour.month,
            "week": week,
            "day": hour.day,
            "hour": hour.hour
        })
    new_dict = {
        "error": {},
        "data": data
    }
    return new_dict


pr = pd.period_range(start='2010-08', end='2011-03', freq='M')

prTupes = [(period.month, period.year) for period in pr]


def reformat_date_output_month(start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        pr = pd.period_range(start=startdate, end=enddate, freq='M')
        new_list = tuple([(period.month, period.year) for period in pr])
        data = []
        for x, y in new_list:
            data.append({
                "year": y,
                "month": x,
            })
        new_dict = {
            "data": data
        }
        return new_dict
    except Exception as e:
        pass


def reformat_date_output_week():
    sdate = datetime(2019, 12, 31, 00, 00, 00)  # start date
    edate = datetime(2021, 1, 5, 23, 59, 00)  # end date

    delta = edate - sdate  # as timedelta
    diff_in_days = delta.days
    print(diff_in_days)
    data = []
    for i in range(0, int(diff_in_days) + 1, 7):
        hour = sdate + timedelta(days=i)
        week = hour.isocalendar()[1]
        data.append({
            "year": hour.year,
            "month": hour.month,
            "week": week
        })
    new_dict = {
        "error": {},
        "data": data
    }

    return new_dict


def reformat_date_output_year(start_date, end_date):
    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        pr = pd.period_range(start=startdate, end=enddate, freq='M')
        new_list = tuple([(period.month, period.year) for period in pr])
        data = []
        for x in new_list:
            data.append({
                "year": x[1],
            })
        new_dict = {
            "data": data
        }
        return new_dict
    except Exception as e:
        pass


def get_number_day_in_year():
    start_date = datetime(2019, 12, 1)
    end_date = datetime(2020, 12, 31)
    years = range(start_date.year, end_date.year + 1)
    start, end = start_date, end_date + timedelta(1)
    new_list = list()
    for year in years:
        year_start = datetime(year, 1, 1, 0, 0)
        year_end = datetime(year + 1, 1, 1, 0, 0)
        formula = min(end, year_end) - max(start, year_start)
        new_list.append(formula.days)
    return new_list


def reformat_date_output_daily(start_date, end_date):
    date_format = '%Y-%m-%dT%H:%M:%S'
    startdate = datetime.strptime(start_date, date_format)
    enddate = datetime.strptime(end_date, date_format)
    delta = enddate - startdate
    data = []
    for i in range(delta.days + 1):
        get_elements = startdate + timedelta(days=i)
        week_number = get_elements.isocalendar()[1]
        data.append({
            "year": get_elements.year,
            "month": get_elements.month,
            "week": week_number,
            "day": get_elements.day,
        })
    new_dict = {
        "error": {},
        "data": data
    }
    return new_dict


def get_numb_day_in_year_1():
    sdate = datetime(2019, 1, 1, 00, 00, 00)
    edate = datetime(2019, 12, 31, 23, 59, 00)
    if sdate.year == edate.year:
        formula = edate - sdate
        get_numb_days = formula + timedelta(1)
        return get_numb_days
    else:
        sdate = datetime(2019, 1, 1, 00, 00, 00)
        nb_day_in_year_st = datetime(2019, 12, 31, 23, 59, 00)
        remaining_day_st = nb_day_in_year_st - sdate
        final_st = remaining_day_st.days + 1

        edate = datetime(2020, 12, 31, 23, 59, 00)
        nb_day_in_year_end = datetime(2020, 1, 1, 00, 00, 00)
        remaining_day_end = edate - nb_day_in_year_end
        final_end = remaining_day_end.days + 1

        get_numb_days = final_st + final_end
        return get_numb_days

    # print(reformat_date_output_month("2019-01-01T00:00:00", "2020-12-31T23:59:00"))
    # print(reformat_date_output_hour())
    # print(reformat_date_output_week())
    # print(reformat_date_output_daily(start_date, end_date))
    # print(reformat_date_output_year(start_date, end_date))


# print(get_numb_days_of_month(start_date, end_date))
# print(get_numb_days_in_month(start_date,end_date))
# print(get_numb_days_of_month(start_date, end_date))
# print(get_numb_days_in_week(start_date,end_date))
# print(get_numb_day_in_year_1())
#
# new_list = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# start_date = datetime(2019, 1, 1, 00, 00, 00)
# end_date = datetime(2020, 12, 31, 23, 59, 00)
# sdate_days_of_month = 12
# edate_days_of_month = 10
# rest_sdate_days_of_month = (sdate_days_of_month - start_date.day) + 1
# rest_edate_days_of_month = edate_days_of_month
# new_list1 = []
# for i in new_list:
#     new_list1.append(i)
# new_list1[0] = rest_sdate_days_of_month
# new_list1[-1] = rest_edate_days_of_month
# print(new_list1)

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
        return new_list1
    except Exception as e:
        pass


def get_numb_day_in_month(sd,ed):
    start_date = datetime(2019, 1, 1, 00, 00, 00)
    end_date = datetime(2020, 12, 31, 23, 59, 00)
    fnc_numb_days_of_month = get_numb_days_of_month(sd, ed)
    sdate_days_of_month = fnc_numb_days_of_month[0]
    print(sdate_days_of_month)
    edate_days_of_month = fnc_numb_days_of_month[-1]
    print(edate_days_of_month)
    rest_sdate_days_of_month = (sdate_days_of_month - start_date.day) + 1
    rest_edate_days_of_month = edate_days_of_month
    new_list = []
    for i in fnc_numb_days_of_month:
        new_list.append(i)
    new_list[0] = rest_sdate_days_of_month
    new_list[-1] = rest_edate_days_of_month
    return new_list


sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
edate = datetime(2020, 12, 31, 23, 59, 00)  # end date

delta = edate - sdate  # as timedelta
diff_in_day = delta.days + 1
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
new_dict = {
    "error": {},
    "data": data
}
print(new_dict)