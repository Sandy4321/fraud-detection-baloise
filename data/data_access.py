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
            "damage_date"   : "2017-09"
        }
    }

    def shouldCheckForHagelRule(self, damage):
        if damage == '7' or damage == '8' or damage == '9' or damage == '10' or damage == '11' or damage == '12':
            return True
        else:
            return False

    def shouldCheckforIphone(self, damage):
        if damage == '1' or damage == '2' or damage == '3' or damage == '4' or damage == '5' or damage == '6':
            return True
        else:
            return False

    def shouldCheckForTooManyDamages(self, damage):
        if damage == '19' or damage == '20' or damage == '21' or damage == '22' or damage == '23' or damage == '24':
            return True
        else:
            return False

    def getDate(self, damage):
        # TODO (only needed for cases 19-24)

    def numberOfDamagesWithinLastTwoYears(self, damage):
        return (damage == '19')

    def getBatch(self):
        return NotImplemented

    def printCurrentBatch(self):
        return NotImplemented
