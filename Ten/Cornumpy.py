import numpy as np

N = 10
X = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
Y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
mux = np.mean(X)
muy = np.mean(Y)
sigx = np.std(X)
sigy = np.std(Y)
cov = np.cov(X, Y, bias = True)[0][1]
r = np.corrcoef(X,Y)[0][1]
print(mux)
print(muy)
print(sigx)
print(sigy)
print(cov)
print(r)
