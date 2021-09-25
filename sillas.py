from pulp import *

S1 = LpVariable("Silla1", 0)
S2 = LpVariable("Silla2", 0)

tmS1 = 20
tmS2 = 30
tqS1 = 20
tqS2 = 10
limitetm = 6000
limitetq = 4800

utilidadS1 = 15
utilidadS2 = 10

problema = LpProblem("Sillas", LpMaximize)

problema += ((tmS1*S1) + (tmS2*S2)) <= limitetm
problema += ((tqS1*S1) + (tqS2*S2)) <= limitetq
problema += ((S1*utilidadS1) + (S2*utilidadS2))

status = problema.solve(GLPK(msg = 0))

print(LpStatus[status])
print(S1.value())
print(S2.value())

gTotal = ((S1.value() * utilidadS1) + (S2.value() * utilidadS2))
print(gTotal)
