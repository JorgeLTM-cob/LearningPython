def factorial(b,a):
    if (b == 0 or (b - a) == 0):
        return (1)
    prod = 1
    limit = b - a
    for i in range(0, limit):
        prod *= b
        b -= 1
    return(prod)

def prefactor(n, r):
    num = factorial(n, (n - r))
    den = factorial(r, 1)
    return(num / den)

n = 10
p = 0.12
q = 0.88
suma = 0

for i in range (0, 3):
    pref = prefactor(n, i)
    suma += pref * (p**i) * (q**(n - i))
sumb = 0
for i in range (0, 2):
    pref = prefactor(n, i)
    sumb += pref * (p**i) * (q**(n - i))

print(round(suma,3))
print(round(1 - sumb, 3))
