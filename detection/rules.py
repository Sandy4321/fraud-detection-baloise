from datetime import datetime #(sig)
from datetime import timedelta

from data_access import LocalData as Data

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

# return tuple (bool, String)
class RuleDetection:

    # Checks if the given there was "hagel" during 'time' in 'place'
    # Could be implemented by using the API of Forecast
    # key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    def hagel(time, place):
        return True

    # This method, given the attributes of a newly issued "Schadensmeldung",
    # will use a prototype set of "hand-crafted" decision rules to classify
    # the request either as potentially fraud, or as safe.
    # Note that there may be false-positives, so the request should further be
    # investigated by "Versicherungsmenschen"
    def isFraud(self, damage):

Data.khvkkhgkkgk(damage)
        # Rule for Hagel
        if ((damage.data['VERSARTGRP'] == 'MF Kasko' or
            damage.data['VERSARTGRP'] == 'MF Haftpflicht' or
            damage.data['VERSARTGRP'] == 'MF Rechtsschutz' or
            damage.data['VERSARTGRP'] == 'Allgemeine Haftpflicht' or
            damage.data['VERSARTGRP'] == 'Sach Elementar' or
            damage.data['VERSARTGRP'] == 'Sach Feuer' or
            damage.data['VERSARTGRP'] == 'Sach Betriebsunterrechnung' or
            damage.data['VERSARTGRP'] == 'Sach Diebstahl / Wertsachen' or
            damage.data['VERSARTGRP'] == 'Sach Wasser' or
            damage.data['VERSARTGRP'] == 'Sach Glas') and
           damage.data['VERSART'] == 'Teilkasko' and
           damage.data['SDART'] == 'Elementar' and
           damage.data['SDURS'] == 'Hagel'):

            # check if the weather actually was as stated in the request
            if hagel(damage.data['SDERDAT'], damage.data['SDERORT']):
                return True, 'Es gab gar keinen Hagel zu dieser Zeit an diesem Ort!'
            else:
                return False, 'Es gab tatsächlich Hagel zu dieser Zeit an diesem Ort'

        # Rule for Iphone
        if (damage.data['VERSARTGRP'] == 'Wertsachen' and
           damage.data['VERSART'] == 'einfacher Diebstahl' and
           damage.data['SDART'] == 'Kombiversicherung Privathaushalt' and
           damage.data['SDURS'] == 'einfacher Diebstahl'):

             # Check if the issue date is within 10 days of
             # the release date of the Iphone 6
             date_obj = datetime.strptime(damage.data['SDERDAT'],'%Y-%m-%d')
             iphonerelease = datetime.strptime('2016-09-16', '%Y-%m-%d')
             delta = date_obj - iphonerelease
             if abs(delta.days) <= 10:
                 return True
             else:
                 return False

        # Rule for "Deckungseinschluss"
        # TODO: Implement this case
        # if datamodule.


        # Rule for too many "Schadensfälle"
        # Note that we assume that VSNR refers to POLO (which may be wrong)
	if (damage.data['VERSARTGRP'] == 'Wertsachen' and
	    Data.numberOfDamagesWithinLastTwoYears(
		damage.data['VSNR'],
		damage.data['SDERDAT']) > 5):
            return True
        else:
            return False
