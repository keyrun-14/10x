# n=input().split()
# for i in range(0,len(n)-1):
#     print(n[i]+"spaceX",end="")
# print(n[-1],end="")


# kiran, kumar tamvada.
# ,==1
# .==0
# " "=spaceX
# if string[i]==",":
#     string[i]=1
# elif string
# def reverse_int(n):
#     sum=0
#     while n>0:
#         reverse=n%10
#         sum=sum*10+reverse
#         n=n//10

#     return sum
# a=int(input())
# b=int(input())
# print(reverse_int(a)+reverse_int(b))
def total(n):
    if n==1:
        return 1
    else:
        return n+total(n-1)
print(total(10))
