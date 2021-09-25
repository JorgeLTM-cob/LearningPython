import math

stats = []
a = 80
stats.append(70)
stats.append(10)

cdf = lambda x: 0.5 * (1 + math.erf((x - stats[0])/(stats[1] * (2**0.5))))

ah = cdf(a)
print("%.2f" % round((1 - ah) * 100, 2))
print("%.2f" % round(ah * 100, 2))
print("%.2f" % round((1 - ah) * 100, 2))

