import pandas as pd
import numpy as np

test_data = pd.read_csv('/modules/cs342/Assignment2/test_set.csv',header=0,chunksize=3000000)

# gets the data frame for an object
def getObjDf(objId):
    dfList = []
    for chunk in pd.read_csv('/modules/cs342/Assignment2/test_set.csv',header=0,chunksize=3000000):

        newDf = chunk[chunk['object_id'] == objId]
        if newDf.shape[0] == 0:
            break
        else:
            dfList.append(newDf)
            continue
    return pd.concat(dfList)
