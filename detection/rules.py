from datetime import datetime #(sig)
from datetime import timedelta

from data.data_access import LocalData as Data

################################
# ASSUMPTIONS ABOUT ATTRIBUTES:#
################################
# SDERDAT: Schadensdatum       #
# VERSARTGRP: Versicherungsartgruppe
# VERSART: Versicherungsart    #
# SDART: Schadensart           #
# SDURS: Schadensursache       #
# SDERORT: Schadensort         #
################################

class RuleDetection:

    hagelmap = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:True, 8:False, 9:True, 10:True, 11:True, 12:True, 13: False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False}

    # Checks if the given there was "hagel" during 'time' in 'place'
    # Could be implemented by using the API of Forecast
    # key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    def hagel(self, damage):
        # Would access fields with Data.getTime(damage) and Data.getLocation(damage)
        return hagelmap[damage]

    # This method, given the attributes of a newly issued "Schadensmeldung",
    # will use a prototype set of "hand-crafted" decision rules to classify
    # the request either as potentially fraud, or as safe.
    # Note that there may be false-positives, so the request should further be
    # investigated by "Versicherungsmenschen"
    def isFraud(self, damage):

        myData = Data()

        # Rule for Hagel
        if myData.shouldCheckForHagelRule(damage):
            # check if the weather actually was as stated in the request
            if (not self.hagel(damage)):
                return True, 'Es gab gar keinen Hagel zu dieser Zeit an diesem Ort!'
            else:
                return False, 'muy'

        # Rule for Iphone
        if myData.shouldCheckforIphone(damage):
             # Check if the issue date is within 10 days of
             # the release date of the Iphone 7
             date_obj = datetime.strptime(myData.getDate(damage),'%Y-%m-%d')
             iphonerelease = datetime.strptime('2016-09-16', '%Y-%m-%d')
             delta = date_obj - iphonerelease
             if abs(delta.days) <= 10:
                 return True
             else:
                 return False

        # Rule for "Deckungseinschluss"
        # not implemented


        # Rule for too many "Schadensfaelle"
	if (myData.shouldCheckForTooManyDamages(damage) and
	    myData.numberOfDamagesWithinLastTwoYears(damage) > 5):
            return True, 'Zu viele Schäden in der letzten Zeit'
        else:
            return False, 'muy'
