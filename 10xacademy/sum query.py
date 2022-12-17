n,q=input().split()
n,q=int(n),int(q)
a=list(map(int,input().split()))[:n]

for i in range(0,q):
    c=list(map(int,input().split()))[:q]
    k=sum(a[((c[0])-1):((c[-1]))])
    print(k)