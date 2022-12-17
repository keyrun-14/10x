arr=list(map(int,input().split()))
arr.sort()
count=1
maxx=float('-inf')
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]==1:
        count+=1
    else:
        if count>maxx:
            maxx=count
        count=1
if count>maxx:
    maxx=count
print(maxx)
    