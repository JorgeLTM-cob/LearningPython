import math
sample = 100
mu = 500
sig = 80
amount = 0.95
z = 1.96
sig = sig * z / math.sqrt(sample)  
print("%.2f" % round((mu - sig),2))
print("%.2f" % round((mu + sig),2))
