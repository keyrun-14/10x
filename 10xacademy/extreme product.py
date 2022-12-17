# n=int(input())
# a=[]
# temp=0
# for i in range(n):
#     b=int(input())
#     a.append(b)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp 
# print(a[0]*a[n-1])
n=int(input())
max=0
min=0
for i in range(n):
    a=int(input())
    if a>min:
        max=a
    elif a<max:
        min=a
print(max)
print(min)
