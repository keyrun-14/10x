from itertools import combinations


n,k=input().split()
n,k=int(n),int(k)
combinations=[]
for i in range(1,n):
    for j in range(i+1,n+1):
        combinations.append([i,j])
print(combinations)