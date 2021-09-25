from sklearn import linear_model
import numpy as np

xl = [1, 2, 3, 4, 5]
Y = [2, 1, 4, 3, 5]
x = np.asarray(xl).reshape(-1, 1)
print(x)
lm = linear_model.LinearRegression()
lm.fit(x, Y)
b = lm.coef_[0]
a = lm.intercept_
print("Y = " + str(a) + " + " + str(b) + "X")

