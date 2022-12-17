def recursive_series(n):
    if n<=9:
        return n
    elif n%2==0:
        n=n-10
        return (recursive_series(n))
    elif n%2!=0:  
        return (recursive_series(n-9))
t=int(input())
for i in range(t):
    n=int(input())
    print(recursive_series(n))


