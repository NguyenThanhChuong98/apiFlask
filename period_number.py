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

            # step 3:Reformat ouput
            if group_by == "site":
                out_put = cls.reformat_site_output(result, group_id, indicator)
            elif group_by == "date" and group_id == "1_hour":
                out_put = cls.reformat_date_output_hour(result, indicator, start_date, end_date)
            elif group_by == "date" and group_id == "daily":
                out_put = cls.reformat_date_output_daily(result, indicator, start_date, end_date)
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
    def group_by_date_hour(cls, start_date, group_id, end_date, indicator):
        try:
            if indicator == "NB_HOUR":
                result = 1
            elif indicator == "NB_DAY":
                result = 1 / 24
            elif indicator == "NB_WEEK":
                result = 1 / (24 * 7)
            elif indicator == "NB_MONTH":
                result = 1 / (24 * cls.duration_widgets(start_date, end_date))
            elif indicator == "NB_YEAR":
                result = 1 / (24 * 365)
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date_daily(cls, start_date, end_date, group_id, indicator):
        try:
            if group_id == "daily":
                if indicator == "NB_HOUR":
                    result = 24
                elif indicator == "NB_DAY":
                    result = 1
                elif indicator == "NB_WEEK":
                    result = 1 / 7
                elif indicator == "NB_MONTH":
                    result = 1 / (cls.duration_widgets(start_date, end_date))
                elif indicator == "NB_YEAR":
                    result = 1 / (24 * 365)
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

    # @classmethod
    # def get_number_day_in_month(cls, start_date, end_date):
    #     try:
    #         date_format = '%Y-%m-%dT%H:%M:%S'
    #         startdate = datetime.strptime(start_date, date_format)
    #         enddate = datetime.strptime(end_date, date_format)
    #         pr = pd.period_range(start=startdate, end=enddate, freq='M')
    #         new_list = tuple([(period.month, period.year) for period in pr])
    #         for x in new_list:
    #             get_days_in_month = monthrange(x[1], x[0])[1]
    #             return get_days_in_month / (cls.duration_widgets(start_date, end_date))
    #     except Exception as e:
    #         pass

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
    def reformat_date_output_hour(cls, result, indicator, start_date, end_date):
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        delta = enddate - startdate
        for i in range(delta.days + 1):
            get_elements = startdate + timedelta(hours=i)
            week_number = get_elements.isocalendar()[1]
            new_dict = {
                "error": {},
                "data": [
                    {
                        "year": get_elements.year,
                        "month": get_elements.month,
                        "week": week_number,
                        "day": get_elements.day,
                        "hour": get_elements.hour,
                        indicator: result
                    }
                ]
            }
            return new_dict

    @classmethod
    def reformat_date_output_daily(cls, result, indicator, start_date, end_date):
        date_format = '%Y-%m-%dT%H:%M:%S'
        startdate = datetime.strptime(start_date, date_format)
        enddate = datetime.strptime(end_date, date_format)
        delta = enddate - startdate
        for i in range(delta.days + 1):
            get_elements = startdate + timedelta(hours=i)
            week_number = get_elements.isocalendar()[1]
            new_dict = {
                "error": {},
                "data": [
                    {
                        "year": get_elements.year,
                        "month": get_elements.month,
                        "week": week_number,
                        "day": get_elements.day,
                        indicator: result
                    }
                ]
            }
            return new_dict
