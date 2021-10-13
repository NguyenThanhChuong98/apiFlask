from datetime import datetime,date
# date_format = '%Y-%m-%dT%H:%M:%S'
# a = datetime.strptime('2019-01-01T00:00:00', date_format)
# b = datetime.strptime('2019-01-31T23:59:00', date_format)
# delta = b - a
# print(delta.days + 1)

import pandas as pd
from calendar import monthrange
get_days_in_the_month = (date(2020, 12, 31) - date(2019, 1, 1)).days
print(get_days_in_the_month)
pr = pd.period_range(start='2010-08',end='2011-03', freq='M')
print(pr)
# prTupes=tuple([(period.month,period.year) for period in pr])
# for x in prTupes:
#     get_numb_in_month = monthrange(x[1], x[0])[1]
#     print(get_numb_in_month)

