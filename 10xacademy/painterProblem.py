for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    for i in range(1,k):
        if arr[i-1]-