from data.data_access_local import LocalData as Data
#from data.data_access_db import DbData as Data

data_var = Data()
data_var.getBatch()
data_var.printCurrentBatch()
