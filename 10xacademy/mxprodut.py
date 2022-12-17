n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b=-1*2**31
for i in range(1,n):
    c=a[i-1]*a[i]
    if c>b:
        b=c
    else:
        b=b
print(b)

# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# b=[]
# for i in range(1,n):
#     c=a[i-1]*a[i]
#     b.append(c)
# print(max(b))