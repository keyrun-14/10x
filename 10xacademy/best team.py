a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
d.append(a)
d.append(b)
d.append(c)
f=[]
for i in range (1):
    for j in range(len(a)):
        if i!=j:
            e=abs(d[i][j]-d[i+1][j])+abs(d[i+2][j]-d[i+1][j])
            f.append(e)
print(f)

for i in range(len(b)):
    print(min(abs(max(a)-(d[1][i]))+abs(min(c)-d[1][i])))