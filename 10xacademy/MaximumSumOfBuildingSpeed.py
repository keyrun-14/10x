n=int(input())
arr=list(map(int,input().split()))[:2*n]
arr.sort()
sum=0
for i in range(0,2*n,2):
    sum=sum+arr[i]
print(sum)