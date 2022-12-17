def pow(x,n):
    if n==0:
        return 1
    if n==1:
        return n
    var=pow(x,n//2)
    if n%2 == 0:
        power=var*var
    else:
         power=var*var*x
    return power
x=float(input())
n=int(input())
pow(x,n)



n=10
n=5
n=2
n=1

n=11
n=5
n=2
n=1


