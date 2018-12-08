import pandas as pd
import numpy as np

meta = pd.read_csv ('/modules/cs342/Assignment2/training_set_metadata.csv',header=0)
ss = pd.read_csv('/modules/cs342/Assignment2/sample_submission.csv',header=0)

arr = meta.loc[meta["hostgal_photoz"] == 0.0].target.unique()
galF=1.0/5.0
exF = 1.0/9.0

testSet = pd.read_csv('/modules/cs342/Assignment2/test_set_metadata.csv',header=0)

galObj = testSet.loc[testSet["hostgal_photoz"] == 0.0].object_id.unique()
extObj = testSet.loc[testSet["hostgal_photoz"] != 0.0].object_id.unique()

sss= ss.copy()

classes = ss.columns.values.tolist()
classes.remove("object_id")
galClass = ["class_" + str(cnum) for cnum in arr.tolist()]
extClass = [x for x in classes if x not in galClass]
extClass.remove("class_99")

df1 = sss.loc[sss['object_id'].isin(galObj)]
df1[galClass] = galF
df1["class_90"] = 0.0
df2 = sss.loc[sss['object_id'].isin(extObj)]
df2[extClass] = exF

arr = [df1,df2]
newDf = pd.concat(arr)


newDf["class_99"] = 0.15

newDf.to_csv("test_prediction_splitGalactic.csv", index = False)
