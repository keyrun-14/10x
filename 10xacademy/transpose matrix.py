def transpose_matrix(m,n):
  
    for i in range(m):
        for j in range(n):
            b[j][i]=a[i][j]
    for i in range(n):
        print(*b[i])
m=int(input())

a=[]
firstRow=list(map(str,input().split()))
a.append(firstRow)
for i in range(m-1):
    a.append(list(map(str,input().split()))[:len(firstRow)])
n=len(a[0])

b=[[0 for j in range(m)] for i in range(n)]
transpose_matrix(m,n)

# def transpose(lst,m,n):
#     for i in range(n):
#      for j in range(m):
#       print(lst[j][i])
#     print(end='\n')
# m=int(input())
# lst=[]
# for i in range (m):
#     row = list(map(int,input().split()))
#     lst.append(row)
# n=len(row)
# transpose(lst,m,n)