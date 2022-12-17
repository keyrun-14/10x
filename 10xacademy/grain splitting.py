t=int(input())
print(t)
for i in range(t):
    arr=list(map(int,input().split()))
    arr.sort()
    total=sum(arr)
    half=total//2
    sumOf=0
    first_vill_last_bag=0
    for i in range(len(arr)):
        sumOf=sumOf+arr[i]
        if sumOf==half:
            first_vill_last_bag=i
            break    
    print(*arr[first_vill_last_bag+1:])
