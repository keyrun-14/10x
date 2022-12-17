# for i in range(int(input())):
#     n,x=map(int,input().split())
#     arr=list(map(int,input().split()))[:n]
#     if x<=arr[0]:
#         print(*([x]+arr))
#     elif x>=arr[-1]:
#         print(*(arr+[x]))
#     else:
#         for i in range(1,n):
#             if x<=arr[i]:
#                 print(*(arr[:i]+[x]+arr[i:]))
#                 break
a="a"
print(id(a))
a=a+"b"
print(id(a))
s=[1,2,3]
print(id(s))
s=s+[3]

print(id(s))