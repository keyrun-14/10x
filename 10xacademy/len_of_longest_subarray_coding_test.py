n,k=input().split()
n,k=int(n),int(k)
arr=list(map(int,input().split()))[:n]
d={}
sum=0
count=0
for i in range(len(arr)):
    sum+=arr[i]

    if sum==k:
        count=i+1 
         
    elif sum-k in d:
        print(i-d[sum-k])
        
        count=max(count,i-d[sum-k])
    if sum not in d:
        d[sum]=i
        print(d)

if count==0:
    print(-1)
else:
    print(count)