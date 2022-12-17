# a=input()
# b=a.split()
# print(b[::-1])
# for i in range(len(b)//2):
#     b[i],b[len(b)-1-i]
# a="-123"
# b=[]
# for i in range(len(a)):
#     b.append(a[i])
# print(b)

# a=3
# a="ki"
# print(a)

def sum(a):
    if a==1:
        return 1
    c=a+sum(a-1)
    return c
a =list(map(int,input().split()))
print(sum(a))
arr.map(x=>x*x)