def sum_of_multiples(L,N):
    a=0
    sum=0
    if N>0:
        for i in L:
            a=i%N
            if a==0:
                sum=sum+i
    print(sum)

L=[int(i) for i in input(). split ()]
N=int(input())
sum_of_multiples(L,N)