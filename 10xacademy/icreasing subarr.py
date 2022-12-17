n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
c=[]
temp=a[0]
for i in range(n-1):
    b=[]
    if temp<a[i+1]:
        b.append(a[i])
        b.append(a[i+1])
        temp=a[i+1]
        
    else:
        temp=a[i+1]
        c.append(b)
        
    print(b)
    print(c)


