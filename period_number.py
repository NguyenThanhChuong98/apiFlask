from datetime import date, timedelta, datetime
import pandas as pd
from calendar import monthrange


class Period_number:

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def main(cls, data_input):
        try:
            result = cls.fnc_period_numbers_site(data_input)
        except Exception as e:
            pass
        else:
            return result

    @classmethod
    def fnc_period_numbers_site(cls, data_input):
        try:
            # step 1:Data Validation
            cls.check_validation(data_input)
            # step 1.1:Get the mandatory data
            start_date = data_input["start_date"]
            end_date = data_input["end_date"]
            group_id = data_input["group_id"][0]
            group_by = data_input["group_by"]
            indicator = data_input["id"][0]
            # step 2:Data Processing
            if group_by == "site":
                result = cls.group_by_site(start_date, end_date, group_id, indicator)
            elif group_by == "date" and group_id == "1_hour":
                result = cls.group_by_date_hour(start_date, end_date, group_id, indicator)
            elif group_by == "date" and group_id == "daily":
                result = cls.group_by_date_daily(start_date, end_date, group_id, indicator)
            elif group_by == "date" and group_id == "weekly":
                result = cls.group_by_date_weekly(start_date, end_date, group_id, indicator)
            elif group_by == "date" and group_id == "monthly":
                result = cls.group_by_date_monthly(start_date, end_date, group_id, indicator)
            elif group_by == "date" and group_id == "yearly":
                result = cls.group_by_date_yearly(start_date, end_date, group_id, indicator)

            # step 3:Reformat ouput
            if group_by == "site":
                out_put = cls.reformat_site_output(result, group_id, indicator)
            elif group_by == "date" and group_id == "1_hour":
                out_put = cls.reformat_date_output_hour(result, indicator)
            elif group_by == "date" and group_id == "daily":
                out_put = cls.reformat_date_output_daily(result, indicator, start_date, end_date)
            elif group_by == "date" and group_id == "weekly":
                out_put = cls.reformat_date_output_week(result, indicator)
            elif group_by == "date" and group_id == "monthly":
                out_put = cls.reformat_date_output_month(result, indicator, start_date, end_date)
            elif group_by == "date" and group_id == "yearly":
                out_put = cls.reformat_date_output_year(result, indicator, start_date, end_date)
            return out_put

        except Exception as e:
            raise e

    @classmethod
    def check_validation(cls, data_validate):
        new_list = [
            "partner.code",
            "widget.chart_type",
            "start_date",
            "end_date",
            "perimeter.type",
            "perimeter.list",
            "group_by",
            "group_id",
            "id"
        ]

        for x in new_list:
            if x not in data_validate:
                raise Exception("Incorrect input")
        start_date = data_validate["start_date"]
        end_date = data_validate["end_date"]
        try:
            format_start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
            format_end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        except Exception as e:
            raise Exception("Incorrect input")

    @classmethod
    def group_by_site(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_HOUR":
                result = cls.duration_widgets(start_date, end_date) * 24
            elif indicator == "NB_DAY":
                result = cls.duration_widgets(start_date, end_date)
            elif indicator == "NB_WEEK":
                result = cls.duration_widgets(start_date, end_date) / 7
            elif indicator == "NB_MONTH":
                result = cls.duration_widgets(start_date, end_date)
            elif indicator == "NB_YEAR":
                result = cls.duration_widgets(start_date, end_date) / 365
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_hour(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 1
            elif indicator == "NB_DAY":
                result = 1 / 24
            elif indicator == "NB_WEEK":
                result = 1 / 24 * 7
            elif indicator == "NB_MONTH":
                for i in cls.get_numb_days_of_month(start_date, end_date):
                    result = 1 / (24 * i)
            elif indicator == "NB_YEAR":
                result = 1 / (24 * 365)
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_daily(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 24
            elif indicator == "NB_DAY":
                result = 1
            elif indicator == "NB_WEEK":
                result = 1 / 7
            elif indicator == "NB_MONTH":
                for i in cls.get_numb_days_of_month(start_date, end_date):
                    result = 1 / i
            elif indicator == "NB_YEAR":
                result = 1 / 365
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_weekly(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_HOUR":
                for i in cls.get_numb_days_in_week(start_date, end_date):
                    result = 24 * i
            elif indicator == "NB_DAY":
                for i in cls.get_numb_days_in_week(start_date, end_date):
                    result = i
            elif indicator == "NB_WEEK":
                for i in cls.get_numb_days_in_week(start_date, end_date):
                    result = i / 7
            elif indicator == "NB_MONTH":
                for i in cls.get_numb_days_in_week(start_date, end_date):
                    for j in cls.get_numb_days_of_month(start_date, end_date):
                        result = i / j
            elif indicator == "NB_YEAR":
                for i in cls.get_numb_days_in_week(start_date, end_date):
                    result = 1 / (52 * i)
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_monthly(cls, start_date, end_date, group_id, indicator):
        try:
            if group_id == "monthly":
                if indicator == "NB_HOUR":
                    for i in cls.get_numb_days_in_month(start_date, end_date):
                        result = 24 * i
                elif indicator == "NB_DAY":
                    for i in cls.get_numb_days_of_month(start_date, end_date):
                        result = i
                elif indicator == "NB_WEEK":
                    for i in cls.get_numb_days_of_month(start_date, end_date):
                        result = i / 7
                elif indicator == "NB_MONTH":
                    for i in cls.get_numb_days_in_month(start_date, end_date):
                        for j in cls.get_numb_days_of_month(start_date, end_date):
                            result = i / j
                elif indicator == "NB_YEAR":
                    for i in cls.get_numb_days_in_month(start_date, end_date):
                        result = i / 365
                return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_yearly(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_HOUR":
                for i in cls.get_numb_day_in_year():
                    result = 24 * i
            elif indicator == "NB_DAY":
                for i in cls.get_numb_day_in_year():
                    result = i
            elif indicator == "NB_WEEK":
                for i in cls.get_numb_day_in_year():
                    result = i / 7
            elif indicator == "NB_MONTH":
                for i in cls.get_numb_day_in_year():
                    result = i / (365 * 12)
            elif indicator == "NB_YEAR":
                for i in cls.get_numb_day_in_year():
                    result = i / 365
            return result
        except Exception as e:
            pass

    @classmethod
    def duration_widgets(cls, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            startdate = datetime.strptime(start_date, date_format)
            enddate = datetime.strptime(end_date, date_format)
            result = enddate - startdate
            return result.days + 1
        except Exception as e:
            pass

    @classmethod
    def reformat_site_output(cls, result, group_id, indicator):
        new_dict = {
            "error": {},
            "data": [
                {
                    "group_id": group_id,
                    indicator: result
                }
            ]
        }
        return new_dict

    @classmethod
    def reformat_date_output_hour(cls, result, indicator):
        try:
            sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
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
                    "hour": hour.hour,
                    indicator: result
                })
            new_dict = {
                "error": {},
                "data": data
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_daily(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            startdate = datetime.strptime(start_date, date_format)
            enddate = datetime.strptime(end_date, date_format)
            delta = enddate - startdate
            data = []
            for i in range(delta.days + 1):
                get_elements = startdate + timedelta(hours=i)
                week_number = get_elements.isocalendar()[1]
                data.append({
                    "year": get_elements.year,
                    "month": get_elements.month,
                    "week": week_number,
                    "day": get_elements.day,
                    indicator: result
                })
            new_dict = {
                "error": {},
                "data": data
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_week(cls, result, indicator):
        try:
            sdate = datetime(2019, 1, 1, 00, 00, 00)  # start date
            edate = datetime(2021, 12, 31, 23, 59, 00)  # end date

            delta = edate - sdate  # as timedelta
            diff_in_day = delta.days
            print(diff_in_day)
            data = []
            for i in range(0, int(diff_in_day) + 1, 7):
                hour = sdate + timedelta(days=i)
                week = hour.isocalendar()[1]
                data.append({
                    "year": hour.year,
                    "month": hour.month,
                    "week": week,
                    indicator: result
                })
            new_dict = {
                "error": {},
                "data": data
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_month(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            startdate = datetime.strptime(start_date, date_format)
            enddate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=startdate, end=enddate, freq='M')
            new_list = [(period.month, period.year) for period in pr]
            data = []
            for x, y in new_list:
                data.append({
                    "year": y,
                    "month": x,
                    indicator: result
                })
            new_dict = {
                "data": data
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_year(cls, result, indicator, start_date, end_date):
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
                    indicator: result
                })
            new_dict = {
                "data": data
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def get_numb_days_in_week(cls, start_date, end_date):
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

    @classmethod
    def get_numb_days_of_month(cls, start_date, end_date):
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

    @classmethod
    def get_numb_days_in_month(cls, start_date, end_date):
        date_format = '%Y-%m-%dT%H:%M:%S'
        sdate = datetime.strptime(start_date, date_format)
        edate = datetime.strptime(end_date, date_format)
        delta = edate - sdate
        new_list = []
        for i in range(delta.days + 1):
            hour = sdate + timedelta(days=i)
            new_list.append(hour.day)
        return new_list

    @classmethod
    def get_numb_day_in_year(cls):
        start_date = datetime(2019, 1, 1)
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
