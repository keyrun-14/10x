t=int(input())
n=list(map(int,input().split()))[:t]
d={}
for i in n:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
a=0
for i in d.values():
    if i>=2 and i%2==0:
        a+=i//2
      
    elif i>=2 and i%2!=0:
        a+=(i-1)//2
print(a)

t=int(input())
n=list(map(int,input().split()))[:t]
d={}
for i in n:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
a=0
for i in d.values():
    if i>=2:
        a+=i//2
print(a)

1 3 3 3 5 5
123
12345
12345