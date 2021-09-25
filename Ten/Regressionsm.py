import numpy as np
import statsmodels.api as sm
import math

X = [1, 2, 3, 4, 5]
Y = [2, 1, 4, 3, 5]

mux = np.mean(X)
muy = np.mean(Y)
model = sm.OLS(Y, X)
res = model.fit()
print(res.params)
#a = model.params[0]
#b = model.params[1]
#print("Y = " + str(a) + " + " + str(b) + "X")

