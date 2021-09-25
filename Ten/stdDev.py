import math

def stdDev(arr):
   N = len(arr)
   mean = 0
   var = 0
   for i in range(0,N):
       mean += arr[i]
   mean /= N
   for i in range(0,N):
       var += ((arr[i] - mean)**2)
   var /= N
   stdD = math.sqrt(var)
   print(round(stdD,1))

test = [10, 40, 30, 50, 20]
stdDev(test)
