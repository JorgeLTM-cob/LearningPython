def avg(A):
    L = len(A)
    suma = 0
    for num in A:
        suma += num
    return(suma/L)

def StdDev(A, mu):
    L = len(A)
    suma = 0
    for num in A:
       suma += (num - mu)**2
    suma = (suma / L)**0.5
    return(suma)

def Covar(A, mua, B, mub):
    L = len(A)
    suma = 0
    for i in range(0,L):
        suma += ((A[i] - mua) * (B[i] - mub))
    return(suma/L)

X = [1, 3, 1, 2, 4, 5]
Y = [2, 3, 4, 1, 3, 3]
mux = avg(X)
muy = avg(Y)
sigx = StdDev(X, mux)
sigy = StdDev(Y, muy)
cov = Covar(X, mux, Y, muy)
r = (cov)/(sigx * sigy)
print(mux)
print(muy)
print(sigx)
print(sigy)
print(cov)
print(r)
