#Code to compute Spearman's Rank Correlation Coefficient
def bs(A,num):
    L = len(A) - 1
    izq = 0
    der = L
    mid = (der - izq) // 2
    while (izq < der):
        if (A[mid] == num):
            izq = der
            return(mid + 1)
        elif (A[mid] > num):
            der = mid
            if ((der - izq) // 2 == 0):
                mid -= 1
            else:
                mid -= (der - izq) // 2
        else:
            izq = mid
            if ((der - izq) // 2 == 0):
                mid += 1
            else:
                mid += (der - izq) // 2

N = 10
X = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
X2 = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
Y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
Y2 = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
X2.sort()
Y2.sort()
RX = []
RY = []
for i in range (0,N):
    RX.append(bs(X2,X[i]))
    RY.append(bs(Y2,Y[i]))
suma = 0
pref = 6 / (N * ((N**2) - 1))
for i in range(0,N):
    suma += (RX[i] - RY[i])**2
Srank = 1 - (suma * pref)
print("%.3f" % round(Srank,3))
