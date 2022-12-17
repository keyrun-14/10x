n=int(input())
a=[]#list(map(int,input().split()))
k=0
l=0
for i in range(0,n):
    ele=int(input())
    a.append(ele)
    #a[i]=ele
    if i%2==0:
        k=k+a[i]
    else:
        l=l+a[i]
print(k-l)

n=int(input())
k=0
for i in range(n):
    a=int(input())
    if i%2==0:
        k=k+a
    else:
        k=k-a
print(k)
