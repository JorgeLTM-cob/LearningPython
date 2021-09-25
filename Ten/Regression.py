def avg(A):
    L = len(A)
    suma = 0
    for num in A:
        suma += num
    return(suma / L)

def Asq(A):
    suma = 0
    for num in A:
        suma += num**2
    return(suma)

def AB(A,B):
    L = len(A)
    suma = 0
    for i in range(L):
        suma += A[i] * B[i]
    return(suma)

X = [1, 2, 3, 4, 5]
Y = [2, 1, 4, 3, 5]

n = len(X)
mux = avg(X)
muy = avg(Y)
xy = AB(X,Y)
x2 = Asq(X)
xi2 = (mux)**2
b = (xy - (mux * muy * n)) / (x2 - (xi2 * n))
a = muy - (b * mux)
print("Y = " + str(a) + " + " + str(b) + "X")

