#import data
from datetime import datetime

# return tuple (int, String)
class RuleDetection:

    # Powered by Forecast
    # key: e0ab1d9dd47415f06c4f182a81d31a13
    def hagel(time, place):
        return True

    def isFraud(self, damage):
        # Hagel Regel
        if damage.data['VERSARTGRP'] == 'MF Kasko' and \
           damage.data['VERSART'] == 'Teilkasko' and \
           damage.data['SDART'] == 'Elementar' and \
           damage.data['SDURS'] == 'Hagel':

            return hagel(damage.data['SDERDAT'], damage.data['SDERORT'])

        # Iphone
        if damage.data['VERSARTGRP'] == 'Wertsachen' and \
           damage.data['VERSART'] == 'einfacher Diebstahl' and \
           damage.data['SDART'] == 'Kombiversicherung Privathaushalt' and \
           damage.data['SDURS'] == 'einfacher Diebstahl':

            date_obj = datetime.striptime(damage.data['SDERDAT'],'%Y-%m-%d')
            iphonerelease = datetime.striptime('2016-09-16', '%Y-%m-%d')
            delta = date_obj - iphonerelease
            if delta <= 10:
                return True
            else:
                return False

        # Deckungseinschluss
        if damage.dat
a[''] ==
