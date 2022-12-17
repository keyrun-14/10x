m=list(input().split())
n=list(input().split())
c=[[]]
for i in range(n):
    for j in range(m):
        c[j][i]=m[i][j]
        print(c)