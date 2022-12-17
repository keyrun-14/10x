import math
def sumofproduct(n):
    sum = 0
    for x in range(1 ,n+1):
        y = math.floor(n/x)
        sum=sum+y*x
    return sum
n = int(input())
print(sumofproduct(n))