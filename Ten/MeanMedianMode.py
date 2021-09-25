import math
N = int(input())
my_string = input().split()
arr =[]
mean = 0
median = 0

for i in range (0,N):
    arr.append(int(my_string[i]))

arr.sort()

for i in range (0,N):
    mean += arr[i]

mean = mean / N
if ((N % 2) == 0):
    median = (arr[N//2] + arr[(N//2) - 1]) / 2
else:
    median = arr[N//2]

current = arr[0]
may = 0
cont = 0
pos = 0
for i in range (0,N):
    if (arr[i] == current):
        cont += 1
        if (cont > may):
            may = cont
            pos = i
    else:
        current = arr[i]
        cont = 1

print((math.floor(mean*10))/10)
print((math.floor(median*10))/10)
print(arr[pos])
