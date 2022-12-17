n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
if len(a)==0:
    print(-1)
else:
    count=1
    maxm=1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count=count+1
            maxm=max(maxm,count)
            continue
        count=1
    c=[-1]
    for i in a:
        if (a.count(i)==maxm and c[-1]!=i):
            c.append(i)  
    for i in c[1:]:
            print(i)