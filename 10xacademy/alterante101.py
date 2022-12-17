n=int(input())
N=list(map(int,input().split()))[:n]
sum=0
for i in range(0,n,2):
    sum+=N[i]
print(sum)
