a=int(input())
for i in range(a):
    n=int(input())
    count=0
    if n==1:
        print("No")
        continue

    for i in range(1,n+1):
        if n%i==0:
            count=count+1
        if  count>2:
            print("No")
            break
                   
    else:
        print("Yes")
