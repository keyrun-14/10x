def rotate_matrix(m,n):
    for i in range(m):
        a.append(list(map(str,input().split()))[:n])
    for i in range(m):
        for j in range(n):
            b[j][m-i-1]=a[i][j]
    for i in range(n):
        print(*b[i])
m=int(input())
n=int(input())
a=[]
b=[[0 for j in range(m)] for i in range(n)]
rotate_matrix(m,n)