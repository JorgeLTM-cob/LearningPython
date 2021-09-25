from pulp import *

A = LpVariable("Mina_A",0)
B = LpVariable("Mina_B",0)

Metas = [70, 130, 150]

ProduccionA = [1, 2, 4]
ProduccionB = 2

CostoA = 500
CostoB = 750

problema = LpProblem("Minas", LpMinimize)
N = len(Metas)
for i in range(0, N):
    problema += ((ProduccionA[i] * A) + (ProduccionB * B)) >= Metas[i]

problema += ((A * CostoA) + (B * CostoB))

status = problema.solve(GLPK(msg = 0))
print(LpStatus[status])
print(A.value())
print(B.value())
Gasto = ((A.value() * CostoA) + (B.value() * CostoB))
print(Gasto)

