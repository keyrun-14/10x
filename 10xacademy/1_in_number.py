# for i in range(int(input())):
#     n=int(input())
#     count=0
#     while n>0:
#         n=n>>1
#         count=count+1
#     print(count)
#     count=0
#     while n>0:
#         n=n<<1
#         count=count+1
#     print(count)
# for i in range(int(input())):
#     n=int(input())
#     count=0
#     while n>0:
#         a=n%2
#         if a==1:
#             count=count+1
#         n=n//2
#         print(a)
# for i in range(10):
#     print(256>>i)
# print(256>>4)



for i in range(int(input())):
    n=int(input())
    count=0
    while n>0:
        if n&1==1:
            count+=1
        n>>=1
    print(count)