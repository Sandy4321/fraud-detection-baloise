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

    customers = {
        1: {
            "name"          : "Ruedi Moor",
            "damage_cases"  : [1]

        }
    }

    damage_cases = {
        1: {
            "police_no"     : 1,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2017-09"
        }
    }

    def getBatch(self):
        return NotImplemented

    def printCurrentBatch(self):
        return NotImplemented