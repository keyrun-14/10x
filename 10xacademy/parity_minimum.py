n=int(input())
if n>0:
    first_value=int(input())
    minim=first_value
    for i in range(n-1):
        element=int(input())
        if element<minim:
            minim=element
    sum=0
    while minim>0:
        rem=minim%10
        sum=sum+rem
        minim=minim//10
    if sum%2 != 0:
        print(0)
    else:
        print(1)
# arr=[1,2,3,4]
# x=min(arr)
# print(x)