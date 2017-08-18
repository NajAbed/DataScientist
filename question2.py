import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import scipy.stats as stats


linshconnection=[];dbuy=[];onactivity=[]; comsize = []
with open('C:/Python27/FanAI/Sales3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        linshconnection.append(row[3])
        onactivity.append(row[4])
        dbuy.append(row[5])

with open('C:/Python27/FanAI/TrendData3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        comsize.append(row[2])


for i in xrange(len(linshconnection)):
    linshconnection[i]=float(linshconnection[i])+0
    onactivity[i]=float(onactivity[i])+0
    dbuy[i]=float(dbuy[i])+0
    comsize[i]=float(comsize[i])+0


# creating arry from the lsit
linshconnection = np.asarray(linshconnection); onactivity = np.asarray(onactivity);
dbuy = np.asarray(dbuy); comsize = np.asarray(comsize)

# Create linear regression object
regr = linear_model.LinearRegression()

predictors = pd.DataFrame(np.asarray([linshconnection, onactivity, comsize]).T)

regr.fit(X= predictors, y=dbuy)
# Make predictions using the testing set
intent = regr.predict(predictors)
print(intent)
