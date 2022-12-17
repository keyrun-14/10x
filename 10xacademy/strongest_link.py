n=int(input())
arr=list(map(int,input().split()))
minm_sum=-float("inf")
sum=0
start=0
k=0
for i in range(n):
    sum=sum+arr[i]
    if minm_sum<sum:
        minm_sum=sum
        end=i
        start=k
    if sum<0:
        sum=0
        k=i+1
print(start,end,minm_sum)