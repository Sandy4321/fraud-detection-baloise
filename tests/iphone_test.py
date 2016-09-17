from datetime import datetime #(sig)
from datetime import timedelta

from data.data_access import LocalData as Data

mydata = Data()

damage = 2
# Rule for Iphone
if mydata.shouldCheckforIphone(damage):
    # Check if the issue date is within 10 days of
    # the release date of the Iphone 7
    date_obj = datetime.strptime(mydata.getDate(damage),'%Y-%m-%d')
    iphonerelease = datetime.strptime('2016-09-16', '%Y-%m-%d')
    delta = date_obj - iphonerelease
    print abs(delta.days)
else:
    print 'should not check'
