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
            "damage_cases"  : [1, 7, 13, 14]
        },
        2: {
            "name"          : "Stefan Ruchti",
            "birthday"      : "1987-04-17",
            "address"       : "Blumenweg 2, Basel",
            "damage_cases"  : [2, 8, 15, 16]
        },
        3: {
            "name"          : "Jonas Jatsch",
            "birthday"      : "1970-04-23",
            "address"       : "Hauptstrasse 2, Bern",
            "damage_cases"  : [3, 9, 17, 18, 19, 20, 21, 22, 23, 24]
        },
        4: {
            "name"          : "Barbara Blau",
            "birthday"      : "1992-08-25",
            "address"       : "Nidaugasse 3, Biel",
            "damage_cases"  : [4, 10]
        },
        5: {
            "name"          : "Hans Herrmann",
            "birthday"      : "1962-01-01",
            "address"       : "Bernstrasse 4, Aarberg",
            "damage_cases"  : [5, 11]
        },
        6: {
            "name"          : "Brigitte Meier",
            "birthday"      : "1974-01-17",
            "address"       : "Sonnmatte 4, Olten",
            "damage_cases"  : [6, 12]
        }
    }

    damage_cases = {
        1: {
            "police_no"     : 1,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-09-10"
        },
        2: {
            "police_no"     : 2,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05"
        },
        3: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2014-06-05"
        },
        4: {
            "police_no"     : 4,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2014-09-04"
        },
        5: {
            "police_no"     : 5,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-06-03"
        },
        6: {
            "police_no"     : 6,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2015-02-01"
        },
        7: {
            "police_no"     : 1,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        8: {
            "police_no"     : 2,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        9: {
            "police_no"     : 3,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        10: {
            "police_no"     : 4,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        11: {
            "police_no"     : 5,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        12: {
            "police_no"     : 6,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "Elementar",
            "damage_reason" : "Hagel",
            "damage_date"   : "2016-08-28"
        },
        13: {
            "police_no"     : 1,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        14: {
            "police_no"     : 1,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        15: {
            "police_no"     : 2,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        16: {
            "police_no"     : 2,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        17: {
            "police_no"     : 3,
            "damage_group"  : "MF Haftpflicht",
            "damage_type"   : "MF Haftpflicht",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        18: {
            "police_no"     : 3,
            "damage_group"  : "MF Kasko",
            "damage_type"   : "Teilkasko",
            "damage_kind"   : "",
            "damage_reason" : "",
            "damage_date"   : "2016-05-05"
        },
        19: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-09"
        },
        20: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05"
        },
        21: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2015-01-03"
        },
        22: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-01-09"
        },
        23: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-02-09"
        },
        24: {
            "police_no"     : 3,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_kind"   : "Kombiversicherung Privathaushalt",
            "damage_reason" : "einfacher Diebstahl",
            "damage_date"   : "2016-10-05"
        }
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
