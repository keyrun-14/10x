t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    sum=0
    res="No"
    if n==0:
        res="No"
    for i in range(n):
        if arr[i]<=0:
            pass
        elif arr[i]>0:
            sum=sum+arr[i]
    print(sum)
    if sum%2!=0:
        res="No"
    else:
        j=sum
        while j>1:
            sum=sum//2
            rem=sum%2
            if rem==0 or sum==1:
                res="Yes"
                j=sum
            else:
                res="No"
                j=1
    print(res)