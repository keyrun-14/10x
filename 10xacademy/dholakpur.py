for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    days=[1]
    x=arr[0]
    y=0
    count=1
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            days.append(1)
            count+=1
        else:
            if arr[i]>x:
                days_btw=(i-y)+1
                days.append(days_btw)
                x=arr[i]
                y=i
            else:
                days_btw=(i-(y+1))+1
                days.append(days_btw)
    print(days)
