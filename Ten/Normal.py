import math

mu = 20
sig = 2
q1 = 19.5
a1 = 20
a2 = 22
cdf = lambda x: 0.5 * (1 + math.erf((x - mu)/(sig*(2**0.5))))

print("%.3f" % cdf(q1))
print("%.3f" % (cdf(a2) - cdf(a1)))
