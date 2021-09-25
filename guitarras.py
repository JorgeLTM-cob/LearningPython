from pulp import *

guitarra = LpVariable("guitarra", 0, 500)
bajo = LpVariable("bajo", 0, 400)

maderag = 2
maderab = 3
maderaDisponible = 1500

utilidadg = 120
utilidadb = 100

problema = LpProblem("Guitarras_y_Bajos", LpMaximize)
problema += ((maderag * guitarra) +(maderab * bajo)) <= maderaDisponible
problema += ((utilidadg * guitarra) + (utilidadb * bajo))

status = problema.solve(GLPK(msg=0))

print(LpStatus[status])
print(guitarra.value())
print(bajo.value())

