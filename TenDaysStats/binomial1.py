def factorial(b,a):
   if (b == 0 or b - a == 0):
       return(1)
   prod = 1
   limit = b - a
   for i in range (0, limit):
       if (b > 1):
          prod *= b
          b -= 1 
   return(prod)

def prefac(n,r):
    num = factorial(n,(n - r))
    den = factorial(r,1)
    return (num/den)

p = 0.5215311005
q = 0.4784688995
n = 6
r = 3
suma = 0

for i in range (0, 3):
    pre = prefac(n,i)
    suma += pre * (p**i) * (q**(n-i))
print(round(1 - suma, 3))
