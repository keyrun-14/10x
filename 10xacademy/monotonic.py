# n=int(input())
# a=int(input())
# temp=a
# count=1
# count1=1
# for i in range(n-1):
#     b=int(input())
#     if temp>b:
#         count=count+1
#         temp=b
#     elif temp<b:
#         count1=count1+1
#         temp=b
#     elif temp==b:
#         temp=b
#         count=count+1
#         count1=count1+1

# if count==n or count1==n:
#     print(True)
# else:
#     print(False)

# n=int(input())
# a=int(input())
# temp=a
# count=1
# count1=1
# increase=1
# decrease=0
# for i in range(n-1):
#     b=int(input())
#     if temp>b:
#         temp=b
#         decrease=1
#         increase=1
#     elif temp<b:       
#         temp=b
#         increase=0
#         decrease=0
#     elif temp==b:
#         temp=b
#         increase=1
#         decrease=0
# if count==n or count1==n:
#     print(True)
# else:
#     print(False)


n=int(input())
a=int(input())
b=int(input())
if a>b:
    flag=1
else:
    flag=0
for i in range(n-2):
    c=int(input())
    if c>b:
        b=c
        flag=0
    else:
        print()
        break
        
    if c<b:
        b=c

if count==n or count1==n:
    print(True)
else:
    print(False)


##############################################
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# count=1
# count1=1
# for i in range(len(a)-1):
#     if a[i]>=a[i+1]:
#         count=count+1
# for i in range(n-1):
#     if a[i]<=a[i+1]:
#         count1=count1+1
# if count==len(a) or count1==len(a):
#     print(True)
# else:
#     print(False)

###########################################################


# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# if n>2:
#     if a[0]<a[1]:
#         for i in range(n-1):
#             if a[i]<=a[i+1]:
#                 flag=True
#             else:
#                 flag=False
#                 break
#     else:
#         for i in range(n-1):
#             if a[i]>=a[i+1]:
#                 flag=True
#             else:
#                 flag=False
#                 break
#     print(flag)
# elif n==1 or n==2:
#     print(True)
# elif n<=0:
#     print(False)