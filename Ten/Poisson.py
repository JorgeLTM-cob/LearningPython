import math
def factori(m):
    if (m == 0):
        return (1)
    prod = 1
    while(m > 0):
        prod *= m
        m -= 1
    return(prod)

l = 5
k = 3
k += 1
e = math.exp(-l)
suma = 0
for i in range(0, k):
   den = factori(i)
   suma += ((l**i) * e) / den

print(suma)
