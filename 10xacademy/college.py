def college(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    print(sum)
n=int(input())
college(n)