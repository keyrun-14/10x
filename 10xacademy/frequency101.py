n,k=input().split()
n,k=int(n),int(k)
a=list(map(int,input().split()))[:n]
count=0
for i in range(n):
    if a[i]==k:
        count+=1
print(count)