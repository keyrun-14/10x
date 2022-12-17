n=int(input())
m=[]
w=[]
for i in range(n):
    a,b=map(int,input().split())
    if a==0:
        w.append(b)
    elif a==1:
        m.append(b)
m.sort()
w.sort()
print(*w[::-1],*m[::-1])