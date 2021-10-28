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
                result = cls.group_by_site(start_date, end_date, indicator)
            elif group_by == "date" and group_id == "1_hour":
                result = cls.group_by_date_hour(indicator)
            elif group_by == "date" and group_id == "daily":
                result = cls.group_by_date_daily(indicator)
            elif group_by == "date" and group_id == "weekly":
                result = cls.group_by_date_weekly(indicator)
            elif group_by == "date" and group_id == "monthly":
                result = cls.group_by_date_monthly(indicator, start_date, end_date)
            elif group_by == "date" and group_id == "yearly":
                result = cls.group_by_date_yearly(indicator, start_date, end_date)

            # step 3:Reformat ouput
            if group_by == "site" and indicator == "NB_MONTH":
                out_put = cls.reformat_site_output_month(result, group_id, indicator, start_date, end_date)
            elif group_by == "site":
                out_put = cls.reformat_site_output(result, group_id, indicator)
            elif group_by == "date" and group_id == "1_hour":
                out_put = cls.reformat_date_output_hour(result, indicator, start_date, end_date)
            elif group_by == "date" and group_id == "daily":
                out_put = cls.reformat_date_output_daily(result, indicator, start_date, end_date)
            elif group_by == "date" and group_id == "weekly":
                out_put = cls.reformat_date_output_week(result, indicator, start_date, end_date)
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
    def group_by_site(cls, start_date, end_date, indicator):
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
    def group_by_date_hour(cls, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 1
            elif indicator == "NB_DAY":
                result = 1 / 24
            elif indicator == "NB_WEEK":
                result = 1 / 24 * 7
            elif indicator == "NB_MONTH":
                result = 1
            elif indicator == "NB_YEAR":
                result = 1 / (24 * 365)
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_daily(cls, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 24
            elif indicator == "NB_DAY":
                result = 1
            elif indicator == "NB_WEEK":
                result = 1 / 7
            elif indicator == "NB_MONTH":
                result = 1
            elif indicator == "NB_YEAR":
                result = 1 / 365
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_weekly(cls, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 24
            elif indicator == "NB_DAY":
                pass
            elif indicator == "NB_WEEK":
                result = 7
            elif indicator == "NB_MONTH":
                pass
            elif indicator == "NB_YEAR":
                result = 1 / 52
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_monthly(cls, indicator, start_date, end_date):
        try:
            if indicator == "NB_HOUR":
                result = 24
            elif indicator == "NB_DAY":
                pass
            elif indicator == "NB_WEEK":
                result = 7
            elif indicator == "NB_MONTH":
                pass
            elif indicator == "NB_YEAR":
                result = 365
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_yearly(cls, indicator, start_date, end_date):
        try:
            if indicator == "NB_HOUR":
                result = 24 * cls.get_numb_day_in_year(start_date, end_date)
            elif indicator == "NB_DAY":
                result = cls.get_numb_day_in_year(start_date, end_date)
            elif indicator == "NB_WEEK":
                result = cls.get_numb_day_in_year(start_date, end_date) / 7
            elif indicator == "NB_MONTH":
                result = cls.get_numb_day_in_year(start_date, end_date) / 365 * 12
            elif indicator == "NB_YEAR":
                result = cls.get_numb_day_in_year(start_date, end_date) / 365
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
    def reformat_site_output_month(cls, result, group_id, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=sdate, end=edate, freq='M')
            new_list = tuple([(period.month, period.year) for period in pr])
            data = []
            for x, y in new_list:
                data.append({
                    "year": y,
                    "month": x,
                })
            new_list_1 = []
            for d, datas in enumerate(data):
                new_dict_1 = {}
                datas["NB_MONTH"] = result / cls.get_days_each_month_without_partial(datas["year"], datas["month"])
                new_dict_1.update(datas)
                new_list_1.append({
                    indicator: datas["NB_MONTH"]
                })
            new_dict = {
                indicator: new_list_1,
                "group_id": group_id
            }
            return new_dict

        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_hour(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)

            delta = (edate - sdate) + timedelta(1)
            diff_in_hours = delta.total_seconds() // 3600
            data = []
            for i in range(int(diff_in_hours)):
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
            if indicator == "NB_MONTH":
                new_list = []
                for d, datas in enumerate(data):
                    new_dict_1 = {}
                    get_days_each_month_without_partial = cls.get_days_each_month_without_partial(datas["year"],
                                                                                                  datas["month"])
                    new_dict_1.update(datas)
                    new_dict_1["NB_MONTH"] = result / (
                            24 * get_days_each_month_without_partial)
                    new_list.append(new_dict_1)
                new_dict = {
                    "error": {},
                    "data": new_list
                }
            else:
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
            new_list = []
            if indicator == "NB_MONTH":
                for d, datas in enumerate(data):
                    new_dict_1 = {}
                    get_days_each_month_without_partial = cls.get_days_each_month_without_partial(datas["year"],
                                                                                                  datas["month"])
                    new_dict_1.update(datas)
                    new_dict_1["NB_MONTH"] = result / get_days_each_month_without_partial
                    new_list.append(new_dict_1)
                new_dict = {
                    "error": {},
                    "data": new_list
                }
            else:
                new_dict = {
                    "error": {},
                    "data": data
                }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_week(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)
            st_week = sdate.isoweekday()
            end_week = edate.isoweekday()
            delta = edate - sdate
            diff_in_day = delta.days + 1
            data = []
            for i in range(0, int(diff_in_day) + 1, 7):
                hour = sdate + timedelta(days=i)
                week = hour.isocalendar()[1]
                data.append({
                    "year": hour.year,
                    "month": hour.month,
                    "week": week
                })
            new_list = []
            if indicator == "NB_HOUR":
                for d, datas in enumerate(data):
                    if d == 0:
                        datas["NB_HOUR"] = result * st_week
                    elif d == (len(datas) - 1):
                        datas["NB_HOUR"] = result * end_week
                    else:
                        datas["NB_HOUR"] = result * 7
                    new_list.append(datas)
            elif indicator == "NB_DAY":
                for d, datas in enumerate(data):
                    if d == 0:
                        datas["NB_DAY"] = st_week
                    elif d == (len(datas) - 1):
                        datas["NB_DAY"] = end_week
                    else:
                        datas["NB_DAY"] = 7
                    new_list.append(datas)
            elif indicator == "NB_WEEK":
                for d, datas in enumerate(data):
                    if d == 0:
                        datas["NB_WEEK"] = st_week / result
                    elif d == (len(datas) - 1):
                        datas["NB_WEEK"] = end_week / result
                    else:
                        datas["NB_WEEK"] = 7 / result
                    new_list.append(datas)
            elif indicator == "NB_MONTH":
                for d, datas in enumerate(data):
                    if d == 0:
                        datas["NB_MONTH"] = st_week / cls.get_days_each_month_without_partial(datas["year"],
                                                                                              datas["month"])
                    elif d == (len(datas) - 1):
                        datas["NB_MONTH"] = end_week / cls.get_days_each_month_without_partial(datas["year"],
                                                                                               datas["month"])
                    else:
                        datas["NB_MONTH"] = 7 / cls.get_days_each_month_without_partial(datas["year"], datas["month"])
                    new_list.append(datas)
            elif indicator == "NB_YEAR":
                for d, datas in enumerate(data):
                    if d == 0:
                        datas["NB_YEAR"] = result * st_week / 7
                    elif d == (len(datas) - 1):
                        datas["NB_YEAR"] = result * end_week / 7
                    else:
                        datas["NB_YEAR"] = result * 7 / 7
                    new_list.append(datas)
            new_dict = {
                "error": {},
                "data": new_list
            }
            return new_dict

        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_month(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=sdate, end=edate, freq='M')
            new_list = [(period.month, period.year) for period in pr]
            data = []
            for x, y in new_list:
                data.append({
                    "year": y,
                    "month": x,
                })
            new_list = []
            if indicator == "NB_HOUR":
                for d, datas in enumerate(data):
                    datas["NB_HOUR"] = result * cls.get_days_each_month_without_partial(datas["year"], datas["month"])
                    new_list.append(datas)
            elif indicator == "NB_DAY":
                for d, datas in enumerate(data):
                    datas["NB_DAY"] = cls.get_days_each_month_without_partial(datas["year"], datas["month"])
                    new_list.append(datas)
            elif indicator == "NB_WEEK":
                for d, datas in enumerate(data):
                    datas["NB_WEEK"] = cls.get_days_each_month_without_partial(datas["year"], datas["month"]) / result
                    new_list.append(datas)
            elif indicator == "NB_MONTH":
                for d, datas in enumerate(data):
                    datas["NB_MONTH"] = cls.get_days_each_month_with_partial(start_date, end_date) / \
                                        cls.get_days_each_month_without_partial(datas["year"], datas["month"])
                    new_list.append(datas)
            elif indicator == "NB_YEAR":
                for d, datas in enumerate(data):
                    datas["NB_YEAR"] = cls.get_days_each_month_without_partial(datas["year"], datas["month"]) / 365
                    new_list.append(datas)
            new_dict = {
                "error": {},
                "data": new_list
            }
            return new_dict
        except Exception as e:
            pass

    @classmethod
    def reformat_date_output_year(cls, result, indicator, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=sdate, end=edate, freq='M')
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
    def get_numb_day_in_year(cls, start_date, end_date):
        date_format = '%Y-%m-%dT%H:%M:%S'
        sdate = datetime.strptime(start_date, date_format)
        edate = datetime.strptime(end_date, date_format)
        if sdate.year == edate.year:
            get_numb_days = (edate - sdate) + timedelta(1)
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

    @classmethod
    def get_numb_days_of_month(cls, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            sdate = datetime.strptime(start_date, date_format)
            edate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=sdate, end=edate, freq='M')
            new_list = tuple([(period.month, period.year) for period in pr])
            new_list1 = []
            for x in new_list:
                get_days_in_month = monthrange(x[1], x[0])[1]
                new_list1.append(get_days_in_month)
            return new_list1
        except Exception as e:
            pass

    @classmethod
    def get_numb_day_in_month(cls, start_date, end_date):
        date_format = '%Y-%m-%dT%H:%M:%S'
        sdate = datetime.strptime(start_date, date_format)
        edate = datetime.strptime(end_date, date_format)
        fnc_numb_days_of_month = cls.get_numb_days_of_month(start_date, end_date)
        sdate_days_of_month = fnc_numb_days_of_month[0]
        edate_days_of_month = fnc_numb_days_of_month[-1]
        rest_sdate_days_of_month = (sdate_days_of_month - sdate.day) + 1
        rest_edate_days_of_month = edate_days_of_month
        new_list = []
        for i in fnc_numb_days_of_month:
            new_list.append(i)
        new_list[0] = rest_sdate_days_of_month
        new_list[-1] = rest_edate_days_of_month
        return new_list

    @classmethod
    def get_days_each_month_without_partial(cls, year_input, month_input):
        try:
            num_days = monthrange(year_input, month_input)[1]
            return num_days
        except Exception as e:
            pass

    @classmethod
    def get_days_each_month_with_partial(cls, start_date, end_date):
        try:
            for x in cls.get_numb_day_in_month(start_date, end_date):
                return x
        except Exception as e:
            pass
