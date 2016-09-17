import pymysql.cursors
from numpy import asarray

class Data:

    headers = None

    def getBatch(self):
        return NotImplementedError

    def printCurrentBatch(self):
        return NotImplementedError

class DbData(Data):

    offset = 0
    batch_size = 100
    current_batch = None
    batch_query = "SELECT * FROM TBSD_SCHADEN LIMIT %s OFFSET %s"
    db_connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    db='fraud-detection-baloise-db')

    headers = ["MANDANT","SDNR","VGNR","ANLDAT","SDERDAT DATE DEFAULT CURRENT DATE NOT NULL","SDERZT","SDERLANDNR","SDERPLZ","SDERORT","SDERSTR","SDERBORT","SDERBAKTZ","BAS_WHGNR","SDSTATUS","SDURS","SDART","SDTYP","SDSPEZART","SDMELDEDAT","SDERLEDAT","SDABLEGRD","DECKERG","KZDOPPEL","KZREGRESS","KZRENTE","KZVIP","KZUMWELT","RESPRUEFDAT","VSNR","ZEICHNART","VNOBJIDART","VNOBJID","BENBERKZ","BENGEBDAT","BENGESCHL","BENNAT","BENPRUEFDAT","KMSTAND","VTRNR","VERS_OBJ_NR","VERSART","RVART","KZSISCHEIN","GEBIET_OENR","ZUST_OENR","BEARB_OENR","ZUST_AWNR","AKNR","KZAKMELD","GENR","SFRRSTSL","SFRRSTDAT","SDHERG_BSTNR","SDHERG_TEXT","TEXTNR","RES_AWNR","DOS_AWNR","WARE","TRIAGE","VIGNETTE","RESWHG","GFKZ","REFERENZDOSS","TRANSPMITTEL","FALLZAEHLER","ABGANGSLAND","BESTIMMLAND","REGRESBETRAG","HAVERIEKOMMI","MFKZID"]

    def getBatch(self):
        cursor = self.db_connection.cursor()
        cursor.execute(self.batch_query, (self.batch_size, self.offset))
        self.offset+=self.batch_size
        self.current_batch = cursor.fetchall()
        return asarray(self.current_batch)

    def printCurrentBatch(self):
        print self.headers
        for row in self.current_batch:
            print row

class LocalData(Data):

    #TODO: Generate all customers
    customers = {
        1: {
            "name"          : "Rudolf Moor",
            "birthday"      : "1993-02-17",
            "address"       : "Stigliweg 14, Lyss",
            "damage_cases"  : [1, 7, 13, 14],
            "police"        : 1
        },
        2: {
            "name"          : "Stefan Ruchti",
            "birthday"      : "1987-04-17",
            "address"       : "Blumenweg 2, Basel",
            "damage_cases"  : [2, 8, 15, 16],
            "police"        : 2
        },
        3: {
            "name"          : "Jonas Jatsch",
            "birthday"      : "1970-04-23",
            "address"       : "Hauptstrasse 2, Bern",
            "damage_cases"  : [3, 9, 17, 18, 19, 20, 21, 22, 23, 24],
            "police"        : 3
        },
        4: {
            "name"          : "Barbara Blau",
            "birthday"      : "1992-08-25",
            "address"       : "Nidaugasse 3, Biel",
            "damage_cases"  : [4, 10],
            "police"        : 4
        },
        5: {
            "name"          : "Hans Herrmann",
            "birthday"      : "1962-01-01",
            "address"       : "Bernstrasse 4, Aarberg",
            "damage_cases"  : [5, 11],
            "police"        : 5
        },
        6: {
            "name"          : "Brigitte Meier",
            "birthday"      : "1974-01-17",
            "address"       : "Sonnmatte 4, Olten",
            "damage_cases"  : [6, 12],
            "police"        : 6
        }
    }

    damage_cases = {
        1: {
            "police_no"     : 1,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-09-10",
            "ml_fraud"      : True,
            "ml_prob"       : 0.87,
            "rule_fraud"    : True,
            "rule_reason"   : "Schadensmeldung nahe am iPhone 7 Release",
            "damage_no"     : 1
        },
        2: {
            "police_no"     : 2,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.21,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 2
        },
        3: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2014-06-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.12,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 3
        },
        4: {
            "police_no"     : 4,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2014-09-04",
            "ml_fraud"      : False,
            "ml_prob"       : 0.33,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 4
        },
        5: {
            "police_no"     : 5,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-06-03",
            "ml_fraud"      : False,
            "ml_prob"       : 0.02,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 5
        },
        6: {
            "police_no"     : 6,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2015-02-01",
            "ml_fraud"      : False,
            "ml_prob"       : 0.15,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 6
        },
        7: {
            "police_no"     : 1,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : False,
            "ml_prob"       : 0.45,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 7
        },
        8: {
            "police_no"     : 2,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : True,
            "ml_prob"       : 0.94,
            "rule_fraud"    : True,
            "rule_reason"   : "Es gab keinen Hagel zu dieser Zeit an diesem Ort",
            "damage_no"     : 8
        },
        9: {
            "police_no"     : 3,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : False,
            "ml_prob"       : 0.22,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 9
        },
        10: {
            "police_no"     : 4,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : False,
            "ml_prob"       : 0.04,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 10
        },
        11: {
            "police_no"     : 5,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : False,
            "ml_prob"       : 0.36,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 11
        },
        12: {
            "police_no"     : 6,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28",
            "ml_fraud"      : False,
            "ml_prob"       : 0.11,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 12
        },
        13: {
            "police_no"     : 1,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.44,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 13
        },
        14: {
            "police_no"     : 1,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : True,
            "ml_prob"       : 0.54,
            "rule_fraud"    : True,
            "rule_reason"   : "Deckungseinschluss nach Schaden",
            "damage_no"     : 14
        },
        15: {
            "police_no"     : 2,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.01,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 15
        },
        16: {
            "police_no"     : 2,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : True,
            "ml_prob"       : 0.99,
            "rule_fraud"    : True,
            "rule_reason"   : "Deckungseinschluss nach Schaden",
            "damage_no"     : 16
        },
        17: {
            "police_no"     : 3,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.27,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 17
        },
        18: {
            "police_no"     : 3,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05",
            "ml_fraud"      : True,
            "ml_prob"       : 0.76,
            "rule_fraud"    : True,
            "rule_reason"   : "Deckungseinschluss nach Schaden",
            "damage_no"     : 18
        },
        19: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-09",
            "ml_fraud"      : True,
            "ml_prob"       : 0.86,
            "rule_fraud"    : True,
            "rule_reason"   : "Zu viele Schaeden in der letzten Zeit",
            "damage_no"     : 19
        },
        20: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05",
            "ml_fraud"      : False,
            "ml_prob"       : 0.42,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 20
        },
        21: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2015-01-03",
            "ml_fraud"      : False,
            "ml_prob"       : 0.12,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 21
        },
        22: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-01-09",
            "ml_fraud"      : False,
            "ml_prob"       : 0.33,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 22
        },
        23: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-02-09",
            "ml_fraud"      : False,
            "ml_prob"       : 0.12,
            "rule_fraud"    : False,
            "rule_reason"   : "",
            "damage_no"     : 23
        },
        # 24: {
        #     "police_no"     : 3,
        #     "damage_group"  : "Wertsachen",
        #     "damage_type"   : "einfacher Diebstahl",
        #     "damage_kind"   : "Kombiversicherung Privathaushalt",
        #     "damage_reason" : "einfacher Diebstahl",
        #     "damage_date"   : "2016-10-05",
        #     "ml_fraud"      : False,
        #     "ml_prob"       : 0.03,
        #     "rule_fraud"    : False,
        #     "rule_reason"   : "",
        #     "damage_no"     : 24
        # }
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
