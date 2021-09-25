def avg(A):
    L = len(A)
    suma = 0
    for num in A:
        suma += num
    return(suma/L)

def stdD(A, mu):
    L = len(A)
    suma = 0
    for num in A:
        suma += (num - mu)**2
    suma /= L
    return(suma**0.5)

def Cov(A, mua, B, mub):
    L = len(A)
    suma = 0
    for i in range(L):
        suma += ((A[i] - mua) * (B[i] - mub))
    return(suma)

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]
n = len(X)
mux = avg(X)
muy = avg(Y)
sigx = stdD(X, mux)
sigy = stdD(Y, muy)
c = Cov(X, mux, Y, muy)
pref = n * sigx * sigy
r = c / pref
b = r * sigy / sigx
a = muy - (b * mux)
ans = (80 * b) + a
print("%.3f" % ans)


