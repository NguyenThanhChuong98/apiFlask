from datetime import datetime
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

            # step 3:Reformat ouput
            if group_by == "site":
                out_put = cls.reformat_site_output(result, group_id, indicator)
            return out_put
        except Exception as e:
            raise e

    def fnc_period_numbers_date(cls, data_input):
        try:
            cls.check_validation(data_input)
            start_date = data_input["start_date"]
            end_date = data_input["end_date"]
            group_id = data_input["group_id"][0]
            group_by = data_input["group_by"][0]
            indicator = data_input["id"][0]
            if group_by == "date":
                out_put = cls.reformat_date_output(start_date, end_date)
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
                result = cls.get_number_day_in_month(start_date, end_date) / 365
            return result
        except Exception as e:
            pass

    @classmethod
    def group_by_date(cls, start_date, end_date, group_id, indicator):
        try:
            if indicator == "NB_YEAR":
                result = cls.get_number_day_in_month(start_date, end_date)
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
    def get_number_day_in_month(cls, start_date, end_date):
        try:
            date_format = '%Y-%m-%dT%H:%M:%S'
            startdate = datetime.strptime(start_date, date_format)
            enddate = datetime.strptime(end_date, date_format)
            pr = pd.period_range(start=startdate, end=enddate, freq='M')
            new_list = tuple([(period.month, period.year) for period in pr])
            for x in new_list:
                get_days_in_month = monthrange(x[1], x[0])[1]
            return get_days_in_month
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
    def reformat_date_output(cls, start_date, end_date):
        new_dict = {
            "error": {},
            "data": [
                {
                    "year": "",
                    "month": "",
                    "NB_YEAR": "",
                }
            ]
        }
        return new_dict
