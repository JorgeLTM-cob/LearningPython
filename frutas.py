from pulp import *

A = LpVariable("LoteA",0)
B = LpVariable("LoteB",0)

Existencias = [800, 800, 500]
ContenidoA = [1, 2, 1]
ContenidoB = [2, 1, 1]

GananciaA = 4800
GananciaB = 5600

problema = LpProblem("Lotes", LpMaximize)

for i in range(0, 3):
    problema += ((ContenidoA[i] * A) + (ContenidoB[i] * B)) <= Existencias[i]

problema += ((GananciaA * A) + (GananciaB * B))

status = problema.solve(GLPK(msg = 0))

print(LpStatus[status])
print(A.value())
print(B.value())
Gan = ((GananciaA * A.value()) + (GananciaB * B.value()))
print(Gan)
