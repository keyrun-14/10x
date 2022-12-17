def recursive_sequence(n):
    if n==1:
        return 1
    mul=1
    for i in range((n*(n+1)//2)-n+1,(n*(n+1)//2)+1):
        mul=mul*i
    return mul+recursive_sequence(n-1)
for i in range(int(input())):
    n=int(input())
    print(recursive_sequence(n))




# n=int(input())
# sum=0
# mul=1
# k=1
# for i in range(1,n+1):
#     print("i = ",i)
#     for j in range(k,k+i):
#         mul=mul*j
#         print("j = ",j)
#     print(mul)
#     sum=sum+mul
#     mul=1
#     k=k+i
# print(sum)

# def recursive_sequence(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return n+recursive_sequence((n-1))
# n=int(input())
# print(recursive_sequence(n))