def insert_in_between(n,x,arr):
    if arr[0]>=x:
        return [x]+arr
    elif arr[-1]<=x:
        return arr+[x]
    else:
        for i in range(1,n):
            if x<=arr[i]:
                return arr[:i]+[x]+arr[i:]
n,x=map(int,input().split())
arr=list(map(int,input().split()))
print(*insert_in_between(n,x,arr))