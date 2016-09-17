#import pymysql.cursors
from numpy import asarray

class Data:

    headers = None

    def getBatch(self):
        return NotImplementedError

    def printCurrentBatch(self):
        return NotImplementedError

class LocalData(Data):

    #TODO: Generate all customers
    customers = {
        1: {
            "name"          : "Ruedi Moor",
            "damage_cases"  : [1]

        }
    }

    #TODO: Generate all damage cases
    damage_cases = {
        1: {
            "police_no"     : 1,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2016-09-10"
        },
        2: {
            "police_no"     : 2,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05"
        },
        3: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2014-05-06"
        },
        4: {
            "police_no"     : 4,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2014-04-09"
        },
        5: {
            "police_no"     : 5,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2016-03-06"
        },
        6: {
            "police_no"     : 6,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2015-01-02"
        },

    }

    def shouldCheckForHagelRule(self, damage):
        if damage == 7 or damage == 8 or damage == 9 or damage == 10 or damage == 11 or damage == 12:
            return True
        else:
            return False

    def shouldCheckforIphone(self, damage):
        if damage == 1 or damage == 2 or damage == 3 or damage == 4 or damage == 5 or damage == 6:
            return True
        else:
            return False

    def shouldCheckForTooManyDamages(self, damage):
        if damage == 19 or damage == 20 or damage == 21 or damage == 22 or damage == 23 or damage == 24:
            return True
        else:
            return False

    def getDate(self, damage):
        case = self.damage_cases[damage]
        return case['damage_date']

    def numberOfDamagesWithinLastTwoYears(self, damage):
        return (damage == 19)

    def getBatch(self):
        return NotImplemented

    def printCurrentBatch(self):
        return NotImplemented
