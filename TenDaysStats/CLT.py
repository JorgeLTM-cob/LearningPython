import math
maxi = 250
boxes = 100
mu = 2.4
sig = 2
sig *= math.sqrt(boxes)
mu *= boxes
cdf = lambda x: 0.5 * (1 + math.erf((x - mu)/(sig * math.sqrt(2))))

print(cdf(maxi))

