from datetime import datetime
from datetime import timedelta

date_obj = datetime.strptime('2016-09-14','%Y-%m-%d')
iphonerelease = datetime.strptime('2016-09-16', '%Y-%m-%d')
delta = date_obj - iphonerelease
print delta.days

