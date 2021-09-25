import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import math

def TrazaError(x,y);
   X = sm.add_constant(x)
   model = sm.OLS(y, X).fit()
   m = model.params[1]
   b = model.params[0]
   desvStd = np.std(y)
   cCor = np.corrcoef(x,y)[0][1]
   err = desvStd * math.sqrt(1 - (cCor*cCor))
   points = np.linspace(x.min(), x.max())
   plt.plot(points, m*points + b)
   plt.plot(points, m*points + (b + err))
   plt.plot(points, m*points + (b - err))
   print(err)

data1 = pd.read_csv('empleados.csv')
div1 = 6
x1 = data1.received
x2 = data1.requested
fig = plt.plot(x2,x1,'x')
plt.axvline(div1, color = 'k')
data2 = data1[(data1.requested <= div1)]
x2 = data2.requested
y2 = data2.received
TrazaError(x2,y2)
data3 = data1[(data1.requeste > div1)]
x3 = data3.requested
y3 = data3.received
TrazaError(x3,y3)
plt.show()
