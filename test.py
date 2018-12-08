import pandas as pd
import numpy as np

t = pd.read_csv('/modules/cs342/Assignment2/sample_submission.csv',header=0)
x=1.0/15.0
t=t.replace(float(0),float(x))
t=t.replace(float(1),float(x))
t.to_csv("test_prediction.csv", index = False
