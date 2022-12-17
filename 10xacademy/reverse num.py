# n=int(input())
# sum=0
# if n<0:
#     n=n*-1
#     while n!=0:
#         reverse=n%10
#         sum=sum*10+reverse
#         n=n//10
#     print(-sum)
# elif n>0:
#      while n!=0:
#         reverse=n%10
#         sum=sum*10+reverse
#         n=n//10
#      print(sum)
# else:
#     print(0)

n=int(input())
sum=0

while n!=0:
    reverse=n%10
    sum=sum*10+reverse
    n=n//10
print(sum)
# elif n>0:
#      while n!=0:
#         reverse=n%10
#         sum=sum*10+reverse
#         n=n//10
#      print(sum)
# else:
#     print(0)