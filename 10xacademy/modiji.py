import math
def modiji(salary):
    k=0
    for i in salary:
        i=math.ceil(i*0.07)
        k+=+i
    return k
n=int(input())
salary=list(map(int,input().split()))
modiji(salary)
print(k)