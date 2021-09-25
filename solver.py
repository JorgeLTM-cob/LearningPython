from pulp import *

pelotaFutbol = LpVariable("pelotaFutbol", 0, 400) #     0 <= x <= 400
pelotaBasquet = LpVariable("pelotaBasquet", 0, 300) #   0 <= y <= 300

materialUnidadF = 100
materialUnidadB = 125

materialDisponible = 50000

gananciaF = 50
gananciaB = 40

problema = LpProblem("problema", LpMaximize)

problema += (materialUnidadF*pelotaFutbol) + (materialUnidadB*pelotaBasquet) <= materialDisponible

problema += (pelotaFutbol * gananciaF) + (pelotaBasquet*gananciaB)

status = problema.solve(GLPK(msg=0))
print(LpStatus[status])
print(value(pelotaFutbol))
print(value(pelotaBasquet))
