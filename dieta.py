from pulp import *

A = LpVariable("ProductoA",0)
B = LpVariable("ProductoB",0)

Limites = [8, 12, 9]
ContenidoA = [2, 6, 1]
ContenidoB = [1, 1, 3]

CostoA = 600
CostoB = 400

problema = LpProblem("Productos",LpMinimize)

for i in range(0, 3):
    problema += ((ContenidoA[i] * A) + (ContenidoB[i] * B)) >= Limites[i]

problema += ((A * CostoA) + (B * CostoB))

status = problema.solve(GLPK(msg = 0))

print(LpStatus[status])
print(A.value())
print(B.value())
costo = ((A.value() * CostoA) + (B.value() * CostoB)) 
print(costo)
