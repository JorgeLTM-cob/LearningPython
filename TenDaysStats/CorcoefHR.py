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

N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))
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
