from data.data_access import LocalData as Data
#from data.data_access import DbData as Data

data_var = Data()
data_var.getBatch()
data_var.printCurrentBatch()
